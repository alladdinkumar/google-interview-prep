# Phase 3 — Dynamic Programming and Advanced DSA (Weeks 25–38)

**Weeks:** 25–38 (14 weeks) · **Budget:** ~136 h at ~9.75 h/week
**Dates:** worked out by the planner from the start date and any skipped days — see `PLAN.md`.

---

## Why this phase

Dynamic programming is where L4 candidates most often fail a Google round, so it gets eight weeks, then the advanced structures (segment trees, string algorithms, advanced graphs) that separate a hire from a strong hire.

---

## How to read the tables

- `LC-<n>` is a problem from `problems.md`; the planner links it, its free alternative if it is Premium, its solution videos, and the Gemini walkthrough.
- `DS-`, `LD-`, `SD-`, `BH-`, `IC-` ids are topics from the curriculum files; the planner shows three lectures, 4–5 practice items, reading, the note file and the Gemini prompts for each.
- Weekday lunch drills the topic learned the Saturday before. Wednesday is a cold redo of a problem from two weeks back.

---

## Weekly breakdown

### Week 25 — Dynamic programming 1D
**Hours: 9.75** | **Topics: DS-28, AL-25**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-442 Find All Duplicates in an Array (Medium, DS-3). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | Theory AL-25 Dynamic programming theory: first lecture below (1.5x), the reading, then the note — definition, proof idea, complexity table, the follow-up an interviewer would ask | Topic lectures | `notes/theory/al-25-dp-theory.md` |
| Wed | Lunch | Redo cold: LC-875 Koko Eating Bananas (Medium, DS-7) — first solved in week 6. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-1109 Corporate Flight Bookings (Medium, DS-4). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-15 3Sum (Medium, DS-5). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn DS-28 Dynamic programming 1D: the three lectures below, then the pattern note (signals, C++ template, complexity, traps); solve LC-70 Climbing Stairs (Easy, DS-28) with the note open | Topic lectures | `notes/dsa/ds-28-dp-1d.md` |
| Sat | 16:15–18:00 | Timed, aloud: LC-746 Min Cost Climbing Stairs (Easy, DS-28); LC-198 House Robber (Medium, DS-28); LC-213 House Robber II (Medium, DS-28). Clarify, state complexity, code, dry-run | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern; misses to `trackers/weak-areas.md` |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1 and Q2 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 25: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-25.md` |

### Week 26 — Dynamic programming 1D
**Hours: 9.75** | **Topics: DS-28, AL-26**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-91 Decode Ways (Medium, DS-28). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | Theory AL-26 Classic dynamic programming problems: first lecture below (1.5x), the reading, then the note — definition, proof idea, complexity table, the follow-up an interviewer would ask | Topic lectures | `notes/theory/al-26-classic-dp.md` |
| Wed | Lunch | Redo cold: LC-1011 Capacity To Ship Packages Within D Days (Medium, DS-7) — first solved in week 6. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-139 Word Break (Medium, DS-28). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-152 Maximum Product Subarray (Medium, DS-28). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn DS-28 Dynamic programming 1D: the three lectures below, then the pattern note (signals, C++ template, complexity, traps); solve LC-279 Perfect Squares (Medium, DS-28) with the note open | Topic lectures | `notes/dsa/ds-28-dp-1d.md` |
| Sat | 16:15–18:00 | Timed, aloud: LC-740 Delete and Earn (Medium, DS-28); LC-5 Longest Palindromic Substring (Medium, DS-28); LC-647 Palindromic Substrings (Medium, DS-28). Clarify, state complexity, code, dry-run | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern; misses to `trackers/weak-areas.md` |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1 and Q2 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 26: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-26.md` |

