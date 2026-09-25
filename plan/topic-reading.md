# Topic Reading — reference material, newsletters and practice links per topic

The planner shows these under each topic, beside its three lectures and its problems.

| Kind | What it is |
|------|------------|
| `read` | Reference material: cp-algorithms, cppreference, Wikipedia, Refactoring Guru, Tech Interview Handbook, Hello Interview, the System Design Primer, and Google's own papers (GFS, MapReduce, Bigtable, Spanner, Borg). |
| `newsletter` | Issues from the engineering newsletters whose authors post on LinkedIn — **AlgoMaster** (Ashish Pratap Singh), **ByteByteGo** (Alex Xu), **System Design One** (Neo Kim), **System Design Codex** (Saurabh Dashora), **Design Gurus**, **Engineer's Codex**. LinkedIn newsletter pages need a login and cannot be checked, so these link the same issues on each author's public Substack. |
| `practice` | A design problem write-up or a practice platform, for topics that are not LeetCode problems. |

**How these were chosen and checked (2026-09-25).** Newsletter issues come from each
newsletter's full archive, fetched through the Substack API — 1,700 issues in all. Only
**free** issues were kept; paid-only posts would open on a paywall. Each issue below was
picked by hand for its topic from its title and subtitle; keyword matching alone paired an
Uber AI-agent article with dynamic arrays, so none of these were accepted automatically.
Every URL in this file was then fetched: it had to answer 200 with a page whose title
matches its label (PDFs had to start with a PDF header). Five candidates failed and are not
here — two 404s on Wikipedia and Tech Interview Handbook, one Hello Interview page that does
not exist.

To add one: append a row, keep the kind honest, and run `python webapp/tests/topics_test.py`.

