# -*- coding: utf-8 -*-
"""Find real, verified YouTube videos for every topic and every scheduled problem.

    python webapp/tools/build_videos.py                 # topics  -> plan/topic-videos.md
    python webapp/tools/build_videos.py --problems      # problems -> plan/problem-videos.md
    python webapp/tools/build_videos.py DS-6 AL-3       # redo only these
    python webapp/tools/build_videos.py --problems --part 1/3   # one of three workers

Topics: search the topic's phrase from plan/topic-lectures.md three ways, score by
channel and title match, keep up to six from different teachers (the planner deals
three per session), and confirm every one against the video itself - uploader's
title, duration, keywords, description - before it is written down.

Problems: search "<number> <title> leetcode"; a candidate is accepted only if its own
title names the problem (the full title, or the number plus most of the title).

Nothing is typed from memory. Caches are gitignored; a crash costs one item.
"""
import json
import re
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import yt                      # noqa: E402
import topics as T             # noqa: E402

ROOT = HERE.parent.parent
PROBLEMS = "--problems" in sys.argv
PART = next((a.split("/") for a in sys.argv if re.fullmatch(r"\d+/\d+", a)), None)
OUT = ROOT / "plan" / ("problem-videos.md" if PROBLEMS else "topic-videos.md")
suffix = f"-{PART[0]}of{PART[1]}" if PART else ""
CACHE = HERE / (f"problem-video-cache{suffix}.json" if PROBLEMS else f"topic-video-cache{suffix}.json")

# Channels worth sending you to, by area. Higher is better. An unknown channel needs
# an overwhelming title match to be considered at all.
TIERS = {
    "neetcode": 9, "neetcodeio": 9, "take u forward": 9, "abdul bari": 9, "williamfiset": 8,
    "back to back swe": 8, "mit opencourseware": 8, "errichto algorithms": 7, "tushar roy - coding made simple": 7,
    "aditya verma": 8, "algomasterio": 7, "greg hogg": 6, "nick white": 5, "kevin naughton jr.": 5,
    "algorithms made easy": 6, "techdose": 6, "codestorywithmik": 7, "codehelp - by babbar": 6,
    "pepcoding": 6, "coder army": 5, "michael sambol": 7, "spanning tree": 7, "reducible": 7,
    "mycodeschool": 7, "computerphile": 6, "the cherno": 8, "cppcon": 6, "codebeauty": 6,
    "cs dojo": 5, "jenny's lectures cs it": 6, "gate smashers": 5, "freecodecamp.org": 4,
    "bro code": 5, "striver": 8, "vivekanand khyade - algorithm every day": 5, "stable sort": 6,
    "code with irfan": 4, "codencode": 5, "luv": 6, "fraz": 5, "anuj bhaiya": 5, "apna college": 5,
    # design
    "gaurav sen": 9, "bytebytego": 9, "hello interview - swe interview preparation": 9, "hello interview": 9,
    "jordan has no life": 8, "concept && coding - by shrayansh": 9, "arpit bhayani": 8, "exponent": 8,
    "system design interview": 6, "sudocode": 7, "tech dummies narendra l": 7, "keerti purswani": 6,
    "christopher okhravi": 9, "geekific": 7, "derek banas": 6, "soumyajit bhattacharyay": 7,
    "udit agarwal": 7, "coding simplified": 5, "code and debug": 6, "interviewready": 6,
    "hussein nasser": 8, "martin kleppmann": 9, "distributed systems course": 7,
    # behavioural / process
    "a life engineered": 8, "jeff h sipe": 8, "life at google": 9, "dan croitor": 7, "jomaclass": 5,
    "clément mihailescu": 6, "algoexpert": 6, "tech with nikola": 5, "sahil & sarra": 6,
    "interviewing.io": 8, "google for developers": 8, "kantan coding": 5,
}

BAD_TITLE = re.compile(
    r"\b(shorts?|#shorts|motivation|salary|vlog|reaction|podcast|live stream|livestream|"
    r"giveaway|announcement|trailer|teaser|meme|day in the life|roadmap|"
    r"one shot|all in one|complete course|full course|crash course|in one video|marathon|"
    r"\d+\s*hours?)\b", re.I)
# A different human language in the title (common on regional channels) - the video
# may be fine, but a title in Hindi script or Indonesian is not what these phrases want.
NON_LATIN = re.compile(r"[ऀ-ॿ؀-ۿ一-鿿Ѐ-ӿ]")
OFF_DOMAIN = re.compile(r"(machine learning|deep learning|neural network|data science|blockchain|"
                        r"excel|power bi|tally|digital marketing|stock market|trading)", re.I)
MIN_SECONDS = 150


def tier_of(channel):
    ch = channel.lower().strip()
    if ch in TIERS:
        return TIERS[ch]
    for name, pts in TIERS.items():
        if len(name) > 5 and name in ch:
            return pts
    return 0