### Week 27 — Grid dynamic programming
**Hours: 9.75** | **Topics: DS-29, AL-27**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-2140 Solving Questions With Brainpower (Medium, DS-28). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | Theory AL-27 Bit manipulation theory: first lecture below (1.5x), the reading, then the note — definition, proof idea, complexity table, the follow-up an interviewer would ask | Topic lectures | `notes/theory/al-27-bits-theory.md` |
| Wed | Lunch | Redo cold: LC-981 Time Based Key-Value Store (Medium, DS-7) — first solved in week 6. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-983 Minimum Cost For Tickets (Medium, DS-28). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-1155 Number of Dice Rolls With Target Sum (Medium, DS-28). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn DS-29 Grid dynamic programming: the three lectures below, then the pattern note (signals, C++ template, complexity, traps); solve LC-62 Unique Paths (Medium, DS-29) with the note open | Topic lectures | `notes/dsa/ds-29-dp-grid.md` |
| Sat | 16:15–18:00 | Timed, aloud: LC-63 Unique Paths II (Medium, DS-29); LC-64 Minimum Path Sum (Medium, DS-29); LC-120 Triangle (Medium, DS-29). Clarify, state complexity, code, dry-run | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern; misses to `trackers/weak-areas.md` |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1 and Q2 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 27: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-27.md` |

### Week 28 — Knapsack dynamic programming
**Hours: 9.75** | **Topics: DS-30, AL-28**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-221 Maximal Square (Medium, DS-29). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | Theory AL-28 Number theory for interviews: first lecture below (1.5x), the reading, then the note — definition, proof idea, complexity table, the follow-up an interviewer would ask | Topic lectures | `notes/theory/al-28-number-theory.md` |
| Wed | Lunch | Redo cold: LC-410 Split Array Largest Sum (Hard, DS-7) — first solved in week 7. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-931 Minimum Falling Path Sum (Medium, DS-29). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-1463 Cherry Pickup II (Hard, DS-29). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn DS-30 Knapsack dynamic programming: the three lectures below, then the pattern note (signals, C++ template, complexity, traps); solve LC-416 Partition Equal Subset Sum (Medium, DS-30) with the note open | Topic lectures | `notes/dsa/ds-30-dp-knapsack.md` |
| Sat | 16:15–18:00 | Timed, aloud: LC-494 Target Sum (Medium, DS-30); LC-1049 Last Stone Weight II (Medium, DS-30); LC-474 Ones and Zeroes (Medium, DS-30). Clarify, state complexity, code, dry-run | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern; misses to `trackers/weak-areas.md` |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1 and Q2 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 28: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-28.md` |

### Week 29 — Dynamic programming on strings
**Hours: 9.75** | **Topics: DS-31, AL-29**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-322 Coin Change (Medium, DS-30). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | Theory AL-29 Combinatorics and probability: first lecture below (1.5x), the reading, then the note — definition, proof idea, complexity table, the follow-up an interviewer would ask | Topic lectures | `notes/theory/al-29-combinatorics-probability.md` |
| Wed | Lunch | Redo cold: LC-4 Median of Two Sorted Arrays (Hard, DS-7) — first solved in week 7. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-518 Coin Change II (Medium, DS-30). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-377 Combination Sum IV (Medium, DS-30). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn DS-31 Dynamic programming on strings: the three lectures below, then the pattern note (signals, C++ template, complexity, traps); solve LC-1143 Longest Common Subsequence (Medium, DS-31) with the note open | Topic lectures | `notes/dsa/ds-31-dp-strings.md` |
| Sat | 16:15–18:00 | Timed, aloud: LC-72 Edit Distance (Medium, DS-31); LC-516 Longest Palindromic Subsequence (Medium, DS-31); LC-583 Delete Operation for Two Strings (Medium, DS-31). Clarify, state complexity, code, dry-run | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern; misses to `trackers/weak-areas.md` |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1 and Q2 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 29: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-29.md` |

### Week 30 — Dynamic programming on strings
**Hours: 9.75** | **Topics: DS-31, AL-30**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-1312 Minimum Insertion Steps to Make a String Palindrome (Hard, DS-31). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | Theory AL-30 Randomized algorithms: first lecture below (1.5x), the reading, then the note — definition, proof idea, complexity table, the follow-up an interviewer would ask | Topic lectures | `notes/theory/al-30-randomized-algorithms.md` |
| Wed | Lunch | Redo cold: LC-81 Search in Rotated Sorted Array II (Medium, DS-7) — first solved in week 7. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-115 Distinct Subsequences (Hard, DS-31). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-97 Interleaving String (Medium, DS-31). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn DS-31 Dynamic programming on strings: the three lectures below, then the pattern note (signals, C++ template, complexity, traps); solve LC-1092 Shortest Common Supersequence  (Hard, DS-31) with the note open | Topic lectures | `notes/dsa/ds-31-dp-strings.md` |
| Sat | 16:15–18:00 | Timed, aloud: LC-44 Wildcard Matching (Hard, DS-31); LC-10 Regular Expression Matching (Hard, DS-31); LC-718 Maximum Length of Repeated Subarray (Medium, DS-31). Clarify, state complexity, code, dry-run | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern; misses to `trackers/weak-areas.md` |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1 and Q2 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 30: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-30.md` |

