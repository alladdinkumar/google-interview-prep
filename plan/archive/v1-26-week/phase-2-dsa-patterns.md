# Phase 2 — DSA Pattern Grinding (Weeks 5–12)

**Dates:** 2026-06-15 → 2026-08-09 (8 weeks)
**Budget:** ~152 hours (19h/week)
**Theme:** Cover every major DSA pattern at medium level. By end of phase you recognize a pattern in <3 minutes on a fresh problem.

---

## Phase Goals

- [ ] 142 more problems (cumulative ~200 with Phase 1)
- [ ] Trees, graphs, DP, heaps comfortable at medium
- [ ] Pattern recognition reflex: see a new problem → name the pattern in 3 min
- [ ] OS chapters 4-6 done + DBMS basics started
- [ ] All notes filed under `notes/dsa/`

---

## Weekly Breakdown

### Week 5 — Linked Lists + Stacks + Queues
**Problems: 18 M** | **Hours: 19**

Linked List patterns: reversal, cycle detection (Floyd), merge, fast/slow pointers, intersection, K-group reversal.

Stack patterns: monotonic stack (Next Greater Element, Largest Rectangle in Histogram), min stack, valid parentheses, expression evaluation.

Queue patterns: implement using stacks, sliding window max with deque.

- AM Mon-Fri: 2-3 medium problems/day
- PM Mon, Wed, Fri: theory videos + notes (`notes/dsa/linked-list-patterns.md`, `notes/dsa/monotonic-stack.md`)
- PM Tue, Thu: OS Ch 4-5 reading
- Sat 9-1: 1 hard or 2 mediums (LRU cache by hand, Largest Rectangle)
- Sun: weekly review

Resource: Striver Linked List + Stack playlists, NeetCode same sections.

---

### Week 6 — Binary Trees (Traversals + Recursion on Trees)
**Problems: 20 M** | **Hours: 19**

All traversals (pre/in/post + level-order) — recursive AND iterative.

Patterns: height, diameter, max-path-sum, root-to-leaf paths, view problems (top/bottom/left/right), serialize/deserialize.

- AM: 2-3 tree problems/day. Force iterative versions on alternate days.
- PM Mon: traversal cheat-sheet (`notes/dsa/tree-traversals.md`)
- PM Tue: morris traversal (advanced)
- PM Wed: OS Ch 6
- PM Thu: tree problem patterns (diameter, path sum)
- PM Fri: revision
- Sat: hard tree problem (Binary Tree Max Path Sum, Recover BST)
- Sun: weekly review

Resource: Striver Tree playlist (entire), https://takeuforward.org/binary-tree

---

### Week 7 — BST + Tree Variants
**Problems: 18 M** | **Hours: 19**

BST: search, insert, delete, validate, kth smallest/largest, ceiling/floor, LCA in BST.

Other tree problems: LCA in binary tree, distance between nodes, count nodes in complete tree, mirror, symmetric.

- AM: BST problems Mon-Wed (8 total), other tree problems Thu-Fri (6 total)
- PM Mon: BST cheat-sheet
- PM Tue: DBMS Ch 1 — Intro to DBMS (`notes/core/dbms-intro.md`)
- PM Wed: DBMS Ch 2 — ER model
- PM Thu: DBMS Ch 3 — Relational model
- PM Fri: revision
- Sat: 1 hard tree (Recover BST without extra space)
- Sun: weekly review

---

### Week 8 — Heaps + Priority Queue Patterns
**Problems: 15 M** | **Hours: 19**

Heap basics: build heap, heapify, k-th smallest/largest, merge K sorted lists, top K frequent.

Patterns: heap of pairs (with custom comparator in C++), k-sorted array, median in stream (two heaps trick).

- AM: 3 heap problems/day Mon-Fri
- PM Mon: C++ priority_queue with custom comparator (`notes/dsa/heap-cpp.md`)
- PM Tue: DBMS — Normalization
- PM Wed: DBMS — SQL queries practice (free SQLZoo or LeetCode SQL Easy)
- PM Thu: DBMS — Indexes + B+ trees
- PM Fri: revision
- Sat: hard (Median in Data Stream + Smallest Range Covering K Lists)
- Sun: weekly review

---

