"""Google interview prep planner — local web server.

Reads the day-by-day tables in plan/phase-*.md, serves the single-page planner, and
stores ticks in webapp/progress.json and the calendar in webapp/schedule.json.
Standard library only.

Run:  python webapp/server.py        (or double-click webapp/start.bat)
Open: http://127.0.0.1:8766
"""

import datetime as dt
import json
import os
import re
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

HOST = "127.0.0.1"
PORT = int(os.environ.get("PREP_PLANNER_PORT", "8766"))   # GATE's planner uses 8765
WEBAPP = Path(__file__).resolve().parent
ROOT = WEBAPP.parent
PLAN = ROOT / "plan"
PROGRESS_FILE = WEBAPP / "progress.json"
DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
TOTAL_WEEKS = 72
WRITE_LOCK = threading.Lock()

sys.path.insert(0, str(WEBAPP))
import gitsync  # noqa: E402
import schedule  # noqa: E402
import topics as T  # noqa: E402

# ---------------------------------------------------------------------------
# Links named in a session's Resource cell. Explicit, short, and nothing else:
# the GATE planner guessed links from free text and emitted a channel page when a
# guess fell through. A Resource the table below does not name renders as text.
# ---------------------------------------------------------------------------

PRAMP = "https://www.pramp.com/"
INTERVIEWING_IO = "https://interviewing.io/"
RESOURCE_LINKS = {
    "LeetCode contest": [{"label": "LeetCode contests", "url": "https://leetcode.com/contest/", "kind": "practice"}],
    "Mock platform": [{"label": "Pramp (free peer mocks)", "url": PRAMP, "kind": "practice"},
                      {"label": "interviewing.io", "url": INTERVIEWING_IO, "kind": "practice"}],
    "Google Doc": [{"label": "New Google Doc (code here, no IDE)", "url": "https://docs.google.com/document/create", "kind": "tool"}],
    "Story template": [{"label": "Story template", "path": "plan/curriculum-behavioral.md", "kind": "file"}],
}

SLOT_LABELS = {
    "Lunch": ("Lunch drill", "13:00–13:45"),
    "14:00–16:00": ("Learn block", "14:00–16:00"),
    "16:15–18:00": ("Practice block", "16:15–18:00"),
    "08:00–09:30": ("Contest", "08:00–09:30"),
    "09:45–10:15": ("Weekly review", "09:45–10:15"),
}


def slot_label(slot, focus):
    label, time = SLOT_LABELS.get(slot, ("Session", slot))
    f = focus.lower()
    if f.startswith("theory"):
        label = "Theory lunch"
    elif f.startswith("redo cold"):
        label = "Redo lunch"
    elif f.startswith("read for"):
        label = "Reading lunch"
    elif f.startswith("story drafting"):
        label = "Story lunch"
    elif f.startswith("build project"):
        label = "Project block"
    elif f.startswith("mock") or "mock interview" in f or f.startswith("full loop"):
        label = "Mock interview"
    return label, time


PHASES = {1: ("foundations", 1), 2: ("core-patterns", 9), 3: ("dp-advanced", 25), 4: ("ood", 39),
          5: ("system-design", 45), 6: ("google-loop", 57), 7: ("final-sprint", 67)}


def phase_of_week(week):
    return max(p for p, (_, w) in PHASES.items() if week >= w) if week >= 1 else 1


# ---------------------------------------------------------------------------
# Plan parser
# ---------------------------------------------------------------------------

ROW_RE = re.compile(r"^\| (Mon|Tue|Wed|Thu|Fri|Sat|Sun) \| ([^|]+) \| (.+) \| ([^|]+) \| ([^|]+) \|\s*$")
WEEK_RE = re.compile(r"^### Week (\d+) — (.+)$")
EDITABLE = ("notes/", "trackers/", "reviews/", "daily-logs/", "plan/", "projects/")