### Week 31 — Longest increasing subsequence and stock DP
**Hours: 9.75** | **Topics: DS-32, AL-31**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-1035 Uncrossed Lines (Medium, DS-31). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | Theory AL-31 Range query structures: first lecture below (1.5x), the reading, then the note — definition, proof idea, complexity table, the follow-up an interviewer would ask | Topic lectures | `notes/theory/al-31-range-queries.md` |
| Wed | Lunch | Redo cold: LC-155 Min Stack (Medium, DS-8) — first solved in week 7. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-712 Minimum ASCII Delete Sum for Two Strings (Medium, DS-31). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-87 Scramble String (Hard, DS-31). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn DS-32 Longest increasing subsequence and stock DP: the three lectures below, then the pattern note (signals, C++ template, complexity, traps); solve LC-300 Longest Increasing Subsequence (Medium, DS-32) with the note open | Topic lectures | `notes/dsa/ds-32-dp-lis-stock.md` |
| Sat | 16:15–18:00 | Timed, aloud: LC-673 Number of Longest Increasing Subsequence (Medium, DS-32); LC-368 Largest Divisible Subset (Medium, DS-32); LC-1048 Longest String Chain (Medium, DS-32). Clarify, state complexity, code, dry-run | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern; misses to `trackers/weak-areas.md` |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 31: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-31.md` |

### Week 32 — Interval and partition DP
**Hours: 9.75** | **Topics: DS-33, AL-32**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-354 Russian Doll Envelopes (Hard, DS-32). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | Theory AL-32 String matching theory: first lecture below (1.5x), the reading, then the note — definition, proof idea, complexity table, the follow-up an interviewer would ask | Topic lectures | `notes/theory/al-32-string-matching.md` |
| Wed | Lunch | Redo cold: LC-150 Evaluate Reverse Polish Notation (Medium, DS-8) — first solved in week 7. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-309 Best Time to Buy and Sell Stock with Cooldown (Medium, DS-32). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-123 Best Time to Buy and Sell Stock III (Hard, DS-32). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn DS-33 Interval and partition DP: the three lectures below, then the pattern note (signals, C++ template, complexity, traps); solve LC-1039 Minimum Score Triangulation of Polygon (Medium, DS-33) with the note open | Topic lectures | `notes/dsa/ds-33-dp-interval.md` |
| Sat | 16:15–18:00 | Timed, aloud: LC-1547 Minimum Cost to Cut a Stick (Hard, DS-33); LC-312 Burst Balloons (Hard, DS-33); LC-132 Palindrome Partitioning II (Hard, DS-33). Clarify, state complexity, code, dry-run | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern; misses to `trackers/weak-areas.md` |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 32: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-32.md` |

