# Phase 1 — Foundations (Weeks 1–4)

**Dates:** 2026-05-18 → 2026-06-14 (4 weeks)
**Budget:** ~76 hours (19h/week)
**Theme:** Re-build DSA muscle in C++. Get complexity reflexes back. Solve 60+ problems.

---

## Why This Phase Exists

Your last consistent DSA practice was college. Five years of test automation and infra work doesn't exercise the algorithmic-thinking muscle. **Don't skip this phase even if you "remember it all."** Speed matters in interviews — knowing the answer isn't enough; you have to *produce* the answer fast.

The goal here isn't to learn new tricks. It's to **make recursion, hashing, two-pointers, and complexity analysis feel automatic again.**

---

## Phase Goals (end-of-phase state)

- [ ] 60+ problems solved (mostly easy, some medium)
- [ ] C++ STL fluency: `vector`, `unordered_map`, `unordered_set`, `set`, `map`, `priority_queue`, `stack`, `queue`, `deque`, `string` ops
- [ ] Complexity analysis automatic: can call out time + space of any code in 30 sec
- [ ] Comfortable with input parsing in C++ (interviews still ask)
- [ ] OS chapters 1-3 (process/thread, scheduling) read
- [ ] Light OOP refresh done (5 core concepts re-explained in your notes)

---

## Weekly Breakdown

### Week 1 — C++ STL Refresher + Complexity + Basic Arrays
**Hours: 19** | **Problems: 12 (all Easy)**

| Day | Slot | Focus | Output |
|-----|------|-------|--------|
| Mon | AM | C++ STL — vector, string, iterators | Notes file: `notes/dsa/cpp-stl.md` |
| Mon | PM | Complexity refresher (O notation, common complexities, master theorem light) | Notes: `notes/dsa/complexity.md` |
| Tue | AM | Striver A2Z Step 1 — basics (loops, patterns) — 3 E problems | Daily log |
| Tue | PM | Striver A2Z Step 3 — arrays easy — 3 E problems | Daily log |
| Wed | AM | Two-sum patterns, single-pass arrays — 3 E problems | Daily log |
| Wed | PM | OS Ch 1: Intro, OS structures | Notes: `notes/core/os-ch1.md` |
| Thu | AM | Array problems (Best Time to Buy Stock, Maximum Subarray) — 3 E problems | Daily log |
| Thu | PM | OS Ch 2: Process & Thread | Notes: `notes/core/os-ch2-process.md` |
| Fri | AM | Mixed array problems | Daily log |
| Fri | PM | OS Ch 3: Scheduling algos | Notes: `notes/core/os-ch3-scheduling.md` |
| Sat | 9-1 | 4h block: redo any failed problems, then revise the week's notes | Daily log |
| Sun | — | Weekly review #1 | `reviews/weekly/2026-05-18-to-2026-05-24.md` |

**Resources:**
- Striver A2Z DSA Sheet — https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2
- C++ STL crash: https://www.geeksforgeeks.org/the-c-standard-template-library-stl/
- NeetCode Roadmap (visual reference): https://neetcode.io/roadmap

---

### Week 2 — Strings, Hashing, Prefix Sums + Sorting (Striver Step 2)
**Hours: 19** | **Problems: 18 (15 E + 3 M)** | **Sort algos implemented: 5**

| Day | Slot | Focus | Output |
|-----|------|-------|--------|
| Mon | AM | String basics — palindrome, anagram, reverse — 3 E | Daily log |
| Mon | PM | HashMap deep dive (open addressing vs chaining, load factor) | Notes: `notes/dsa/hashmap-internals.md` |
| Tue | AM | Hashing problems — Two Sum family, Group Anagrams — 3 (2E 1M) | Daily log |
| Tue | PM | Prefix sum theory + 2 E problems | Notes: `notes/dsa/prefix-sum.md` |
| Wed | AM | Subarray sum problems — 3 (2E 1M) | Daily log |
| Wed | PM | OS Ch: Synchronization (semaphores, mutexes) | Notes |
| Thu | AM | String matching — 3 E | Daily log |
| Thu | PM | OS Ch: Deadlocks | Notes |
| Fri | AM | Mixed hashing/string — 3 (2E 1M) | Daily log |
| Fri | PM | **Sorting Part 1**: Selection / Bubble / Insertion sort — watch video + implement all 3 in C++ | Notes: `notes/dsa/sorting.md` (start) |
| Sat | 9-1 | 4h block: (a) 10-11am hard problem — Longest Substring Without Repeating Characters (M); (b) 11am-12pm **Sorting Part 2**: Merge Sort + Quick Sort — watch videos + implement both in C++; (c) 12-1pm redo week's failures + finalize `notes/dsa/sorting.md` | Daily log + notes |
| Sun | — | Weekly review #2 | `reviews/weekly/2026-05-25-to-2026-05-31.md` |

