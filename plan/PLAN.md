# Master Plan — 72 Weeks to a Google SWE Offer (L4, stretch L5)

**Weeks:** 72, the same window as the GATE 2028 plan · **Budget:** ~9.75 h/week, ~700 h total
**Default start:** Mon 2026-09-14 · **Dates:** worked out by the planner from the start date and
any skipped days (Settings → Schedule). Change the start, skip a holiday, and every later day moves.

**Goal:** pass the Google loop — 3–4 coding rounds, 1 system design, 1 Googleyness & Leadership —
with the onsite in the second half of **February 2028**, after the GATE paper.

The previous 26-week plan (May–Nov 2026, not followed) is kept in `archive/v1-26-week/`.

---

## Why this shape

- **Coding is most of the loop**, so DSA is weeks 1–38 as the main track and never stops: every
  week to the end has 3–5 lunch problems and a Sunday contest.
- **Theory runs beside the patterns**, one topic every Tuesday (`AL-` topics), so "why is that
  O(1)?" and "prove it" have answers.
- **Design comes after the coding base**: object-oriented design with runnable projects (weeks
  39–44), then system design built on Google's own papers (45–56).
- **The loop itself is practised with people**: weekly peer mocks from week 57, full loop
  simulations in 65–69, a taper in 71–72.
- **It runs beside GATE.** The slots below never touch GATE's (weekdays 08:30–10:00 and
  20:00–21:30, Saturday 09:00–13:00). The two exams collide in February 2028: apply in
  Week 64 and ask for the onsite after the GATE paper.

## Phases

| Phase | Weeks | Theme | Outcome |
|-------|-------|-------|---------|
| 1. Foundations | 1–8 | C++ STL, complexity, arrays, hashing, two pointers, sliding window, binary search, stacks, queues, linked lists | Fluent C++; easy problems in < 15 min |
| 2. Core Patterns | 9–24 | Recursion, sorting, trees, BST, heaps, backtracking, graphs (BFS, topo, DSU, Dijkstra, MST), greedy, intervals, tries | First self-run mock in Week 24 |
| 3. DP & Advanced | 25–38 | Dynamic programming (8 weeks), bits, math, monotonic stack, segment/Fenwick trees, string algorithms, advanced graphs, design data structures | Mediums in < 25 min; hards attempted |
| 4. Object-Oriented Design | 39–44 | OOP in C++, SOLID, patterns, UML, concurrency, six case studies | Six runnable projects in `projects/lld/`, tests green |
| 5. System Design | 45–56 | Framework, estimation, networking, caching, databases, sharding, consensus, queues, Google papers, 13 case studies | Every design written up in the 45-minute shape |
| 6. Google Loop | 57–66 | Hiring process, communication, coding without an IDE, story bank, weekly peer mocks, application | Referral and application in Week 64 |
| 7. Final Sprint | 67–72 | Full loop simulations, weak-area redos, taper | Onsite-ready |

Each phase file (`phase-*.md`) has the day-by-day table for every week.

## The week

| When | Slot | What |
|------|------|------|
| Mon, Thu, Fri 13:00–13:45 | Lunch drill | One new problem, timed, drilling the pattern learned last Saturday |
| Tue 13:00–13:45 | Theory lunch | One `AL-` theory topic (weeks 1–38), then problems |
| Wed 13:00–13:45 | Redo lunch | A problem from two weeks back, from a blank file |
| Sat 14:00–16:00 | Learn block | The week's topic: three lectures, the pattern note, one guided problem |
| Sat 16:15–18:00 | Practice block | Three problems timed and aloud · LLD weeks: build the project · SD weeks: a timed design |
| Sun 08:00–09:30 | Contest | LeetCode Weekly Contest, live (08:00 IST) |
| Sun 09:45–10:15 | Weekly review | `reviews/weekly/week-NN.md`, trackers, next Wednesday's redo |

9 sessions, 9.75 hours. Details in `weekly-schedule.md`.

## Google interview coverage

What Google's coding and design rounds test, and where each lives in this plan. Problem counts
are from `problems.md` (527 problems, all verified against LeetCode; 394 are scheduled, the rest
appear as extra practice under their topic).