### Week 33 — Tree DP, bitmask DP and digit DP
**Hours: 9.75** | **Topics: DS-34, AL-33**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-664 Strange Printer (Hard, DS-33). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | Theory AL-33 Network flow: first lecture below (1.5x), the reading, then the note — definition, proof idea, complexity table, the follow-up an interviewer would ask | Topic lectures | `notes/theory/al-33-network-flow.md` |
| Wed | Lunch | Redo cold: LC-739 Daily Temperatures (Medium, DS-8) — first solved in week 7. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-877 Stone Game (Medium, DS-33). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-486 Predict the Winner (Medium, DS-33). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn DS-34 Tree DP, bitmask DP and digit DP: the three lectures below, then the pattern note (signals, C++ template, complexity, traps); solve LC-337 House Robber III (Medium, DS-34) with the note open | Topic lectures | `notes/dsa/ds-34-dp-tree-bitmask-digit.md` |
| Sat | 16:15–18:00 | Timed, aloud: LC-968 Binary Tree Cameras (Hard, DS-34); LC-96 Unique Binary Search Trees (Medium, DS-34); LC-834 Sum of Distances in Tree (Hard, DS-34). Clarify, state complexity, code, dry-run | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern; misses to `trackers/weak-areas.md` |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 33: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-33.md` |

### Week 34 — Bit manipulation + Math and matrices for interviews
**Hours: 9.75** | **Topics: DS-35, DS-36, AL-34**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-464 Can I Win (Medium, DS-34). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | Theory AL-34 Computational geometry basics: first lecture below (1.5x), the reading, then the note — definition, proof idea, complexity table, the follow-up an interviewer would ask | Topic lectures | `notes/theory/al-34-geometry.md` |
| Wed | Lunch | Redo cold: LC-503 Next Greater Element II (Medium, DS-8) — first solved in week 8. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-847 Shortest Path Visiting All Nodes (Hard, DS-34). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-1125 Smallest Sufficient Team (Hard, DS-34). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn DS-35 Bit manipulation and DS-36 Math and matrices for interviews: the three lectures below, then the pattern note (signals, C++ template, complexity, traps); solve LC-191 Number of 1 Bits (Easy, DS-35) with the note open | Topic lectures | `notes/dsa/ds-35-bit-manipulation.md` + `notes/dsa/ds-36-math-matrix.md` |
| Sat | 16:15–18:00 | Timed, aloud: LC-338 Counting Bits (Easy, DS-35); LC-190 Reverse Bits (Easy, DS-35); LC-371 Sum of Two Integers (Medium, DS-35). Clarify, state complexity, code, dry-run | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern; misses to `trackers/weak-areas.md` |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 34: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-34.md` |

### Week 35 — Advanced monotonic stack and queue
**Hours: 9.75** | **Topics: DS-40, AL-35**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-137 Single Number II (Medium, DS-35). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | Theory AL-35 Complexity classes: first lecture below (1.5x), the reading, then the note — definition, proof idea, complexity table, the follow-up an interviewer would ask | Topic lectures | `notes/theory/al-35-complexity-classes.md` |
| Wed | Lunch | Redo cold: LC-735 Asteroid Collision (Medium, DS-8) — first solved in week 8. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-260 Single Number III (Medium, DS-35). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-201 Bitwise AND of Numbers Range (Medium, DS-35). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn DS-40 Advanced monotonic stack and queue: the three lectures below, then the pattern note (signals, C++ template, complexity, traps); solve LC-84 Largest Rectangle in Histogram (Hard, DS-40) with the note open | Topic lectures | `notes/dsa/ds-40-monotonic-advanced.md` |
| Sat | 16:15–18:00 | Timed, aloud: LC-85 Maximal Rectangle (Hard, DS-40); LC-907 Sum of Subarray Minimums (Medium, DS-40); LC-456 132 Pattern (Medium, DS-40). Clarify, state complexity, code, dry-run | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern; misses to `trackers/weak-areas.md` |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 35: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-35.md` |

### Week 36 — Segment tree and Fenwick tree
**Hours: 9.75** | **Topics: DS-37, AL-36**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-853 Car Fleet (Medium, DS-40). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | Theory AL-36 Probabilistic data structures: first lecture below (1.5x), the reading, then the note — definition, proof idea, complexity table, the follow-up an interviewer would ask | Topic lectures | `notes/theory/al-36-probabilistic-structures.md` |
| Wed | Lunch | Redo cold: LC-19 Remove Nth Node From End of List (Medium, DS-10) — first solved in week 9. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-1944 Number of Visible People in a Queue (Hard, DS-40). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-1425 Constrained Subsequence Sum (Hard, DS-40). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn DS-37 Segment tree and Fenwick tree: the three lectures below, then the pattern note (signals, C++ template, complexity, traps); solve LC-307 Range Sum Query - Mutable (Medium, DS-37) with the note open | Topic lectures | `notes/dsa/ds-37-segment-fenwick.md` |
| Sat | 16:15–18:00 | Timed, aloud: LC-327 Count of Range Sum (Hard, DS-37); LC-732 My Calendar III (Hard, DS-37); LC-715 Range Module (Hard, DS-37). Clarify, state complexity, code, dry-run | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern; misses to `trackers/weak-areas.md` |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 36: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-36.md` |