def seconds(text):
    parts = [p for p in (text or "").split(":") if p.strip().isdigit()]
    s = 0
    for p in parts:
        s = s * 60 + int(p)
    return s


# ---------------------------------------------------------------- topics

def topic_accept(v, entry, want_words):
    det = yt.details(v["id"])
    if not det:
        return None
    if det["seconds"] and det["seconds"] < MIN_SECONDS:
        return None
    if BAD_TITLE.search(det["title"]) or OFF_DOMAIN.search(det["title"]) or NON_LATIN.search(det["title"]):
        return None
    blob = det["title"] + " " + " ".join(det["keywords"][:40]) + " " + cut_boilerplate(det["description"])[:800]
    if len(T.words(blob) & want_words) < 2:
        return None
    return {"id": v["id"], "title": det["title"].strip(), "channel": det["channel"].strip()}


BOILER = re.compile(r"(https?://|#\w|subscribe|join our|follow us|timestamps?:|chapters?:)", re.I)


def cut_boilerplate(desc):
    """Descriptions end in course links and hashtags; only what precedes them is evidence."""
    m = BOILER.search(desc)
    return desc[:m.start()] if m else desc


def pick_topic(entry, want=6):
    words = T.words(entry["name"] + " " + entry["phrase"])
    phrase = entry["phrase"]
    short = entry["short"].rstrip("…")
    queries = [phrase, f"{short} explained", f"{short} {entry['areaName']}"]
    candidates, seen = [], set()
    for q in queries:
        try:
            results = yt.search(q, limit=20)
        except Exception as e:
            print(f"    search failed ({e})", flush=True)
            results = []
        for v in results:
            if v["id"] in seen:
                continue
            seen.add(v["id"])
            if BAD_TITLE.search(v["title"]) or OFF_DOMAIN.search(v["title"]) or NON_LATIN.search(v["title"]):
                continue
            dur = seconds(v["duration"])
            if dur and (dur < MIN_SECONDS or dur > 3 * 3600):
                continue
            tier = tier_of(v["channel"])
            hits = T.words(v["title"]) & words
            overlap = len(hits)
            if tier == 0 and overlap < 4:
                continue
            if overlap == 0:
                continue
            v["score"] = tier * 2 + overlap * 2
            candidates.append(v)
        time.sleep(1.5)
    candidates.sort(key=lambda v: -v["score"])
    chosen, chans = [], set()
    for v in candidates:
        if len(chosen) >= want:
            break
        ch = v["channel"].lower()
        if ch in chans:
            continue
        got = topic_accept(v, entry, words)
        if got:
            chans.add(ch)
            chosen.append(got)
        time.sleep(0.2)
    # Fewer than three teachers: allow a second video from a channel already chosen.
    if len(chosen) < 3:
        have = {c["id"] for c in chosen}
        for v in candidates:
            if len(chosen) >= 3:
                break
            if v["id"] in have:
                continue
            got = topic_accept(v, entry, words)
            if got:
                chosen.append(got)
    return chosen


# ---------------------------------------------------------------- problems

def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def names_problem(title, p):
    """Does a video title name this exact problem?"""
    nt, pt = norm(title), norm(p["title"])
    if f" {pt} " in f" {nt} ":
        return True
    pw = [w for w in pt.split() if len(w) > 2]
    has_num = re.search(rf"(?<!\d){p['num']}(?!\d)", title) is not None
    if has_num and pw:
        hit = sum(1 for w in pw if w in nt.split())
        return hit / len(pw) >= 0.6
    return False


def pick_problem(p, want=2):
    queries = [f"leetcode {p['num']} {p['title']}", f"{p['title']} leetcode solution"]
    candidates, seen = [], set()
    for q in queries:
        try:
            results = yt.search(q, limit=15)
        except Exception as e:
            print(f"    search failed ({e})", flush=True)
            results = []
        for v in results:
            if v["id"] in seen:
                continue
            seen.add(v["id"])
            if not names_problem(v["title"], p):
                continue
            if BAD_TITLE.search(v["title"]) or NON_LATIN.search(v["title"]):
                continue
            dur = seconds(v["duration"])
            if dur and (dur < 120 or dur > 2 * 3600):
                continue
            tier = tier_of(v["channel"])
            v["score"] = tier * 3 + (3 if re.search(r"c\+\+|cpp", v["title"], re.I) else 0)
            candidates.append(v)
        if len(candidates) >= 4:
            break
        time.sleep(1.5)
    candidates.sort(key=lambda v: -v["score"])
    chosen, chans = [], set()
    for v in candidates:
        if len(chosen) >= want:
            break
        ch = v["channel"].lower()
        if ch in chans:
            continue
        det = yt.details(v["id"])
        if not det or (det["seconds"] and det["seconds"] < 120):
            continue
        if not names_problem(det["title"], p):
            continue
        chans.add(ch)
        chosen.append({"id": v["id"], "title": det["title"].strip(), "channel": det["channel"].strip()})
        time.sleep(0.2)
    return chosen