def file_links(cell):
    """Backticked .md paths in a cell become in-planner edit links."""
    out = []
    for ref in re.findall(r"`([^`]+)`", cell):
        if ref.endswith(".md") and ref.startswith(EDITABLE):
            out.append({"label": Path(ref).name, "path": ref, "kind": "file"})
    return out


def parse_plan():
    catalogue, problems = T.build_catalogue()
    phases, days = [], {}
    for pf in sorted(PLAN.glob("phase-*.md")):
        lines = pf.read_text(encoding="utf-8").splitlines()
        m = re.match(r"^# Phase (\d+) — (.+?) \(Weeks", lines[0])
        phase = {"number": int(m.group(1)), "title": m.group(2), "file": f"plan/{pf.name}", "weeks": []}
        phases.append(phase)
        week = None
        for line in lines:
            wm = WEEK_RE.match(line)
            if wm:
                week = {"number": int(wm.group(1)), "title": wm.group(2).strip(), "meta": "", "notes": []}
                phase["weeks"].append(week)
                continue
            if week is None:
                continue
            if line.startswith("## "):
                week = None
                continue
            if line.startswith("**Hours"):
                week["meta"] = line.strip()
                continue
            rm = ROW_RE.match(line)
            if not rm:
                continue
            day, slot, focus, resource, output = [g.strip() for g in rm.groups()]
            label, time = slot_label(slot, focus)
            slot_id = "L" if slot == "Lunch" else re.sub(r"[^0-9]", "", slot)[:4]
            tids, probs = T.session_refs(focus + " " + output, catalogue, problems)
            if re.search(r"weekly review", focus, re.I):
                tids, probs = [], []
            links = list(RESOURCE_LINKS.get(resource, []))
            task = {
                "id": f"w{week['number']}-{day}-{slot_id}",
                "slot": label, "time": time, "focus": focus,
                "links": links,
                "outputs": file_links(output),
                "outputText": output if output not in ("—", "-") else "",
                "topics": tids, "problems": probs,
            }
            n = (week["number"] - 1) * 7 + DAY_NAMES.index(day) + 1
            if n not in days:
                days[n] = {"dayNumber": n, "weekday": day, "week": week["number"],
                           "phase": phase["number"], "tasks": []}
            days[n]["tasks"].append(task)
    ordered = [days[k] for k in sorted(days)]
    T.deal(ordered, catalogue, problems)
    used_t = sorted({t for d in ordered for task in d["tasks"] for t in task["topics"]})
    used_p = {p for d in ordered for task in d["tasks"] for p in task["problems"]}
    for d in ordered:
        for task in d["tasks"]:
            for cut in task["deal"].values():
                used_p.update(cut["practice"])
    return {
        "totalWeeks": TOTAL_WEEKS,
        "phases": phases,
        "days": ordered,
        "topics": {t: T.public(catalogue[t]) for t in used_t},
        "problems": {k: problems[k] for k in sorted(used_p, key=lambda k: int(k[3:]))},
        "prompts": {
            "head": T.GEMINI_HEAD,
            "topic": T.TOPIC_PROMPTS,
            "problem": T.PROBLEM_PROMPTS,
            "question": T.QUESTION_PROMPT,
            "url": T.GEMINI_URL,
            "app": T.GEMINI_APP,
            "max": T.PROMPT_URL_MAX,
        },
        "common": [
            {"label": "LeetCode problem set", "url": "https://leetcode.com/problemset/", "kind": "practice"},
            {"label": "Google: how we hire", "url": "https://www.google.com/about/careers/applications/how-we-hire/", "kind": "material"},
            {"label": "Tech Interview Handbook", "url": "https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/", "kind": "material"},
            {"label": "System Design Primer", "url": "https://github.com/donnemartin/system-design-primer", "kind": "material"},
        ],
    }


