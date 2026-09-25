# Phase 5 — System Design (Weeks 45–56)

**Weeks:** 45–56 (12 weeks) · **Budget:** ~117 h at ~9.75 h/week
**Dates:** worked out by the planner from the start date and any skipped days — see `PLAN.md`.

---

## Why this phase

System design: the vocabulary first, then Google's own papers, then twelve case studies in the 45-minute shape. Your infrastructure background is the lever here. Lunches: three DSA problems and one reading.

---

## How to read the tables

- `LC-<n>` is a problem from `problems.md`; the planner links it, its free alternative if it is Premium, its solution videos, and the Gemini walkthrough.
- `DS-`, `LD-`, `SD-`, `BH-`, `IC-` ids are topics from the curriculum files; the planner shows three lectures, 4–5 practice items, reading, the note file and the Gemini prompts for each.
- Weekday lunch drills the topic learned the Saturday before. Wednesday is a cold redo of a problem from two weeks back.

---

## Weekly breakdown

### Week 45 — System design interview framework + Back of the envelope estimation
**Hours: 9.75** | **Topics: SD-1, SD-2**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-443 String Compression (Medium, DS-5). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-992 Subarrays with K Different Integers (Hard, DS-6). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-199 Binary Tree Right Side View (Medium, DS-13) — first solved in week 11. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-378 Kth Smallest Element in a Sorted Matrix (Medium, DS-7). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | Read for SD-1 System design interview framework: the reading list under this topic, 45 min, then three lines in the note | Reading list | `notes/system-design/sd-01-framework.md` |
| Sat | 14:00–16:00 | Learn SD-1 System design interview framework, SD-2 Back of the envelope estimation: the lectures and reading below, then the note in the six-step shape | Topic lectures | `notes/system-design/sd-01-framework.md` + `notes/system-design/sd-02-estimation.md` |
| Sat | 16:15–18:00 | Estimate for YouTube: daily uploads, storage per year, egress bandwidth — written, with every assumption stated (topics: SD-1, SD-2) | Own notes | `notes/system-design/` write-up |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 45: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-45.md` |

### Week 46 — Networking and APIs for system design + Load balancing
**Hours: 9.75** | **Topics: SD-3, SD-4**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-42 Trapping Rain Water (Hard, DS-5). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-76 Minimum Window Substring (Hard, DS-6). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-113 Path Sum II (Medium, DS-14) — first solved in week 11. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-287 Find the Duplicate Number (Medium, DS-7). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | Read for SD-3 Networking and APIs for system design: the reading list under this topic, 45 min, then three lines in the note | Reading list | `notes/system-design/sd-03-networking-apis.md` |
| Sat | 14:00–16:00 | Learn SD-3 Networking and APIs for system design, SD-4 Load balancing: the lectures and reading below, then the note in the six-step shape | Topic lectures | `notes/system-design/sd-03-networking-apis.md` + `notes/system-design/sd-04-load-balancing.md` |
| Sat | 16:15–18:00 | Explain aloud, 10 min each: what happens when you type google.com and press enter; how an L7 load balancer picks a backend (topics: SD-3, SD-4) | Own notes | `notes/system-design/` write-up |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 46: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-46.md` |

### Week 47 — Caching + Databases
**Hours: 9.75** | **Topics: SD-5, SD-6**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-239 Sliding Window Maximum (Hard, DS-6). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-792 Number of Matching Subsequences (Medium, DS-7). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-236 Lowest Common Ancestor of a Binary Tree (Medium, DS-14) — first solved in week 11. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-901 Online Stock Span (Medium, DS-8). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | Read for SD-5 Caching: the reading list under this topic, 45 min, then three lines in the note | Reading list | `notes/system-design/sd-05-caching.md` |
| Sat | 14:00–16:00 | Learn SD-5 Caching, SD-6 Databases: the lectures and reading below, then the note in the six-step shape | Topic lectures | `notes/system-design/sd-05-caching.md` + `notes/system-design/sd-06-databases.md` |
| Sat | 16:15–18:00 | Design the caching and database layer for a product catalogue at 50k QPS reads; justify SQL vs NoSQL (topics: SD-5, SD-6) | Own notes | `notes/system-design/` write-up |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 47: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-47.md` |

### Week 48 — Sharding and consistent hashing + CAP theorem and consensus
**Hours: 9.75** | **Topics: SD-7, SD-8**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-71 Simplify Path (Medium, DS-8). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-622 Design Circular Queue (Medium, DS-9). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-105 Construct Binary Tree from Preorder and Inorder Traversal (Medium, DS-14) — first solved in week 11. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-2 Add Two Numbers (Medium, DS-10). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | Read for SD-7 Sharding and consistent hashing: the reading list under this topic, 45 min, then three lines in the note | Reading list | `notes/system-design/sd-07-sharding.md` |
| Sat | 14:00–16:00 | Learn SD-7 Sharding and consistent hashing, SD-8 CAP theorem and consensus: the lectures and reading below, then the note in the six-step shape | Topic lectures | `notes/system-design/sd-07-sharding.md` + `notes/system-design/sd-08-cap-consensus.md` |
| Sat | 16:15–18:00 | Shard a 10 TB user table: choose the key, handle a hot key, add a node without downtime; where does Raft fit (topics: SD-7, SD-8) | Own notes | `notes/system-design/` write-up |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 48: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-48.md` |