**Resources:**
- NeetCode 150 — Arrays & Hashing section — https://neetcode.io/practice
- Striver A2Z Step 3 — Arrays Easy — https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2
- Striver A2Z Step 2 — Sorting — https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2
- **Fri PM video** — Sorting Part 1 (Selection/Bubble/Insertion) — https://www.youtube.com/watch?v=HGk_ypEuS24
- **Sat video 1** — Merge Sort — https://www.youtube.com/watch?v=ogjf7ORKfd8
- **Sat video 2** — Quick Sort — https://www.youtube.com/watch?v=WIrA4YexLRQ
- Hashmap-internals reading (Mon PM) — search "hashmap open addressing vs chaining" on geeksforgeeks.org

---

### Week 3 — Two Pointers + Sliding Window + Binary Search
**Hours: 19** | **Problems: 18 (12 E + 6 M)**

| Day | Slot | Focus | Output |
|-----|------|-------|--------|
| Mon | AM | Two pointer pattern (intro + 3 problems) | Notes: `notes/dsa/two-pointers.md` |
| Mon | PM | Aditya Verma sliding window playlist videos 1-3 | Notes: `notes/dsa/sliding-window.md` |
| Tue | AM | Sliding window fixed-size — 3 problems (2E 1M) | Daily log |
| Tue | PM | Sliding window variable-size — 3 problems (1E 2M) | Daily log |
| Wed | AM | Two pointer hard cases (3-sum, container with most water) — 3 M | Daily log |
| Wed | PM | OOP refresh: encapsulation, inheritance, polymorphism, abstraction | Notes: `notes/core/oop-basics.md` |
| Thu | AM | Binary search basics — 3 E | Notes: `notes/dsa/binary-search.md` |
| Thu | PM | Binary search on answer pattern intro + 1 problem | Daily log |
| Fri | AM | Binary search variants (rotated array, search range) — 3 (1E 2M) | Daily log |
| Fri | PM | Revision: pattern cheat-sheet for two-pointers / sliding-window / binary-search | Update notes |
| Sat | 9-1 | 4h: hard sliding-window (Minimum Window Substring) + redo failures | Daily log |
| Sun | — | Weekly review #3 | `reviews/weekly/2026-06-01-to-2026-06-07.md` |

**Resources:**
- Aditya Verma sliding window playlist — https://www.youtube.com/playlist?list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj
- NeetCode Two Pointers + Sliding Window sections

---

### Week 4 — Recursion + Backtracking Foundations
**Hours: 19** | **Problems: 15 (15 M)**

| Day | Slot | Focus | Output |
|-----|------|-------|--------|
| Mon | AM | Recursion intro — print N to 1, factorial, fibonacci, sum of digits | Notes: `notes/dsa/recursion-basics.md` |
| Mon | PM | Recursion tree theory + space/time analysis | Notes |
| Tue | AM | Recursion on arrays/strings — 3 problems | Daily log |
| Tue | PM | Subset/subsequence generation pattern — 2 problems | Notes: `notes/dsa/subsequence-pattern.md` |
| Wed | AM | Backtracking intro: N-Queens, Sudoku Solver, Permutations | 3 M problems |
| Wed | PM | Combination Sum I + II + Subsets I + II | 2 problems |
| Thu | AM | Word Search, Palindrome Partitioning | 2 M problems |
| Thu | PM | OS Ch: Memory management intro | Notes |
| Fri | AM | Mixed recursion problems | 3 M problems |
| Fri | PM | Revision: backtracking template | Update notes |
| Sat | 9-1 | 4h: Generate Parentheses + Letter Combinations of Phone Number + redo failures | Daily log |
| Sun | — | **Weekly review + Phase 1 retrospective** | `reviews/weekly/2026-06-08-to-2026-06-14.md` + start `reviews/monthly/2026-06.md` |

**Resources:**
- Striver Recursion playlist — https://www.youtube.com/playlist?list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9
- Aditya Verma Recursion playlist

---

## Daily Quota Cheat Sheet

| Day | Problems target | Concept/theory time |
|-----|-----------------|---------------------|
| Mon-Fri AM | 2-3 problems | — |
| Mon-Fri PM | 0-1 problem (theory-heavy) | 1-1.5h |
| Sat | 1-3 problems (focus on harder ones / redos) | — |

---

## Phase-1 Exit Criteria

Before moving to Phase 2 (Mon 2026-06-15), confirm:

- [ ] 60+ problems solved with notes
- [ ] Can write a recursion template (parameters, base case, recursive case) without thinking
- [ ] Can write a binary search template without off-by-one bugs
- [ ] Can write a sliding window template (fixed and variable)
- [ ] STL operations are reflexive (no looking up `unordered_map::find` syntax)
- [ ] OS chapters 1-3 + OOP basics notes written
- [ ] Adherence ≥70%

If any of these are "no", **extend Phase 1 by 1 week.** Don't bluff your way into Phase 2.