# ---------------------------------------------------------------------------
# Files created from templates. lib/templates.js is the browser twin of this
# section; tests/parity.mjs asserts both produce identical bytes.
# ---------------------------------------------------------------------------

ALLOWED_DIRS = ("notes", "trackers", "reviews", "daily-logs", "plan", "docs", "projects")

NOTE_SKELETONS = {
    "dsa": "# {title}\n\n## Recognise it\n- \n\n## C++ template\n```cpp\n```\n\n## Complexity\n\n"
           "## Variations\n\n## Traps\n\n## Problems solved (LC number, time, first try Y/N)\n",
    "theory": "# {title}\n\n## Definitions\n\n## Key result and proof idea\n\n## Complexity table\n\n"
              "| operation | best | average | worst | space |\n|---|---|---|---|---|\n\n## Diagram\n\n"
              "## Interview follow-ups and my answers\n",
    "lld": "# {title}\n\n## Requirements I would clarify\n\n## Class diagram\n\n## Core interfaces (C++)\n"
           "```cpp\n```\n\n## Patterns used and why\n\n## Concurrency\n\n## Extension: requirement N+1\n",
    "system-design": "# {title}\n\n## Requirements (functional, non-functional with numbers)\n\n## Estimation\n\n"
                     "## API\n\n## Data model\n\n## High-level design\n\n## Deep dives\n\n## Bottlenecks and failures\n",
    "behavioral": "# {title}\n\n## What Google scores here\n\n## Questions\n\n## My story for this (link)\n\n"
                  "## Red flags to avoid\n",
    "interview": "# {title}\n\n## What matters\n\n## My checklist\n\n## Notes from mocks\n",
}
NOTE_DEFAULT = "# {title}\n\n## Notes\n"


def note_title(path):
    stem = Path(path).stem
    parts = stem.split("-", 2)
    tail = parts[2] if len(parts) == 3 else parts[-1]
    words = tail.replace("-", " ")
    return words[:1].upper() + words[1:]


def note_skeleton(path):
    folder = path.split("/")[1] if path.count("/") >= 2 else ""
    return NOTE_SKELETONS.get(folder, NOTE_DEFAULT).replace("{title}", note_title(path))


def safe_path(rel):
    rel = rel.replace("\\", "/").lstrip("/")
    target = (ROOT / rel).resolve()
    if ROOT not in target.parents or target.suffix != ".md" or ".." in rel.split("/"):
        return None
    if target.relative_to(ROOT).parts[0] not in ALLOWED_DIRS:
        return None
    return target


def create_if_missing(target):
    if target.exists():
        return False
    rel = target.relative_to(ROOT).as_posix()
    if rel.startswith("notes/"):
        text = note_skeleton(rel)
    elif rel.startswith("reviews/weekly/"):
        text = (ROOT / "reviews/weekly/TEMPLATE.md").read_text(encoding="utf-8")
    elif rel.startswith("reviews/monthly/"):
        text = (ROOT / "reviews/monthly/TEMPLATE.md").read_text(encoding="utf-8")
    else:
        return None
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return True


def daily_log_text(date_str, sched):
    """The Markdown a new daily log starts from. Pure: reads only the template."""
    date = dt.date.fromisoformat(date_str)
    n = schedule.day_of(date_str, sched)
    n = n or 0
    week = (n - 1) // 7 + 1 if n >= 1 else 0
    phase = phase_of_week(week)
    weekday = date.strftime("%A")
    plan_weekday = DAY_NAMES[(n - 1) % 7] if n >= 1 else "-"
    hours = {"Sat": "3.75", "Sun": "2.0"}.get(plan_weekday, "0.75")
    text = (ROOT / "daily-logs" / "TEMPLATE.md").read_text(encoding="utf-8")
    fields = {
        "date": date.isoformat(),
        "day_of_week": weekday,
        "plan_day": str(n),
        "plan_weekday": plan_weekday,
        "phase": PHASES[phase][0],
        "overall_week": str(week),
        "target_hours": hours,
    }
    for key, value in fields.items():
        text = re.sub(rf"^{key}: .*$", f"{key}: {value}", text, count=1, flags=re.M)
    return text


