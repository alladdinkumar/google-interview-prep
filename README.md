# Google Interview Prep — 72-week plan and day-by-day planner

A personal preparation system for the Google software engineer loop (L4, stretch L5), run
alongside GATE 2028 preparation at ~10 hours a week.

**Planner:** https://alladdinkumar.github.io/google-interview-prep/ — open it on any device, add it
to the home screen, tick sessions as you go. Local copy: `webapp\start.bat`.

**Want your own?** Clone it and run one command — see [Host your own copy](#host-your-own-copy).

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

## Host your own copy

Anyone can run this plan with their own planner on their own GitHub account, free. Your copy
gets your own progress, schedule and notes; nothing is shared with the original.

### What you need

- **Git** — https://git-scm.com/downloads
- **Python 3.10+** — https://www.python.org/downloads/ (the planner and scripts use only the standard library)
- **GitHub CLI**, logged in — https://cli.github.com, then run `gh auth login` once
- Optional: **Node 18+** to run the JavaScript parity test locally; a **C++17 compiler with
  threads** (g++ 9+, clang 10+) for the design projects

### One command

```bash
git clone https://github.com/alladdinkumar/google-interview-prep.git my-google-prep
cd my-google-prep
python scripts/setup_own_copy.py --repo my-google-prep --start 2026-10-05
```

It prints everything it will do and asks you to type the repo name before doing it. Then it:

1. clears the previous owner's personal data — ticked sessions, skipped days, daily logs,
   reviews, notes, filled-in trackers, their coaching persona and archives, and their solutions
   to the design projects (restored to the unsolved stubs);
2. sets your start date and your profile (used to phrase every Gemini prompt);
3. commits, creates `<your-account>/<repo>` on GitHub and pushes;
4. turns on GitHub Pages (source: GitHub Actions), runs the first deploy — which runs all the
   tests first — and waits for it;
5. prints your planner address and how to make the phone token.

Your planner is then at `https://<your-account>.github.io/<repo>/`.

| Option | Meaning |
|--------|---------|
| `--repo NAME` | Name of your new repository |
| `--start YYYY-MM-DD` | Plan Day 1. **Pick a Monday** — every plan week starts on Monday, so Saturday's long block only lands on a Saturday if Day 1 is a Monday. Default: next Monday. Changeable later in Settings → Schedule. |
| `--level L4` / `--hours 10` | Your target level and weekly hours, written into the Gemini prompts |
| `--private` | Private repository. GitHub Pages on a private repo needs GitHub Pro; the local planner works either way |
| `--fresh-history` | Start your repository with one commit instead of the original history |
| `--keep-data` | Move your *own* copy to a new repository without clearing anything |
| `--local-only` | Clear and commit locally, skip GitHub (then push by hand, below) |
| `--dry-run` | Show what would happen; change nothing |
| `--yes` | Skip the confirmation |

The script refuses to clear a copy whose `origin` already belongs to your own account, so it
cannot wipe your progress by accident.

### By hand (no GitHub CLI)

```bash
python scripts/setup_own_copy.py --local-only --start 2026-10-05     # clear and commit
```

1. On github.com create an **empty** repository (no README, no licence).
2. `git remote rename origin upstream`
3. `git remote add origin https://github.com/<you>/<repo>.git && git push -u origin main`
4. Repository → **Settings → Pages → Source: GitHub Actions**.
5. **Actions** tab → **Build and deploy the planner** → **Run workflow**. About a minute later
   the site is live at `https://<you>.github.io/<repo>/`.

(Forking on GitHub also works, but a fork keeps the original's data and has Actions switched off
until you enable them — cloning and running the script is cleaner.)

### Then, on each device

Open your planner → **Add token**. Make a fine-grained token at
https://github.com/settings/personal-access-tokens/new with **only your repository** and
**Contents: Read and write**, nothing else. Details in `webapp/README.md`.

### Making it yours

| To change | Edit |
|-----------|------|
| Start date, skipped days | Settings → Schedule in the planner (or `webapp/schedule.json`) |
| How the Gemini prompts describe you | `webapp/profile.json` |
| What a day contains | `plan/phase-*.md` — keep the `LC-n` and topic ids (`DS-6`), they drive the links |
| The session times | This plan's slots (weekday lunch, Saturday afternoon, Sunday morning) were fitted around a second exam; change `SLOT_LABELS` in `webapp/server.py` and `plan/weekly-schedule.md` to your own |
| Videos for a topic | its phrase in `plan/topic-lectures.md`, then `python webapp/tools/build_videos.py DS-6` |

Every push that touches `plan/` or `webapp/` rebuilds the site, and the tests must pass first.

### Getting later improvements from the original

```bash
git fetch upstream
git merge upstream/main
```

Conflicts can only arise in files you both changed; for your own data (`webapp/progress.json`,
`webapp/schedule.json`, `webapp/profile.json`, `trackers/`, `notes/`) keep yours:
`git checkout --ours <file>`.