| Area | Topics | Problems |
|------|--------|----------|
| Arrays, strings, hashing | DS-1…DS-6, AL-2, AL-3, AL-6 | 75 |
| Searching and sorting | DS-7, DS-11, DS-12, AL-5, AL-9, AL-10 | 35 |
| Stacks, queues, linked lists | DS-8, DS-9, DS-10, DS-40, AL-7, AL-8 | 54 |
| Trees and BSTs | DS-13…DS-15, AL-11…AL-13 | 48 |
| Heaps | DS-16, AL-14 | 15 |
| Backtracking | DS-17, DS-18, AL-15 | 24 |
| Graphs | DS-19…DS-24, DS-39, AL-16…AL-21, AL-33 | 77 |
| Greedy and intervals | DS-25, DS-26, AL-22 | 34 |
| Tries and string algorithms | DS-27, DS-38, AL-23, AL-32 | 21 |
| Dynamic programming | DS-28…DS-34, AL-25, AL-26 | 86 |
| Bits, math, geometry, probability | DS-35, DS-36, AL-27…AL-30, AL-34 | 30 |
| Range queries | DS-37, AL-31 | 8 |
| Design data structures and concurrency | DS-41, AL-24, AL-36…AL-38, LD-7 | 20 |
| Complexity and proofs | DS-2, AL-1, AL-4, AL-35 | (DS-2's 5 are in the first row) |
| Object-oriented design | LD-1…LD-15 | 6 runnable projects |
| System design | SD-1…SD-25 | 13 case studies + Google papers |
| Googleyness, leadership, the loop | BH-1…BH-5, IC-1…IC-6 | 10 stories, weekly mocks |

Difficulty mix of what is scheduled: 50 Easy (weeks 1–3 only), 265 Medium, 79 Hard. Google's
rounds sit at medium-to-hard; mixed drills after Week 38 contain no Easy problems.

## What every day gives you in the planner

- **Problem cards** for every `LC-` problem: the LeetCode link (or a free **LintCode** link for the
  17 Premium problems), two solution videos to watch *after* an attempt, and four Gemini prompts:
  a **visual walkthrough** with an ASCII diagram at every step, a hint ladder, a code review, and a
  **Gemini Canvas** prompt that builds an interactive step-through animation.
- **Topic blocks**: three verified lectures (the next three each time the topic recurs), 4–5
  practice problems, reference reading, **newsletter issues** (AlgoMaster, ByteByteGo, System
  Design One, System Design Codex, Design Gurus, Engineer's Codex), **ten interview questions**
  each with a Gemini "Answer" link, five Gemini prompts, and the note file.
- **Every Gemini prompt carries the full context**: plan day and week, the phase, the topic with
  its full concept list, the session's focus, what you have already done today.

## Success criteria

- [ ] ~400 problems solved, first-try rate on mediums ≥ 70% by Week 38
- [ ] Every `DS-` and `AL-` topic at confidence ≥ 4 in `trackers/dsa.md`
- [ ] Six LLD projects green, with the extension done
- [ ] Every system design case study written up; can do any of them in 45 minutes aloud
- [ ] Ten stories written and timed; weekly peer mocks from Week 57
- [ ] Referral and application in Week 64; onsite requested for late February 2028

## Files

| File | What |
|------|------|
| `phase-1-foundations.md` … `phase-7-final-sprint.md` | Day-by-day tables |
| `curriculum-dsa.md`, `curriculum-algorithms-theory.md`, `curriculum-lld.md`, `curriculum-system-design.md`, `curriculum-behavioral.md` | The 130 topics |
| `problems.md` | The 527 verified problems |
| `topic-lectures.md` → `topic-videos.md` | Search phrases → verified lecture videos |
| `problem-videos.md` | Verified solution videos |
| `topic-reading.md` | Verified reading, newsletters, practice links |
| `topic-questions.md` | Ten interview questions per topic |
| `weekly-schedule.md` | The weekly rhythm in detail |
| `company-targets.md` | Google (and other) loop notes |
