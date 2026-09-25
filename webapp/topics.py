"""Topic and problem catalogue — joins the plan's tables, never repeats them.

Reads, all from plan/:

    curriculum-*.md      topic id, name, first week, note file, tags
    topic-lectures.md    the search phrase each topic's videos were found with
    topic-videos.md      verified lecture videos per topic      (generated)
    topic-reading.md     verified reading, newsletters, practice links per topic
    problems.md          every LeetCode problem the plan schedules, verified
    problem-videos.md    verified solution videos per problem   (generated)

A session is tied to topics and problems **only by ids written in its row** — `DS-6`,
`AL-14`, `LC-239`. There is no word-overlap guessing. The GATE planner guessed, and
filed "AVL rotations" under an English-grammar topic because both said "rotation".

Standard library only. Touches nothing outside plan/.
"""

import re
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "plan"

AREAS = {
    "DS": "DSA patterns",
    "AL": "Algorithms theory",
    "LD": "Object-oriented design",
    "SD": "System design",
    "BH": "Behavioural",
    "IC": "Interview craft",
}

WATCH = "https://www.youtube.com/watch?v={}"
YOUTUBE_SEARCH = "https://www.youtube.com/results?search_query={}"
LEETCODE = "https://leetcode.com/problems/{}/"
LEETCODE_TAG = "https://leetcode.com/problem-list/{}/"
# A topic row offers individual videos. A channel page and a playlist both hand over a
# list to sift instead of the video that teaches the topic.
CHANNEL_PAGE = re.compile(r"youtube\.com/(@|channel/|c/)|[?&]list=")

TOPIC_ID = r"(?:DS|AL|LD|SD|BH|IC)-\d+"
TOPIC_RE = re.compile(rf"\b({TOPIC_ID})\b")
PROBLEM_RE = re.compile(r"\bLC-(\d+)\b")
ROW_RE = re.compile(rf"^\|\s*({TOPIC_ID})\s*\|(.+)\|\s*$")
PROBLEM_ROW = re.compile(r"^\|\s*LC-(\d+)\s*\|(.+)\|\s*$")
VIDEO_RE = re.compile(
    rf"^\|\s*({TOPIC_ID}|LC-\d+)\s*\|\s*([A-Za-z0-9_-]{{11}})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$")
READING_RE = re.compile(
    rf"^\|\s*({TOPIC_ID})\s*\|\s*(read|newsletter|practice)\s*\|\s*([^|]+?)\s*\|\s*(https://\S+?)\s*\|\s*$")

STOPWORDS = {
    "a", "an", "and", "the", "of", "to", "in", "on", "for", "with", "vs", "or", "by",
    "from", "its", "it", "as", "at", "into", "via", "per", "that", "this", "these",
    "then", "than", "not", "no", "is", "are", "be", "using", "use", "used", "each",
    "one", "two", "all", "any", "only", "also", "up", "out", "how", "what", "why",
    "lecture", "lectures", "explained", "explanation", "tutorial", "interview",
    "interviews", "coding", "problem", "problems", "pattern", "patterns", "design",
    "system", "leetcode", "question", "questions", "series", "course", "part",
    "video", "introduction", "intro", "complete", "guide", "easy", "simple", "best",
    "week", "day", "notes", "note", "practice", "data", "structure", "structures",
    "algorithm", "algorithms", "based", "technique", "techniques", "example", "examples",
}


def words(text):
    """Lowercase significant words, with crude singulars and US/UK spelling variants."""
    out = set()
    for raw in re.split(r"[^a-z0-9+]+", text.lower()):
        if len(raw) < 3 or raw in STOPWORDS:
            continue
        out.add(raw)
        for a, b in (("isation", "ization"), ("ise", "ize"), ("yse", "yze"), ("our", "or")):
            if a in raw:
                out.add(raw.replace(a, b))
        if raw.endswith("ies") and len(raw) > 4:
            out.add(raw[:-3] + "y")
        elif raw.endswith("es") and len(raw) > 4:
            out.add(raw[:-2])
        if raw.endswith("s") and not raw.endswith("ss"):
            out.add(raw[:-1])
    return out