# ---------------------------------------------------------------- driver

def scheduled_problem_keys(problems):
    keys = []
    for f in sorted((ROOT / "plan").glob("phase-*.md")):
        for num in T.PROBLEM_RE.findall(f.read_text(encoding="utf-8")):
            k = f"LC-{num}"
            if k in problems and k not in keys:
                keys.append(k)
    rest = [k for k in problems if k not in keys]
    return keys + rest


def main():
    catalogue, problems = T.build_catalogue()
    only = [a for a in sys.argv[1:] if not a.startswith("--") and not re.fullmatch(r"\d+/\d+", a)]
    ids = only or (scheduled_problem_keys(problems) if PROBLEMS else list(catalogue))
    if PART and not only:               # explicit ids are always done, into this part's cache
        i, n = int(PART[0]), int(PART[1])
        ids = ids[i - 1::n]
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    if only:
        for k in only:
            cache.pop(k, None)
    for n, key in enumerate(ids, 1):
        if key in cache:
            continue
        if PROBLEMS:
            p = problems[key]
            print(f"[{n}/{len(ids)}] {key} {p['title']}", flush=True)
            got = pick_problem(p)
        else:
            entry = catalogue[key]
            print(f"[{n}/{len(ids)}] {key} {entry['phrase'][:60]}", flush=True)
            got = pick_topic(entry)
        cache[key] = got
        for g in got:
            print(f"      {g['channel'][:24]:<24} {g['title'][:70]}", flush=True)
        if not got:
            print("      (nothing passed)", flush=True)
        CACHE.write_text(json.dumps(cache, indent=1), encoding="utf-8")
    if not PART:
        write(catalogue, problems, cache)


def merged_cache():
    stem = "problem-video-cache" if PROBLEMS else "topic-video-cache"
    out = {}
    for f in sorted(HERE.glob(f"{stem}*.json")):
        out.update(json.loads(f.read_text(encoding="utf-8")))
    return out


HEAD_TOPICS = """# Topic Videos — the lectures for each topic

One row per video: **the video itself**, never a playlist or a channel page. The planner
shows three per session and, when a topic comes round again, the next three.

**How these were chosen.** Each topic's phrase from `topic-lectures.md` was searched on
YouTube three ways. Results were ranked by channel (a fixed list of teachers worth your time —
NeetCode, take U forward, Abdul Bari, WilliamFiset, MIT OCW, Gaurav Sen, ByteByteGo, Hello
Interview, Christopher Okhravi and others) and by how well the title matches the topic. The
best, one per teacher, were then **checked against the video itself**: YouTube's own record of
the uploader's title, duration, keywords and description, with the description cut at the
first link or hashtag so channel boilerplate cannot vouch for anything. Rejected outright:
anything under 2½ minutes (trailers, shorts), whole-course marathons, titles in another
script, and titles from another field.

Titles and channels below are what YouTube returned, not what was remembered. Regenerate a
topic with `python webapp/tools/build_videos.py <id>`; delete a row if a video turns out wrong.

| # | Video ID | Channel | Title |
|---|----------|---------|-------|
"""

HEAD_PROBLEMS = """# Problem Videos — solutions for each problem, to watch after you attempt it

One or two per problem, from different teachers. **Watch after an honest attempt**, never
before: the value of a problem is the 25 minutes of being stuck.

**How these were chosen.** YouTube was searched for the problem's number and title. A video
was accepted only when **its own title names this exact problem** — the full title, or the
LeetCode number plus most of the title — and its duration and existence were confirmed against
YouTube's record of the video. Ranked by channel (NeetCode, take U forward, codestorywithMIK,
Algorithms Made Easy, and similar), with a small preference for C++ explanations.

Regenerate with `python webapp/tools/build_videos.py --problems <LC-n>`.

| # | Video ID | Channel | Title |
|---|----------|---------|-------|
"""


def write(catalogue, problems, cache):
    order = scheduled_problem_keys(problems) if PROBLEMS else list(catalogue)
    rows, total, covered = [], 0, 0
    for key in order:
        vids = cache.get(key) or []
        if vids:
            covered += 1
        for v in vids:
            title = v["title"].replace("|", "/").strip()
            chan = v["channel"].replace("|", "/").strip()
            rows.append(f"| {key} | {v['id']} | {chan} | {title} |")
            total += 1
    OUT.write_text((HEAD_PROBLEMS if PROBLEMS else HEAD_TOPICS) + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"\nwrote {OUT.name}: {total} videos, {covered}/{len(order)} covered")


if __name__ == "__main__":
    if "--merge" in sys.argv:
        cat, probs = T.build_catalogue()
        write(cat, probs, merged_cache())
    else:
        main()
