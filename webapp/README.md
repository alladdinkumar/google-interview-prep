# The planner

A day-by-day view of the plan with checkboxes, verified videos and problems, reading, interview
questions, Gemini prompts, and an in-page Markdown editor. One page, two ways to run it, the
same data:

| | Where | Backend | For |
|---|---|---|---|
| **Hosted** | https://alladdinkumar.github.io/google-interview-prep/ | The repository, via the GitHub API | Phone, tablet, any machine |
| **Local** | `webapp\start.bat` → http://127.0.0.1:8766 | `webapp/server.py` on this disk | The desk, offline, long notes |

The local server pulls on start and pushes ten seconds after each save (`PREP_NO_SYNC=1` turns
that off), so the two never drift. It uses port 8766 so it can run beside the GATE planner (8765).

## First run on a new device (hosted)

The page is read-only until that browser has a token.

1. Tap **Add token** (or Settings).
2. On github.com → Settings → Developer settings → **Fine-grained tokens** → Generate new token:
   - Repository access: **Only select repositories → google-interview-prep**
   - Permissions → Repository → **Contents: Read and write**. Nothing else.
   - An expiry you are willing to renew.
   Direct link: https://github.com/settings/personal-access-tokens/new
3. Paste it and save.

Do **not** use `gh auth token` or a classic token: those can write to every repository you own,
which is the wrong thing to keep on a phone. The token stays in that browser's storage, is never
committed, and is only ever sent to api.github.com.

## Schedule: start date and skipped days

Dates are not written in the plan. The planner works them out from `webapp/schedule.json`:

```json
{ "skips": ["2026-10-02"], "start": "2026-09-14", "version": 1 }
```

- **Skip this day** (day view) or **Settings → Schedule → Skip a date**: nothing is planned that
  date; that plan day and everything after it moves one calendar day later. Undo from the toast
  or the list.
- **Settings → Schedule → start date**: Day 1 moves, everything moves with it.
- Progress is keyed by plan position (`w12-Wed-L`), never by date, so no change to the schedule
  can lose a tick.

## Saving

Ticks on the hosted page are batched: four seconds after the last tap, one commit
(`progress: +3 -1 (w4-Mon-L, …)`). Offline ticks queue and go up when the connection returns.
Progress is merged by replaying the tick log onto the latest copy, so unticking on one device and
ticking on another never resurrects anything.

Schedule changes and Markdown saves are one commit each. None of these trigger a site rebuild.

After a plan change is deployed, a phone may show the old page for a minute (CDN cache): pull to
refresh, or close and reopen the home-screen app.

## Gemini

Every "Ask Gemini" button opens Google AI Mode (`google.com/search?udm=50&q=…`) — the Gemini
model, answering immediately. The Gemini app itself ignores prompts in the URL (tested), so the
one Canvas button copies the prompt and opens gemini.google.com for a paste. Every button also
copies the full prompt to the clipboard.

Each prompt begins with where you are (plan day, week, phase, date), the topic's full concept list,
the session's focus and what you have already ticked today — ticking as you go makes the answers
better. Every prompt dictates its answer's structure; `tests/catalogue_test.py` fails if one stops
saying "exactly".

## Maintaining the data

| To | Do |
|----|----|
| Change what a day says | Edit `plan/phase-*.md`; keep `LC-n` and topic ids (`DS-6`) in the text — they drive the links |
| Better videos for a topic | Improve its phrase in `plan/topic-lectures.md`, then `python webapp/tools/build_videos.py DS-6` |
| Solution videos for a new problem | Add it to `plan/problems.md`, then `python webapp/tools/build_videos.py --problems LC-123` |
| Add reading | Append a row to `plan/topic-reading.md` |
| Check everything | `python webapp/build_site.py && python webapp/tests/catalogue_test.py && python webapp/tests/make_fixtures.py && node webapp/tests/parity.mjs` |
| See what the page shows | Paste `webapp/tests/render-sweep.js` into the browser console on the planner |

CI runs the build and the tests on every push that touches the plan or the planner, and refuses to
deploy if any fail.

## Files

| File | Role |
|------|------|
| `server.py` | Plan parser, link resolution, file templates, local HTTP API |
| `topics.py` | Topic and problem catalogue, the three-videos / five-practice dealing, all prompts |
| `schedule.py` | Plan day ↔ calendar date, from `schedule.json` |
| `build_site.py` | Builds `site/` for GitHub Pages with the same parser |
| `gitsync.py` | Pull on start, push after saves |
| `index.html` | The page |
| `lib/templates.js` | Browser twins of `schedule.py` and the file templates — kept identical by `tests/parity.mjs` |
| `lib/backend-*.js` | Local server or GitHub API |
| `tools/` | The YouTube harvester (`yt.py`, `build_videos.py`) |
