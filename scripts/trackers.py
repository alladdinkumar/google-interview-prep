"""Generate the tracker files from the plan, so they always match the curriculum.

    python scripts/trackers.py            # rewrite the plan-derived trackers (dsa, lld, hld, mocks, progress)
    python scripts/trackers.py --blank    # also reset weak-areas and behavioral to empty templates

Without --blank, trackers you fill in by hand (weak-areas.md, behavioral.md) are left
alone. setup_own_copy.py calls this with --blank when handing the repo to a new owner.
Standard library only.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "webapp"))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import topics as T  # noqa: E402

TRACKERS = ROOT / "trackers"
CONF = "**Confidence:** 1 lost · 2 needs lookup · 3 solves with hints · 4 first try most of the time · 5 could teach it"


def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "|".join("---" for _ in head) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def dsa(cat):
    rows = [(t, e["short"], e["week"], 0, 0, 1, "—") for t, e in cat.items() if e["area"] in ("DS", "AL")]
    return "\n".join([
        "# DSA Tracker", "",
        "Updated every Sunday in the weekly review. Two tables: confidence per topic, and a",
        "log of every problem attempted (the lunch and Saturday sessions each ask for a row here).", "",
        CONF, "", "## By topic", "",
        table(["#", "Topic", "First week", "Attempted", "First try", "Confidence", "Last revisited"], rows), "",
        "## Problem log", "",
        table(["Date", "LC", "Title", "Difficulty", "Topic", "Minutes", "First try Y/N", "Pattern", "Redo by"], []), "",
    ])


def lld(cat):
    rows = [(t, e["short"], e["week"], "no", 1, "—") for t, e in cat.items() if e["area"] == "LD"]
    projects = sorted(p.name for p in (ROOT / "projects" / "lld").iterdir() if p.is_dir() and p.name[:2].isdigit())
    prow = [(p, f"`projects/lld/{p}/`", "0/8", "no", "—") for p in projects]
    return "\n".join([
        "# LLD Tracker", "", "Object-oriented design, weeks 39–44. Updated in the weekly review.", "", CONF, "",
        "## Topics", "", table(["#", "Topic", "Week", "Note written", "Confidence", "Last revisited"], rows), "",
        "## Projects", "", "Score is what `make test` prints. Extension = the section at the end of the project README.", "",
        table(["Project", "Path", "Tests", "Extension done", "Finished"], prow), "",
    ])


def hld(cat):
    rows = [(t, e["short"], e["week"], "no", "no", 1, "—") for t, e in cat.items() if e["area"] == "SD"]
    return "\n".join([
        "# System Design Tracker", "", "Weeks 45–56. A case study is done when its note has all six parts:",
        "requirements with numbers, estimation, API, data model, high-level design, two deep dives.", "", CONF, "",
        table(["#", "Topic", "Week", "Note complete", "Done aloud in 45 min", "Confidence", "Last revisited"], rows), "",
    ])


def mocks():
    planned = []
    for f in sorted((ROOT / "plan").glob("phase-*.md")):
        week = None
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^### Week (\d+)", line)
            if m:
                week = int(m.group(1))
                continue
            if line.startswith("| Sat |") and re.search(r"mock|full loop|mini-loop", line, re.I):
                focus = line.split("|")[3].strip()
                planned.append((len(planned) + 1, week, focus[:90].replace("|", "/"), "—", "—", "planned"))
    return "\n".join([
        "# Mocks and Contests", "",
        "Every mock interview the plan schedules, and a log for the Sunday LeetCode contests.",
        "Score mocks on Google's four coding dimensions (coding, algorithms, communication, problem",
        "solving), each Strong No Hire → Strong Hire.", "",
        "## Planned mocks", "", table(["#", "Week", "What", "Partner / platform", "Result", "Status"], planned), "",
        "## Mock notes", "", "For each: the problem, what went well, the one thing the interviewer would write down, the fix.", "",
        "## Contest log", "", table(["Date", "Contest", "Solved (of 4)", "Rank", "Time on Q2", "What cost the most time"], []), "",
    ])


def progress():
    phases = []
    for f in sorted((ROOT / "plan").glob("phase-*.md")):
        head = f.read_text(encoding="utf-8").splitlines()[0]
        m = re.match(r"^# Phase (\d+) — (.+?) \(Weeks (\d+)–(\d+)\)", head)
        if m:
            n, name, a, b = int(m.group(1)), m.group(2), int(m.group(3)), int(m.group(4))
            phases.append((n, name, f"{a}–{b}", round((b - a + 1) * 9.75), "__", "__"))
    weeks = [(w, "9.75", "__", "__", "__", "__") for w in range(1, 73)]
    return "\n".join([
        "# Progress", "", "Filled in during the Sunday review. Dates come from the planner (Settings → Schedule).", "",
        "## By phase", "", table(["Phase", "Name", "Weeks", "Target h", "Actual h", "Sessions ticked"], phases), "",
        "## By week", "", table(["Week", "Target h", "Actual h", "Sessions ticked (of 9)", "Problems", "Contest solved"], weeks), "",
    ])


def weak_areas():
    return "\n".join([
        "# Weak Areas", "",
        "Fed by misses: a problem that needed the solution, a mock weakness, a topic at confidence < 3.",
        "An item leaves only after it is redone cold and passes. Wednesday redos come from here.", "",
        "## Active", "",
        table(["#", "Topic / problem", "Source", "Found", "Why it is weak", "Fix", "Redo on", "Status"], []), "",
        "## Remediated", "",
        table(["#", "Topic / problem", "Found", "Fix", "Re-tested", "Outcome"], []), "",
    ])


def behavioral_blank():
    """The behavioural tracker with the previous owner's stories replaced by empty slots."""
    text = (TRACKERS / "behavioral.md").read_text(encoding="utf-8")
    text = text.replace("Working story (Privafy incident)", "Working story (from your work)")
    text = text.replace("Why are you leaving Privafy?", "Why are you leaving your current company?")
    out = []
    for line in text.splitlines():
        cells = line.split("|")
        # Story slot rows: | n | slot | story | note | ... -> blank the story column.
        if len(cells) > 4 and cells[1].strip().isdigit() and "notes/behavioral/stories/" in line:
            n = int(cells[1])
            slug = re.sub(r"[^a-z0-9]+", "-", cells[2].split("/")[0].lower()).strip("-")
            cells[3] = " (pick a story from your own work) "
            cells[4] = f" `notes/behavioral/stories/{n:02d}-{slug}.md` "
            line = "|".join(cells)
        out.append(line)
    return "\n".join(out) + "\n"


def main():
    blank = "--blank" in sys.argv
    cat, _ = T.build_catalogue()
    files = {"dsa.md": dsa(cat), "lld.md": lld(cat), "hld.md": hld(cat), "mocks.md": mocks(), "progress.md": progress()}
    if blank:
        files["weak-areas.md"] = weak_areas()
        files["behavioral.md"] = behavioral_blank()
    for name, text in files.items():
        (TRACKERS / name).write_text(text, encoding="utf-8", newline="\n")
    print("wrote trackers/" + ", trackers/".join(files))


if __name__ == "__main__":
    main()