PROGRESS_START = "<!-- planner-progress:start -->"
PROGRESS_END = "<!-- planner-progress:end -->"


def progress_block(day, done, stamp):
    """The planner checklist snapshot for one day. Pure."""
    completed = sum(bool(done.get(t["id"])) for t in day["tasks"])
    lines = [PROGRESS_START, "## Planner progress",
             f"Saved from the planner: {stamp}. **{completed}/{len(day['tasks'])} sessions completed.**", ""]
    for t in day["tasks"]:
        mark = "x" if done.get(t["id"]) else " "
        focus = re.sub(r"`([^`]+)`", r"\1", t["focus"])
        lines.append(f"- [{mark}] **{t['slot']} ({t['time']})** — {focus}")
        if t["outputText"]:
            lines.append(f"  - Record: {t['outputText']}")
    lines += ["", PROGRESS_END]
    return "\n".join(lines), completed


def apply_progress_block(text, block):
    pattern = re.compile(re.escape(PROGRESS_START) + r".*?" + re.escape(PROGRESS_END), re.S)
    if pattern.search(text):
        return pattern.sub(lambda _: block, text)
    return text.rstrip() + "\n\n" + block + "\n"


# ---------------------------------------------------------------------------
# Progress + local files
# ---------------------------------------------------------------------------

def read_progress():
    try:
        data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        data.setdefault("done", {})
        return data
    except (OSError, ValueError):
        return {"version": 1, "done": {}}


def write_progress(data):
    tmp = PROGRESS_FILE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, PROGRESS_FILE)


def read_markdown(target):
    if not target.exists():
        created = create_if_missing(target)
        if created is None:
            return None, False
        return target.read_text(encoding="utf-8"), True
    return target.read_text(encoding="utf-8"), False


def daily_log(date_str):
    target = ROOT / "daily-logs" / f"{dt.date.fromisoformat(date_str).isoformat()}.md"
    if target.exists():
        return target, False
    target.write_text(daily_log_text(date_str, schedule.read()), encoding="utf-8")
    return target, True


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

STATIC = {"/": "index.html", "/index.html": "index.html", "/manifest.webmanifest": "manifest.webmanifest",
          "/icon.svg": "icon.svg"}
TYPES = {".html": "text/html; charset=utf-8", ".webmanifest": "application/manifest+json",
         ".svg": "image/svg+xml", ".js": "text/javascript; charset=utf-8"}


