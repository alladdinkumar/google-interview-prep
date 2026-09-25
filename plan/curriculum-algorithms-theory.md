# Algorithms & Data Structures Theory — basic to advanced, one topic a week

**Every Tuesday lunch, Weeks 1–38.** The DSA track (`curriculum-dsa.md`) teaches *patterns* —
how to recognise and solve a problem. This track teaches the *theory underneath*: why a hash
table is O(1) on average and when it is not, why Dijkstra fails on negative edges, why
comparison sorting cannot beat n log n. Google interviewers push on exactly this in follow-ups
("what's the worst case?", "prove the greedy choice is safe", "what if the input doesn't fit in
memory?"), and it is what separates "solved it" from "strong hire".

Order runs from first principles to advanced, and each topic sits in the week its pattern is
drilled, so Tuesday's theory explains Saturday's pattern.

**The Tag column** lists the DSA topics whose problems exercise this theory — the planner
uses them for the practice list under the topic.

---

## Topics

| # | Topic | Week | Note file | Tag |
|---|-------|------|-----------|-----|
| AL-1 | Asymptotic notation — Big O, Big Omega, Big Theta, best, average and worst case, growth rates | 1 | `notes/theory/al-01-asymptotic-notation.md` | DS-2 |
| AL-2 | Arrays and dynamic arrays — contiguous memory, cache locality, vector growth, amortized doubling | 2 | `notes/theory/al-02-dynamic-arrays.md` | DS-1, DS-3 |
| AL-3 | Hash table internals — hash functions, separate chaining, open addressing, load factor, rehashing, worst case | 3 | `notes/theory/al-03-hash-tables.md` | DS-3 |
| AL-4 | Recurrence relations — substitution method, recursion tree method, master theorem | 4 | `notes/theory/al-04-recurrences-master-theorem.md` | DS-11 |
| AL-5 | Searching theory — linear search, binary search invariants and correctness, ternary search, exponential search | 5 | `notes/theory/al-05-searching.md` | DS-7 |
| AL-6 | Strings in memory — character encoding ASCII and UTF-8, std::string, string immutability, string builder cost | 6 | `notes/theory/al-06-strings-memory.md` | DS-5, DS-6 |
| AL-7 | Stack and queue abstract data types — array vs linked implementation, circular buffer, the call stack | 7 | `notes/theory/al-07-stack-queue-adt.md` | DS-8, DS-9 |
| AL-8 | Linked list variants — singly, doubly, circular, sentinel nodes, skip list | 8 | `notes/theory/al-08-linked-list-variants.md` | DS-10 |
| AL-9 | Comparison sorting algorithms — bubble, selection, insertion, merge sort, quicksort, heap sort, stability, in-place | 9 | `notes/theory/al-09-comparison-sorting.md` | DS-11, DS-12 |
| AL-10 | Sorting lower bound and linear sorts — decision tree lower bound, counting sort, radix sort, bucket sort | 10 | `notes/theory/al-10-sorting-lower-bound.md` | DS-12 |
| AL-11 | Tree fundamentals — binary tree properties, full complete and perfect trees, tree representations, tree traversal theory | 11 | `notes/theory/al-11-tree-fundamentals.md` | DS-13, DS-14 |
| AL-12 | Balanced binary search trees — AVL tree rotations, red black tree properties, std::map guarantees | 12 | `notes/theory/al-12-balanced-bst.md` | DS-15 |
| AL-13 | B-trees and B+ trees — disk based indexes, node fanout, database index structure | 13 | `notes/theory/al-13-b-trees.md` | DS-15 |
| AL-14 | Binary heap internals — array representation, sift up and sift down, build heap in linear time, heap sort | 14 | `notes/theory/al-14-binary-heap.md` | DS-16 |
| AL-15 | Recursion and backtracking theory — state space tree, pruning, complexity of subsets and permutations | 15 | `notes/theory/al-15-backtracking-theory.md` | DS-17, DS-18 |
| AL-16 | Graph theory basics — adjacency matrix vs adjacency list, directed and undirected, weighted graphs, degree, handshake lemma | 16 | `notes/theory/al-16-graph-basics.md` | DS-19 |
| AL-17 | DFS and BFS theory — edge classification, discovery and finish times, BFS layers, correctness of BFS shortest path | 17 | `notes/theory/al-17-dfs-bfs-theory.md` | DS-19, DS-20 |
| AL-18 | Directed acyclic graphs — topological order existence, cycle detection proof, strongly connected components concept | 18 | `notes/theory/al-18-dags.md` | DS-21 |
| AL-19 | Disjoint set union analysis — union by rank, path compression, inverse Ackermann complexity | 19 | `notes/theory/al-19-dsu-analysis.md` | DS-22 |
| AL-20 | Shortest path theory — edge relaxation, Dijkstra correctness, negative edges, Bellman-Ford, Floyd-Warshall, A star search | 20 | `notes/theory/al-20-shortest-path-theory.md` | DS-23 |
| AL-21 | Minimum spanning tree theory — cut property, cycle property, Kruskal vs Prim complexity | 21 | `notes/theory/al-21-mst-theory.md` | DS-24 |
| AL-22 | Greedy algorithm proofs — greedy choice property, exchange argument, activity selection, Huffman coding | 22 | `notes/theory/al-22-greedy-proofs.md` | DS-25, DS-26 |
| AL-23 | Tries and suffix structures — trie complexity, compressed trie, suffix array, suffix tree | 23 | `notes/theory/al-23-tries-suffix-structures.md` | DS-27, DS-38 |
| AL-24 | Amortized analysis — aggregate method, accounting method, potential method | 24 | `notes/theory/al-24-amortized-analysis.md` | DS-9, DS-41 |
| AL-25 | Dynamic programming theory — optimal substructure, overlapping subproblems, state design, top down vs bottom up, space optimization | 25 | `notes/theory/al-25-dp-theory.md` | DS-28 |
| AL-26 | Classic dynamic programming problems — 0/1 knapsack pseudo polynomial time, longest common subsequence, edit distance, matrix chain multiplication | 26 | `notes/theory/al-26-classic-dp.md` | DS-30, DS-31 |
| AL-27 | Bit manipulation theory — two's complement, signed and unsigned integers, bit shifts, integer overflow | 27 | `notes/theory/al-27-bits-theory.md` | DS-35 |
| AL-28 | Number theory for interviews — prime numbers, sieve of Eratosthenes, Euclid GCD, extended Euclid, modular inverse, fast exponentiation | 28 | `notes/theory/al-28-number-theory.md` | DS-36 |
| AL-29 | Combinatorics and probability — permutations and combinations, pigeonhole principle, expected value, inclusion exclusion | 29 | `notes/theory/al-29-combinatorics-probability.md` | DS-36 |
| AL-30 | Randomized algorithms — randomized quicksort, quickselect expected time, Fisher-Yates shuffle, reservoir sampling | 30 | `notes/theory/al-30-randomized-algorithms.md` | DS-11, DS-36 |
| AL-31 | Range query structures — sparse table, square root decomposition, segment tree theory, Fenwick tree theory | 31 | `notes/theory/al-31-range-queries.md` | DS-37 |
| AL-32 | String matching theory — naive matching, KMP failure function, Rabin-Karp hashing, Z function | 32 | `notes/theory/al-32-string-matching.md` | DS-38 |
| AL-33 | Network flow — max flow min cut theorem, Ford-Fulkerson, Edmonds-Karp, bipartite matching | 33 | `notes/theory/al-33-network-flow.md` | DS-39 |
| AL-34 | Computational geometry basics — cross product, orientation test, line segment intersection, convex hull | 34 | `notes/theory/al-34-geometry.md` | DS-36 |
| AL-35 | Complexity classes — P, NP, NP-complete, NP-hard, polynomial reductions, approximation algorithms | 35 | `notes/theory/al-35-complexity-classes.md` | DS-18, DS-34 |
| AL-36 | Probabilistic data structures — Bloom filter, count-min sketch, HyperLogLog, consistent hashing | 36 | `notes/theory/al-36-probabilistic-structures.md` | DS-3, DS-41 |
| AL-37 | External memory and cache-aware algorithms — external merge sort, memory hierarchy, cache lines, locality | 37 | `notes/theory/al-37-external-memory.md` | DS-12 |
| AL-38 | Concurrency data structures — locks, lock-free queue concept, concurrent hash map, read write locks | 38 | `notes/theory/al-38-concurrent-structures.md` | DS-41 |

---

## How a theory lunch runs (45 min)

1. **15–25 min**: the first lecture under the topic (1.5× speed is fine).
2. **10 min**: the reading link — the precise definitions and the proof sketch.
3. **10 min**: write the note: definition, the one proof idea in three lines, the complexity
   table, and **the follow-up question an interviewer would ask** with your answer.

The Gemini "Explain it" prompt on the topic produces the same structure if the lecture
did not land.
