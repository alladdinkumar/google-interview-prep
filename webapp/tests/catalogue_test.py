"""Offline checks on the plan and everything hung off it. Runs in CI before every deploy.

    python webapp/tests/catalogue_test.py

The failure mode of a hand-edited plan is not a crash; it is a topic quietly losing its
videos, a typo'd LC number that links nowhere, or a prompt edited until it no longer
demands a format. Each assertion below guards one of those.
"""

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

WEBAPP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WEBAPP))

import server  # noqa: E402
import topics as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
failures = []


def check(name, ok, detail=""):
    print(f"  {'ok  ' if ok else 'FAIL'}  {name}{'' if ok else ' - ' + str(detail)[:300]}")
    if not ok:
        failures.append(name)


WATCH = re.compile(r"^https://www\.youtube\.com/watch\?v=[A-Za-z0-9_-]{11}$")
ALLOWED_HOSTS = {
    "www.youtube.com", "leetcode.com", "www.lintcode.com", "en.wikipedia.org", "cp-algorithms.com",
    "en.cppreference.com", "www.techinterviewhandbook.org", "refactoring.guru", "www.hellointerview.com",
    "github.com", "gist.github.com", "raft.github.io", "static.googleusercontent.com", "research.google",
    "www.allthingsdistributed.com", "www.google.com", "www.levels.fyi", "www.pramp.com", "interviewing.io",
    "docs.google.com", "gemini.google.com",
    "blog.algomaster.io", "blog.bytebytego.com", "newsletter.systemdesign.one", "newsletter.systemdesigncodex.com",
    "designgurus.substack.com", "read.engineerscodex.com",
}

print("\ncatalogue")
catalogue, problems = T.build_catalogue()
check("130 topics across six areas", len(catalogue) == 130, len(catalogue))
check("every topic has a search phrase", all(t in T.load_phrases() for t in catalogue),
      [t for t in catalogue if t not in T.load_phrases()])
thin = {t: len(e["lectures"]) for t, e in catalogue.items() if len(e["lectures"]) < 3}
check("every topic has 3+ verified lecture videos", not thin, thin)
check("every lecture is a watch?v= link", all(WATCH.match(v["url"]) for e in catalogue.values() for v in e["lectures"]))
dup = [t for t, e in catalogue.items() if len({v["url"] for v in e["lectures"]}) != len(e["lectures"])]
check("no topic lists the same video twice", not dup, dup)
# A lecture whose title shares no vocabulary with its topic is probably filed under the
# wrong one (the GATE planner had "RISC vs CISC" under a control-unit topic). The five
# topics below were hand-picked on 2026-09-25 because their only shared words -
# "system", "design", "interview", "coding" - are stopwords; each video was checked by eye.
HAND_PICKED = {"SD-1", "SD-11", "SD-17", "SD-24", "IC-2"}
offtopic = []
for tid, e in catalogue.items():
    if tid in HAND_PICKED:
        continue
    vocab = T.words(e["name"] + " " + e["phrase"])
    offtopic += [f"{tid}: {v['label'][:70]}" for v in e["lectures"] if not T.words(v["label"].split(" — ", 1)[-1]) & vocab]
check("every harvested lecture title shares vocabulary with its topic", not offtopic, offtopic[:5])
q = {t: len(e["questions"]) for t, e in catalogue.items() if len(e["questions"]) != 10}
check("every topic has exactly 10 interview questions", not q, q)
few = {t: len(e["problems"]) + len(e["practiceLinks"]) for t, e in catalogue.items()
       if len(e["problems"]) + len(e["practiceLinks"]) < 4 and e["area"] in ("DS", "AL")}
check("every DSA and theory topic has 4+ practice items", not few, few)
noread = [t for t, e in catalogue.items() if not (e["reading"] or e["newsletters"] or e["practiceLinks"])]
check("every topic has reading, a newsletter or a practice link", not noread, noread)
check("every topic names a note file", all(e["notes"] for e in catalogue.values()),
      [t for t, e in catalogue.items() if not e["notes"]])
tags = {t for e in catalogue.values() if e["area"] == "DS" for t in e["tags"]}
known = {"array", "hash-table", "math", "prefix-sum", "two-pointers", "sliding-window", "binary-search", "stack",
         "monotonic-stack", "queue", "monotonic-queue", "linked-list", "recursion", "divide-and-conquer", "sorting",
         "binary-tree", "tree", "depth-first-search", "breadth-first-search", "binary-search-tree",
         "heap-priority-queue", "backtracking", "graph", "topological-sort", "union-find", "shortest-path",
         "minimum-spanning-tree", "greedy", "sweep-line", "trie", "dynamic-programming", "memoization", "matrix",
         "string", "game-theory", "bitmask", "bit-manipulation", "number-theory", "segment-tree",
         "binary-indexed-tree", "string-matching", "rolling-hash", "biconnected-component", "eulerian-circuit",
         "design"}