class Handler(BaseHTTPRequestHandler):
    server_version = "PrepPlanner/1.0"

    def log_message(self, fmt, *args):
        pass

    def send_json(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_static(self, name):
        target = WEBAPP / name
        if not target.exists():
            self.send_json({"error": "Not found"}, 404)
            return
        body = target.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", TYPES.get(target.suffix, "application/octet-stream"))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def read_json(self):
        length = int(self.headers.get("Content-Length") or 0)
        if length > 1_000_000:
            raise ValueError("payload too large")
        return json.loads(self.rfile.read(length) or b"{}")

    def do_GET(self):
        req = urlparse(self.path)
        path = req.path
        if path in STATIC:
            self.send_static(STATIC[path])
        elif re.fullmatch(r"/lib/[a-z0-9-]+\.js", path):
            self.send_static(path.lstrip("/"))
        elif path == "/api/plan":
            try:
                plan = parse_plan()
                plan["templates"] = templates()
                self.send_json(plan)
            except Exception as exc:
                self.send_json({"error": f"Couldn't read the plan files: {exc}"}, 500)
        elif path == "/api/progress":
            self.send_json(read_progress())
        elif path == "/api/schedule":
            self.send_json(schedule.read())
        elif path == "/api/file":
            target = safe_path(parse_qs(req.query).get("path", [""])[0])
            if target is None:
                self.send_json({"error": "That file isn't inside the prep folders."}, 400)
                return
            with WRITE_LOCK:
                content, created = read_markdown(target)
            if content is None:
                self.send_json({"error": f"{target.name} doesn't exist yet."}, 404)
                return
            self.send_json({"ok": True, "created": created,
                            "path": target.relative_to(ROOT).as_posix(), "content": content})
        else:
            self.send_json({"error": "Not found"}, 404)

    def do_POST(self):
        # A custom header forces a CORS preflight, so other sites cannot post here.
        if self.headers.get("X-Prep-Planner") != "1":
            self.send_json({"error": "Missing X-Prep-Planner header"}, 403)
            return
        path = urlparse(self.path).path
        try:
            payload = self.read_json()
        except ValueError as exc:
            self.send_json({"error": str(exc)}, 400)
            return
        if path == "/api/progress":
            tid, done = payload.get("id"), payload.get("done")
            if not isinstance(tid, str) or not re.fullmatch(r"w\d+-[A-Za-z]{3}-[0-9A-Za-z]+", tid):
                self.send_json({"error": "Invalid task id"}, 400)
                return
            with WRITE_LOCK:
                data = read_progress()
                if done:
                    data["done"][tid] = dt.datetime.now().isoformat(timespec="seconds")
                else:
                    data["done"].pop(tid, None)
                write_progress(data)
            gitsync.touch()
            self.send_json({"ok": True, "done": data["done"]})
        elif path == "/api/schedule":
            try:
                with WRITE_LOCK:
                    data = schedule.write(payload)
            except (ValueError, TypeError) as exc:
                self.send_json({"error": f"Invalid schedule: {exc}"}, 400)
                return
            gitsync.touch()
            self.send_json(data)
        elif path == "/api/file":
            target = safe_path(str(payload.get("path", "")))
            content = payload.get("content")
            if target is None or not isinstance(content, str):
                self.send_json({"error": "That file isn't inside the prep folders."}, 400)
                return
            with WRITE_LOCK:
                target.parent.mkdir(parents=True, exist_ok=True)
                existed = target.exists()
                target.write_text(content, encoding="utf-8")
            gitsync.touch()
            self.send_json({"ok": True, "created": not existed, "path": target.relative_to(ROOT).as_posix()})
        elif path == "/api/daily-log":
            try:
                target, created = daily_log(str(payload.get("date", "")))
            except ValueError:
                self.send_json({"error": "Invalid date"}, 400)
                return
            if created:
                gitsync.touch()
            self.send_json({"ok": True, "created": created, "path": target.relative_to(ROOT).as_posix(),
                            "content": target.read_text(encoding="utf-8")})
        else:
            self.send_json({"error": "Not found"}, 404)


def templates():
    """What the browser needs to create the same files the server creates."""
    read = lambda rel: (ROOT / rel).read_text(encoding="utf-8")  # noqa: E731
    return {
        "notes": NOTE_SKELETONS,
        "noteDefault": NOTE_DEFAULT,
        "dailyLog": read("daily-logs/TEMPLATE.md"),
        "reviewWeekly": read("reviews/weekly/TEMPLATE.md"),
        "reviewMonthly": read("reviews/monthly/TEMPLATE.md"),
        "phases": {str(k): {"slug": v[0], "startWeek": v[1]} for k, v in PHASES.items()},
        "allowedDirs": list(ALLOWED_DIRS),
        "progressStart": PROGRESS_START,
        "progressEnd": PROGRESS_END,
    }


def main():
    print(gitsync.init(ROOT))
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    url = f"http://{HOST}:{PORT}"
    print(f"Google prep planner running at {url}  (Ctrl+C to stop)")
    if "--no-browser" not in sys.argv:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        gitsync.flush()
        print("\nStopped.")


if __name__ == "__main__":
    main()
