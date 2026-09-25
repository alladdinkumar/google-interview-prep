# How to Use This Prep System

A practical guide. Keep this open for the first week — habits form by Day 14.

---

## Day 0 — Setup (1 hour, do this on the Sunday before Week 1)

1. Read `README.md` end-to-end.
2. Skim `plan/PLAN.md` so you know the 26-week shape.
3. Read `plan/phase-1-foundations.md` in detail.
4. Bookmark every link in `plan/resources.md` in your browser.
5. Set up recurring calendar blocks (see `plan/weekly-schedule.md`).
6. Open `daily-logs/2026-05-18.md` — your bootstrap day-1 log is already there.
7. Create a LeetCode account if you don't have one (free tier is fine for now).
8. Pick a C++ IDE setup you like: VS Code + clangd, or CLion, or just leetcode.com's online editor. Don't waste time tooling.

---

## Daily Flow (Mon-Fri, ~5 minutes of overhead)

### Morning (08:30, before logging in for work)

1. Open `daily-logs/YYYY-MM-DD.md` (today's file)
   - If it doesn't exist, copy `daily-logs/TEMPLATE.md` to today's date filename
2. Fill in YAML frontmatter (date, day_of_week, phase, overall_week, etc.)
3. **Re-attempt yesterday's redos first** (10 min) — anything you flagged "needed hint" or "couldn't solve"
4. Solve today's problem quota per `plan/phase-X-*.md`
5. Capture problem entries as you go (one line per problem under Morning Session → Problems Solved)
6. If you write a notes file (`notes/dsa/...`), link it in the daily log

**Don't:** track time obsessively. Round to nearest 15 min.

### Evening (20:00, after dinner)

1. Open the same daily log
2. Watch a topic video or read theory chapter (45-60 min)
3. Take notes — one new note file or update an existing one
4. Fill in Evening Session section
5. Spend the last 5 min on the Reflection section — even one-line answers
6. Update Adherence Flags before sleep

**Don't:** skip the Reflection section. It's where insights compound.

---

## Saturday Flow

1. Open today's daily log (Saturday's file)
2. 9:00 — 1 hard problem OR 2 hard mediums (focus on weak topics from this week)
3. 10:30 — Break, snack
4. 11:00 — HLD or LLD deep dive (Phase 3+) OR core subjects intensive (Phase 1-2)
5. 12:00 — Mock interview (Phase 3+) OR weekly review data compile
6. 13:00 — Done. Rest of day is yours.

---

## Sunday Flow (30-45 min, morning recommended)

1. Open `reviews/weekly/2026-MM-DD-to-2026-MM-DD.md`
   - Copy `reviews/weekly/TEMPLATE.md` to that filename
2. Read this week's 6 daily logs
3. Fill in hours, problems solved, what worked / didn't
4. Update all 8 trackers:
   - `trackers/progress.md` — master numbers
   - `trackers/dsa.md` — per-topic counts and confidence
   - `trackers/hld.md` — case studies status (Phase 4+)
   - `trackers/lld.md` — LLD problems (Phase 3+)
   - `trackers/core-subjects.md` — what got read
   - `trackers/behavioral.md` — story refinement (Phase 5)
   - `trackers/mocks.md` — log this week's mock (Phase 3+)
   - `trackers/weak-areas.md` — add new gaps, mark remediated old ones
5. Set focus for next week (one sentence)
6. **Close laptop. Rest.**

---

## Monthly Flow (last Sunday of month, 90 min)

1. Do the weekly review first (above)
2. Then open `reviews/monthly/YYYY-MM.md` (copy template)
3. Read all 4-5 weekly reviews from the month
4. Re-rank weak areas
5. Decide: proceed / extend / re-scope
6. Write 3 concrete commitments for next month

---

## When You Want to Run a Claude Code Coach Session

Open this folder in Claude Code (just `cd D:\Projects\Study` and run `claude`). The coach reads `prompt.md` automatically.

Useful prompts:

- **"Read this week's daily logs and write the weekly review."** — full Sunday automation
- **"Read today's log. What should I focus on this evening?"** — mid-day course-correct
- **"Generate 3 medium problems on my weakest topic from `trackers/weak-areas.md`."** — practice generator
- **"Walk me through a Twitter feed system design like an interviewer would."** — mock prep
- **"Review my STAR story #1 (EDR scaling) and tell me where it's weak."** — story drill
- **"What's the current state of my prep? Be honest."** — readiness check

The coach won't write code for you. It coaches.

---

## Common Pitfalls

| Pitfall | Why it happens | Fix |
|---------|----------------|-----|
| Skipping the Reflection section | "I'll do it tomorrow" | Force it. 60 sec, one-line answers ok |
| Not re-attempting yesterday's failures | Feels redundant | It isn't. This is the highest-leverage 10 min of the day. |
| Watching too many videos, solving too few problems | Videos feel productive but aren't | 2:1 ratio max: 2 problems per video |
| Editing `plan/` files when frustrated | Procrastination disguised as planning | Don't. Flag in weekly review instead. |
| Tracking time to the minute | OCD signal | Round to 15 min. Move on. |
| Adding more topics to the plan | "Just one more thing" | The plan is fixed. Adding = phase extension |
| Doing Sunday session anyway | "I have time, why not?" | Don't. Sunday rest = Monday performance. |

---

## Habit Building Tip

**Week 1-2 will feel hard.** Habit research says 14-21 days to feel natural. Push through. If you only adhere 50% in Week 1, that's normal — log honestly and don't panic. Adherence climbs to 70-80% by Week 3 if you don't quit.

If after 3 weeks you're still <50% adherent, **don't push harder**. Re-evaluate: is the schedule realistic? Is morning the wrong slot for you? Is something at work draining you? Adjust the *schedule*, not your willpower.
