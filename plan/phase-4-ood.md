# Phase 4 — Object-Oriented Design (Weeks 39–44)

**Weeks:** 39–44 (6 weeks) · **Budget:** ~58 h at ~9.75 h/week
**Dates:** worked out by the planner from the start date and any skipped days — see `PLAN.md`.

---

## Why this phase

Object-oriented design as it appears inside Google coding rounds: clean interfaces, the patterns that earn their place, and thread safety. Weekday lunches keep DSA warm with mixed problems.

---

## How to read the tables

- `LC-<n>` is a problem from `problems.md`; the planner links it, its free alternative if it is Premium, its solution videos, and the Gemini walkthrough.
- `DS-`, `LD-`, `SD-`, `BH-`, `IC-` ids are topics from the curriculum files; the planner shows three lectures, 4–5 practice items, reading, the note file and the Gemini prompts for each.
- Weekday lunch drills the topic learned the Saturday before. Wednesday is a cold redo of a problem from two weeks back.

---

## Weekly breakdown

### Week 39 — Object-oriented programming in C++ + SOLID principles
**Hours: 9.75** | **Topics: LD-1, LD-2**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-554 Brick Wall (Medium, DS-3). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-1248 Count Number of Nice Subarrays (Medium, DS-4). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-215 Kth Largest Element in an Array (Medium, DS-11) — first solved in week 9. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-11 Container With Most Water (Medium, DS-5). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-340 Longest Substring with At Most K Distinct Characters (Medium, DS-6). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn LD-1 Object-oriented programming in C++, LD-2 SOLID principles: the lectures and reading below, then the note | Topic lectures | `notes/lld/ld-01-oop-cpp.md` + `notes/lld/ld-02-solid.md` |
| Sat | 16:15–18:00 | Build project `projects/lld/01-lru-cache/` — generic LRU cache library: interfaces first, SOLID checklist from the note (LD-1, LD-2). Implement the stubs until `make test` is all green, then the extension at the end of its README | Project README | `projects/lld/01-lru-cache/README.md` checklist; tests green |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 39: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-39.md` |

### Week 40 — Creational design patterns + UML for interviews
**Hours: 9.75** | **Topics: LD-3, LD-6**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-454 4Sum II (Medium, DS-3). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-1314 Matrix Block Sum (Medium, DS-4). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-912 Sort an Array (Medium, DS-11) — first solved in week 9. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-75 Sort Colors (Medium, DS-5). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-1423 Maximum Points You Can Obtain from Cards (Medium, DS-6). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn LD-3 Creational design patterns, LD-6 UML for interviews: the lectures and reading below, then the note | Topic lectures | `notes/lld/ld-03-creational-patterns.md` + `notes/lld/ld-06-uml.md` |
| Sat | 16:15–18:00 | Build project `projects/lld/02-notification-service/` — notification service: factory for channels, builder for messages, class diagram in the README (LD-3, LD-6). Implement the stubs until `make test` is all green, then the extension at the end of its README | Project README | `projects/lld/02-notification-service/README.md` checklist; tests green |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 40: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-40.md` |

### Week 41 — Structural design patterns + Behavioral design patterns
**Hours: 9.75** | **Topics: LD-4, LD-5**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-939 Minimum Area Rectangle (Medium, DS-3). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-1074 Number of Submatrices That Sum to Target (Hard, DS-4). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-315 Count of Smaller Numbers After Self (Hard, DS-11) — first solved in week 10. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-881 Boats to Save People (Medium, DS-5). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-1493 Longest Subarray of 1's After Deleting One Element (Medium, DS-6). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn LD-4 Structural design patterns, LD-5 Behavioral design patterns: the lectures and reading below, then the note | Topic lectures | `notes/lld/ld-04-structural-patterns.md` + `notes/lld/ld-05-behavioral-patterns.md` |
| Sat | 16:15–18:00 | Build project `projects/lld/03-text-editor/` — text editor with undo/redo (command), formatting (decorator), document tree (composite) (LD-4, LD-5). Implement the stubs until `make test` is all green, then the extension at the end of its README | Project README | `projects/lld/03-text-editor/README.md` checklist; tests green |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 41: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-41.md` |

### Week 42 — Concurrency in C++ + Parking lot design
**Hours: 9.75** | **Topics: LD-7, LD-8**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-18 4Sum (Medium, DS-5). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-1052 Grumpy Bookstore Owner (Medium, DS-6). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-241 Different Ways to Add Parentheses (Medium, DS-11) — first solved in week 10. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-658 Find K Closest Elements (Medium, DS-7). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-394 Decode String (Medium, DS-8). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn LD-7 Concurrency in C++, LD-8 Parking lot design: the lectures and reading below, then the note | Topic lectures | `notes/lld/ld-07-concurrency.md` + `notes/lld/ld-08-parking-lot.md` |
| Sat | 16:15–18:00 | Build project `projects/lld/04-parking-lot/` — thread-safe parking lot: allocation strategy, pricing, concurrent park/unpark (LD-7, LD-8). Implement the stubs until `make test` is all green, then the extension at the end of its README | Project README | `projects/lld/04-parking-lot/README.md` checklist; tests green |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 42: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-42.md` |

### Week 43 — Elevator system design + Game design + Splitwise expense sharing design
**Hours: 9.75** | **Topics: LD-9, LD-10, LD-11**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-16 3Sum Closest (Medium, DS-5). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-1658 Minimum Operations to Reduce X to Zero (Medium, DS-6). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-493 Reverse Pairs (Hard, DS-11) — first solved in week 10. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-1482 Minimum Number of Days to Make m Bouquets (Medium, DS-7). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-227 Basic Calculator II (Medium, DS-8). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn LD-9 Elevator system design, LD-10 Game design, LD-11 Splitwise expense sharing design: the lectures and reading below, then the note | Topic lectures | `notes/lld/ld-09-elevator.md` + `notes/lld/ld-10-games.md` + `notes/lld/ld-11-splitwise.md` |
| Sat | 16:15–18:00 | Build project `projects/lld/05-splitwise/` — Splitwise: split strategies and balance simplification (LD-9, LD-10, LD-11). Implement the stubs until `make test` is all green, then the extension at the end of its README | Project README | `projects/lld/05-splitwise/README.md` checklist; tests green |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 43: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-43.md` |

### Week 44 — Movie ticket booking design + Rate limiter low level design + Vending machine and ATM design + Logging framework and pub sub design
**Hours: 9.75** | **Topics: LD-12, LD-13, LD-14, LD-15**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-31 Next Permutation (Medium, DS-5). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-1838 Frequency of the Most Frequent Element (Medium, DS-6). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-102 Binary Tree Level Order Traversal (Medium, DS-13) — first solved in week 11. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-1552 Magnetic Force Between Two Balls (Medium, DS-7). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-402 Remove K Digits (Medium, DS-8). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn LD-12 Movie ticket booking design, LD-13 Rate limiter low level design, LD-14 Vending machine and ATM design, LD-15 Logging framework and pub sub design: the lectures and reading below, then the note | Topic lectures | `notes/lld/ld-12-ticket-booking.md` + `notes/lld/ld-13-rate-limiter.md` + `notes/lld/ld-14-vending-atm.md` + `notes/lld/ld-15-logger-pubsub.md` |
| Sat | 16:15–18:00 | Build project `projects/lld/06-ticket-booking/` — movie ticket booking with concurrent seat holds that expire (LD-12, LD-13, LD-14, LD-15). Implement the stubs until `make test` is all green, then the extension at the end of its README | Project README | `projects/lld/06-ticket-booking/README.md` checklist; tests green |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 44: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-44.md` |