def _cells(body):
    return [c.strip() for c in body.split("|")]


def _lines(name):
    path = PLAN / name
    return path.read_text(encoding="utf-8").splitlines() if path.exists() else []


def load_curriculum():
    """Topic id -> {id, area, areaName, name, week, notes, tags} in file order."""
    topics = {}
    for path in sorted(PLAN.glob("curriculum-*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            m = ROW_RE.match(line)
            if not m:
                continue
            cells = _cells(m.group(2))
            if len(cells) < 4:
                continue
            tid = m.group(1)
            name, week, notes, tags = cells[0], cells[1], cells[2].strip("`"), cells[3]
            topics[tid] = {
                "id": tid,
                "area": tid[:2],
                "areaName": AREAS[tid[:2]],
                "name": name,
                "week": int(week) if week.isdigit() else None,
                "notes": notes if notes.endswith(".md") else None,
                "tags": [t.strip() for t in tags.split(",") if t.strip() and t.strip() != "—"],
            }
    return topics


def load_phrases():
    phrases = {}
    for line in _lines("topic-lectures.md"):
        m = ROW_RE.match(line)
        if m:
            phrases[m.group(1)] = _cells(m.group(2))[0]
    return phrases


def load_problems():
    """'LC-<n>' -> {key, num, title, difficulty, topic, slug, url, alt, premium}."""
    problems = {}
    for line in _lines("problems.md"):
        m = PROBLEM_ROW.match(line)
        if not m:
            continue
        cells = _cells(m.group(2))
        if len(cells) < 5:
            continue
        title, diff, topic, slug, alt = cells[:5]
        key = f"LC-{m.group(1)}"
        alt = alt if alt.startswith("https://") else None
        problems[key] = {
            "key": key, "num": int(m.group(1)), "title": title, "difficulty": diff,
            "topic": topic, "slug": slug, "url": LEETCODE.format(slug),
            "alt": alt, "premium": bool(alt),
        }
    return problems


def _read_videos(name):
    videos = {}
    for line in _lines(name):
        m = VIDEO_RE.match(line)
        if m:
            videos.setdefault(m.group(1), []).append(
                {"id": m.group(2), "channel": m.group(3), "title": m.group(4)})
    return videos


def load_topic_videos():
    return _read_videos("topic-videos.md")


def load_problem_videos():
    return _read_videos("problem-videos.md")


def load_questions():
    """Topic id -> [question, ...] from plan/topic-questions.md."""
    qs = {}
    for line in _lines("topic-questions.md"):
        m = ROW_RE.match(line)
        if m:
            qs.setdefault(m.group(1), []).append(_cells(m.group(2))[0])
    return qs


def load_reading():
    """Topic id -> {'read': [...], 'newsletter': [...], 'practice': [...]} of {label, url}."""
    reading = {}
    for line in _lines("topic-reading.md"):
        m = READING_RE.match(line)
        if m:
            reading.setdefault(m.group(1), {}).setdefault(m.group(2), []).append(
                {"label": m.group(3), "url": m.group(4)})
    return reading


SHORT_MAX = 46


def short_name(name):
    """The topic, not its detail list: cut at the dash, then at a comma that fits."""
    head = name.split(" — ")[0].split("(")[0].strip().rstrip(",;")
    if len(head) <= SHORT_MAX:
        return head
    cut = head.rfind(",", 0, SHORT_MAX)
    if cut < 12:
        cut = head.rfind(" ", 0, SHORT_MAX)
    return (head[:cut].rstrip(",; ") if cut > 12 else head[:SHORT_MAX].rstrip()) + "…"


def build_catalogue():
    """(topics, problems) ready to attach to sessions."""
    curriculum = load_curriculum()
    phrases = load_phrases()
    videos = load_topic_videos()
    reading = load_reading()
    questions = load_questions()
    problems = load_problems()
    pvideos = load_problem_videos()

    by_topic = {}
    for p in problems.values():
        by_topic.setdefault(p["topic"], []).append(p["key"])

    catalogue = {}
    for tid, t in curriculum.items():
        entry = dict(t)
        entry["phrase"] = phrases.get(tid, t["name"])
        entry["short"] = short_name(t["name"])
        entry["lectures"] = [
            {"label": f"{v['channel']} — {v['title']}", "url": WATCH.format(v["id"]),
             "kind": "video", "video": True}
            for v in videos.get(tid, [])
        ]
        entry["search"] = {"label": f'YouTube: "{entry["phrase"]}"',
                           "url": YOUTUBE_SEARCH.format(quote_plus(entry["phrase"])), "kind": "video"}
        rd = reading.get(tid, {})
        entry["reading"] = [dict(r, kind="material") for r in rd.get("read", [])]
        entry["newsletters"] = [dict(r, kind="material") for r in rd.get("newsletter", [])]
        entry["practiceLinks"] = [dict(r, kind="practice") for r in rd.get("practice", [])]
        entry["questions"] = questions.get(tid, [])
        # Problems that exercise this topic: its own, or for a theory / design topic the
        # DSA topics its Tag column names.
        own = list(by_topic.get(tid, []))
        if not own:
            for tag in t["tags"]:
                own += by_topic.get(tag, [])
        entry["problems"] = own
        if t["area"] == "DS":
            entry["tagLinks"] = [{"label": f"LeetCode list: {tag}", "url": LEETCODE_TAG.format(tag), "kind": "practice"}
                                 for tag in t["tags"]]
        else:
            entry["tagLinks"] = []
        catalogue[tid] = entry

    for key, p in problems.items():
        p["videos"] = [
            {"label": f"{v['channel']} — {v['title']}", "url": WATCH.format(v["id"]),
             "kind": "video", "video": True}
            for v in pvideos.get(key, [])
        ]
    return catalogue, problems


def session_refs(text, catalogue, problems):
    """(topic ids, problem keys) named in a session's cells, in order of appearance."""
    probs = []
    for num in PROBLEM_RE.findall(text):
        key = f"LC-{num}"
        if key in problems and key not in probs:
            probs.append(key)
    tids = []
    for tid in TOPIC_RE.findall(text):
        if tid in catalogue and tid not in tids:
            tids.append(tid)
    # A lunch drill names a problem and, in brackets, its topic. Make sure every
    # problem's topic is present even if the row forgot to say it.
    for key in probs:
        t = problems[key]["topic"]
        if t in catalogue and t not in tids:
            tids.append(t)
    return tids, probs


VIDEOS_PER_SESSION = 3
PRACTICE_PER_SESSION = 5


def deal(ordered_days, catalogue, problems):
    """Give every topic block three videos and five practice problems.

    Each time a topic recurs, the next three of its verified videos are offered, so
    two sessions on the same topic do not repeat the same links; once a topic's
    videos are all used they come round again, marked as a rewatch. Practice follows
    the same rotation over the topic's problems, skipping any the session itself
    already names, so the list is always extra work rather than the same problems.
    """
    seen = {}
    for day in ordered_days:
        for task in day["tasks"]:
            cut = {}
            for tid in task["topics"]:
                entry = catalogue[tid]
                k = seen.get(tid, 0)
                seen[tid] = k + 1
                lec = entry["lectures"]
                idx, rewatch = [], False
                if lec:
                    start = (k * VIDEOS_PER_SESSION) % len(lec)
                    rewatch = k * VIDEOS_PER_SESSION >= len(lec)
                    for i in range(min(VIDEOS_PER_SESSION, len(lec))):
                        idx.append((start + i) % len(lec))
                pool = [p for p in entry["problems"] if p not in task["problems"]]
                pidx = []
                if pool:
                    start = (k * PRACTICE_PER_SESSION) % len(pool)
                    for i in range(min(PRACTICE_PER_SESSION, len(pool))):
                        pidx.append(pool[(start + i) % len(pool)])
                cut[tid] = {"lidx": idx, "rewatch": rewatch, "practice": pidx, "visit": k + 1}
            task["deal"] = cut


def public(entry):
    return {k: v for k, v in entry.items() if not k.startswith("_")}


# ---------------------------------------------------------------------------
# Assistant prompts
# ---------------------------------------------------------------------------
#
# Two rules carried over from the GATE planner, both learned the hard way:
#
# 1. gemini.google.com ignores ?q= and ?prompt= (tested: the input box stays empty).
#    Google AI Mode (udm=50) is the same model and does read the URL, and the query
#    survives to at least 2044 characters - hence PROMPT_URL_MAX. The Canvas prompt is
#    the exception: Canvas lives only in the Gemini app, so that button copies the
#    prompt and opens gemini.google.com for a paste.
# 2. Every prompt dictates its answer shape. An ask without one returns an essay that
#    cannot be pasted into a notes file at 13:40 with five minutes of lunch left. A
#    test asserts each prompt contains the word "exactly".
#
# Templates ship once and are interpolated in the browser with the session context.

GEMINI_URL = "https://www.google.com/search?udm=50&q={q}"
GEMINI_APP = "https://gemini.google.com/app"
PROMPT_URL_MAX = 1900

# Who is asking. Read from webapp/profile.json so a copy of this repo speaks for its
# own owner (scripts/setup_own_copy.py rewrites it); these are the fallbacks.
PROFILE_FILE = Path(__file__).resolve().parent / "profile.json"
PROFILE_DEFAULT = {
    "head": ("I am preparing for the Google software engineer interview, writing C++. "
             "Answer as a Google interviewer and coach would: precise, terse, no encouragement, "
             "no filler."),
    "situation": "I study about 10 hours a week, so I need answers I can use in a 45-minute slot.",
}


def load_profile():
    import json
    try:
        data = json.loads(PROFILE_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        data = {}
    return {k: str(data.get(k) or v) for k, v in PROFILE_DEFAULT.items()}


GEMINI_HEAD = load_profile()["head"]

# Per topic area: the five asks shown under each topic block.
TOPIC_PROMPTS = {
    "DS": [
        {"label": "Make notes", "icon": "notes", "text":
            "Write my pattern note for this topic in exactly this structure and nothing else:\n\n"
            "## <pattern>\n### Recognise it\n- the 3-5 signals in a problem statement that mean this pattern\n"
            "### C++ template\n```cpp\n// the reusable skeleton, commented\n```\n"
            "### Complexity\n- time and space, and why\n### Variations\n- each variation, one line, one LeetCode example\n"
            "### Traps\n- the off-by-one or edge case that fails hidden tests\n\n"
            "Plain markdown, no preamble, no closing remarks."},
        {"label": "Mock interview me", "icon": "practice", "text":
            "Act as a Google interviewer. Give me exactly one unseen problem on this topic at Google L4 "
            "difficulty, stated the way Google states it: slightly vague, no constraints given unless I ask. "
            "Then stop and wait. Do not print hints, the approach, or a solution. Answer my clarifying "
            "questions in one line each. When I paste code, reply with exactly: 1) correct or not, with the "
            "failing input if not; 2) time and space; 3) a Google rubric score (Strong No Hire to Strong Hire) "
            "for coding, algorithms, communication; 4) the one thing to fix."},
        {"label": "Explain it", "icon": "video", "text":
            "Explain this topic in exactly these sections:\n1. Core idea - 5 lines maximum\n"
            "2. A worked example with an ASCII diagram of the data structure at each step\n"
            "3. Why it is correct - the invariant, in two lines\n"
            "4. The three hardest interview variations - what changes and the one move that cracks each\n"
            "I write production code daily; skip history and motivation."},
        {"label": "Where did I go wrong", "icon": "error", "text":
            "I will paste a problem, my C++ code, and the failing test or the verdict. Reply in exactly this form:\n"
            "1. What the problem actually asks - one line\n2. The bug or wrong idea - quote the line\n"
            "3. The concept I am missing - three words\n4. The rule for next time - one line\n"
            "5. One similar problem to retry now - name only\n"
            "Do not rewrite my whole solution unless I ask. Wait for me to paste it."},
        {"label": "Ask anything", "icon": "gem", "text":
            "That is what I am working on. I will ask follow-ups. Answer every one in exactly this shape: "
            "the direct answer in one line; then at most 5 lines of why; complexity stated for anything "
            "algorithmic; C++ for any code. No preamble, no summary. Wait for my first question."},
    ],
    "AL": [
        {"label": "Make notes", "icon": "notes", "text":
            "Write my theory note in exactly this structure and nothing else:\n\n"
            "## <topic>\n### Definitions\n- precise, with every symbol defined\n"
            "### Key result\n- the theorem or property, then the proof idea in at most 4 lines\n"
            "### Complexity table\n| operation | best | average | worst | space |\n"
            "### Diagram\nan ASCII diagram of the structure or the algorithm mid-run\n"
            "### Interview follow-ups\n- the 3 questions an interviewer asks about this, each with a 2-line answer\n\n"
            "Plain markdown, no preamble."},
        {"label": "Quiz me", "icon": "practice", "text":
            "Ask me exactly 5 questions on this theory, one at a time, the way a Google interviewer probes "
            "after a coding answer (\"what is the worst case\", \"prove it\", \"what if memory is limited\"). "
            "Wait for my answer after each. After each answer reply with exactly: correct / partly / wrong, "
            "the missing piece in one line, then the next question. After question 5, a one-line verdict."},
        {"label": "Explain it", "icon": "video", "text":
            "Explain this in exactly these sections:\n1. Intuition - 5 lines\n"
            "2. Step-by-step on a small example, with an ASCII diagram at every step\n"
            "3. Proof sketch - the key invariant or argument\n4. Where it shows up in real systems and in interview problems\n"
            "Skip history."},
        {"label": "Compare", "icon": "error", "text":
            "Build exactly one comparison table for this topic against its closest alternatives: rows are the "
            "alternatives, columns are time complexity, space, when to use, when it breaks, and a C++ STL or "
            "library equivalent. Then 3 lines on how to choose in an interview. Nothing else."},
        {"label": "Ask anything", "icon": "gem", "text":
            "That is the theory I am studying. I will ask follow-ups. Answer every one in exactly this shape: "
            "the direct answer in one line; at most 5 lines of why; a tiny example if it helps. No preamble. "
            "Wait for my first question."},
    ],
    "LD": [
        {"label": "Make notes", "icon": "notes", "text":
            "Write my object-oriented design note in exactly this structure:\n\n## <topic>\n"
            "### Requirements I would clarify\n- bullets\n### Class diagram\nASCII class diagram with relationships\n"
            "### Core interfaces (C++)\n```cpp\n// headers only\n```\n### Patterns used and why\n- pattern: the reason in one line\n"
            "### Concurrency\n- what is shared, what locks it\n### Extension\n- requirement N+1 and which classes change\n\n"
            "No preamble."},
        {"label": "Mock interview me", "icon": "practice", "text":
            "Act as a Google interviewer running an object-oriented design question on this topic. State the "
            "problem in two vague lines and wait. Answer clarifying questions in one line each. When I paste my "
            "classes, reply with exactly: 1) the design smell you see first; 2) a missing requirement I ignored; "
            "3) one extension request to test my design; 4) a hire / no-hire signal with one reason."},
        {"label": "Explain it", "icon": "video", "text":
            "Explain this in exactly these sections:\n1. The problem it solves - 3 lines\n"
            "2. ASCII class diagram\n3. Minimal C++ example that compiles\n"
            "4. When NOT to use it\n5. How it appears in an interview design question"},
        {"label": "Review my design", "icon": "error", "text":
            "I will paste my C++ classes. Review them in exactly this form: 1) SOLID violations, each quoted; "
            "2) coupling problems; 3) thread-safety bugs; 4) the single refactor with the biggest payoff, "
            "shown as a diff. Nothing else. Wait for me to paste."},
        {"label": "Ask anything", "icon": "gem", "text":
            "That is the design topic I am working on. Answer each of my follow-ups in exactly this shape: "
            "one-line answer, at most 5 lines of why, C++ for any code. Wait for my first question."},
    ],
    "SD": [
        {"label": "Make notes", "icon": "notes", "text":
            "Write my system design note in exactly this structure:\n\n## <topic>\n"
            "### Requirements\nfunctional and non-functional, with numbers\n### Estimation\nQPS, storage, bandwidth, shown as arithmetic\n"
            "### API\n### Data model\n### High-level design\nASCII box-and-arrow diagram, then one request traced through it\n"
            "### Deep dives\ntwo, each with the trade-off named\n### Bottlenecks and failures\n\nNo preamble."},
        {"label": "Mock interview me", "icon": "practice", "text":
            "Act as a Google system design interviewer for this topic. Give me the prompt in one line, then "
            "wait. Answer clarifying questions briefly with realistic numbers. After each stage I post, reply "
            "with exactly: what is good in one line, the gap in one line, and your next probing question. "
            "At the end: a level assessment (L3/L4/L5) with the two reasons."},
        {"label": "Explain it", "icon": "video", "text":
            "Explain this in exactly these sections:\n1. The core problem - 3 lines\n"
            "2. ASCII architecture diagram\n3. How it works step by step, one request traced end to end\n"
            "4. The trade-offs, as a table\n5. How Google does it (GFS, Bigtable, Spanner, Borg, etc.) where relevant"},
        {"label": "Estimate with me", "icon": "error", "text":
            "Do a back-of-the-envelope estimate for this system in exactly this form: assumptions as a list, "
            "then QPS (average and peak), storage per day and per 5 years, bandwidth, and memory for cache, "
            "each as one line of arithmetic. Then the one number that drives the design."},
        {"label": "Ask anything", "icon": "gem", "text":
            "That is the design I am working on. Answer each follow-up in exactly this shape: one-line answer, "
            "at most 5 lines of why, a number wherever a number exists. Wait for my first question."},
    ],
    "BH": [
        {"label": "Make notes", "icon": "notes", "text":
            "Write my note on this behavioural area in exactly this structure:\n## <area>\n"
            "### What Google is scoring\n- bullets\n### Questions they ask\n- 8 real phrasings\n"
            "### What a strong answer shows\n- bullets\n### Red flags\n- bullets\nNo preamble."},
        {"label": "Mock interview me", "icon": "practice", "text":
            "Act as a Google Googleyness and Leadership interviewer. Ask me exactly one question on this area "
            "and wait. After my answer, ask two follow-ups one at a time, the way Google digs. Then reply "
            "with exactly: STAR completeness, the signal I gave, the signal I missed, a score from 1 to 4."},
        {"label": "Shape my story", "icon": "video", "text":
            "I will paste a rough story from my work (senior engineer, distributed systems, Python/Go/K8s). "
            "Rewrite it in exactly STAR form: Situation (2 lines), Task (1 line), Action (4-6 bullets, all "
            "\"I\"), Result (a number, then the learning). Under 250 words. Then list 3 follow-up questions "
            "an interviewer will ask. Wait for me to paste it."},
        {"label": "Critique my answer", "icon": "error", "text":
            "I will paste my spoken answer. Reply in exactly this form: 1) timing estimate; 2) where I said "
            "\"we\" instead of \"I\"; 3) the missing result or number; 4) one sentence to cut; 5) a 1-4 score. "
            "Wait for me to paste."},
        {"label": "Ask anything", "icon": "gem", "text":
            "Answer my questions about Google behavioural interviews in exactly this shape: one-line answer, "
            "at most 5 lines of why. Wait for my first question."},
    ],
}
TOPIC_PROMPTS["IC"] = TOPIC_PROMPTS["BH"][:1] + [
    {"label": "Mock interview me", "icon": "practice", "text":
        "Run exactly one 45-minute Google coding interview with me, turn by turn. Give a vague problem and "
        "wait. Answer my clarifying questions in one line. Do not give the approach. When I finish, reply "
        "with exactly the four Google rubric scores (coding, algorithms, communication, problem solving), "
        "each Strong No Hire to Strong Hire with one line of evidence."},
] + TOPIC_PROMPTS["DS"][2:]

# Per interview question: {question} is replaced in the browser.
QUESTION_PROMPT = (
    "A Google interviewer asks me: \"{question}\"\n"
    "Answer in exactly this structure:\n"
    "1. The answer in one or two sentences - what I should say first\n"
    "2. Explanation - at most 8 lines, precise\n"
    "3. Diagram or worked example - an ASCII diagram or a small concrete example; C++ if code helps\n"
    "4. Complexity or trade-offs - a short table where there is more than one option\n"
    "5. The follow-up the interviewer will ask next, and a two-line answer to it\n"
    "No preamble, no encouragement."
)

# Per problem: shown on every LC-<n> card. {problem} is replaced in the browser with
# "LC-239 Sliding Window Maximum (Hard)".
PROBLEM_PROMPTS = [
    {"label": "Visual walkthrough", "icon": "video", "target": "search", "text":
        "Teach me {problem} (LeetCode) in depth, visually. Use exactly this structure:\n"
        "1. The problem in 2 lines, and the pattern it belongs to\n"
        "2. Brute force - idea and complexity, 3 lines\n"
        "3. The key insight that makes it fast, in one sentence\n"
        "4. Dry run on a small example: for EVERY step, an ASCII diagram of the array / pointers / stack / "
        "tree / table, with an arrow for what changed, and one line saying why\n"
        "5. Final C++ solution, commented line by line\n"
        "6. Time and space complexity, with the reasoning\n"
        "7. Edge cases the hidden tests check\n"
        "8. Two follow-up questions Google would ask, with short answers"},
    {"label": "Hint ladder", "icon": "practice", "target": "search", "text":
        "I am solving {problem} (LeetCode) and I am stuck. Give me exactly one hint and stop. Hints go in "
        "this order and you give the next only when I say next: 1) which pattern, 2) what to store, "
        "3) the invariant, 4) the loop skeleton in pseudocode. Never print the full solution unless I "
        "type: solution."},
    {"label": "Review my code", "icon": "error", "target": "search", "text":
        "Review my C++ solution to {problem} (LeetCode) as a Google interviewer. I will paste it next. "
        "Reply in exactly this form: 1) correct or not, with a failing input; 2) time and space; "
        "3) naming and readability issues, quoted; 4) the edge case I missed; 5) Google rubric score. "
        "Wait for my code."},
    {"label": "Animate it (Gemini Canvas)", "icon": "gem", "target": "app", "text":
        "Use Canvas. Build a single-page interactive visualisation of the optimal solution to {problem} "
        "(LeetCode). Requirements, exactly: an editable input box prefilled with the example; Step, Back, "
        "Play and Reset buttons; the data structure drawn visually (array cells, pointers as arrows, stack "
        "or queue boxes, tree nodes, DP table) and updated at every step; the current line of C++ code "
        "highlighted beside it; a text panel explaining what just happened and why; the variables' current "
        "values in a table. Use plain HTML, CSS and JavaScript."},
]