### Week 37 — String algorithms + Advanced graphs
**Hours: 9.75** | **Topics: DS-38, DS-39, AL-37**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-699 Falling Squares (Hard, DS-37). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | Theory AL-37 External memory and cache-aware algorithms: first lecture below (1.5x), the reading, then the note — definition, proof idea, complexity table, the follow-up an interviewer would ask | Topic lectures | `notes/theory/al-37-external-memory.md` |
| Wed | Lunch | Redo cold: LC-143 Reorder List (Medium, DS-10) — first solved in week 9. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-1649 Create Sorted Array through Instructions (Hard, DS-37). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-2407 Longest Increasing Subsequence II (Hard, DS-37). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn DS-38 String algorithms and DS-39 Advanced graphs: the three lectures below, then the pattern note (signals, C++ template, complexity, traps); solve LC-28 Find the Index of the First Occurrence in a String (Easy, DS-38) with the note open | Topic lectures | `notes/dsa/ds-38-string-algorithms.md` + `notes/dsa/ds-39-advanced-graphs.md` |
| Sat | 16:15–18:00 | Timed, aloud: LC-459 Repeated Substring Pattern (Easy, DS-38); LC-187 Repeated DNA Sequences (Medium, DS-38); LC-214 Shortest Palindrome (Hard, DS-38). Clarify, state complexity, code, dry-run | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern; misses to `trackers/weak-areas.md` |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 37: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-37.md` |

### Week 38 — Design data structures
**Hours: 9.75** | **Topics: DS-41, AL-38**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-1392 Longest Happy Prefix (Hard, DS-38). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | Theory AL-38 Concurrency data structures: first lecture below (1.5x), the reading, then the note — definition, proof idea, complexity table, the follow-up an interviewer would ask | Topic lectures | `notes/theory/al-38-concurrent-structures.md` |
| Wed | Lunch | Redo cold: LC-50 Pow(x, n) (Medium, DS-11) — first solved in week 9. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-1044 Longest Duplicate Substring (Hard, DS-38). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | LC-2223 Sum of Scores of Built Strings (Hard, DS-38). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Sat | 14:00–16:00 | Learn DS-41 Design data structures: the three lectures below, then the pattern note (signals, C++ template, complexity, traps); solve LC-359 Logger Rate Limiter (Easy, DS-41) with the note open | Topic lectures | `notes/dsa/ds-41-design-data-structures.md` |
| Sat | 16:15–18:00 | Timed, aloud: LC-362 Design Hit Counter (Medium, DS-41); LC-146 LRU Cache (Medium, DS-41); LC-706 Design HashMap (Easy, DS-41). Clarify, state complexity, code, dry-run | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern; misses to `trackers/weak-areas.md` |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 38: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-38.md` |
