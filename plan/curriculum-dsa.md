# DSA Curriculum — Patterns, Problems, Notes

**Weeks 1–38 as the main track, then 4–5 lunch drills a week until the end.** Google's loop is
3–4 coding rounds out of 5, each one or two problems in 45 minutes, written in a shared doc
without autocomplete or a run button. This track is the bulk of the preparation for that reason.

**Language:** C++17. Every note has a C++ template. (Python only as a fallback for a stuck
string-manipulation problem — the interview is in C++.)

**How the tables are used.** The planner reads the table below: each row is a topic with its
first week, the note file it writes into, and the LeetCode tags for its practice list. The
problems themselves live in `problems.md`, the videos in `topic-videos.md` and
`problem-videos.md`, the reading in `topic-reading.md`. Nothing is typed twice.

**The topic name is a list of concepts, not one idea.** "Sliding window — fixed window,
variable window, at-most-K trick" is covered when all three are, not when the first is.

---

## Topics

| # | Topic | Week | Note file | Tag |
|---|-------|------|-----------|-----|
| DS-1 | C++ STL for interviews — vector, string, unordered_map, unordered_set, map, set, priority_queue, deque, sort with lambda comparators, lower_bound | 1 | `notes/dsa/ds-01-cpp-stl.md` | array |
| DS-2 | Time and space complexity — Big-O, amortized analysis, recursion complexity, reading constraints to pick the complexity | 1 | `notes/dsa/ds-02-complexity.md` | array, math |
| DS-3 | Arrays and hashing — frequency counting, hash sets, grouping by canonical key, anagrams | 2 | `notes/dsa/ds-03-arrays-hashing.md` | hash-table, array |
| DS-4 | Prefix sums — 1D prefix sum, 2D prefix sum, difference array, subarray sum with hashmap | 3 | `notes/dsa/ds-04-prefix-sums.md` | prefix-sum |
| DS-5 | Two pointers — opposite ends, same direction, pair sums in sorted arrays, 3Sum, Dutch national flag partition | 3 | `notes/dsa/ds-05-two-pointers.md` | two-pointers |
| DS-6 | Sliding window — fixed window, variable window, at-most-K distinct trick, minimum window substring | 4 | `notes/dsa/ds-06-sliding-window.md` | sliding-window |
| DS-7 | Binary search — lower bound and upper bound, rotated sorted array, binary search on the answer, peak finding | 5 | `notes/dsa/ds-07-binary-search.md` | binary-search |
| DS-8 | Stacks — valid parentheses, monotonic stack, next greater element, expression evaluation | 7 | `notes/dsa/ds-08-stacks.md` | stack, monotonic-stack |
| DS-9 | Queues and deques — queue with stacks, circular queue, monotonic deque, sliding window maximum | 7 | `notes/dsa/ds-09-queues-deques.md` | queue, monotonic-queue |
| DS-10 | Linked lists — reversal, fast and slow pointers, cycle detection, merging lists, dummy head | 8 | `notes/dsa/ds-10-linked-lists.md` | linked-list |
| DS-11 | Recursion and divide and conquer — recursion tree, merge sort, quickselect, counting inversions | 9 | `notes/dsa/ds-11-recursion-divide-conquer.md` | recursion, divide-and-conquer |
| DS-12 | Sorting — custom comparators, counting sort, bucket sort, sorting as preprocessing | 9 | `notes/dsa/ds-12-sorting.md` | sorting |
| DS-13 | Binary tree traversals — preorder, inorder, postorder, iterative traversal, level order BFS, height and diameter | 10 | `notes/dsa/ds-13-binary-tree-traversals.md` | binary-tree, tree |
| DS-14 | Binary tree paths and construction — path sum, lowest common ancestor, build from preorder and inorder, serialize and deserialize | 11 | `notes/dsa/ds-14-tree-paths-construction.md` | binary-tree, depth-first-search |
| DS-15 | Binary search trees — validate BST, insert and delete, kth smallest, BST iterator, inorder successor | 13 | `notes/dsa/ds-15-bst.md` | binary-search-tree |
| DS-16 | Heaps and priority queues — top K elements, k-way merge, two heaps for running median, scheduling with heaps | 14 | `notes/dsa/ds-16-heaps.md` | heap-priority-queue |
| DS-17 | Backtracking — subsets, permutations, combinations, pruning duplicates | 15 | `notes/dsa/ds-17-backtracking.md` | backtracking |
| DS-18 | Constraint backtracking — N-Queens, word search on grid, sudoku solver, palindrome partitioning | 16 | `notes/dsa/ds-18-constraint-backtracking.md` | backtracking |
| DS-19 | Graph traversal — adjacency list, depth first search, breadth first search, connected components, islands on a grid, bipartite check | 17 | `notes/dsa/ds-19-graph-traversal.md` | graph, depth-first-search, breadth-first-search |
| DS-20 | BFS shortest paths — multi-source BFS, 0-1 BFS, word ladder, BFS with state | 18 | `notes/dsa/ds-20-bfs-shortest-path.md` | breadth-first-search |
| DS-21 | Topological sort — Kahn algorithm, DFS postorder, cycle detection in directed graph, course schedule | 19 | `notes/dsa/ds-21-topological-sort.md` | topological-sort |
| DS-22 | Union find — disjoint set union, path compression, union by rank, connected components, redundant connection | 20 | `notes/dsa/ds-22-union-find.md` | union-find |
| DS-23 | Weighted shortest paths — Dijkstra algorithm, Bellman-Ford, Floyd-Warshall | 21 | `notes/dsa/ds-23-shortest-paths.md` | shortest-path |
| DS-24 | Minimum spanning tree — Kruskal algorithm, Prim algorithm | 21 | `notes/dsa/ds-24-mst.md` | minimum-spanning-tree |
| DS-25 | Greedy algorithms — exchange argument, jump game, gas station, task assignment | 22 | `notes/dsa/ds-25-greedy.md` | greedy |
| DS-26 | Intervals — merge intervals, insert interval, meeting rooms, sweep line | 23 | `notes/dsa/ds-26-intervals.md` | sweep-line, sorting |
| DS-27 | Tries — insert and search, prefix search, word search II, autocomplete | 23 | `notes/dsa/ds-27-tries.md` | trie |
| DS-28 | Dynamic programming 1D — memoization, tabulation, climbing stairs, house robber, decode ways, word break | 25 | `notes/dsa/ds-28-dp-1d.md` | dynamic-programming, memoization |
| DS-29 | Grid dynamic programming — unique paths, minimum path sum, maximal square, falling path | 27 | `notes/dsa/ds-29-dp-grid.md` | dynamic-programming, matrix |
| DS-30 | Knapsack dynamic programming — 0/1 knapsack, subset sum, unbounded knapsack, coin change | 28 | `notes/dsa/ds-30-dp-knapsack.md` | dynamic-programming |
| DS-31 | Dynamic programming on strings — longest common subsequence, edit distance, palindromic subsequence, wildcard matching | 29 | `notes/dsa/ds-31-dp-strings.md` | dynamic-programming, string |
| DS-32 | Longest increasing subsequence and stock DP — LIS in n log n, patience sorting, Russian doll envelopes, buy and sell stock states | 31 | `notes/dsa/ds-32-dp-lis-stock.md` | dynamic-programming, binary-search |
| DS-33 | Interval and partition DP — matrix chain multiplication, burst balloons, palindrome partitioning II, game DP | 32 | `notes/dsa/ds-33-dp-interval.md` | dynamic-programming, game-theory |
| DS-34 | Tree DP, bitmask DP and digit DP — house robber III, rerooting, bitmask over subsets, digit DP | 33 | `notes/dsa/ds-34-dp-tree-bitmask-digit.md` | dynamic-programming, bitmask |
| DS-35 | Bit manipulation — XOR tricks, bit masks, counting set bits, bitwise operators | 34 | `notes/dsa/ds-35-bit-manipulation.md` | bit-manipulation |
| DS-36 | Math and matrices for interviews — GCD, modular arithmetic, fast exponentiation, sieve of Eratosthenes, matrix rotation and spiral | 34 | `notes/dsa/ds-36-math-matrix.md` | math, matrix, number-theory |
| DS-37 | Segment tree and Fenwick tree — range sum query, point update, binary indexed tree, lazy propagation | 36 | `notes/dsa/ds-37-segment-fenwick.md` | segment-tree, binary-indexed-tree |
| DS-38 | String algorithms — KMP prefix function, Z algorithm, Rabin-Karp rolling hash | 37 | `notes/dsa/ds-38-string-algorithms.md` | string-matching, rolling-hash |
| DS-39 | Advanced graphs — bridges and articulation points, Tarjan algorithm, strongly connected components, Eulerian path | 37 | `notes/dsa/ds-39-advanced-graphs.md` | biconnected-component, eulerian-circuit |
| DS-40 | Advanced monotonic stack and queue — largest rectangle in histogram, trapping rain water, sum of subarray minimums | 35 | `notes/dsa/ds-40-monotonic-advanced.md` | monotonic-stack, monotonic-queue |
| DS-41 | Design data structures — LRU cache, LFU cache, iterators, randomized set, rate limiter and hit counter | 38 | `notes/dsa/ds-41-design-data-structures.md` | design |

---

## How a DSA week runs

| Slot | What happens |
|------|--------------|
| Mon, Tue, Thu, Fri lunch (45 min) | One new problem. 25 min to solve, 10 to read the best solution, 10 to log it. |
| Wed lunch (45 min) | **Redo cold** — a problem from two weeks back, from a blank file. Spaced repetition is what makes a pattern stick. |
| Sat learn block (2 h) | The week's topic: the three lecture videos, the pattern note with a C++ template, one problem walked through. |
| Sat practice block (1 h 45) | Three problems, timed, talking aloud as if in the interview. |
| Sun contest (90 min) | LeetCode Weekly Contest, live (08:00 IST). A virtual contest if you miss it. |

## Rules that make the practice count

- **Timer on, always.** Easy 15 min, Medium 25, Hard 40. Past the cap: read the hint ladder
  (Gemini "Hint ladder" button), not the solution.
- **Talk aloud** from Week 5. Google grades the communication, not just the code.
- **State complexity before coding**, then write it, then dry-run one example by hand.
- **Log every problem** in `trackers/dsa.md`: time, first-try Y/N, the pattern in three words.
- A problem you needed the solution for goes to `trackers/weak-areas.md` and comes back as a
  Wednesday redo.
