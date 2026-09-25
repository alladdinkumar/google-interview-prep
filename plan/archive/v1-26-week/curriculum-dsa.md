# DSA Curriculum — Topics, Problem Counts, Resources

**Total target:** ~290 problems over 26 weeks (60 Easy + 200 Medium + 30 Hard).
**Language:** C++ primary, Python fallback.
**Primary sheet:** Striver A2Z DSA Sheet (https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2)
**Backup sheet:** NeetCode 150 / 250 (https://neetcode.io/practice)

---

## Topic-by-Topic Coverage

### 1. C++ STL + Complexity (Week 1)
**Problems: 12 E** | Foundational only.

Sub-topics:
- vector, string, iterators, range-for
- unordered_map, unordered_set, map, set
- priority_queue, stack, queue, deque
- pair, tuple, struct
- algorithm header (sort, lower_bound, upper_bound, binary_search, accumulate)
- Big-O analysis, master theorem light

**Must-know problems:** Two Sum, Reverse String, Valid Palindrome, Find Pivot Index, Running Sum, Squares of Sorted Array, Move Zeroes, Plus One, Best Time to Buy and Sell Stock, Maximum Subarray, Contains Duplicate, Single Number.

---

### 2. Arrays + Hashing + Prefix Sums (Week 2)
**Problems: 18 (15 E + 3 M)**

Sub-topics:
- HashMap internals
- Frequency counting
- Prefix sum (1D), difference array
- Subarray sum patterns

**Must-know problems:** Group Anagrams (M), Top K Frequent Elements (M), Product of Array Except Self (M), Subarray Sum Equals K (M), Find All Duplicates, Intersection of Two Arrays, First Unique Character, Valid Anagram, Longest Consecutive Sequence (M).

---

### 3. Two Pointers + Sliding Window + Binary Search (Week 3)
**Problems: 18 (12 E + 6 M)**

Sub-topics:
- Two pointer (same direction, opposite direction)
- Sliding window (fixed size, variable size)
- Binary search (standard, on answer, rotated array)

**Must-know problems:** 3Sum (M), Container with Most Water (M), Trapping Rain Water (H — Week 4 stretch), Longest Substring Without Repeating Characters (M), Minimum Window Substring (H — Week 4 stretch), Find First and Last Position (M), Search in Rotated Sorted Array (M), Median of Two Sorted Arrays (H — Phase 3 stretch), Koko Eating Bananas (M), Find Peak Element (M).

---

### 4. Recursion + Backtracking (Week 4)
**Problems: 15 M**

Sub-topics:
- Recursion fundamentals (parameter passing, return-style vs accumulator-style)
- Subset / subsequence generation
- Backtracking template
- Pruning

**Must-know problems:** Subsets I + II, Permutations I + II, Combination Sum I + II, Word Search, N-Queens, Sudoku Solver, Palindrome Partitioning, Generate Parentheses, Letter Combinations of a Phone Number, Restore IP Addresses.

---

### 5. Linked Lists (Week 5)
**Problems: 8 M of Week 5's 18**

Sub-topics:
- Single, double, circular LL
- Reversal (full, K-group, between positions)
- Cycle detection (Floyd)
- Merge sorted LLs
- Fast/slow pointers, middle, palindrome check

**Must-know problems:** Reverse Linked List I + II, Linked List Cycle I + II, Merge Two Sorted Lists, Reorder List, Remove Nth from End, Add Two Numbers, Copy List with Random Pointer, Sort List (merge sort on LL), Reverse Nodes in K-Group, Intersection of Two LLs.

---

### 6. Stacks + Queues (Week 5)
**Problems: 10 M of Week 5's 18**

Sub-topics:
- Monotonic stack
- Min stack
- Expression evaluation (postfix, infix)
- Implement queue using stacks / stack using queues
- Sliding window max with deque

**Must-know problems:** Next Greater Element I + II + III, Largest Rectangle in Histogram (H), Maximal Rectangle (H), Daily Temperatures, Min Stack, Evaluate Reverse Polish Notation, Sliding Window Maximum (H), Decode String, Valid Parentheses, Asteroid Collision.

---

### 7. Trees (Weeks 6-7)
**Problems: 38 M (20 + 18)**

Sub-topics (Week 6 — Binary Trees):
- All 4 traversals (recursive + iterative)
- Height, depth, diameter, max path sum
- Views (top, bottom, left, right)
- Serialize / deserialize
- Lowest Common Ancestor (binary tree)

Sub-topics (Week 7 — BST):
- BST validate, insert, delete
- Kth smallest/largest in BST
- Ceiling, floor
- BST to sorted DLL
- Recover BST

**Must-know problems:** Maximum Depth, Same Tree, Invert Binary Tree, Diameter of Binary Tree, Binary Tree Level Order Traversal, Validate BST, Kth Smallest in BST, LCA in BT, LCA in BST, Binary Tree Right Side View, Serialize and Deserialize BT, Path Sum I + II + III, Construct Binary Tree from Preorder and Inorder, Binary Tree Max Path Sum (H), Recover BST.

---

### 8. Heaps + Priority Queue (Week 8)
**Problems: 15 M**

Sub-topics:
- Build heap, heapify
- Top K problems
- Merge K sorted (lists / arrays)
- Heap with custom comparator (C++ priority_queue + lambda)
- Two heaps for median

**Must-know problems:** Kth Largest in Array, Top K Frequent, Find Median from Data Stream (H), Merge K Sorted Lists (H), Reorganize String, Task Scheduler, K Closest Points to Origin, Find K Pairs with Smallest Sums, Smallest Range Covering Elements from K Lists (H).

---

### 9. Graphs (Weeks 9-10)
**Problems: 35 (33 M + 2 H)**

Week 9 — BFS, DFS, topo:
- Adjacency list representation
- BFS, DFS templates
- Cycle detection (directed via DFS color, undirected via DSU/DFS)
- Topological sort (Kahn + DFS)
- Bipartite check
- Number of connected components

Week 10 — Shortest path + MST + DSU:
- Dijkstra (priority_queue-based)
- Bellman-Ford intro (1 problem)
- DSU with path compression + union-by-rank
- Kruskal's MST
- Prim's MST

**Must-know problems:** Number of Islands, Clone Graph, Course Schedule I + II, Pacific Atlantic Water Flow, Surrounded Regions, Rotting Oranges, Word Ladder, Word Ladder II (H), Network Delay Time, Cheapest Flights Within K Stops, Min Cost to Connect All Points, Redundant Connection, Accounts Merge, Number of Provinces, Critical Connections (Tarjan — H), Alien Dictionary.

---

### 10. Dynamic Programming (Weeks 11-12)
**Problems: 40 (38 M + 2 H)**

Aditya Verma framework (5 patterns):
1. **0/1 Knapsack family** — Subset Sum, Equal Subset Sum Partition, Count Subset Sum, Target Sum, Min Subset Sum Difference
2. **Unbounded Knapsack family** — Coin Change I + II, Rod Cutting, Min Coins
3. **LCS family** — Longest Common Subsequence, Longest Common Substring, Edit Distance, Distinct Subsequences, Min Insertions/Deletions, Palindromic Subsequence, Wildcard Matching
4. **Grid DP** — Unique Paths I + II, Min Path Sum, Triangle, Dungeon Game (H), Cherry Pickup II
5. **MCM family** — Matrix Chain Multiplication, Burst Balloons (H), Palindrome Partitioning II, Boolean Parenthesization

Plus 1D classics: Climbing Stairs, House Robber I + II, Decode Ways, Longest Increasing Subsequence, Maximum Product Subarray.

---

### 11. Tries + Advanced Strings (Week 13)
**Problems: 12**

Sub-topics:
- Trie insert/search/prefix-search
- Trie + DFS (Word Search II)
- KMP (LPS array)
- Rabin-Karp rolling hash
- Z-algorithm intro

**Must-know problems:** Implement Trie, Word Search II (H), Replace Words, Map Sum Pairs, Longest Word in Dictionary, KMP — Find substring in string, Repeated DNA Sequences.

---

### 12. Segment Tree + Fenwick + Advanced DP (Week 14)
**Problems: 12**

Sub-topics:
- Segment tree (build + range query + point update; lazy propagation light)
- Fenwick tree (BIT)
- Tree DP (House Robber III, Diameter via DP, LIS on tree)
- Bitmask DP (Partition to K Subsets, Smallest Sufficient Team, TSP intro)
- Digit DP (Count Numbers with Unique Digits, Numbers with property X)

---

### Phase 3+ Hard Practice (Weeks 13-22, ad hoc)
~10-15 hards across phases. Pick from:

- Median of Two Sorted Arrays
- Merge K Sorted Lists
- Trapping Rain Water (DP/two-pointer)
- Sliding Window Maximum
- Largest Rectangle in Histogram
- Burst Balloons
- Edit Distance
- Word Ladder II
- Critical Connections
- Serialize and Deserialize Binary Tree
- LRU Cache (also LLD)
- LFU Cache
- Regular Expression Matching
- N-Queens II (count)

---

## Daily Quota Summary

| Phase | Weeks | Easy/wk | Medium/wk | Hard/wk |
|-------|-------|---------|-----------|---------|
| 1 | 4 | ~12 | ~3 | 0 |
| 2 | 8 | 0 | ~18 | ~0.5 |
| 3 | 5 | 0 | ~3 (mixed in) | ~1 |
| 4 | 5 | 0 | ~1 (revision) | 0 |
| 5 | 4 | 0 | ~3 (weak-area drill) | ~1 |

---

## Tracking

Every problem solved goes in:
1. Your **daily log** (problem name, time taken, first-try Y/N)
2. **trackers/dsa.md** per topic (updated weekly)
3. **trackers/weak-areas.md** if you needed a hint or couldn't solve

Don't track problems you didn't attempt seriously. A skim of the solution doesn't count.
