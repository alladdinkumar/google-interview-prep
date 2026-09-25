"""Calendar dates for plan days: a start date plus a list of skipped dates.

The plan (plan/phase-*.md) numbers weeks and days; it never names a date. This module
maps plan day N to a calendar date and back, from webapp/schedule.json:

    {"version": 1, "start": "2026-09-14", "skips": ["2026-10-02", ...]}

A skipped date holds no plan day, so every plan day after it moves one calendar day
later - the whole preparation extends by a day. Moving `start` moves everything.

Progress is keyed by plan position (w12-Wed-L), never by date, so rescheduling can
never lose a tick. lib/templates.js carries the JavaScript twin of these functions;
tests/parity.mjs keeps them identical.
"""

import datetime as dt
import json
import os
from pathlib import Path

WEBAPP = Path(__file__).resolve().parent
SCHEDULE_FILE = WEBAPP / "schedule.json"
DEFAULT = {"version": 1, "start": "2026-09-14", "skips": []}


def read():
    try:
        data = json.loads(SCHEDULE_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return dict(DEFAULT, skips=[])
    return normalise(data)


def normalise(data):
    start = str(data.get("start") or DEFAULT["start"])
    dt.date.fromisoformat(start)                       # raises on nonsense
    skips = sorted({str(s) for s in data.get("skips", []) if _is_date(s)})
    return {"version": 1, "start": start, "skips": skips}


def write(data):
    data = normalise(data)
    tmp = SCHEDULE_FILE.with_suffix(".json.tmp")
    # Trailing newline, sorted keys, indent 2: byte-identical to backend-github.js.
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, SCHEDULE_FILE)
    return data


def _is_date(s):
    try:
        dt.date.fromisoformat(str(s))
        return True
    except ValueError:
        return False


def date_of(day_number, sched):
    """Calendar date (ISO) of plan day N (1-based)."""
    start = dt.date.fromisoformat(sched["start"])
    date = start + dt.timedelta(days=day_number - 1)
    for s in sched["skips"]:                           # sorted ascending
        sd = dt.date.fromisoformat(s)
        if sd < start:
            continue
        if sd <= date:
            date += dt.timedelta(days=1)
        else:
            break
    return date.isoformat()


def day_of(date_iso, sched):
    """Plan day number on a calendar date, 0 if before the start, None if skipped."""
    date = dt.date.fromisoformat(date_iso)
    start = dt.date.fromisoformat(sched["start"])
    if date_iso in sched["skips"]:
        return None
    if date < start:
        return 0
    skipped = sum(1 for s in sched["skips"] if start <= dt.date.fromisoformat(s) < date)
    return (date - start).days + 1 - skipped