| # | Kind | Label | URL |
|---|------|-------|-----|
| DS-1 | read | cppreference: containers library | https://en.cppreference.com/w/cpp/container |
| DS-1 | read | cppreference: algorithms library | https://en.cppreference.com/w/cpp/algorithm |
| DS-1 | read | cppreference: std::priority_queue | https://en.cppreference.com/w/cpp/container/priority_queue |
| DS-1 | newsletter | AlgoMaster: How to Start LeetCode | https://blog.algomaster.io/p/how-to-start-leetcode-in-2025 |
| DS-2 | read | Wikipedia: Big O notation | https://en.wikipedia.org/wiki/Big_O_notation |
| DS-2 | read | Tech Interview Handbook: algorithms study cheatsheet | https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/ |
| DS-2 | newsletter | ByteByteGo: Big O Notation 101 | https://blog.bytebytego.com/p/ep132-big-o-notation-101-the-secret |
| DS-3 | read | Tech Interview Handbook: hash table | https://www.techinterviewhandbook.org/algorithms/hash-table/ |
| DS-3 | read | Tech Interview Handbook: array | https://www.techinterviewhandbook.org/algorithms/array/ |
| DS-3 | newsletter | AlgoMaster: 12 Must-Know Data Structures | https://blog.algomaster.io/p/12-must-know-data-structures-for-coding-interviews |
| DS-4 | read | Wikipedia: prefix sum | https://en.wikipedia.org/wiki/Prefix_sum |
| DS-4 | read | Tech Interview Handbook: array (prefix sum section) | https://www.techinterviewhandbook.org/algorithms/array/ |
| DS-4 | newsletter | AlgoMaster: LeetCode was HARD until I learned these 15 patterns | https://blog.algomaster.io/p/15-leetcode-patterns |
| DS-5 | read | Tech Interview Handbook: string | https://www.techinterviewhandbook.org/algorithms/string/ |
| DS-5 | read | Wikipedia: Dutch national flag problem | https://en.wikipedia.org/wiki/Dutch_national_flag_problem |
| DS-5 | newsletter | AlgoMaster: 15 LeetCode patterns | https://blog.algomaster.io/p/15-leetcode-patterns |
| DS-5 | newsletter | ByteByteGo: 16 Coding Patterns That Make Interviews Easy | https://blog.bytebytego.com/p/ep174-16-coding-patterns-that-make |
| DS-6 | read | Tech Interview Handbook: string (sliding window) | https://www.techinterviewhandbook.org/algorithms/string/ |
| DS-6 | newsletter | AlgoMaster: 15 LeetCode patterns | https://blog.algomaster.io/p/15-leetcode-patterns |
| DS-6 | newsletter | ByteByteGo: 16 Coding Patterns | https://blog.bytebytego.com/p/ep174-16-coding-patterns-that-make |
| DS-7 | read | cp-algorithms: binary search | https://cp-algorithms.com/num_methods/binary_search.html |
| DS-7 | read | Tech Interview Handbook: sorting and searching | https://www.techinterviewhandbook.org/algorithms/sorting-searching/ |
| DS-7 | read | cppreference: std::lower_bound | https://en.cppreference.com/w/cpp/algorithm/lower_bound |
| DS-8 | read | Tech Interview Handbook: stack | https://www.techinterviewhandbook.org/algorithms/stack/ |
| DS-8 | read | cp-algorithms: minimum stack / minimum queue | https://cp-algorithms.com/data_structures/stack_queue_modification.html |
| DS-8 | read | Wikipedia: stack (abstract data type) | https://en.wikipedia.org/wiki/Stack_(abstract_data_type) |
| DS-9 | read | Tech Interview Handbook: queue | https://www.techinterviewhandbook.org/algorithms/queue/ |
| DS-9 | read | cp-algorithms: minimum stack / minimum queue | https://cp-algorithms.com/data_structures/stack_queue_modification.html |
| DS-9 | read | cppreference: std::deque | https://en.cppreference.com/w/cpp/container/deque |
| DS-10 | read | Tech Interview Handbook: linked list | https://www.techinterviewhandbook.org/algorithms/linked-list/ |
| DS-10 | read | Wikipedia: cycle detection (Floyd) | https://en.wikipedia.org/wiki/Cycle_detection |
| DS-11 | read | Tech Interview Handbook: recursion | https://www.techinterviewhandbook.org/algorithms/recursion/ |
| DS-11 | read | Wikipedia: merge sort | https://en.wikipedia.org/wiki/Merge_sort |
| DS-11 | read | Wikipedia: quickselect | https://en.wikipedia.org/wiki/Quickselect |
| DS-12 | read | Tech Interview Handbook: sorting and searching | https://www.techinterviewhandbook.org/algorithms/sorting-searching/ |
| DS-12 | read | cppreference: std::sort | https://en.cppreference.com/w/cpp/algorithm/sort |
| DS-12 | read | Wikipedia: counting sort | https://en.wikipedia.org/wiki/Counting_sort |
| DS-12 | newsletter | System Design One: Timsort deep dive | https://newsletter.systemdesign.one/p/timsort-algorithm |
| DS-13 | read | Tech Interview Handbook: tree | https://www.techinterviewhandbook.org/algorithms/tree/ |
| DS-13 | read | Wikipedia: tree traversal | https://en.wikipedia.org/wiki/Tree_traversal |
| DS-14 | read | Tech Interview Handbook: tree | https://www.techinterviewhandbook.org/algorithms/tree/ |
| DS-14 | read | Wikipedia: lowest common ancestor | https://en.wikipedia.org/wiki/Lowest_common_ancestor |
| DS-14 | read | cp-algorithms: lowest common ancestor | https://cp-algorithms.com/graph/lca.html |
| DS-15 | read | Wikipedia: binary search tree | https://en.wikipedia.org/wiki/Binary_search_tree |
| DS-16 | read | Tech Interview Handbook: heap | https://www.techinterviewhandbook.org/algorithms/heap/ |
| DS-16 | read | cppreference: std::priority_queue | https://en.cppreference.com/w/cpp/container/priority_queue |
| DS-16 | newsletter | ByteByteGo: How Facebook's distributed priority queue handles trillions of items | https://blog.bytebytego.com/p/how-facebooks-distributed-priority |
| DS-17 | read | Wikipedia: backtracking | https://en.wikipedia.org/wiki/Backtracking |
| DS-17 | read | Tech Interview Handbook: recursion | https://www.techinterviewhandbook.org/algorithms/recursion/ |
| DS-18 | read | Wikipedia: eight queens puzzle | https://en.wikipedia.org/wiki/Eight_queens_puzzle |
| DS-18 | read | Wikipedia: sudoku solving algorithms | https://en.wikipedia.org/wiki/Sudoku_solving_algorithms |
| DS-19 | read | Tech Interview Handbook: graph | https://www.techinterviewhandbook.org/algorithms/graph/ |
| DS-19 | read | cp-algorithms: depth first search | https://cp-algorithms.com/graph/depth-first-search.html |
| DS-19 | read | cp-algorithms: breadth first search | https://cp-algorithms.com/graph/breadth-first-search.html |
| DS-19 | newsletter | AlgoMaster: 7 Graph Algorithms You Should Know | https://blog.algomaster.io/p/7-graph-algorithms-you-should-know |
| DS-19 | newsletter | AlgoMaster: Master Graph Algorithms for Coding Interviews | https://blog.algomaster.io/p/master-graph-algorithms-for-coding |
| DS-20 | read | cp-algorithms: breadth first search | https://cp-algorithms.com/graph/breadth-first-search.html |
| DS-20 | read | cp-algorithms: 0-1 BFS | https://cp-algorithms.com/graph/01_bfs.html |
| DS-20 | newsletter | AlgoMaster: Master Graph Algorithms | https://blog.algomaster.io/p/master-graph-algorithms-for-coding |
| DS-21 | read | cp-algorithms: topological sort | https://cp-algorithms.com/graph/topological-sort.html |
| DS-21 | read | Wikipedia: topological sorting | https://en.wikipedia.org/wiki/Topological_sorting |
| DS-21 | newsletter | AlgoMaster: 7 Graph Algorithms You Should Know | https://blog.algomaster.io/p/7-graph-algorithms-you-should-know |
| DS-22 | read | cp-algorithms: disjoint set union | https://cp-algorithms.com/data_structures/disjoint_set_union.html |
| DS-22 | read | Wikipedia: disjoint-set data structure | https://en.wikipedia.org/wiki/Disjoint-set_data_structure |
| DS-23 | read | cp-algorithms: Dijkstra | https://cp-algorithms.com/graph/dijkstra.html |
| DS-23 | read | cp-algorithms: Bellman-Ford | https://cp-algorithms.com/graph/bellman_ford.html |
| DS-23 | read | cp-algorithms: Floyd-Warshall | https://cp-algorithms.com/graph/all-pair-shortest-path-floyd-warshall.html |
| DS-23 | newsletter | AlgoMaster: 7 Graph Algorithms | https://blog.algomaster.io/p/7-graph-algorithms-you-should-know |
| DS-24 | read | cp-algorithms: Kruskal | https://cp-algorithms.com/graph/mst_kruskal.html |
| DS-24 | read | cp-algorithms: Prim | https://cp-algorithms.com/graph/mst_prim.html |
| DS-25 | read | Wikipedia: greedy algorithm | https://en.wikipedia.org/wiki/Greedy_algorithm |
| DS-25 | read | Wikipedia: interval scheduling | https://en.wikipedia.org/wiki/Interval_scheduling |
| DS-26 | read | Tech Interview Handbook: interval | https://www.techinterviewhandbook.org/algorithms/interval/ |
| DS-26 | read | Wikipedia: sweep line algorithm | https://en.wikipedia.org/wiki/Sweep_line_algorithm |
| DS-27 | read | Tech Interview Handbook: trie | https://www.techinterviewhandbook.org/algorithms/trie/ |
| DS-27 | read | Wikipedia: trie | https://en.wikipedia.org/wiki/Trie |
| DS-27 | read | cp-algorithms: Aho-Corasick (trie-based) | https://cp-algorithms.com/string/aho_corasick.html |
| DS-28 | read | cp-algorithms: introduction to dynamic programming | https://cp-algorithms.com/dynamic_programming/intro-to-dp.html |
| DS-28 | read | Tech Interview Handbook: dynamic programming | https://www.techinterviewhandbook.org/algorithms/dynamic-programming/ |
| DS-28 | newsletter | AlgoMaster: 20 Patterns to Master Dynamic Programming | https://blog.algomaster.io/p/20-patterns-to-master-dynamic-programming |
| DS-29 | read | Tech Interview Handbook: matrix | https://www.techinterviewhandbook.org/algorithms/matrix/ |
| DS-29 | newsletter | AlgoMaster: 20 DP patterns | https://blog.algomaster.io/p/20-patterns-to-master-dynamic-programming |
| DS-30 | read | cp-algorithms: knapsack problem | https://cp-algorithms.com/dynamic_programming/knapsack.html |
| DS-30 | read | Wikipedia: knapsack problem | https://en.wikipedia.org/wiki/Knapsack_problem |
| DS-30 | newsletter | AlgoMaster: 20 DP patterns | https://blog.algomaster.io/p/20-patterns-to-master-dynamic-programming |
| DS-31 | read | Wikipedia: longest common subsequence | https://en.wikipedia.org/wiki/Longest_common_subsequence |
| DS-31 | read | Wikipedia: edit distance | https://en.wikipedia.org/wiki/Edit_distance |
| DS-31 | newsletter | AlgoMaster: 20 DP patterns | https://blog.algomaster.io/p/20-patterns-to-master-dynamic-programming |
| DS-32 | read | cp-algorithms: longest increasing subsequence | https://cp-algorithms.com/sequences/longest_increasing_subsequence.html |
| DS-32 | read | Wikipedia: patience sorting | https://en.wikipedia.org/wiki/Patience_sorting |
| DS-33 | read | Wikipedia: matrix chain multiplication | https://en.wikipedia.org/wiki/Matrix_chain_multiplication |
| DS-33 | newsletter | AlgoMaster: 20 DP patterns | https://blog.algomaster.io/p/20-patterns-to-master-dynamic-programming |
| DS-34 | read | cp-algorithms: DP on broken profile / bitmask | https://cp-algorithms.com/dynamic_programming/profile-dynamics.html |
| DS-34 | read | Wikipedia: travelling salesman problem (Held-Karp) | https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm |
| DS-35 | read | Tech Interview Handbook: binary | https://www.techinterviewhandbook.org/algorithms/binary/ |
| DS-35 | read | cp-algorithms: bit manipulation | https://cp-algorithms.com/algebra/bit-manipulation.html |
| DS-36 | read | Tech Interview Handbook: math | https://www.techinterviewhandbook.org/algorithms/math/ |
| DS-36 | read | Tech Interview Handbook: matrix | https://www.techinterviewhandbook.org/algorithms/matrix/ |
| DS-36 | read | cp-algorithms: binary exponentiation | https://cp-algorithms.com/algebra/binary-exp.html |
| DS-36 | read | cp-algorithms: sieve of Eratosthenes | https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html |
| DS-37 | read | cp-algorithms: segment tree | https://cp-algorithms.com/data_structures/segment_tree.html |
| DS-37 | read | cp-algorithms: Fenwick tree | https://cp-algorithms.com/data_structures/fenwick.html |
| DS-38 | read | cp-algorithms: prefix function (KMP) | https://cp-algorithms.com/string/prefix-function.html |
| DS-38 | read | cp-algorithms: Z-function | https://cp-algorithms.com/string/z-function.html |
| DS-38 | read | cp-algorithms: Rabin-Karp | https://cp-algorithms.com/string/rabin-karp.html |
| DS-38 | read | cp-algorithms: string hashing | https://cp-algorithms.com/string/string-hashing.html |
| DS-39 | read | cp-algorithms: finding bridges | https://cp-algorithms.com/graph/bridge-searching.html |
| DS-39 | read | cp-algorithms: articulation points | https://cp-algorithms.com/graph/cutpoints.html |
| DS-39 | read | cp-algorithms: strongly connected components | https://cp-algorithms.com/graph/strongly-connected-components.html |
| DS-39 | read | cp-algorithms: Eulerian path | https://cp-algorithms.com/graph/euler_path.html |
| DS-40 | read | Tech Interview Handbook: stack | https://www.techinterviewhandbook.org/algorithms/stack/ |
| DS-40 | read | Wikipedia: all nearest smaller values | https://en.wikipedia.org/wiki/All_nearest_smaller_values |
| DS-41 | read | Wikipedia: cache replacement policies (LRU, LFU) | https://en.wikipedia.org/wiki/Cache_replacement_policies |
| DS-41 | newsletter | AlgoMaster: 7 Cache Eviction Strategies | https://blog.algomaster.io/p/7-cache-eviction-strategies |
| DS-41 | newsletter | System Design Codex: Top Cache Eviction Strategies | https://newsletter.systemdesigncodex.com/p/top-cache-eviction-strategies |
| AL-1 | read | Wikipedia: Big O notation | https://en.wikipedia.org/wiki/Big_O_notation |
| AL-1 | read | Wikipedia: best, worst and average case | https://en.wikipedia.org/wiki/Best,_worst_and_average_case |
| AL-1 | newsletter | ByteByteGo: Big O Notation 101 | https://blog.bytebytego.com/p/ep132-big-o-notation-101-the-secret |
| AL-2 | read | Wikipedia: dynamic array | https://en.wikipedia.org/wiki/Dynamic_array |
| AL-2 | read | Wikipedia: locality of reference | https://en.wikipedia.org/wiki/Locality_of_reference |
| AL-2 | read | cppreference: std::vector | https://en.cppreference.com/w/cpp/container/vector |
| AL-3 | read | Wikipedia: hash table | https://en.wikipedia.org/wiki/Hash_table |
| AL-3 | read | Wikipedia: open addressing | https://en.wikipedia.org/wiki/Open_addressing |
| AL-3 | read | cppreference: std::unordered_map | https://en.cppreference.com/w/cpp/container/unordered_map |
| AL-4 | read | Wikipedia: master theorem | https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms) |
| AL-4 | read | Wikipedia: Akra-Bazzi method | https://en.wikipedia.org/wiki/Akra%E2%80%93Bazzi_method |
| AL-5 | read | Wikipedia: binary search | https://en.wikipedia.org/wiki/Binary_search |
| AL-5 | read | Wikipedia: ternary search | https://en.wikipedia.org/wiki/Ternary_search |
| AL-5 | read | Wikipedia: exponential search | https://en.wikipedia.org/wiki/Exponential_search |
| AL-5 | read | cp-algorithms: binary search | https://cp-algorithms.com/num_methods/binary_search.html |
| AL-6 | read | Wikipedia: UTF-8 | https://en.wikipedia.org/wiki/UTF-8 |
| AL-6 | read | cppreference: std::basic_string | https://en.cppreference.com/w/cpp/string/basic_string |
| AL-6 | newsletter | ByteByteGo: Encoding vs Encryption vs Tokenization | https://blog.bytebytego.com/p/ep102-encoding-vs-encryption-vs-tokenization |
| AL-7 | read | Wikipedia: stack (abstract data type) | https://en.wikipedia.org/wiki/Stack_(abstract_data_type) |
| AL-7 | read | Wikipedia: queue (abstract data type) | https://en.wikipedia.org/wiki/Queue_(abstract_data_type) |
| AL-7 | read | Wikipedia: circular buffer | https://en.wikipedia.org/wiki/Circular_buffer |
| AL-7 | read | Wikipedia: call stack | https://en.wikipedia.org/wiki/Call_stack |
| AL-8 | read | Wikipedia: doubly linked list | https://en.wikipedia.org/wiki/Doubly_linked_list |
| AL-8 | read | Wikipedia: skip list | https://en.wikipedia.org/wiki/Skip_list |
| AL-9 | read | Wikipedia: sorting algorithm | https://en.wikipedia.org/wiki/Sorting_algorithm |
| AL-9 | read | Wikipedia: quicksort | https://en.wikipedia.org/wiki/Quicksort |
| AL-9 | read | Wikipedia: heapsort | https://en.wikipedia.org/wiki/Heapsort |
| AL-9 | newsletter | System Design One: Timsort deep dive | https://newsletter.systemdesign.one/p/timsort-algorithm |
| AL-10 | read | Wikipedia: comparison sort (lower bound) | https://en.wikipedia.org/wiki/Comparison_sort |
| AL-10 | read | Wikipedia: radix sort | https://en.wikipedia.org/wiki/Radix_sort |
| AL-10 | read | Wikipedia: bucket sort | https://en.wikipedia.org/wiki/Bucket_sort |
| AL-11 | read | Wikipedia: binary tree | https://en.wikipedia.org/wiki/Binary_tree |
| AL-11 | read | Wikipedia: tree traversal | https://en.wikipedia.org/wiki/Tree_traversal |
| AL-11 | newsletter | ByteByteGo: 10 Key Data Structures We Use Every Day | https://blog.bytebytego.com/p/ep58-10-key-data-structures-we-use |
| AL-12 | read | Wikipedia: AVL tree | https://en.wikipedia.org/wiki/AVL_tree |
| AL-12 | read | Wikipedia: red-black tree | https://en.wikipedia.org/wiki/Red%E2%80%93black_tree |
| AL-12 | read | cppreference: std::map | https://en.cppreference.com/w/cpp/container/map |
| AL-13 | read | Wikipedia: B-tree | https://en.wikipedia.org/wiki/B-tree |
| AL-13 | read | Wikipedia: B+ tree | https://en.wikipedia.org/wiki/B%2B_tree |
| AL-13 | newsletter | AlgoMaster: Database Indexes — a detailed guide | https://blog.algomaster.io/p/a-detailed-guide-on-database-indexes |
| AL-13 | newsletter | Design Gurus: Database indexing with B-tree indexes | https://designgurus.substack.com/p/database-indexing-the-ultimate-guide |
| AL-13 | newsletter | System Design Codex: An intro to LSM trees | https://newsletter.systemdesigncodex.com/p/an-intro-to-lsm-trees |
| AL-14 | read | Wikipedia: binary heap | https://en.wikipedia.org/wiki/Binary_heap |
| AL-14 | read | Wikipedia: heapsort | https://en.wikipedia.org/wiki/Heapsort |
| AL-15 | read | Wikipedia: backtracking | https://en.wikipedia.org/wiki/Backtracking |
| AL-15 | read | Wikipedia: branch and bound | https://en.wikipedia.org/wiki/Branch_and_bound |
| AL-16 | read | Wikipedia: graph (abstract data type) | https://en.wikipedia.org/wiki/Graph_(abstract_data_type) |
| AL-16 | read | Wikipedia: adjacency list | https://en.wikipedia.org/wiki/Adjacency_list |
| AL-16 | read | Wikipedia: handshaking lemma | https://en.wikipedia.org/wiki/Handshaking_lemma |
| AL-17 | read | Wikipedia: depth-first search | https://en.wikipedia.org/wiki/Depth-first_search |
| AL-17 | read | Wikipedia: breadth-first search | https://en.wikipedia.org/wiki/Breadth-first_search |
| AL-17 | read | cp-algorithms: depth first search (edge classification) | https://cp-algorithms.com/graph/depth-first-search.html |
| AL-18 | read | Wikipedia: directed acyclic graph | https://en.wikipedia.org/wiki/Directed_acyclic_graph |
| AL-18 | read | Wikipedia: strongly connected component | https://en.wikipedia.org/wiki/Strongly_connected_component |
| AL-19 | read | Wikipedia: disjoint-set data structure | https://en.wikipedia.org/wiki/Disjoint-set_data_structure |
| AL-19 | read | cp-algorithms: disjoint set union | https://cp-algorithms.com/data_structures/disjoint_set_union.html |
| AL-20 | read | Wikipedia: Dijkstra's algorithm | https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm |
| AL-20 | read | Wikipedia: Bellman-Ford algorithm | https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm |
| AL-20 | read | Wikipedia: A* search algorithm | https://en.wikipedia.org/wiki/A*_search_algorithm |
| AL-21 | read | Wikipedia: minimum spanning tree (cut and cycle properties) | https://en.wikipedia.org/wiki/Minimum_spanning_tree |
| AL-22 | read | Wikipedia: greedy algorithm | https://en.wikipedia.org/wiki/Greedy_algorithm |
| AL-22 | read | Wikipedia: activity selection problem | https://en.wikipedia.org/wiki/Activity_selection_problem |
| AL-22 | read | Wikipedia: Huffman coding | https://en.wikipedia.org/wiki/Huffman_coding |
| AL-23 | read | Wikipedia: suffix array | https://en.wikipedia.org/wiki/Suffix_array |
| AL-23 | read | Wikipedia: suffix tree | https://en.wikipedia.org/wiki/Suffix_tree |
| AL-23 | read | Wikipedia: radix tree | https://en.wikipedia.org/wiki/Radix_tree |
| AL-23 | read | cp-algorithms: suffix array | https://cp-algorithms.com/string/suffix-array.html |
| AL-24 | read | Wikipedia: amortized analysis | https://en.wikipedia.org/wiki/Amortized_analysis |
| AL-24 | read | Wikipedia: potential method | https://en.wikipedia.org/wiki/Potential_method |
| AL-24 | read | Wikipedia: accounting method | https://en.wikipedia.org/wiki/Accounting_method_(computer_science) |
| AL-25 | read | Wikipedia: dynamic programming | https://en.wikipedia.org/wiki/Dynamic_programming |
| AL-25 | read | Wikipedia: optimal substructure | https://en.wikipedia.org/wiki/Optimal_substructure |
| AL-25 | read | cp-algorithms: introduction to DP | https://cp-algorithms.com/dynamic_programming/intro-to-dp.html |
| AL-25 | newsletter | AlgoMaster: 20 DP patterns | https://blog.algomaster.io/p/20-patterns-to-master-dynamic-programming |
| AL-26 | read | Wikipedia: knapsack problem | https://en.wikipedia.org/wiki/Knapsack_problem |
| AL-26 | read | Wikipedia: pseudo-polynomial time | https://en.wikipedia.org/wiki/Pseudo-polynomial_time |
| AL-26 | read | Wikipedia: matrix chain multiplication | https://en.wikipedia.org/wiki/Matrix_chain_multiplication |
| AL-27 | read | Wikipedia: two's complement | https://en.wikipedia.org/wiki/Two%27s_complement |
| AL-27 | read | Wikipedia: bitwise operation | https://en.wikipedia.org/wiki/Bitwise_operation |
| AL-27 | read | Wikipedia: integer overflow | https://en.wikipedia.org/wiki/Integer_overflow |
| AL-28 | read | cp-algorithms: Euclid algorithm | https://cp-algorithms.com/algebra/euclid-algorithm.html |
| AL-28 | read | cp-algorithms: extended Euclid | https://cp-algorithms.com/algebra/extended-euclid-algorithm.html |
| AL-28 | read | cp-algorithms: modular inverse | https://cp-algorithms.com/algebra/module-inverse.html |
| AL-28 | read | cp-algorithms: sieve of Eratosthenes | https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html |
| AL-29 | read | cp-algorithms: binomial coefficients | https://cp-algorithms.com/combinatorics/binomial-coefficients.html |
| AL-29 | read | Wikipedia: pigeonhole principle | https://en.wikipedia.org/wiki/Pigeonhole_principle |
| AL-29 | read | Wikipedia: inclusion-exclusion principle | https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle |
| AL-29 | read | Wikipedia: expected value | https://en.wikipedia.org/wiki/Expected_value |
| AL-30 | read | Wikipedia: reservoir sampling | https://en.wikipedia.org/wiki/Reservoir_sampling |
| AL-30 | read | Wikipedia: Fisher-Yates shuffle | https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle |
| AL-30 | read | Wikipedia: randomized algorithm | https://en.wikipedia.org/wiki/Randomized_algorithm |
| AL-31 | read | cp-algorithms: sparse table | https://cp-algorithms.com/data_structures/sparse-table.html |
| AL-31 | read | cp-algorithms: sqrt decomposition | https://cp-algorithms.com/data_structures/sqrt_decomposition.html |
| AL-31 | read | cp-algorithms: range minimum query | https://cp-algorithms.com/sequences/rmq.html |
| AL-32 | read | cp-algorithms: prefix function | https://cp-algorithms.com/string/prefix-function.html |
| AL-32 | read | cp-algorithms: Z-function | https://cp-algorithms.com/string/z-function.html |
| AL-32 | read | Wikipedia: Knuth-Morris-Pratt algorithm | https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm |
| AL-33 | read | Wikipedia: max-flow min-cut theorem | https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem |
| AL-33 | read | cp-algorithms: Edmonds-Karp | https://cp-algorithms.com/graph/edmonds_karp.html |
| AL-33 | read | cp-algorithms: bipartite matching (Kuhn) | https://cp-algorithms.com/graph/kuhn_maximum_bipartite_matching.html |
| AL-34 | read | cp-algorithms: oriented area / orientation | https://cp-algorithms.com/geometry/oriented-triangle-area.html |
| AL-34 | read | cp-algorithms: convex hull | https://cp-algorithms.com/geometry/convex-hull.html |
| AL-34 | read | cp-algorithms: segment intersection | https://cp-algorithms.com/geometry/check-segments-intersection.html |
| AL-34 | read | Tech Interview Handbook: geometry | https://www.techinterviewhandbook.org/algorithms/geometry/ |
| AL-35 | read | Wikipedia: NP-completeness | https://en.wikipedia.org/wiki/NP-completeness |
| AL-35 | read | Wikipedia: P versus NP problem | https://en.wikipedia.org/wiki/P_versus_NP_problem |
| AL-35 | read | Wikipedia: approximation algorithm | https://en.wikipedia.org/wiki/Approximation_algorithm |
| AL-36 | read | Wikipedia: Bloom filter | https://en.wikipedia.org/wiki/Bloom_filter |
| AL-36 | read | Wikipedia: count-min sketch | https://en.wikipedia.org/wiki/Count%E2%80%93min_sketch |
| AL-36 | read | Wikipedia: HyperLogLog | https://en.wikipedia.org/wiki/HyperLogLog |
| AL-36 | newsletter | AlgoMaster: What are Bloom Filters | https://blog.algomaster.io/p/bloom-filters |
| AL-36 | newsletter | AlgoMaster: Consistent Hashing Explained | https://blog.algomaster.io/p/consistent-hashing-explained |
| AL-36 | newsletter | ByteByteGo: Counting billions of content usage at Canva | https://blog.bytebytego.com/p/counting-billions-of-content-usage |
| AL-37 | read | Wikipedia: external sorting | https://en.wikipedia.org/wiki/External_sorting |
| AL-37 | read | Wikipedia: memory hierarchy | https://en.wikipedia.org/wiki/Memory_hierarchy |
| AL-37 | read | Wikipedia: cache-oblivious algorithm | https://en.wikipedia.org/wiki/Cache-oblivious_algorithm |
| AL-37 | read | Latency numbers every programmer should know | https://gist.github.com/jboner/2841832 |
| AL-38 | read | Wikipedia: non-blocking algorithm | https://en.wikipedia.org/wiki/Non-blocking_algorithm |
| AL-38 | read | Wikipedia: readers-writer lock | https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock |
| AL-38 | read | cppreference: std::atomic | https://en.cppreference.com/w/cpp/atomic/atomic |
| AL-38 | newsletter | ByteByteGo: What is a deadlock? | https://blog.bytebytego.com/p/ep112-what-is-a-deadlock |
| AL-38 | newsletter | AlgoMaster: Concurrency vs Parallelism | https://blog.algomaster.io/p/concurrency-vs-parallelism |
| LD-1 | read | cppreference: virtual function specifier | https://en.cppreference.com/w/cpp/language/virtual |
| LD-1 | read | cppreference: abstract class | https://en.cppreference.com/w/cpp/language/abstract_class |
| LD-1 | newsletter | AlgoMaster: Basic OOP Concepts Explained with Code | https://blog.algomaster.io/p/basic-oop-concepts-explained-with-code |
| LD-1 | newsletter | AlgoMaster: 12 OOP Concepts Every Developer Should Know | https://blog.algomaster.io/p/12-oop-concepts-every-developer-should-know |
| LD-2 | read | Wikipedia: SOLID | https://en.wikipedia.org/wiki/SOLID |
| LD-2 | newsletter | AlgoMaster: SOLID Principles Explained With Code | https://blog.algomaster.io/p/solid-principles-explained-with-code |
| LD-2 | newsletter | ByteByteGo: What is the SOLID principle? | https://blog.bytebytego.com/p/ep175-what-is-the-solid-principle |
| LD-3 | read | Refactoring Guru: factory method | https://refactoring.guru/design-patterns/factory-method |
| LD-3 | read | Refactoring Guru: abstract factory | https://refactoring.guru/design-patterns/abstract-factory |
| LD-3 | read | Refactoring Guru: builder | https://refactoring.guru/design-patterns/builder |
| LD-3 | read | Refactoring Guru: singleton | https://refactoring.guru/design-patterns/singleton |
| LD-3 | newsletter | AlgoMaster: Singleton pattern and 7 ways to implement it | https://blog.algomaster.io/p/singleton-design-pattern |
| LD-4 | read | Refactoring Guru: adapter | https://refactoring.guru/design-patterns/adapter |
| LD-4 | read | Refactoring Guru: decorator | https://refactoring.guru/design-patterns/decorator |
| LD-4 | read | Refactoring Guru: composite | https://refactoring.guru/design-patterns/composite |
| LD-4 | read | Refactoring Guru: facade | https://refactoring.guru/design-patterns/facade |
| LD-4 | read | Refactoring Guru: proxy | https://refactoring.guru/design-patterns/proxy |
| LD-4 | newsletter | AlgoMaster: Every Important Design Pattern Explained | https://blog.algomaster.io/p/every-important-design-pattern-explained |
| LD-5 | read | Refactoring Guru: strategy | https://refactoring.guru/design-patterns/strategy |
| LD-5 | read | Refactoring Guru: observer | https://refactoring.guru/design-patterns/observer |
| LD-5 | read | Refactoring Guru: command | https://refactoring.guru/design-patterns/command |
| LD-5 | read | Refactoring Guru: state | https://refactoring.guru/design-patterns/state |
| LD-5 | read | Refactoring Guru: iterator | https://refactoring.guru/design-patterns/iterator |
| LD-5 | read | Refactoring Guru: chain of responsibility | https://refactoring.guru/design-patterns/chain-of-responsibility |
| LD-5 | newsletter | ByteByteGo: Design patterns cheat sheet | https://blog.bytebytego.com/p/ep17-design-patterns-cheat-sheet |
| LD-5 | newsletter | Design Gurus: 9 top object-oriented design patterns | https://designgurus.substack.com/p/9-top-object-oriented-design-patterns |
| LD-6 | read | Wikipedia: class diagram | https://en.wikipedia.org/wiki/Class_diagram |
| LD-6 | read | Wikipedia: sequence diagram | https://en.wikipedia.org/wiki/Sequence_diagram |
| LD-6 | newsletter | AlgoMaster: UML Class Diagram Explained | https://blog.algomaster.io/p/uml-class-diagram-explained-with-examples |
| LD-7 | read | cppreference: thread support library | https://en.cppreference.com/w/cpp/thread |
| LD-7 | read | cppreference: std::condition_variable | https://en.cppreference.com/w/cpp/thread/condition_variable |
| LD-7 | read | Wikipedia: producer-consumer problem | https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem |
| LD-7 | newsletter | AlgoMaster: Concurrency vs Parallelism | https://blog.algomaster.io/p/concurrency-vs-parallelism |
| LD-7 | newsletter | ByteByteGo: What is a deadlock? | https://blog.bytebytego.com/p/ep112-what-is-a-deadlock |
| LD-7 | newsletter | ByteByteGo: Process vs thread | https://blog.bytebytego.com/p/ep37-process-vs-thread |
| LD-8 | newsletter | AlgoMaster: How to Answer a LLD Interview Problem | https://blog.algomaster.io/p/how-to-answer-a-lld-interview-problem |
| LD-8 | practice | Awesome LLD: parking lot | https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/parking-lot.md |
| LD-9 | practice | Awesome LLD: elevator system | https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/elevator-system.md |
| LD-9 | newsletter | AlgoMaster: How to Answer a LLD Interview Problem | https://blog.algomaster.io/p/how-to-answer-a-lld-interview-problem |
| LD-10 | practice | Awesome LLD: tic tac toe | https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/tic-tac-toe.md |
| LD-10 | practice | Awesome LLD: snake and ladder | https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/snake-and-ladder.md |
| LD-11 | practice | Awesome LLD: Splitwise | https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/splitwise.md |
| LD-12 | practice | Awesome LLD: movie ticket booking | https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/movie-ticket-booking-system.md |
| LD-12 | read | Refactoring Guru: observer | https://refactoring.guru/design-patterns/observer |
| LD-12 | newsletter | ByteByteGo: Optimistic locking | https://blog.bytebytego.com/p/optimistic-locking |
| LD-13 | newsletter | AlgoMaster: Rate Limiting Algorithms Explained with Code | https://blog.algomaster.io/p/rate-limiting-algorithms-explained-with-code |
| LD-13 | read | Wikipedia: token bucket | https://en.wikipedia.org/wiki/Token_bucket |
| LD-14 | practice | Awesome LLD: vending machine | https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/vending-machine.md |
| LD-14 | practice | Awesome LLD: ATM | https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/atm.md |
| LD-14 | read | Refactoring Guru: state | https://refactoring.guru/design-patterns/state |
| LD-15 | practice | Awesome LLD: logging framework | https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/logging-framework.md |
| LD-15 | practice | Awesome LLD: pub-sub system | https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/pub-sub-system.md |
| LD-15 | read | Refactoring Guru: chain of responsibility | https://refactoring.guru/design-patterns/chain-of-responsibility |
| SD-1 | read | System Design Primer | https://github.com/donnemartin/system-design-primer |
| SD-1 | read | Hello Interview: system design in a hurry | https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction |
| SD-1 | newsletter | AlgoMaster: How to Answer a System Design Interview Problem | https://blog.algomaster.io/p/how-to-answer-a-system-design-interview-problem |
| SD-1 | newsletter | ByteByteGo: Step-by-step guide on system design interview | https://blog.bytebytego.com/p/ep46-step-by-step-guide-on-system |
| SD-1 | newsletter | Design Gurus: How to fill 45 minutes with senior-level reasoning | https://designgurus.substack.com/p/system-design-interview-a-7-step |
| SD-1 | newsletter | System Design Codex: 23 system design interview tips | https://newsletter.systemdesigncodex.com/p/system-design-interview-tips |
| SD-2 | read | Latency numbers every programmer should know | https://gist.github.com/jboner/2841832 |
| SD-2 | newsletter | System Design One: Back of the envelope | https://newsletter.systemdesign.one/p/back-of-the-envelope |
| SD-2 | newsletter | Design Gurus: The role of estimations (traffic, storage, bandwidth) | https://designgurus.substack.com/p/the-role-of-estimations-in-system |
| SD-2 | newsletter | ByteByteGo: Latency numbers you should know | https://blog.bytebytego.com/p/ep22-latency-numbers-you-should-know |
| SD-3 | newsletter | System Design One: What happens when you type google.com | https://newsletter.systemdesign.one/p/what-happens-when-you-type-google-com-in-browser |
| SD-3 | newsletter | AlgoMaster: 20 Networking Concepts | https://blog.algomaster.io/p/20-networking-concepts-explained |
| SD-3 | newsletter | AlgoMaster: Long polling vs WebSockets | https://blog.algomaster.io/p/long-polling-vs-websockets |
| SD-3 | newsletter | ByteByteGo: SOAP vs REST vs GraphQL vs RPC | https://blog.bytebytego.com/p/soap-vs-rest-vs-graphql-vs-rpc |
| SD-3 | newsletter | System Design One: How DNS works | https://newsletter.systemdesign.one/p/what-is-a-dns-server-and-how-does-it-work |
| SD-3 | newsletter | ByteByteGo: HTTP/2 over TCP vs HTTP/3 over QUIC | https://blog.bytebytego.com/p/ep200-http2-over-tcp-vs-http3-over |
| SD-4 | newsletter | AlgoMaster: Load Balancing Algorithms Explained with Code | https://blog.algomaster.io/p/load-balancing-algorithms-explained-with-code |
| SD-4 | newsletter | System Design One: How load balancing algorithms really work | https://newsletter.systemdesign.one/p/load-balancing-algorithms |
| SD-4 | newsletter | System Design One: API gateway vs load balancer vs reverse proxy | https://newsletter.systemdesign.one/p/api-gateway-load-balancer-reverse-proxy |
| SD-4 | newsletter | ByteByteGo: What is a load balancer? | https://blog.bytebytego.com/p/ep123-what-is-a-load-balancer |
| SD-5 | read | Hello Interview: caching (core concepts) | https://www.hellointerview.com/learn/system-design/core-concepts/caching |
| SD-5 | newsletter | AlgoMaster: Top 5 Caching Strategies | https://blog.algomaster.io/p/top-5-caching-strategies-explained |
| SD-5 | newsletter | System Design One: Everything about cache strategies | https://newsletter.systemdesign.one/p/cache-strategies |
| SD-5 | newsletter | Design Gurus: Complete guide to cache invalidation | https://designgurus.substack.com/p/the-complete-guide-to-cache-invalidation |
| SD-5 | newsletter | AlgoMaster: What is a CDN? | https://blog.algomaster.io/p/content-delivery-networks |
| SD-5 | newsletter | ByteByteGo: How Facebook served billions of requests with Memcached | https://blog.bytebytego.com/p/how-facebook-served-billions-of-requests |
| SD-6 | read | Hello Interview: database indexing | https://www.hellointerview.com/learn/system-design/core-concepts/db-indexing |
| SD-6 | newsletter | AlgoMaster: SQL vs NoSQL — 7 key differences | https://blog.algomaster.io/p/sql-vs-nosql-7-key-differences |
| SD-6 | newsletter | AlgoMaster: Database indexes — a detailed guide | https://blog.algomaster.io/p/a-detailed-guide-on-database-indexes |
| SD-6 | newsletter | ByteByteGo: What are database isolation levels | https://blog.bytebytego.com/p/what-are-database-isolation-levels |
| SD-6 | newsletter | System Design Codex: Database replication under the hood | https://newsletter.systemdesigncodex.com/p/database-replication-under-the-hood |
| SD-6 | newsletter | ByteByteGo: 8 data structures that power your databases | https://blog.bytebytego.com/p/8-data-structures-that-power-your |
| SD-7 | read | Hello Interview: sharding | https://www.hellointerview.com/learn/system-design/core-concepts/sharding |
| SD-7 | newsletter | AlgoMaster: Consistent Hashing Explained | https://blog.algomaster.io/p/consistent-hashing-explained |
| SD-7 | newsletter | System Design One: Everything about consistent hashing | https://newsletter.systemdesign.one/p/what-is-consistent-hashing |
| SD-7 | newsletter | AlgoMaster: What is database sharding? | https://blog.algomaster.io/p/what-is-database-sharding |
| SD-7 | newsletter | System Design One: How Quora shards MySQL | https://newsletter.systemdesign.one/p/mysql-sharding |
| SD-8 | read | Raft consensus (visual) | https://raft.github.io/ |
| SD-8 | read | Wikipedia: CAP theorem | https://en.wikipedia.org/wiki/CAP_theorem |
| SD-8 | newsletter | AlgoMaster: CAP Theorem Explained | https://blog.algomaster.io/p/cap-theorem-explained |
| SD-8 | newsletter | AlgoMaster: Strong vs eventual consistency | https://blog.algomaster.io/p/strong-vs-eventual-consistency |
| SD-8 | newsletter | Design Gurus: 16 replication concepts | https://designgurus.substack.com/p/16-replication-concepts-every-software |
| SD-9 | newsletter | AlgoMaster: What are message queues | https://blog.algomaster.io/p/message-queues |
| SD-9 | newsletter | System Design One: How Kafka works | https://newsletter.systemdesign.one/p/how-kafka-works |
| SD-9 | newsletter | ByteByteGo: Why is Kafka fast? | https://blog.bytebytego.com/p/why-is-kafka-fast |
| SD-9 | newsletter | ByteByteGo: RabbitMQ vs Kafka vs Pulsar | https://blog.bytebytego.com/p/ep203-rabbitmq-vs-kafka-vs-pulsar |
| SD-9 | read | Hello Interview: Kafka deep dive | https://www.hellointerview.com/learn/system-design/deep-dives/kafka |
| SD-10 | newsletter | AlgoMaster: Rate Limiting Algorithms Explained with Code | https://blog.algomaster.io/p/rate-limiting-algorithms-explained-with-code |
| SD-10 | newsletter | System Design One: 5 rate limiting strategies | https://newsletter.systemdesign.one/p/rate-limiting |
| SD-10 | newsletter | System Design One: How Stripe does rate limiting | https://newsletter.systemdesign.one/p/rate-limiter |
| SD-10 | newsletter | ByteByteGo: High performance rate limiting at Databricks | https://blog.bytebytego.com/p/high-performance-rate-limiting-at |
| SD-11 | read | Paper: The Google File System (2003) | https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf |
| SD-11 | read | Paper: MapReduce (2004) | https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf |
| SD-11 | read | Paper: Bigtable (2006) | https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf |
| SD-11 | read | Paper: Spanner (2012) | https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf |
| SD-11 | read | Paper: Borg (2015) | https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/ |
| SD-11 | newsletter | ByteByteGo: How Google Spanner powers trillions of rows | https://blog.bytebytego.com/p/how-google-spanner-powers-trillions |
| SD-11 | newsletter | ByteByteGo: How Google manages trillions of authorizations with Zanzibar | https://blog.bytebytego.com/p/how-google-manages-trillions-of-authorizations |
| SD-12 | read | Wikipedia: Snowflake ID | https://en.wikipedia.org/wiki/Snowflake_ID |
| SD-12 | read | Wikipedia: universally unique identifier | https://en.wikipedia.org/wiki/Universally_unique_identifier |
| SD-13 | read | Hello Interview: design Bitly | https://www.hellointerview.com/learn/system-design/problem-breakdowns/bitly |
| SD-13 | newsletter | AlgoMaster: Design a URL shortener | https://blog.algomaster.io/p/design-a-url-shortener |
| SD-13 | practice | System Design Primer: Pastebin / Bitly solution | https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/pastebin/README.md |
| SD-14 | read | Paper: Dynamo (Amazon, 2007) | https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf |
| SD-14 | newsletter | System Design Codex: Amazon's Dynamo breakdown | https://newsletter.systemdesigncodex.com/p/amazon-dynamo-breakdown |
| SD-14 | newsletter | ByteByteGo: A deep dive into DynamoDB architecture | https://blog.bytebytego.com/p/a-deep-dive-into-amazon-dynamodb |
| SD-14 | newsletter | ByteByteGo: How Airbnb built a key-value store | https://blog.bytebytego.com/p/how-airbnb-built-a-key-value-store |
| SD-15 | read | Hello Interview: design WhatsApp | https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp |
| SD-15 | newsletter | AlgoMaster: Design WhatsApp | https://blog.algomaster.io/p/design-a-chat-application-like-whatsapp |
| SD-15 | newsletter | Design Gurus: Designing WhatsApp in 45 minutes | https://designgurus.substack.com/p/designing-whatsapp-in-45-minutes |
| SD-15 | newsletter | ByteByteGo: How WhatsApp handles 40 billion messages a day | https://blog.bytebytego.com/p/how-whatsapp-handles-40-billion-messages |
| SD-16 | read | Hello Interview: design Facebook news feed | https://www.hellointerview.com/learn/system-design/problem-breakdowns/fb-news-feed |
| SD-16 | newsletter | ByteByteGo: Design Twitter | https://blog.bytebytego.com/p/interview-question-design-twitter |
| SD-16 | newsletter | ByteByteGo: Twitter architecture 2022 vs 2012 | https://blog.bytebytego.com/p/twitter-architecture-2022-vs-2012 |
| SD-16 | practice | System Design Primer: Twitter timeline solution | https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/twitter/README.md |
| SD-17 | read | Hello Interview: design YouTube | https://www.hellointerview.com/learn/system-design/problem-breakdowns/youtube |
| SD-17 | newsletter | ByteByteGo: Design a system like YouTube | https://blog.bytebytego.com/p/ep130-design-a-system-like-youtube |
| SD-17 | newsletter | System Design One: YouTube with 9 engineers | https://newsletter.systemdesign.one/p/youtube-scalability |
| SD-17 | newsletter | ByteByteGo: How YouTube supports billions of users with MySQL and Vitess | https://blog.bytebytego.com/p/how-youtube-supports-billions-of |
| SD-18 | read | Hello Interview: design top-K / trending | https://www.hellointerview.com/learn/system-design/problem-breakdowns/top-k |
| SD-18 | read | Wikipedia: trie | https://en.wikipedia.org/wiki/Trie |
| SD-18 | newsletter | System Design One: How Google Search works | https://newsletter.systemdesign.one/p/search-engine-architecture |
| SD-19 | read | Hello Interview: design a web crawler | https://www.hellointerview.com/learn/system-design/problem-breakdowns/web-crawler |
| SD-19 | newsletter | ByteByteGo: Avoiding duplicate URLs at Google scale | https://blog.bytebytego.com/p/how-to-avoid-crawling-duplicate-urls |
| SD-19 | practice | System Design Primer: web crawler solution | https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/web_crawler/README.md |
| SD-20 | read | Hello Interview: design Dropbox | https://www.hellointerview.com/learn/system-design/problem-breakdowns/dropbox |
| SD-20 | newsletter | System Design One: How Dropbox scaled | https://newsletter.systemdesign.one/p/dropbox-architecture |
| SD-21 | read | Hello Interview: design Uber | https://www.hellointerview.com/learn/system-design/problem-breakdowns/uber |
| SD-21 | read | Hello Interview: design Yelp | https://www.hellointerview.com/learn/system-design/problem-breakdowns/yelp |
| SD-21 | newsletter | ByteByteGo: How quadtree works | https://blog.bytebytego.com/p/how-quadtree-works |
| SD-21 | newsletter | ByteByteGo: Proximity service | https://blog.bytebytego.com/p/proximity-service |
| SD-21 | newsletter | ByteByteGo: Design Google Maps | https://blog.bytebytego.com/p/design-google-maps |
| SD-22 | newsletter | AlgoMaster: Design a scalable notification service | https://blog.algomaster.io/p/design-a-scalable-notification-service |
| SD-22 | newsletter | ByteByteGo: How Reddit delivers notifications | https://blog.bytebytego.com/p/how-reddit-delivers-notifications |
| SD-22 | newsletter | ByteByteGo: How Slack decides to send a notification | https://blog.bytebytego.com/p/flowchart-of-how-slack-decides-to |
| SD-23 | newsletter | ByteByteGo: Metric monitoring | https://blog.bytebytego.com/p/metric-monitoring |
| SD-23 | newsletter | ByteByteGo: Push vs pull in metrics collecting systems | https://blog.bytebytego.com/p/push-vs-pull-in-metrics-collecting |
| SD-23 | newsletter | Design Gurus: Time series databases explained | https://designgurus.substack.com/p/system-design-deep-dive-time-series |
| SD-23 | newsletter | ByteByteGo: How Datadog built a database for billions of metrics | https://blog.bytebytego.com/p/how-datadog-built-a-custom-database |
| SD-24 | newsletter | ByteByteGo: Payment system | https://blog.bytebytego.com/p/payment-system |
| SD-24 | newsletter | ByteByteGo: How to avoid double payment | https://blog.bytebytego.com/p/how-to-avoid-double-payment |
| SD-24 | newsletter | ByteByteGo: Payment reconciliation | https://blog.bytebytego.com/p/payment-reconciliation |
| SD-24 | newsletter | AlgoMaster: What is idempotency in distributed systems | https://blog.algomaster.io/p/idempotency-in-distributed-systems |
| SD-25 | read | Hello Interview: design Google Docs | https://www.hellointerview.com/learn/system-design/problem-breakdowns/google-docs |
| SD-25 | read | Wikipedia: operational transformation | https://en.wikipedia.org/wiki/Operational_transformation |
| SD-25 | read | Wikipedia: conflict-free replicated data type | https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type |
| SD-25 | newsletter | ByteByteGo: How to design Google Docs | https://blog.bytebytego.com/p/how-to-design-google-docs-episode |
| BH-1 | read | Google: how we hire | https://www.google.com/about/careers/applications/how-we-hire/ |
| BH-1 | read | Google: interview tips | https://www.google.com/about/careers/applications/interview-tips/ |
| BH-1 | newsletter | Engineer's Codex: How Google writes clean, maintainable code | https://read.engineerscodex.com/p/how-google-writes-clean-maintainable |
| BH-2 | read | Tech Interview Handbook: behavioral interview | https://www.techinterviewhandbook.org/behavioral-interview/ |
| BH-2 | read | Tech Interview Handbook: behavioral questions | https://www.techinterviewhandbook.org/behavioral-interview-questions/ |
| BH-3 | read | Tech Interview Handbook: behavioral questions | https://www.techinterviewhandbook.org/behavioral-interview-questions/ |
| BH-3 | newsletter | AlgoMaster: How engineers really get promoted to senior | https://blog.algomaster.io/p/how-engineers-really-get-promoted |
| BH-4 | read | Tech Interview Handbook: behavioral interview | https://www.techinterviewhandbook.org/behavioral-interview/ |
| BH-5 | read | Tech Interview Handbook: self introduction | https://www.techinterviewhandbook.org/self-introduction/ |
| BH-5 | read | Tech Interview Handbook: final questions to ask | https://www.techinterviewhandbook.org/final-questions/ |
| IC-1 | read | Google: how we hire | https://www.google.com/about/careers/applications/how-we-hire/ |
| IC-1 | read | Google: Build your future — resources | https://www.google.com/about/careers/applications/buildyourfuture/resources/ |
| IC-1 | newsletter | AlgoMaster: Resources I used to crack multiple big tech interviews | https://blog.algomaster.io/p/resources-for-big-tech-interviews |
| IC-2 | read | Tech Interview Handbook: coding interview techniques | https://www.techinterviewhandbook.org/coding-interview-techniques/ |
| IC-2 | read | Tech Interview Handbook: coding interview cheatsheet | https://www.techinterviewhandbook.org/coding-interview-cheatsheet/ |
| IC-2 | newsletter | AlgoMaster: 6 coding interview secrets from an ICPC finalist | https://blog.algomaster.io/p/coding-interview-secrets-from-a-icpc-finalist |
| IC-3 | read | Google: interview tips | https://www.google.com/about/careers/applications/interview-tips/ |
| IC-3 | read | Tech Interview Handbook: coding interview best practices | https://www.techinterviewhandbook.org/coding-interview-cheatsheet/ |
| IC-4 | read | Tech Interview Handbook: resume | https://www.techinterviewhandbook.org/resume/ |
| IC-4 | read | Google careers | https://www.google.com/about/careers/applications/ |
| IC-5 | read | Tech Interview Handbook: mock interviews | https://www.techinterviewhandbook.org/mock-interviews/ |
| IC-5 | practice | Pramp (free peer mock interviews) | https://www.pramp.com/ |
| IC-5 | practice | interviewing.io | https://interviewing.io/ |
| IC-6 | read | Tech Interview Handbook: negotiation | https://www.techinterviewhandbook.org/negotiation/ |
| IC-6 | read | Tech Interview Handbook: understanding compensation | https://www.techinterviewhandbook.org/understanding-compensation/ |
| IC-6 | read | levels.fyi: Google | https://www.levels.fyi/companies/google/salaries/software-engineer |