check("DSA tags are real LeetCode tag slugs (checked 2026-09-25)", tags <= known, tags - known)

print("\nproblems")
check("500+ verified problems", len(problems) >= 500, len(problems))
check("every problem has a solution video", all(p["videos"] for p in problems.values()),
      [k for k, p in problems.items() if not p["videos"]])
check("premium problems all have a free LintCode alternative",
      all(p["alt"] and p["alt"].startswith("https://www.lintcode.com/problem/") for p in problems.values() if p["premium"]))
check("problem topics exist", all(p["topic"] in catalogue for p in problems.values()))
slug = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
check("slugs are well-formed", all(slug.match(p["slug"]) for p in problems.values()))

print("\nplan")
plan = server.parse_plan()
days = plan["days"]
check("504 plan days (72 weeks)", len(days) == 504 and days[-1]["dayNumber"] == 504, len(days))
ids = [t["id"] for d in days for t in d["tasks"]]
check("task ids are unique", len(ids) == len(set(ids)), [i for i, c in Counter(ids).items() if c > 1][:5])
check("every week has 9 sessions", all(c == 9 for c in Counter(i.split("-")[0] for i in ids).values()))
text = "\n".join(p.read_text(encoding="utf-8") for p in sorted((server.PLAN).glob("phase-*.md")))
bad_lc = sorted({f"LC-{n}" for n in T.PROBLEM_RE.findall(text)} - set(problems))
check("every LC-n in the plan is in problems.md", not bad_lc, bad_lc)
bad_t = sorted(set(T.TOPIC_RE.findall(text)) - set(catalogue))
check("every topic id in the plan exists", not bad_t, bad_t)
study = [t for d in days for t in d["tasks"] if not re.search(r"weekly review|contest", t["focus"], re.I)]
bare = [t["id"] for t in study if not t["topics"] and not t["problems"]
        and not re.search(r"mock|apply|debrief|full loop|mini-loop|light|taper|redo every|story bank|consolidation", t["focus"], re.I)]
check("every study session resolves to a topic or a problem", not bare, bare[:10])
share = sum(1 for t in study if t["topics"]) / len(study)
check(f"≥90% of study sessions carry topics ({share:.0%})", share >= 0.9)
used = {t for d in days for task in d["tasks"] for t in task["topics"]}
check("every topic is scheduled somewhere", used == set(catalogue), sorted(set(catalogue) - used))
for d in days:
    for task in d["tasks"]:
        for tid, cut in task["deal"].items():
            if len(cut["lidx"]) < 3 or len(cut["practice"]) < 4 and catalogue[tid]["area"] in ("DS", "AL"):
                check(f"{task['id']} {tid} gets 3 videos and 4+ practice", False, cut)
                break
check("every topic block gets 3 videos and (DSA/theory) 4+ practice problems", True)

print("\nlinks")
urls = []
for e in catalogue.values():
    urls += [x["url"] for x in e["lectures"] + e["reading"] + e["newsletters"] + e["practiceLinks"] + e["tagLinks"]]
for p in problems.values():
    urls += [p["url"]] + ([p["alt"]] if p["alt"] else []) + [v["url"] for v in p["videos"]]
for d in days:
    for task in d["tasks"]:
        urls += [x["url"] for x in task["links"] if "url" in x]
urls += [x["url"] for x in plan["common"]]
check("every link is https", all(u.startswith("https://") for u in urls), [u for u in urls if not u.startswith("https://")][:5])
check("no {placeholder} survived", not [u for u in urls if "{" in u])
check("no channel page or playlist anywhere", not [u for u in urls if T.CHANNEL_PAGE.search(u)],
      [u for u in urls if T.CHANNEL_PAGE.search(u)][:5])
hosts = {urlsplit(u).netloc for u in urls}
check("every link is on an allowed host", hosts <= ALLOWED_HOSTS, hosts - ALLOWED_HOSTS)

print("\nprompts")
allp = [p["text"] for ps in T.TOPIC_PROMPTS.values() for p in ps] + [p["text"] for p in T.PROBLEM_PROMPTS] + [T.QUESTION_PROMPT]
check("every prompt dictates its answer shape (says 'exactly')", all("exactly" in p.lower() for p in allp),
      [p[:60] for p in allp if "exactly" not in p.lower()])
check("every area has five topic prompts", all(len(v) == 5 for v in T.TOPIC_PROMPTS.values()))
check("the question prompt carries the question", "{question}" in T.QUESTION_PROMPT)
check("problem prompts carry the problem", all("{problem}" in p["text"] for p in T.PROBLEM_PROMPTS))
check("Gemini URL is AI Mode (the app ignores ?q=)", T.GEMINI_URL.startswith("https://www.google.com/search?udm=50&q="))

print(f"\n{'FAILED: ' + ', '.join(failures) if failures else 'all catalogue checks passed'}")
sys.exit(1 if failures else 0)