### Week 49 — Message queues and streaming + Rate limiting + Unique ID generation
**Hours: 9.75** | **Topics: SD-9, SD-10, SD-12**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-2390 Removing Stars From a String (Medium, DS-8). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-1696 Jump Game VI (Medium, DS-9). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-114 Flatten Binary Tree to Linked List (Medium, DS-14) — first solved in week 12. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-142 Linked List Cycle II (Medium, DS-10). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | Read for SD-9 Message queues and streaming: the reading list under this topic, 45 min, then three lines in the note | Reading list | `notes/system-design/sd-09-queues-streaming.md` |
| Sat | 14:00–16:00 | Learn SD-9 Message queues and streaming, SD-10 Rate limiting, SD-12 Unique ID generation: the lectures and reading below, then the note in the six-step shape | Topic lectures | `notes/system-design/sd-09-queues-streaming.md` + `notes/system-design/sd-10-rate-limiting.md` + `notes/system-design/sd-12-unique-ids.md` |
| Sat | 16:15–18:00 | Design a distributed rate limiter (SD-10) end to end in 45 min, including ID generation for its audit log (topics: SD-9, SD-10, SD-12) | Own notes | `notes/system-design/` write-up |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 49: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-49.md` |

### Week 50 — Google infrastructure papers
**Hours: 9.75** | **Topics: SD-11**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-1249 Minimum Remove to Make Valid Parentheses (Medium, DS-8). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-862 Shortest Subarray with Sum at Least K (Hard, DS-9). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-437 Path Sum III (Medium, DS-14) — first solved in week 12. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-138 Copy List with Random Pointer (Medium, DS-10). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | Read for SD-11 Google infrastructure papers: the reading list under this topic, 45 min, then three lines in the note | Reading list | `notes/system-design/sd-11-google-papers.md` |
| Sat | 14:00–16:00 | Learn SD-11 Google infrastructure papers: the lectures and reading below, then the note in the six-step shape | Topic lectures | `notes/system-design/sd-11-google-papers.md` |
| Sat | 16:15–18:00 | Write a one-page summary of each of GFS, Bigtable and Spanner: the problem, the key idea, the trade-off (topics: SD-11) | Own notes | `notes/system-design/` write-up |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 50: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-50.md` |

### Week 51 — Design a URL shortener + Design a distributed key value store
**Hours: 9.75** | **Topics: SD-13, SD-14**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-224 Basic Calculator (Hard, DS-8). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-92 Reverse Linked List II (Medium, DS-10). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-863 All Nodes Distance K in Binary Tree (Medium, DS-14) — first solved in week 12. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-451 Sort Characters By Frequency (Medium, DS-12). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | Read for SD-13 Design a URL shortener: the reading list under this topic, 45 min, then three lines in the note | Reading list | `notes/system-design/sd-13-url-shortener.md` |
| Sat | 14:00–16:00 | Learn SD-13 Design a URL shortener, SD-14 Design a distributed key value store: the lectures and reading below, then the note in the six-step shape | Topic lectures | `notes/system-design/sd-13-url-shortener.md` + `notes/system-design/sd-14-key-value-store.md` |
| Sat | 16:15–18:00 | Timed 45 min: design a URL shortener (SD-13) from requirements to deep dive; record yourself (topics: SD-13, SD-14) | Own notes | `notes/system-design/` write-up |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 51: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-51.md` |

### Week 52 — Design a chat system + Design a news feed
**Hours: 9.75** | **Topics: SD-15, SD-16**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-32 Longest Valid Parentheses (Hard, DS-8). 40 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-148 Sort List (Medium, DS-10). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-297 Serialize and Deserialize Binary Tree (Hard, DS-14) — first solved in week 12. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-179 Largest Number (Medium, DS-12). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | Read for SD-15 Design a chat system: the reading list under this topic, 45 min, then three lines in the note | Reading list | `notes/system-design/sd-15-chat.md` |
| Sat | 14:00–16:00 | Learn SD-15 Design a chat system, SD-16 Design a news feed: the lectures and reading below, then the note in the six-step shape | Topic lectures | `notes/system-design/sd-15-chat.md` + `notes/system-design/sd-16-news-feed.md` |
| Sat | 16:15–18:00 | Timed 45 min: design WhatsApp (SD-15); then 30 min on news-feed fan-out trade-offs (SD-16) (topics: SD-15, SD-16) | Own notes | `notes/system-design/` write-up |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 52: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-52.md` |

