# Google Interview Prep — 72-week plan and day-by-day planner

A personal preparation system for the Google software engineer loop (L4, stretch L5), run
alongside GATE 2028 preparation at ~10 hours a week.

**Planner:** https://alladdinkumar.github.io/google-interview-prep/ — open it on any device, add it
to the home screen, tick sessions as you go. Local copy: `webapp\start.bat`.

## What is here

| Path | What |
|------|------|
| `plan/PLAN.md` | The 72-week plan, the phases, the week, and a Google-coverage table — start here |
| `plan/phase-*.md` | Every day, every session (504 days, 648 sessions) |
| `plan/curriculum-*.md` | 130 topics: 41 DSA patterns, 38 algorithms-theory topics, 15 OOD, 25 system design, 11 behavioural and interview craft |
| `plan/problems.md` | 527 LeetCode problems, each verified; Premium ones have a free LintCode link |
| `plan/topic-videos.md`, `plan/problem-videos.md` | 745 lecture videos and 1,054 solution videos, each confirmed against YouTube |
| `plan/topic-reading.md` | 423 verified reading links, including issues from engineering newsletters |
| `plan/topic-questions.md` | Ten interview questions for every topic |
| `projects/lld/` | Six C++ design projects with tests: they compile and run from day one, you make them pass |
| `notes/`, `trackers/`, `daily-logs/`, `reviews/` | What you write |
| `webapp/` | The planner (see `webapp/README.md`) |

## How a day works

Open the planner, go to **Today**. Each session shows what to do, what to record, and under it:

- **Problem cards** — solve link, solution videos for after the attempt, and Gemini prompts for a
  step-by-step visual walkthrough, a hint ladder, a code review, and an interactive Canvas animation.
- **Topic blocks** — three lectures, 4–5 practice problems, reading, newsletter notes, ten interview
  questions with an "Answer" button each, five Gemini prompts, and your note file.

Tick the session when it is done. Every Gemini button opens Google AI Mode (Gemini) already
answering, with your day, week, topic and today's progress in the prompt, and copies the full
prompt too.

**Behind or away?** Press **Skip this day** — the rest of the plan moves one day later and nothing
you ticked is lost. Change the start date in **Settings → Schedule**.

## The rules

1. Timer on for every problem; hint ladder before the solution; solution video only after an attempt.
2. Log every problem in `trackers/dsa.md`. Misses go to `trackers/weak-areas.md` and come back as Wednesday redos.
3. Skip a day honestly rather than doubling up. The plan is built to move.
4. Never schedule into GATE's slots.

`plan/archive/v1-26-week/` holds the original May–Nov 2026 plan; `prompt.md` is the coaching persona for Claude Code sessions here.