### Week 9 — Graphs Part 1 (BFS, DFS, Topo Sort, Connected Components)
**Problems: 18 M** | **Hours: 19**

Representation: adjacency list (preferred) vs matrix.

Patterns: BFS shortest path in unweighted, DFS for connectivity, cycle detection (directed and undirected), topological sort (Kahn + DFS), bipartite check, number of islands family.

- AM: 3 graph problems/day Mon-Fri
- PM Mon: graph representation + traversal templates (`notes/dsa/graph-templates.md`)
- PM Tue: cycle detection cheat-sheet
- PM Wed: DBMS — Transactions + ACID
- PM Thu: DBMS — Isolation levels
- PM Fri: revision
- Sat: hard problem (Course Schedule II, Alien Dictionary)
- Sun: weekly review

Resource: Striver Graph playlist Parts 1-3, https://takeuforward.org/graph

---

### Week 10 — Graphs Part 2 (Dijkstra + MST + Union-Find)
**Problems: 17 (15 M + 2 H)** | **Hours: 19**

Dijkstra, Bellman-Ford intro, Floyd-Warshall intro. Prim's + Kruskal's MST. Union-Find (DSU) with path compression and union-by-rank.

Patterns: shortest path in weighted graph, network delay time, MST cost, accounts merge / number of provinces / redundant connection.

- AM: 3 problems/day, mix shortest-path + DSU
- PM Mon: Dijkstra implementation (`notes/dsa/dijkstra.md`)
- PM Tue: DSU template (`notes/dsa/union-find.md`)
- PM Wed: DBMS — NoSQL overview + when to use
- PM Thu: revision graph cheat-sheets
- PM Fri: revision
- Sat: hard problems — Word Ladder II + Critical Connections (Tarjan light)
- Sun: weekly review

---

### Week 11 — DP Part 1 (1D DP + Aditya Verma Patterns)
**Problems: 20 M** | **Hours: 19**

Aditya Verma DP playlist — 0/1 Knapsack, Unbounded Knapsack, then 1D problems (Climbing Stairs, House Robber I+II, Fibonacci variants, Coin Change).

Patterns: identify "choices at each step + overlap"; memoization → tabulation conversion; space optimization.

- AM: 3 DP problems/day Mon-Fri, all starting from recursion → memoization → tabulation
- PM Mon: DP recursion template (`notes/dsa/dp-recursion.md`)
- PM Tue: memoization rules (`notes/dsa/dp-memo.md`)
- PM Wed: CN basics — OSI/TCP/IP layers (`notes/core/cn-layers.md`)
- PM Thu: CN — HTTP request/response cycle
- PM Fri: revision
- Sat: hard DP (Decode Ways II)
- Sun: weekly review

Resource: Aditya Verma DP playlist — https://www.youtube.com/playlist?list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go

---

### Week 12 — DP Part 2 (2D + LCS + Knapsack + MCM)
**Problems: 20 (18 M + 2 H)** | **Hours: 19**

LCS family (Longest Common Subsequence, Longest Palindromic Subsequence, Edit Distance, Distinct Subsequences).

Knapsack subset-sum family, MCM (Matrix Chain Multiplication, Burst Balloons, Palindrome Partitioning II).

Grid DP (Unique Paths, Min Path Sum, Dungeon Game).

- AM: 3 DP problems/day Mon-Fri
- PM Mon: LCS pattern template
- PM Tue: MCM pattern template
- PM Wed: CN — TCP vs UDP
- PM Thu: CN — DNS + how the internet works
- PM Fri: revision
- Sat: 2 hard DPs (Burst Balloons + Edit Distance)
- Sun: **Weekly + Phase 2 retrospective** (write to `reviews/monthly/2026-08.md` too)

---

## Phase-2 Exit Criteria

Before Phase 3 (Mon 2026-08-10):

- [ ] 200+ total problems solved
- [ ] Tree, graph, DP comfortable at medium tier
- [ ] Pattern-name recall: given a problem, can name the pattern in 3 min
- [ ] OS Ch 4-6 + DBMS basics + CN basics all noted
- [ ] Adherence ≥65%
- [ ] At least 80% of weak-areas list from weekly reviews has remediation plans

If <180 problems solved or pattern recognition still slow, extend Phase 2 by 1 week.
