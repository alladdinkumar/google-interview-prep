# System Architecture

How this prep system is built and why.

---

## Design Philosophy

**Markdown is the source of truth.** Everything else is a convenience layer.

This means:
- The files in `daily-logs/`, `trackers/`, `plan/`, `reviews/`, `notes/` are *the system*.
- You can edit them in any editor — VS Code, Notepad++, vim, Obsidian.
- Git tracks the markdown — you get free version history, free backup.
- Claude Code reads and writes the same markdown.
- A future webapp (Track B) is a *thin shell over markdown*, not a replacement.

This is borrowed directly from `D:\Projects\Fitness and SkinCare\`, which has proven this pattern works for daily-habit systems.

---

## Two-Track Build

### Track A — Content (already built)

All markdown:
- 5 phase plans
- 5 curriculum docs (DSA, HLD, LLD, core subjects, behavioral)
- 1 company-targets doc
- 1 resources doc
- 1 weekly-schedule doc
- 1 daily-log template + day-1 bootstrap
- 8 tracker files
- 2 review templates (weekly + monthly)
- 4 notes index files
- 3 docs files

**Sandeep can use the system today with zero additional tooling.**

### Track B — Webapp Dashboard (deferred)

Built ~Week 5+ when:
- Daily logging habit is established
- The markdown schema has been battle-tested by 3-4 weeks of real use
- The fields that actually matter have been identified (some will turn out to be cruft)

**Tech stack** (mirror `D:\Projects\Fitness and SkinCare\webapp\`):
- **Backend:** Flask 3+, python-frontmatter (YAML+markdown), Pillow (if photos), anthropic SDK (optional, for AI-generated reviews)
- **Frontend:** Vanilla HTML + Alpine.js (CDN) + Tailwind (CDN) — **zero build step**
- **Storage:** Pure markdown (no DB)

**Features** (in priority order):
1. Open today's daily log (auto-create from template if missing)
2. Schema-driven form generation from a `schema.py` (like Fitness app)
3. Auto-save (debounced, every 1s when idle)
4. Tracker visualizations:
   - Problems-solved trend line (cumulative + per-week)
   - Topic accuracy heatmap
   - Hours adherence bar chart
   - Mock score trend
5. Weekly review generator (read 6 daily logs, draft synthesis, ask user to refine)
6. Pending items rule engine ("Mock not logged for this week", "No daily log for yesterday", "Confidence on topic X stale 21+ days")

**Re-use from Fitness webapp:**
- `parsers.py` — markdown ↔ dict round-trip
- `schema.py` pattern — field definitions drive both parser and UI
- Auto-save mechanism
- `DATA_ROOT` env var for sandbox-vs-live mode
- `weekly_review.py` aggregation logic
- The general Flask routes structure

**Don't re-use:**
- Photo upload (irrelevant — replace with optional code-snippet capture)
- HEIC conversion
- Lift / macro / supplement schema (entirely different domain)

**New for this domain:**
- LeetCode link autocomplete
- Per-topic accuracy auto-calc
- Mock-interview score trend chart
- Weak-area auto-flag rule (confidence <3, last revisited >21 days)
- STAR story rehearsal cadence reminder

---

## File Organization Rationale

### Why `plan/` is read-only

The plan represents *committed decisions*. Editing it casually leaks "I'll just tweak one thing" into procrastination. The plan only changes during the monthly review's explicit adjustment step.

### Why `trackers/` are updated weekly (not daily)

Daily updates create busy-work and false signal. A week is the smallest window where you have enough data to update trends meaningfully. Per-day data lives in `daily-logs/`.

### Why `notes/` is by topic, not by date

Notes are reference material — you'll go back to `notes/dsa/sliding-window.md` next month when you re-touch sliding window. Organize by what you're searching *for*, not when you wrote it.

### Why `reviews/` separates weekly from monthly

They serve different functions: weekly = "what happened" + "next week"; monthly = "are we on track" + "phase adjust". Mixing them dilutes both.

### Why YAML frontmatter on daily logs

It makes the file machine-readable (Claude Code can parse it, future webapp can parse it) while staying human-readable. `python-frontmatter` round-trips it cleanly.

---

## How Claude Code Coach Sessions Work

When you run `claude` in this directory:

1. Claude Code loads `prompt.md` (the coach persona)
2. Claude Code has tools to Read, Write, Glob, Grep across this directory
3. You issue a coaching prompt (see `docs/how-to-use.md` for examples)
4. Claude reads relevant files (today's log, the plan, the trackers)
5. Claude responds in-conversation or writes to files (reviews, etc.)
6. Closing the session preserves all file changes (they're real markdown)

There's no shared state outside markdown files. Restart-safe.

---

## Future Track B Webapp Architecture (Sketch)

```
webapp/
├── app.py                  # Flask routes (mirror Fitness app.py structure)
├── schema.py               # Field schema for daily logs + trackers
├── parsers.py              # Markdown ↔ dict round-trip
├── plan_loader.py          # Reads plan/phase-N-*.md to fill in "what to do today"
├── coach.py                # Pending items rule engine
├── weekly_review.py        # 7-day rollup into structured review
├── requirements.txt        # Flask, frontmatter, anthropic, markdown
├── templates/
│   └── index.html          # SPA shell, Alpine.js mounts here
├── static/
│   ├── app.js              # Alpine.js component
│   └── styles.css          # Tailwind + custom
├── .env.example            # ANTHROPIC_API_KEY, DATA_ROOT, PORT
└── test-data/              # Sandbox markdown for dev
```

### Routes (sketch)

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | SPA shell |
| `/api/config` | GET | Schema definition for the UI |
| `/api/today` | GET | Today's log (auto-create if missing) |
| `/api/log/<date>` | GET / PUT | Read or save a daily log |
| `/api/trackers/<name>` | GET / PUT | Read or save a tracker |
| `/api/plan` | GET | Current phase + week info |
| `/api/weekly-review` | POST | Generate weekly review from last 7 days |
| `/api/pending/<date>` | GET | Pending items for the given day |
| `/api/suggest` | POST | (Optional) Claude-generated coaching nudge |

### When to build Track B

Trigger conditions (any one):
1. End of Week 4 — habit is formed, markdown schema feels stable
2. Daily logging starts to feel slow due to copy-paste of TEMPLATE.md
3. Trackers feel hard to update by hand (when there's enough data to chart)

Not before. Premature optimization is the death of habit systems.

---

## Why Not Use [Notion / Obsidian / Roam / etc.]?

| Tool | Why not |
|------|---------|
| Notion | Lock-in, slow on phone, export-import friction |
| Obsidian | Actually fine — could use it on top of these files. But adds another tool. |
| Roam | Even more lock-in, niche format |
| Excel / Sheets | Bad for prose, version-control hostile |
| Trello / Linear | Optimized for project mgmt, not personal study tracking |

**Markdown wins on:** portability, version control, tool flexibility, longevity, plain-text durability, AI-readability.

The fitness/skincare project has been using this pattern long enough to validate it. We're standing on a proven design.