### Week 53 — Design YouTube video streaming + Design search autocomplete
**Hours: 9.75** | **Topics: SD-17, SD-18**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-328 Odd Even Linked List (Medium, DS-10). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-274 H-Index (Medium, DS-12). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-116 Populating Next Right Pointers in Each Node (Medium, DS-14) — first solved in week 12. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-103 Binary Tree Zigzag Level Order Traversal (Medium, DS-13). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | Read for SD-17 Design YouTube video streaming: the reading list under this topic, 45 min, then three lines in the note | Reading list | `notes/system-design/sd-17-youtube.md` |
| Sat | 14:00–16:00 | Learn SD-17 Design YouTube video streaming, SD-18 Design search autocomplete: the lectures and reading below, then the note in the six-step shape | Topic lectures | `notes/system-design/sd-17-youtube.md` + `notes/system-design/sd-18-autocomplete.md` |
| Sat | 16:15–18:00 | Timed 45 min: design Google search autocomplete (SD-18); 30 min on the YouTube upload pipeline (SD-17) (topics: SD-17, SD-18) | Own notes | `notes/system-design/` write-up |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 53: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-53.md` |

### Week 54 — Design a web crawler + Design Google Drive file storage
**Hours: 9.75** | **Topics: SD-19, SD-20**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-61 Rotate List (Medium, DS-10). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-791 Custom Sort String (Medium, DS-12). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-129 Sum Root to Leaf Numbers (Medium, DS-14) — first solved in week 12. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-1448 Count Good Nodes in Binary Tree (Medium, DS-13). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | Read for SD-19 Design a web crawler: the reading list under this topic, 45 min, then three lines in the note | Reading list | `notes/system-design/sd-19-web-crawler.md` |
| Sat | 14:00–16:00 | Learn SD-19 Design a web crawler, SD-20 Design Google Drive file storage: the lectures and reading below, then the note in the six-step shape | Topic lectures | `notes/system-design/sd-19-web-crawler.md` + `notes/system-design/sd-20-google-drive.md` |
| Sat | 16:15–18:00 | Timed 45 min: design a web crawler (SD-19); 30 min on Google Drive chunked sync (SD-20) (topics: SD-19, SD-20) | Own notes | `notes/system-design/` write-up |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 54: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-54.md` |

### Week 55 — Design a proximity service + Design a notification system
**Hours: 9.75** | **Topics: SD-21, SD-22**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-82 Remove Duplicates from Sorted List II (Medium, DS-10). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-324 Wiggle Sort II (Medium, DS-12). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-106 Construct Binary Tree from Inorder and Postorder Traversal (Medium, DS-14) — first solved in week 13. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-366 Find Leaves of Binary Tree (Medium, DS-13). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | Read for SD-21 Design a proximity service: the reading list under this topic, 45 min, then three lines in the note | Reading list | `notes/system-design/sd-21-proximity.md` |
| Sat | 14:00–16:00 | Learn SD-21 Design a proximity service, SD-22 Design a notification system: the lectures and reading below, then the note in the six-step shape | Topic lectures | `notes/system-design/sd-21-proximity.md` + `notes/system-design/sd-22-notifications.md` |
| Sat | 16:15–18:00 | Timed 45 min: design Uber / nearby search (SD-21); 30 min on notification retries and dedup (SD-22) (topics: SD-21, SD-22) | Own notes | `notes/system-design/` write-up |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 55: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-55.md` |

### Week 56 — Design a metrics monitoring and alerting system + Design a payment system + Design Google Docs collaborative editing
**Hours: 9.75** | **Topics: SD-23, SD-24, SD-25**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | Lunch | LC-24 Swap Nodes in Pairs (Medium, DS-10). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Tue | Lunch | LC-164 Maximum Gap (Medium, DS-12). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Wed | Lunch | Redo cold: LC-1110 Delete Nodes And Return Forest (Medium, DS-14) — first solved in week 13. Blank file, 25 min, no peeking at old code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Thu | Lunch | LC-662 Maximum Width of Binary Tree (Medium, DS-13). 25 min cap; say the complexity before you code | LeetCode | `trackers/dsa.md` row: time, first try Y/N, pattern |
| Fri | Lunch | Read for SD-23 Design a metrics monitoring and alerting system: the reading list under this topic, 45 min, then three lines in the note | Reading list | `notes/system-design/sd-23-metrics-monitoring.md` |
| Sat | 14:00–16:00 | Learn SD-23 Design a metrics monitoring and alerting system, SD-24 Design a payment system, SD-25 Design Google Docs collaborative editing: the lectures and reading below, then the note in the six-step shape | Topic lectures | `notes/system-design/sd-23-metrics-monitoring.md` + `notes/system-design/sd-24-payments.md` + `notes/system-design/sd-25-google-docs.md` |
| Sat | 16:15–18:00 | Timed 45 min: design Google Docs collaborative editing (SD-25); 30 min each on metrics (SD-23) and payments idempotency (SD-24) (topics: SD-23, SD-24, SD-25) | Own notes | `notes/system-design/` write-up |
| Sun | 08:00–09:30 | LeetCode Weekly Contest, live at 08:00 IST (virtual contest if missed). Aim: Q1–Q3 | LeetCode contest | `trackers/mocks.md` contest row |
| Sun | 09:45–10:15 | Weekly review 56: fill the trackers, move misses to weak-areas, pick next week's redo | — | `reviews/weekly/week-56.md` |
