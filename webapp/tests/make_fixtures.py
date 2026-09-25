"""Dump what the Python produces, for tests/parity.mjs to check the JavaScript twins against.

    python webapp/tests/make_fixtures.py     # writes webapp/tests/fixtures.json (gitignored)
"""

import json
import sys
from pathlib import Path

WEBAPP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WEBAPP))

import schedule  # noqa: E402
import server  # noqa: E402

SCHEDULES = [
    {"start": "2026-09-14", "skips": []},
    {"start": "2026-09-14", "skips": ["2026-09-16", "2026-09-20", "2026-12-31", "2027-02-28"]},
    {"start": "2026-09-28", "skips": ["2026-09-01", "2026-09-28", "2026-10-02", "2026-10-03"]},
]
DAY_NUMBERS = [1, 2, 3, 7, 8, 100, 365, 504]
DATES = ["2026-09-10", "2026-09-14", "2026-09-16", "2026-09-17", "2026-10-02", "2027-01-01", "2027-02-28", "2028-02-02"]
NOTE_PATHS = ["notes/dsa/ds-06-sliding-window.md", "notes/theory/al-03-hash-tables.md", "notes/lld/ld-08-parking-lot.md",
              "notes/system-design/sd-13-url-shortener.md", "notes/behavioral/bh-01-googleyness.md",
              "notes/interview/ic-02-communication.md", "notes/misc/x.md", "notes/top.md",
              "reviews/weekly/week-07.md", "reviews/monthly/2026-10.md", "trackers/dsa.md"]
SAFE = ["notes/dsa/x.md", "trackers/dsa.md", "projects/lld/01-lru-cache/README.md", "webapp/server.py",
        "../secrets.md", "notes/../../escape.md", "plan/PLAN.md", "notes/dsa/x.txt", "site/index.md"]
STAMP = "2026-10-01 13:40"


def main():
    plan = server.parse_plan()
    by_num = {d["dayNumber"]: d for d in plan["days"]}
    out = {"schedules": [], "notes": {}, "safe": {}, "progress": []}
    for s in SCHEDULES:
        sched = schedule.normalise(s)
        out["schedules"].append({
            "sched": sched,
            "text": json.dumps(sched, indent=2, sort_keys=True) + "\n",
            "dateOf": {str(n): schedule.date_of(n, sched) for n in DAY_NUMBERS},
            "dayOf": {d: schedule.day_of(d, sched) for d in DATES},
            "dailyLog": {d: server.daily_log_text(d, sched) for d in DATES},
        })
    for p in NOTE_PATHS:
        target = server.ROOT / p
        if p.startswith("notes/"):
            out["notes"][p] = server.note_skeleton(p)
        elif p.startswith("reviews/weekly/"):
            out["notes"][p] = (server.ROOT / "reviews/weekly/TEMPLATE.md").read_text(encoding="utf-8")
        elif p.startswith("reviews/monthly/"):
            out["notes"][p] = (server.ROOT / "reviews/monthly/TEMPLATE.md").read_text(encoding="utf-8")
        else:
            out["notes"][p] = None
        del target
    for p in SAFE:
        out["safe"][p] = server.safe_path(p) is not None
    for n in (1, 6, 13, 300):
        day = by_num[n]
        done = {t["id"]: "x" for i, t in enumerate(day["tasks"]) if i % 2 == 0}
        block, completed = server.progress_block(day, done, STAMP)
        base = server.daily_log_text("2026-10-01", schedule.normalise(SCHEDULES[0]))
        out["progress"].append({"day": n, "done": done, "block": block, "completed": completed,
                                "appended": server.apply_progress_block(base, block),
                                "replaced": server.apply_progress_block(server.apply_progress_block(base, block), block)})
    out["stamp"] = STAMP
    path = Path(__file__).parent / "fixtures.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {path.name}: {len(SCHEDULES)} schedules, {len(NOTE_PATHS)} skeletons, {len(out['progress'])} checklists")


if __name__ == "__main__":
    main()
