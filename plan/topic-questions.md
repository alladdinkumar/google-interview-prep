# Topic Questions — ten interview questions per topic

The questions a Google interviewer asks *about* a topic — the conceptual probes that follow a
coding answer ("why is that O(1)?", "what breaks if the input is negative?") and the questions
of the design and behavioural rounds. The planner lists them under each topic, each with a
Gemini button that answers it in a fixed structure: the one-line answer, the explanation, a
diagram or worked example, complexity or trade-offs, and the follow-up you should expect.

**Where these come from.** Written for this plan from the curriculum, the reading, and the
commonly reported shape of Google rounds. They are *not* a verified ranking of the most-asked
questions — no public source can establish one. Edit freely: replace a question you find weak,
add your own from mocks, keep ten per topic so the page stays scannable.

| # | Question |
|---|----------|
| AL-1 | What is the formal definition of Big O, and how do you prove f(n) = O(g(n))? |
| AL-1 | What is the difference between Big O, Big Omega and Big Theta? |
| AL-1 | What do best, average and worst case mean, with quicksort as the example? |
| AL-1 | Rank these by growth: log n, sqrt n, n, n log n, n^2, 2^n, n!. |
| AL-1 | Is O(2n) different from O(n)? Why are constants dropped? |
| AL-1 | What is little o notation, and how does it differ from Big O? |
| AL-1 | Why is log base irrelevant inside Big O? |
| AL-1 | What is the complexity of an algorithm that halves n each step, and one that halves and loops over n each step? |
| AL-1 | Can an algorithm be O(n^2) and Omega(n) at the same time? Explain. |
| AL-1 | How do input size and input value differ when stating complexity (pseudo-polynomial)? |
| AL-2 | How is a dynamic array implemented, and what happens when it is full? |
| AL-2 | Why does doubling capacity give O(1) amortized append, but growing by a constant does not? |
| AL-2 | What is cache locality, and why is an array faster to iterate than a linked list? |
| AL-2 | What is the cost of inserting at the front of an array? |
| AL-2 | When does std::vector shrink, and how do you force it to release memory? |
| AL-2 | What is the difference between size and capacity? |
| AL-2 | How are 2D arrays laid out in memory in C++, and why does loop order matter? |
| AL-2 | What happens to pointers and references into a vector after it reallocates? |
| AL-2 | What growth factor do real implementations use, and why not always 2? |
| AL-2 | How would you implement a dynamic array that supports O(1) amortized pop from both ends? |
| AL-3 | How does a hash table achieve O(1) average lookup? |
| AL-3 | What is a collision, and how do separate chaining and open addressing handle it? |
| AL-3 | What is the load factor, and when should a hash table resize? |
| AL-3 | What are linear probing, quadratic probing and double hashing? |
| AL-3 | Why is deletion tricky with open addressing, and what are tombstones? |
| AL-3 | What makes a good hash function? |
| AL-3 | What is the worst-case lookup time of a hash table, and how can an attacker trigger it? |
| AL-3 | How does std::unordered_map handle collisions? |
| AL-3 | What is consistent hashing, and how is it different from ordinary hashing? |
| AL-3 | What is the amortized cost of rehashing? |
| AL-4 | What is a recurrence relation, and how do you write one for merge sort? |
| AL-4 | State the master theorem and its three cases. |
| AL-4 | Solve T(n) = 2T(n/2) + n, T(n) = T(n/2) + 1, and T(n) = 2T(n/2) + 1. |
| AL-4 | When does the master theorem not apply? |
| AL-4 | How does the recursion tree method work? |
| AL-4 | What is the recurrence for binary search, and its solution? |
| AL-4 | Solve T(n) = T(n-1) + n and T(n) = 2T(n-1) + 1. |
| AL-4 | What is the recurrence for Strassen's algorithm, and why is it faster? |
| AL-4 | How do you use substitution to prove a guessed bound? |
| AL-4 | What is the recurrence for naive recursive Fibonacci, and why is it exponential? |
| AL-5 | What loop invariant makes binary search correct? |
| AL-5 | What is the classic overflow bug in binary search, and how do you avoid it? |
| AL-5 | How do you write lower_bound so it works on an empty array? |
| AL-5 | What is ternary search, and what property must the function have? |
| AL-5 | What is exponential search, and when is it useful? |
| AL-5 | Can binary search work on a linked list? At what cost? |
| AL-5 | What is interpolation search, and when does it beat binary search? |
| AL-5 | How do you binary search on real numbers, and when do you stop? |
| AL-5 | Why is binary search O(log n), with the argument? |
| AL-5 | How do you binary search over the answer space rather than an array? |
| AL-6 | How are strings stored in C++, and what is small string optimisation? |
| AL-6 | What is the difference between ASCII, Unicode, UTF-8 and UTF-16? |
| AL-6 | Why is string concatenation in a loop quadratic in some languages? |
| AL-6 | What does string immutability mean in Java or Python, and what does it cost? |
| AL-6 | How do you reverse a UTF-8 string correctly? |
| AL-6 | What is the complexity of substr and comparison in C++? |
| AL-6 | What is a string view, and when is it dangerous? |
| AL-6 | How do you count characters when the input may contain multibyte characters? |
| AL-6 | How is a string hashed for use in a hash map? |
| AL-6 | How would you implement a string builder? |
| AL-7 | What operations define a stack and a queue, and what are their complexities? |
| AL-7 | What are the pros and cons of array-based and linked-list-based stacks? |
| AL-7 | How does a circular buffer work, and how do you tell full from empty? |
| AL-7 | What is the call stack, and what causes a stack overflow? |
| AL-7 | How does recursion use the call stack, and how can you replace it with an explicit stack? |
| AL-7 | What is a priority queue, and how is it different from a queue? |
| AL-7 | How would you implement a stack with a getMin in O(1)? |
| AL-7 | What is a deque, and how is std::deque implemented? |
| AL-7 | How are stacks used in expression parsing and undo features? |
| AL-7 | How are queues used in BFS and in scheduling? |
| AL-8 | Compare singly, doubly and circular linked lists. |
| AL-8 | What is a sentinel node, and why does it simplify code? |
| AL-8 | What is a skip list, and what is its expected search complexity? |
| AL-8 | Why are linked lists bad for cache performance? |
| AL-8 | How would you implement an XOR linked list, and why is it rarely used? |
| AL-8 | When is a linked list better than an array? |
| AL-8 | How does an LRU cache use a doubly linked list? |
| AL-8 | How does std::list differ from std::forward_list? |
| AL-8 | How do you delete a node given only a pointer to it? |
| AL-8 | How do skip lists compare with balanced trees, and where are they used in practice? |
| AL-9 | Compare bubble, selection, insertion, merge, quick and heap sort on time, space and stability. |
| AL-9 | Why is insertion sort fast for nearly sorted data? |
| AL-9 | Why is quicksort usually faster than merge sort in practice despite its worse worst case? |
| AL-9 | What is introsort, and why does std::sort use it? |
| AL-9 | What makes a sort in-place, and which of these are in-place? |
| AL-9 | Why is merge sort preferred for linked lists and external sorting? |
| AL-9 | How does the choice of pivot affect quicksort? |
| AL-9 | What is three-way partitioning, and when does it help? |
| AL-9 | How is heap sort done in place? |
| AL-9 | What is Timsort, and why does Python use it? |
| AL-10 | Why can no comparison sort beat Omega(n log n) in the worst case? |
| AL-10 | How does counting sort work, and what are its limits? |
| AL-10 | How does radix sort work, and why must the inner sort be stable? |
| AL-10 | How does bucket sort work, and what input makes it degrade? |
| AL-10 | When is radix sort faster than quicksort? |
| AL-10 | What is the decision tree model of sorting? |
| AL-10 | How would you sort a million 32-bit integers fastest? |
| AL-10 | How do you sort strings with radix sort? |
| AL-10 | What is the lower bound for finding the minimum element, and why? |
| AL-10 | How do you sort n numbers in the range 0 to n^2 in O(n)? |
| AL-11 | What is the difference between full, complete and perfect binary trees? |
| AL-11 | What is the maximum number of nodes in a binary tree of height h? |
| AL-11 | What is the minimum height of a binary tree with n nodes? |
| AL-11 | How are trees represented in memory, including the array representation? |
| AL-11 | Which traversal orders can uniquely reconstruct a binary tree? |
| AL-11 | How many structurally different binary trees have n nodes? |
| AL-11 | What is the relationship between leaves and internal nodes in a full binary tree? |
| AL-11 | What is an Euler tour of a tree, and what is it used for? |
| AL-11 | How do you represent an n-ary tree? |
| AL-11 | What is the difference between depth and height of a node? |
| AL-12 | Why do binary search trees need balancing? |
| AL-12 | How do AVL rotations work, and when do you need a double rotation? |
| AL-12 | What are the properties of a red-black tree? |
| AL-12 | Compare AVL and red-black trees on lookup and update performance. |
| AL-12 | What data structure backs std::map and std::set, and what does it guarantee? |
| AL-12 | What is the height of an AVL tree with n nodes? |
| AL-12 | What is a treap, and how does randomness keep it balanced? |
| AL-12 | What is a splay tree, and what is its amortized cost? |
| AL-12 | How would you augment a balanced BST to answer order-statistic queries? |
| AL-12 | When would you choose a hash map over a balanced BST, and vice versa? |
| AL-13 | What is a B-tree, and why is it suited to disks? |
| AL-13 | What is the difference between a B-tree and a B+ tree? |
| AL-13 | Why do databases use B+ trees for indexes? |
| AL-13 | What is the fanout of a B-tree, and how does it affect height? |
| AL-13 | How does a B-tree split a full node? |
| AL-13 | How do range queries work on a B+ tree? |
| AL-13 | What is an LSM tree, and how does it compare with a B-tree? |
| AL-13 | What is a clustered versus a non-clustered index? |
| AL-13 | Why are B-trees rarely used for in-memory maps? |
| AL-13 | How many disk reads does a lookup take in a B+ tree with a billion keys? |
| AL-14 | How is a binary heap stored in an array, and how do you find parent and children? |
| AL-14 | How do sift up and sift down work? |
| AL-14 | Why is build-heap O(n)? |
| AL-14 | How does heap sort work, and is it stable? |
| AL-14 | How do you implement decrease-key in a heap? |
| AL-14 | What is a d-ary heap, and when is it better? |
| AL-14 | What are the complexities of heap operations? |
| AL-14 | How does std::priority_queue relate to make_heap and push_heap? |
| AL-14 | How would you merge two heaps, and what structure makes it efficient? |
| AL-14 | Why is a heap not suitable for searching an arbitrary element? |
| AL-15 | What is a state space tree? |
| AL-15 | How do you estimate the complexity of a backtracking algorithm? |
| AL-15 | What is the difference between backtracking and brute force? |
| AL-15 | What is branch and bound? |
| AL-15 | How does pruning change the complexity in practice but not in the worst case? |
| AL-15 | When should backtracking be replaced by dynamic programming? |
| AL-15 | What is constraint propagation, with sudoku as the example? |
| AL-15 | Why is the number of permutations n! and subsets 2^n? |
| AL-15 | How do you avoid duplicate results in backtracking? |
| AL-15 | What is iterative deepening, and when is it useful? |
| AL-16 | What are the adjacency matrix and adjacency list representations, and their trade-offs? |
| AL-16 | What is the handshake lemma? |
| AL-16 | What is the difference between a directed and an undirected graph, and a weighted and an unweighted one? |
| AL-16 | What is a sparse graph versus a dense graph, and how does it affect algorithm choice? |
| AL-16 | How many edges can a simple graph with n vertices have? |
| AL-16 | What is a connected component, and a strongly connected component? |
| AL-16 | What is an edge list, and when is it the best representation? |
| AL-16 | How do you represent an implicit graph such as a grid or a puzzle? |
| AL-16 | What is a multigraph? |
| AL-16 | What is a bipartite graph, and how is it characterised? |
| AL-17 | What are tree, back, forward and cross edges in DFS? |
| AL-17 | What do discovery and finish times tell you in DFS? |
| AL-17 | Why does BFS compute shortest paths in unweighted graphs? |
| AL-17 | What is the complexity of DFS and BFS with an adjacency list and with a matrix? |
| AL-17 | How does DFS detect a cycle in directed and undirected graphs? |
| AL-17 | What is the white-grey-black colouring in DFS? |
| AL-17 | What is bidirectional BFS, and when does it help? |
| AL-17 | How much memory does BFS use compared with DFS? |
| AL-17 | What is iterative deepening DFS? |
| AL-17 | What is the parenthesis theorem in DFS? |
| AL-18 | What is a directed acyclic graph? |
| AL-18 | Why does every DAG have a topological order? |
| AL-18 | How do you prove that a graph with a topological order has no cycle? |
| AL-18 | How do you find the longest path in a DAG? |
| AL-18 | What is a strongly connected component? |
| AL-18 | Why is the condensation of any graph a DAG? |
| AL-18 | How are DAGs used in build systems and task schedulers? |
| AL-18 | How do you count the number of paths in a DAG? |
| AL-18 | What is transitive reduction? |
| AL-18 | How do you find shortest paths in a DAG in linear time? |
| AL-19 | What operations does a disjoint set support? |
| AL-19 | What does path compression do? |
| AL-19 | What is union by rank or by size? |
| AL-19 | What is the inverse Ackermann function, and why is it effectively constant? |
| AL-19 | What is the complexity of union-find without optimisations? |
| AL-19 | How is union-find used in Kruskal's algorithm? |
| AL-19 | How do you track the size of each set? |
| AL-19 | How would you support rollback in union-find? |
| AL-19 | How is union-find used for offline dynamic connectivity? |
| AL-19 | What is weighted union-find, and where is it used? |
| AL-20 | What is edge relaxation? |
| AL-20 | Why is Dijkstra's algorithm correct for non-negative weights? |
| AL-20 | Why does Dijkstra fail with negative edges? |
| AL-20 | How does Bellman-Ford detect a negative cycle? |
| AL-20 | What is the complexity of Dijkstra with a binary heap and with a Fibonacci heap? |
| AL-20 | How does Floyd-Warshall work, and what is its complexity? |
| AL-20 | What is A* search, and what is an admissible heuristic? |
| AL-20 | What is Johnson's algorithm? |
| AL-20 | How do you reconstruct the shortest path, not just its length? |
| AL-20 | What is the shortest path faster algorithm (SPFA)? |
| AL-21 | What is the cut property of minimum spanning trees? |
| AL-21 | What is the cycle property? |
| AL-21 | Why do Kruskal and Prim both produce an MST? |
| AL-21 | What is the complexity of Kruskal and of Prim? |
| AL-21 | When is the MST unique? |
| AL-21 | What is Boruvka's algorithm? |
| AL-21 | How do you find the second-best MST? |
| AL-21 | Can an MST contain the heaviest edge of the graph? |
| AL-21 | What is the difference between an MST and a Steiner tree? |
| AL-21 | How does an MST relate to the shortest path tree? |
| AL-22 | What is the greedy choice property? |
| AL-22 | What is the exchange argument, and how do you use it to prove correctness? |
| AL-22 | Why does picking the earliest finishing activity give the optimal schedule? |
| AL-22 | How does Huffman coding build an optimal prefix code? |
| AL-22 | Why does greedy fail for 0/1 knapsack but work for fractional knapsack? |
| AL-22 | What is a matroid, intuitively? |
| AL-22 | Why does greedy coin change fail for some coin systems? |
| AL-22 | What is the difference between greedy and dynamic programming? |
| AL-22 | How do you prove a greedy algorithm wrong with a counterexample? |
| AL-22 | What is interval partitioning, and why is greedy optimal? |
| AL-23 | What is the space complexity of a trie, and how can it be reduced? |
| AL-23 | What is a radix tree (compressed trie)? |
| AL-23 | What is a suffix array, and how is it built? |
| AL-23 | What is a suffix tree, and what problems does it solve? |
| AL-23 | What is the LCP array, and how does it pair with the suffix array? |
| AL-23 | How do you find the longest repeated substring with a suffix array? |
| AL-23 | What is Aho-Corasick, and how does it extend a trie? |
| AL-23 | How do you count distinct substrings of a string? |
| AL-23 | When would you use a trie instead of a hash map for strings? |
| AL-23 | What is a ternary search tree? |
| AL-24 | What is amortized analysis? |
| AL-24 | What is the aggregate method? |
| AL-24 | What is the accounting method? |
| AL-24 | What is the potential method? |
| AL-24 | Why is dynamic array append O(1) amortized? |
| AL-24 | What is the amortized cost of a queue built from two stacks? |
| AL-24 | What is the amortized cost of union-find operations? |
| AL-24 | How is amortized cost different from average-case cost? |
| AL-24 | What is the amortized cost of incrementing a binary counter? |
| AL-24 | When is amortized complexity not good enough, such as for real-time systems? |
| AL-25 | What are optimal substructure and overlapping subproblems? |
| AL-25 | How do you define a DP state? |
| AL-25 | What is the difference between top-down and bottom-up DP? |
| AL-25 | How do you find the order in which to fill a DP table? |
| AL-25 | How do you reduce the space of a DP? |
| AL-25 | How do you reconstruct the solution from a DP table? |
| AL-25 | What is the complexity of a DP in terms of states and transitions? |
| AL-25 | What problems look like DP but need greedy or graph algorithms instead? |
| AL-25 | What is the relationship between DP and shortest paths in a DAG? |
| AL-25 | What is a DP optimisation such as convex hull trick or divide and conquer optimisation? |
| AL-26 | Why is 0/1 knapsack pseudo-polynomial and not polynomial? |
| AL-26 | What is the LCS recurrence? |
| AL-26 | What is the edit distance recurrence, and what are the three operations? |
| AL-26 | What is the matrix chain multiplication recurrence? |
| AL-26 | What is the LIS recurrence, and how does the O(n log n) version work? |
| AL-26 | What is the coin change recurrence? |
| AL-26 | What is the rod cutting problem? |
| AL-26 | What is the subset sum problem, and its complexity? |
| AL-26 | What is the longest palindromic subsequence recurrence? |
| AL-26 | How is edit distance used in real systems like spell checkers and diff? |
| AL-27 | What is two's complement, and why is it used? |
| AL-27 | What happens on signed integer overflow in C++? |
| AL-27 | What is the difference between logical and arithmetic right shift? |
| AL-27 | How do you get, set, clear and toggle the ith bit? |
| AL-27 | What does x & -x return? |
| AL-27 | How do you detect overflow when adding two integers? |
| AL-27 | What is the range of a 32-bit signed and unsigned integer? |
| AL-27 | How is a negative number stored in memory? |
| AL-27 | What is endianness? |
| AL-27 | What does __builtin_popcount do, and what is its cost? |
| AL-28 | How does the Euclidean algorithm compute GCD, and what is its complexity? |
| AL-28 | What is the extended Euclidean algorithm? |
| AL-28 | What is a modular inverse, and when does it exist? |
| AL-28 | How do you compute a modular inverse with Fermat's little theorem? |
| AL-28 | How does the sieve of Eratosthenes work, and what is its complexity? |
| AL-28 | How do you factorise a number efficiently? |
| AL-28 | How does fast exponentiation work? |
| AL-28 | How do you compute nCr mod p efficiently? |
| AL-28 | What is the LCM of two numbers, and how do you avoid overflow computing it? |
| AL-28 | What is the Chinese remainder theorem? |
| AL-29 | What is the difference between permutations and combinations? |
| AL-29 | What is the pigeonhole principle, with an interview example? |
| AL-29 | What is inclusion-exclusion? |
| AL-29 | What is expected value, and what is linearity of expectation? |
| AL-29 | What is the probability of at least two people sharing a birthday among 23? |
| AL-29 | How do you count paths in a grid combinatorially? |
| AL-29 | What are Catalan numbers, and where do they appear? |
| AL-29 | What is conditional probability and Bayes' theorem? |
| AL-29 | How many expected coin flips until two heads in a row? |
| AL-29 | What is stars and bars? |
| AL-30 | What is a randomized algorithm, and what are Las Vegas and Monte Carlo algorithms? |
| AL-30 | Why is randomized quicksort O(n log n) expected? |
| AL-30 | How does the Fisher-Yates shuffle work, and why is it uniform? |
| AL-30 | How does reservoir sampling pick k items from a stream uniformly? |
| AL-30 | What is the expected complexity of quickselect? |
| AL-30 | How would you generate a random number from 1 to 7 using a random 1 to 5? |
| AL-30 | What is a random skip list level, and why does it keep the list balanced? |
| AL-30 | How do you pick a random element from a linked list of unknown length? |
| AL-30 | What is the Miller-Rabin primality test? |
| AL-30 | What is universal hashing? |
| AL-31 | What is a sparse table, and why does it give O(1) range minimum queries? |
| AL-31 | Why can a sparse table not support updates efficiently? |
| AL-31 | What is square root decomposition? |
| AL-31 | What is Mo's algorithm? |
| AL-31 | How does a segment tree compare with a Fenwick tree? |
| AL-31 | What is the complexity of building and querying each range query structure? |
| AL-31 | What operations can a segment tree support, and what must be true of the operation? |
| AL-31 | What is a persistent segment tree? |
| AL-31 | How do you answer range queries offline? |
| AL-31 | What is the lowest common ancestor reduction to range minimum query? |
| AL-32 | What is the naive string matching complexity, and its worst case? |
| AL-32 | How does the KMP failure function avoid re-checking characters? |
| AL-32 | How does Rabin-Karp use hashing, and what is its expected complexity? |
| AL-32 | What is the Z-function, and how does it compare with KMP? |
| AL-32 | What is the Boyer-Moore algorithm? |
| AL-32 | How do you handle hash collisions in Rabin-Karp? |
| AL-32 | What is double hashing for strings? |
| AL-32 | How do you find all occurrences of multiple patterns at once? |
| AL-32 | How do you find the longest palindromic substring in linear time (Manacher)? |
| AL-32 | Where is string matching used in real systems? |
| AL-33 | What is a flow network? |
| AL-33 | What is the max-flow min-cut theorem? |
| AL-33 | How does Ford-Fulkerson work, and when might it not terminate? |
| AL-33 | How does Edmonds-Karp improve Ford-Fulkerson? |
| AL-33 | How is bipartite matching reduced to max flow? |
| AL-33 | What is an augmenting path? |
| AL-33 | What is a residual graph? |
| AL-33 | What is Dinic's algorithm? |
| AL-33 | What real problems are modelled as flow? |
| AL-33 | What is the Hungarian algorithm? |
| AL-34 | How does the cross product tell you the orientation of three points? |
| AL-34 | How do you check whether two line segments intersect? |
| AL-34 | How does Graham scan compute the convex hull? |
| AL-34 | How does the monotone chain algorithm work? |
| AL-34 | How do you compute the area of a polygon? |
| AL-34 | How do you check whether a point is inside a polygon? |
| AL-34 | How do you find the closest pair of points in O(n log n)? |
| AL-34 | How do you avoid floating-point errors in geometry code? |
| AL-34 | How do you check whether four points form a square? |
| AL-34 | How do you find the maximum points on a line without floating point? |
| AL-35 | What are P and NP? |
| AL-35 | What does NP-complete mean, and what does NP-hard mean? |
| AL-35 | What is a polynomial-time reduction? |
| AL-35 | Name some NP-complete problems. |
| AL-35 | How would you respond in an interview if a problem is NP-hard? |
| AL-35 | What is an approximation algorithm, with an example? |
| AL-35 | What is the travelling salesman problem, and how is it attacked in practice? |
| AL-35 | Is knapsack NP-complete if it has a pseudo-polynomial algorithm? |
| AL-35 | What is the difference between decision and optimisation problems? |
| AL-35 | What happens if P equals NP? |
| AL-36 | How does a Bloom filter work, and what errors can it make? |
| AL-36 | How do you choose the size and number of hash functions for a Bloom filter? |
| AL-36 | What is a count-min sketch, and what does it estimate? |
| AL-36 | What is HyperLogLog, and how does it estimate cardinality? |
| AL-36 | Where does Google use probabilistic structures (Bigtable Bloom filters)? |
| AL-36 | Can you delete from a Bloom filter? |
| AL-36 | What is a counting Bloom filter? |
| AL-36 | How would you find the top-k frequent items in a massive stream? |
| AL-36 | What is MinHash, and what is it used for? |
| AL-36 | What is the trade-off between memory and accuracy in these structures? |
| AL-37 | What is the memory hierarchy, and what are typical latencies? |
| AL-37 | What is a cache line, and why does it matter for algorithm speed? |
| AL-37 | What is external merge sort? |
| AL-37 | How do you sort 1 TB of data with 8 GB of RAM? |
| AL-37 | What is the I/O model of computation? |
| AL-37 | What is a cache-oblivious algorithm? |
| AL-37 | Why is iterating a 2D array row by row faster than column by column? |
| AL-37 | What is false sharing? |
| AL-37 | How do you find duplicates in a file too large for memory? |
| AL-37 | How do you count word frequencies across many machines? |
| AL-38 | What is a race condition? |
| AL-38 | What is a mutex, and what is a spinlock? |
| AL-38 | What is a deadlock, and what are the four conditions for one? |
| AL-38 | What is a lock-free data structure? |
| AL-38 | What is compare-and-swap, and what is the ABA problem? |
| AL-38 | How does a concurrent hash map reduce lock contention? |
| AL-38 | What is a readers-writer lock? |
| AL-38 | What is the difference between a condition variable and a semaphore? |
| AL-38 | What is memory ordering in C++ atomics? |
| AL-38 | How would you implement a thread-safe queue? |
| BH-1 | What does Googleyness mean? |
| BH-1 | Tell me about a time you had to work with incomplete information. |
| BH-1 | Tell me about a time you helped a teammate succeed. |
| BH-1 | Tell me about a time you challenged the status quo. |
| BH-1 | Tell me about a time you did the right thing when it was hard. |
| BH-1 | Tell me about a time you had to learn something quickly. |
| BH-1 | How do you handle ambiguity? |
| BH-1 | Tell me about a time you put the user first. |
| BH-1 | Tell me about a time you received critical feedback. |
| BH-1 | What does Google look for in the leadership part of the interview? |
| BH-2 | Tell me about your most impactful project. |
| BH-2 | Tell me about the hardest technical problem you solved. |
| BH-2 | Tell me about a time you improved a process. |
| BH-2 | Tell me about a time you mentored someone. |
| BH-2 | Tell me about a time you worked across teams. |
| BH-2 | Tell me about a time you worked on a project with a tight deadline. |
| BH-2 | Tell me about a time you made a technical decision with trade-offs. |
| BH-2 | Tell me about a time you went beyond your role. |
| BH-2 | Tell me about a time you learned a new technology for a project. |
| BH-2 | Tell me about a long-running project you owned. |
| BH-3 | Tell me about a time you disagreed with your manager. |
| BH-3 | Tell me about a time you had a conflict with a teammate. |
| BH-3 | Tell me about a time you influenced a decision without authority. |
| BH-3 | Tell me about a time you had to say no. |
| BH-3 | Tell me about a time you resolved a conflict between others. |
| BH-3 | Tell me about a time you persuaded someone with data. |
| BH-3 | Tell me about a time you disagreed and committed. |
| BH-3 | Tell me about a time you led a team. |
| BH-3 | Tell me about a time you dealt with a difficult stakeholder. |
| BH-3 | Tell me about a time you changed your mind. |
| BH-4 | Tell me about a time you failed. |
| BH-4 | Tell me about a mistake you made in production. |
| BH-4 | Tell me about a time a project was cancelled or failed. |
| BH-4 | Tell me about a time you missed a deadline. |
| BH-4 | Tell me about a time requirements were unclear. |
| BH-4 | Tell me about a time you had to make a decision quickly. |
| BH-4 | Tell me about a time you received negative feedback. |
| BH-4 | Tell me about a time you took a risk. |
| BH-4 | What would you do differently in your last project? |
| BH-4 | Tell me about a time you had to prioritise competing tasks. |
| BH-5 | Tell me about yourself. |
| BH-5 | Why Google? |
| BH-5 | Why are you leaving your current job? |
| BH-5 | Walk me through a project on your resume. |
| BH-5 | What are you most proud of? |
| BH-5 | Where do you see yourself in five years? |
| BH-5 | What kind of team do you want to join? |
| BH-5 | What questions do you have for me? |
| BH-5 | What is your biggest weakness? |
| BH-5 | What product at Google would you improve, and how? |
| IC-1 | What are the stages of the Google hiring process? |
| IC-1 | What happens in hiring committee? |
| IC-1 | What is team matching? |
| IC-1 | What is the difference between L3, L4 and L5 expectations? |
| IC-1 | How are coding interviews scored at Google? |
| IC-1 | How long does the process usually take? |
| IC-1 | What happens if you fail an interview round? |
| IC-1 | How long must you wait to reapply? |
| IC-1 | How does a phone screen differ from an onsite round? |
| IC-1 | What does Google look for in role-related knowledge? |
| IC-2 | What clarifying questions should you ask before coding? |
| IC-2 | How do you think aloud without rambling? |
| IC-2 | When should you state the brute-force solution? |
| IC-2 | How do you handle a hint from the interviewer? |
| IC-2 | What do you do when you are stuck? |
| IC-2 | How do you state complexity, and when? |
| IC-2 | How do you test your code in an interview? |
| IC-2 | How do you handle a follow-up question? |
| IC-2 | How do you recover from a bug you find late? |
| IC-2 | How do you manage time in a 45-minute round? |
| IC-3 | How is coding in a Google Doc different from an IDE? |
| IC-3 | How do you write code without autocomplete? |
| IC-3 | How do you dry-run code by hand? |
| IC-3 | Which edge cases should you always test? |
| IC-3 | How do you structure code with helper functions in an interview? |
| IC-3 | How much should you care about exact syntax? |
| IC-3 | How do you name variables well under pressure? |
| IC-3 | How do you handle input validation in an interview? |
| IC-3 | How do you write test cases on paper? |
| IC-3 | How do you practise coding without an IDE? |
| IC-4 | How do you write resume bullets with impact? |
| IC-4 | How do you get a referral? |
| IC-4 | What should a recruiter screen conversation cover? |
| IC-4 | How do you handle the salary expectations question? |
| IC-4 | How long should your resume be? |
| IC-4 | How do you present projects on your resume? |
| IC-4 | How do you tailor your resume for Google? |
| IC-4 | What should you do after applying? |
| IC-4 | How do you schedule interviews around other commitments? |
| IC-4 | How do you prepare for the recruiter call? |
| IC-5 | How do you run a useful peer mock interview? |
| IC-5 | How do you give and receive feedback in mocks? |
| IC-5 | How do you score yourself on the Google rubric? |
| IC-5 | How many mocks should you do before the onsite? |
| IC-5 | How do you record and review a mock? |
| IC-5 | What should you practise in a mock beyond correctness? |
| IC-5 | How do you simulate interview pressure? |
| IC-5 | How do you use mocks to find weak areas? |
| IC-5 | How do you mock a system design round? |
| IC-5 | How do you mock a behavioural round? |
| IC-6 | How does team matching work after passing hiring committee? |
| IC-6 | What questions should you ask in a team match call? |
| IC-6 | How is Google compensation structured? |
| IC-6 | How do you negotiate an offer? |
| IC-6 | How do competing offers affect negotiation? |
| IC-6 | How is levelling decided? |
| IC-6 | Can you negotiate your level? |
| IC-6 | How do you evaluate an offer? |
| IC-6 | What happens if no team matches? |
| IC-6 | How do you decline or defer an offer politely? |
| DS-1 | What is the time complexity of insert, find and erase in std::map versus std::unordered_map, and when would you choose each? |
| DS-1 | Why can std::vector::push_back be O(1) amortized when it sometimes copies every element? |
| DS-1 | What does iterator invalidation mean, and which operations invalidate iterators for vector, deque, list and map? |
| DS-1 | How do you make std::priority_queue a min-heap, and how do you give it a custom comparator for pairs? |
| DS-1 | What is the difference between lower_bound and upper_bound, and what do they return when the value is absent? |
| DS-1 | When would you use std::deque instead of std::vector? |
| DS-1 | How would you use a custom struct as a key in unordered_map versus in map? |
| DS-1 | What is the difference between emplace_back and push_back? |
| DS-1 | Why is passing a vector by value to a recursive function a performance bug, and how do you fix it? |
| DS-1 | What is the worst-case complexity of unordered_map operations and what causes it? |
| DS-2 | What exactly does O(n log n) mean, and why is it the lower bound for comparison sorting? |
| DS-2 | Given n up to 10^5, which time complexities are acceptable and why? |
| DS-2 | What is the time complexity of generating all subsets of n elements, and all permutations? |
| DS-2 | What is amortized analysis, and give an example where amortized and worst-case costs differ. |
| DS-2 | How do you compute the space complexity of a recursive function, including the call stack? |
| DS-2 | What is the complexity of a nested loop where the inner loop runs i times for each i? |
| DS-2 | Why is O(n + m) different from O(n * m) in graph algorithms, and when does each appear? |
| DS-2 | What is the difference between Big O, Big Omega and Big Theta, with an example of each? |
| DS-2 | How can an O(n^2) algorithm beat an O(n log n) one in practice? |
| DS-2 | What is the time complexity of string concatenation in a loop, and how do you avoid the quadratic trap? |
| DS-3 | How would you find two numbers in an array that add up to a target in O(n)? |
| DS-3 | How do you group anagrams efficiently, and what key would you use for the hash map? |
| DS-3 | How would you find the longest consecutive sequence in an unsorted array in O(n)? |
| DS-3 | How would you detect duplicates within k positions of each other? |
| DS-3 | What trade-offs are there between sorting the input and using a hash set for a membership problem? |
| DS-3 | How would you find the top k most frequent elements, and can you do better than O(n log n)? |
| DS-3 | How would you encode and decode a list of strings into a single string safely? |
| DS-3 | How would you design a data structure with O(1) insert, delete and getRandom? |
| DS-3 | How would you check whether two strings are isomorphic? |
| DS-3 | What happens to your hash-based solution if an adversary controls the input keys? |
| DS-4 | How do you answer many range-sum queries on a static array in O(1) each? |
| DS-4 | How do you count subarrays whose sum equals k, including negative numbers? |
| DS-4 | How does a difference array let you apply many range updates efficiently? |
| DS-4 | How do you compute the sum of any sub-rectangle of a matrix in O(1)? |
| DS-4 | How do you find the longest subarray with an equal number of 0s and 1s? |
| DS-4 | How would you compute product of array except self without division? |
| DS-4 | How do you check whether any subarray has a sum that is a multiple of k? |
| DS-4 | Why does the prefix-sum-plus-hashmap trick need the entry for prefix 0 at the start? |
| DS-4 | How would you handle range-sum queries if the array also receives point updates? |
| DS-4 | How do prefix XORs let you answer range-XOR queries? |
| DS-5 | How do you find all unique triplets that sum to zero, and how do you avoid duplicates? |
| DS-5 | Why does the two-pointer approach work for container with most water? |
| DS-5 | How do you partition an array into three parts in one pass (Dutch national flag)? |
| DS-5 | How do you remove duplicates from a sorted array in place? |
| DS-5 | When does two pointers require the array to be sorted, and when does it not? |
| DS-5 | How do you merge two sorted arrays in place when the first has extra capacity at the end? |
| DS-5 | How would you check whether a string is a palindrome, ignoring non-alphanumeric characters? |
| DS-5 | How do you find the next lexicographic permutation of an array? |
| DS-5 | How would you compute trapping rain water with two pointers in O(1) space? |
| DS-5 | How do you find the pair with sum closest to a target in a sorted array? |
| DS-6 | How do you find the longest substring without repeating characters? |
| DS-6 | What is the difference between a fixed-size and a variable-size sliding window, with an example of each? |
| DS-6 | How do you find the minimum window substring that contains all characters of another string? |
| DS-6 | How does the at-most-K trick turn "exactly K distinct" into two sliding windows? |
| DS-6 | How would you find the longest subarray of 1s if you may flip at most k zeros? |
| DS-6 | How do you check whether one string contains a permutation of another? |
| DS-6 | Why does sliding window fail for minimum subarray sum when the array contains negative numbers? |
| DS-6 | How do you compute the maximum of every window of size k in O(n)? |
| DS-6 | How would you find the longest repeating character replacement with k changes? |
| DS-6 | How do you pick the maximum points from the ends of an array in k picks? |
| DS-7 | How do you find the first and last position of a target in a sorted array? |
| DS-7 | How do you search in a rotated sorted array, and what changes if it has duplicates? |
| DS-7 | What is binary search on the answer, and how do you recognise a problem that needs it? |
| DS-7 | How would you find the minimum capacity needed to ship packages within d days? |
| DS-7 | How do you find a peak element in O(log n)? |
| DS-7 | How do you find the median of two sorted arrays in O(log(min(m, n)))? |
| DS-7 | What loop invariant do you maintain so that binary search never goes into an infinite loop? |
| DS-7 | How do you find the kth smallest element in a sorted matrix? |
| DS-7 | How do you compute the integer square root of a number without library functions? |
| DS-7 | How would you find the duplicate number in an array of n+1 integers without modifying it? |
| DS-8 | How do you check whether a string of brackets is balanced? |
| DS-8 | How do you design a stack that returns its minimum in O(1)? |
| DS-8 | What is a monotonic stack, and how does it find the next greater element for every index? |
| DS-8 | How do you compute daily temperatures (days until a warmer day) in O(n)? |
| DS-8 | How do you evaluate an expression in reverse Polish notation? |
| DS-8 | How would you implement a basic calculator with +, -, *, / and parentheses? |
| DS-8 | How do you simulate asteroid collisions with a stack? |
| DS-8 | How do you remove k digits from a number to make it as small as possible? |
| DS-8 | How do you decode a string like 3[a2[c]]? |
| DS-8 | How do you find the longest valid parentheses substring? |
| DS-9 | How do you implement a queue using two stacks, and what is the amortized cost? |
| DS-9 | How do you implement a circular queue with a fixed-size array? |
| DS-9 | What is a monotonic deque, and how does it solve sliding window maximum? |
| DS-9 | How would you compute a moving average over a data stream? |
| DS-9 | When would you use a deque instead of a queue in a BFS? |
| DS-9 | How do you find the shortest subarray with sum at least k when numbers can be negative? |
| DS-9 | How would you implement a hit counter for the last 5 minutes? |
| DS-9 | What is the difference between a queue, a deque and a priority queue? |
| DS-9 | How do you implement a stack using queues? |
| DS-9 | How would you design a bounded blocking queue for producer and consumer threads? |
| DS-10 | How do you reverse a linked list iteratively and recursively? |
| DS-10 | How do you detect a cycle in a linked list, and find where it starts? |
| DS-10 | How do you find the middle of a linked list in one pass? |
| DS-10 | How do you merge k sorted linked lists efficiently? |
| DS-10 | How do you remove the nth node from the end in one pass? |
| DS-10 | How do you copy a linked list with random pointers in O(1) extra space? |
| DS-10 | How do you reverse nodes in groups of k? |
| DS-10 | How would you check whether a linked list is a palindrome in O(1) space? |
| DS-10 | Why does a dummy head node simplify linked list code? |
| DS-10 | How do you sort a linked list in O(n log n) time? |
| DS-11 | How does merge sort work, and why is it O(n log n)? |
| DS-11 | How does quickselect find the kth largest element, and what is its worst case? |
| DS-11 | How do you count inversions in an array using merge sort? |
| DS-11 | How do you compute x to the power n in O(log n)? |
| DS-11 | What is the recursion tree for merge sort, and how does it give the complexity? |
| DS-11 | How do you count smaller numbers after self for every element? |
| DS-11 | How do you randomize quicksort to avoid the worst case? |
| DS-11 | What is tail recursion, and does C++ guarantee tail-call optimisation? |
| DS-11 | How do you find all ways to add parentheses to an expression? |
| DS-11 | How would you convert a recursive solution into an iterative one? |
| DS-12 | What is a stable sort, and when does stability matter? |
| DS-12 | How do you sort strings to form the largest possible number? |
| DS-12 | When is counting sort better than comparison sorting? |
| DS-12 | How do you sort characters by frequency? |
| DS-12 | How would you sort a nearly sorted array where each element is at most k away from its position? |
| DS-12 | How do you write a comparator for std::sort that is a strict weak ordering, and what goes wrong if it is not? |
| DS-12 | How do you find the maximum gap between successive elements in sorted form in linear time? |
| DS-12 | How would you sort a file too large to fit in memory? |
| DS-12 | How do you compute the h-index of a researcher? |
| DS-12 | How does bucket sort work, and when does it degrade? |
| DS-13 | What are the four tree traversals, and when would you use each? |
| DS-13 | How do you do an inorder traversal iteratively? |
| DS-13 | How do you find the maximum depth and the diameter of a binary tree? |
| DS-13 | How do you print the right side view of a binary tree? |
| DS-13 | How do you check whether a binary tree is height-balanced in O(n)? |
| DS-13 | How do you check whether two trees are identical, or one is a subtree of another? |
| DS-13 | How do you traverse a tree level by level in zigzag order? |
| DS-13 | How do you find the maximum width of a binary tree? |
| DS-13 | How do you do a vertical order traversal? |
| DS-13 | How would you do Morris traversal, and why is it O(1) space? |
| DS-14 | How do you find the lowest common ancestor of two nodes in a binary tree? |
| DS-14 | How do you construct a binary tree from preorder and inorder traversals? |
| DS-14 | How do you serialize and deserialize a binary tree? |
| DS-14 | How do you find the maximum path sum between any two nodes? |
| DS-14 | How do you count paths that sum to a target, starting and ending anywhere? |
| DS-14 | How do you find all nodes at distance k from a target node? |
| DS-14 | How do you flatten a binary tree to a linked list in place? |
| DS-14 | How do you find the path from the root to a given node? |
| DS-14 | How do you get step-by-step directions between two nodes in a tree? |
| DS-14 | How do you delete nodes and return the remaining forest? |
| DS-15 | How do you validate a binary search tree, and what is the common wrong approach? |
| DS-15 | How do you find the kth smallest element in a BST? |
| DS-15 | How do you delete a node from a BST? |
| DS-15 | How do you find the inorder successor of a node in a BST? |
| DS-15 | How do you implement a BST iterator with O(h) memory? |
| DS-15 | How do you build a height-balanced BST from a sorted array? |
| DS-15 | How do you recover a BST in which two nodes were swapped? |
| DS-15 | What is the time complexity of BST operations in the worst case, and how do balanced trees fix it? |
| DS-15 | How do you find the lowest common ancestor in a BST? |
| DS-15 | How would you check whether a value within t of any of the last k values exists? |
| DS-16 | How do you find the kth largest element using a heap, and what is the complexity? |
| DS-16 | How do you find the median of a data stream? |
| DS-16 | How do you merge k sorted lists with a heap? |
| DS-16 | How do you schedule tasks with a cooldown to minimise total time? |
| DS-16 | How do you rearrange a string so no two adjacent characters are equal? |
| DS-16 | How do you find the k closest points to the origin? |
| DS-16 | Why is building a heap O(n) and not O(n log n)? |
| DS-16 | How do you find the smallest range covering at least one element from each of k lists? |
| DS-16 | How would you pick projects to maximise capital (IPO problem)? |
| DS-16 | When would you use a heap versus sorting versus quickselect for top-k? |
| DS-17 | How do you generate all subsets of a set, with and without duplicates? |
| DS-17 | How do you generate all permutations, and handle duplicates? |
| DS-17 | How do you find all combinations that sum to a target when numbers can be reused? |
| DS-17 | What is the backtracking template, and where does the undo step go? |
| DS-17 | How do you generate all valid combinations of n pairs of parentheses? |
| DS-17 | How do you generate letter combinations of a phone number? |
| DS-17 | What is the time complexity of generating all subsets and all permutations? |
| DS-17 | How do you restore all valid IP addresses from a digit string? |
| DS-17 | How do you prune a backtracking search, with an example? |
| DS-17 | How do you generate combinations of size k from 1 to n? |
| DS-18 | How do you solve N-Queens, and how do you check conflicts in O(1)? |
| DS-18 | How do you search for a word in a grid of letters? |
| DS-18 | How would you write a sudoku solver, and how would you speed it up? |
| DS-18 | How do you partition a string into all possible palindromes? |
| DS-18 | How do you partition an array into k subsets of equal sum? |
| DS-18 | How do you find all words from a dictionary on a board (word search II)? |
| DS-18 | How do you remove the minimum number of invalid parentheses? |
| DS-18 | How would you count the number of N-Queens solutions without building boards? |
| DS-18 | How do you find all sentences from word break with a dictionary? |
| DS-18 | How do you insert operators into a digit string to reach a target value? |
| DS-19 | How do you count the number of islands in a grid? |
| DS-19 | What are the trade-offs between DFS and BFS for graph traversal? |
| DS-19 | How do you clone a graph? |
| DS-19 | How do you check whether a graph is bipartite? |
| DS-19 | How do you find cells that can flow to both oceans (Pacific Atlantic)? |
| DS-19 | How do you capture surrounded regions in a board? |
| DS-19 | How do you avoid stack overflow in DFS on a large grid? |
| DS-19 | How do you count connected components in an undirected graph? |
| DS-19 | How do you check whether a graph is a valid tree? |
| DS-19 | How do you find the town judge given trust relationships? |
| DS-20 | Why does BFS find the shortest path in an unweighted graph? |
| DS-20 | What is multi-source BFS, and how does it solve rotting oranges? |
| DS-20 | How do you solve word ladder, and how would you speed it up? |
| DS-20 | What is 0-1 BFS, and when do you use it instead of Dijkstra? |
| DS-20 | How do you find the shortest path in a grid when you may remove up to k obstacles? |
| DS-20 | How do you find the distance to the nearest 0 for every cell? |
| DS-20 | How do you model a puzzle like open the lock as a graph search? |
| DS-20 | How do you find the minimum number of buses to reach a destination? |
| DS-20 | How do you fill each empty room with the distance to its nearest gate? |
| DS-20 | What state do you need in BFS when the problem involves keys and doors? |
| DS-21 | How do you detect whether a set of courses can be finished? |
| DS-21 | Explain Kahn's algorithm and DFS-based topological sort. |
| DS-21 | How do you detect a cycle in a directed graph? |
| DS-21 | How do you derive the order of letters in an alien dictionary? |
| DS-21 | How do you find the minimum height trees of a tree? |
| DS-21 | How do you find eventual safe states in a directed graph? |
| DS-21 | How would you compute the minimum time to finish courses with durations and prerequisites? |
| DS-21 | How can a topological order be used for dynamic programming on a DAG? |
| DS-21 | How do you find the longest increasing path in a matrix? |
| DS-21 | What happens if there are multiple valid topological orders, and how do you get the lexicographically smallest? |
| DS-22 | How does union-find work, and what do path compression and union by rank achieve? |
| DS-22 | How do you find the redundant connection in a graph? |
| DS-22 | How do you merge accounts that share emails? |
| DS-22 | How many operations are needed to connect all computers in a network? |
| DS-22 | How do you check whether equality equations are satisfiable? |
| DS-22 | When would you use union-find instead of DFS for connected components? |
| DS-22 | How do you compute the result of division queries (evaluate division)? |
| DS-22 | How do you find the earliest time when you can swim to the corner (swim in rising water)? |
| DS-22 | Can union-find support deletion? Why or why not? |
| DS-22 | How do you find the smallest string after allowed swaps? |
| DS-23 | How does Dijkstra's algorithm work, and what is its complexity with a binary heap? |
| DS-23 | Why does Dijkstra fail with negative edge weights? |
| DS-23 | How do you find the cheapest flight with at most k stops? |
| DS-23 | When would you use Bellman-Ford instead of Dijkstra? |
| DS-23 | How does Floyd-Warshall work, and when is it the right choice? |
| DS-23 | How do you find the path with minimum effort in a grid? |
| DS-23 | How do you count the number of shortest paths to a destination? |
| DS-23 | How do you find the network delay time for a signal? |
| DS-23 | What is A* search, and how does its heuristic affect correctness? |
| DS-23 | How do you find the path with maximum probability? |
| DS-24 | What is a minimum spanning tree, and when is it unique? |
| DS-24 | How does Kruskal's algorithm work, and what is its complexity? |
| DS-24 | How does Prim's algorithm work, and when is it better than Kruskal? |
| DS-24 | How do you connect all points with minimum total Manhattan distance? |
| DS-24 | How do you find critical and pseudo-critical edges in an MST? |
| DS-24 | Why does the cut property guarantee the greedy choice is safe? |
| DS-24 | How would you find a maximum spanning tree? |
| DS-24 | How would you update an MST if one edge weight decreases? |
| DS-24 | How is MST used in clustering? |
| DS-24 | What is the difference between an MST and a shortest path tree? |
| DS-25 | How do you decide whether you can reach the last index (jump game)? |
| DS-25 | How do you find the minimum number of jumps? |
| DS-25 | How do you find the starting gas station that completes the circuit? |
| DS-25 | How do you prove a greedy algorithm is correct? |
| DS-25 | How do you distribute candies with the minimum total? |
| DS-25 | How do you partition a string into as many parts as possible so each letter appears in one part? |
| DS-25 | How do you find the minimum arrows to burst all balloons? |
| DS-25 | How do you check whether a hand of cards can be grouped into straights? |
| DS-25 | When does a greedy approach fail and dynamic programming is needed? |
| DS-25 | How do you reconstruct a queue by height? |
| DS-26 | How do you merge overlapping intervals? |
| DS-26 | How do you insert an interval into a sorted non-overlapping list? |
| DS-26 | How do you find the minimum number of meeting rooms required? |
| DS-26 | How do you remove the minimum number of intervals to make the rest non-overlapping? |
| DS-26 | How do you find the intersections of two interval lists? |
| DS-26 | What is a sweep line, and how does it solve the skyline problem? |
| DS-26 | How do you find the free time common to all employees? |
| DS-26 | How would you design a calendar that rejects double bookings? |
| DS-26 | How do you answer queries for the smallest interval containing each point? |
| DS-26 | How do you attend the maximum number of events? |
| DS-27 | How do you implement a trie with insert, search and startsWith? |
| DS-27 | What are the time and space complexities of a trie? |
| DS-27 | How do you support wildcard search with '.' in a trie? |
| DS-27 | How do you implement search suggestions as a user types? |
| DS-27 | How does a trie speed up word search II compared with searching each word separately? |
| DS-27 | How do you find the maximum XOR of two numbers using a binary trie? |
| DS-27 | How do you replace words with their shortest root? |
| DS-27 | When would you use a trie instead of a hash set? |
| DS-27 | How would you reduce the memory of a trie? |
| DS-27 | How do you find palindrome pairs in a list of words? |
| DS-28 | How do you recognise that a problem needs dynamic programming? |
| DS-28 | What is the difference between memoization and tabulation? |
| DS-28 | How do you solve house robber, and the circular version? |
| DS-28 | How do you count the ways to decode a digit string? |
| DS-28 | How do you decide whether a string can be segmented into dictionary words? |
| DS-28 | How do you find the maximum product subarray? |
| DS-28 | How do you find the longest palindromic substring? |
| DS-28 | How do you reduce space from O(n) to O(1) in a 1D DP? |
| DS-28 | How do you find the fewest perfect squares that sum to n? |
| DS-28 | How do you define the state and transition for delete and earn? |
| DS-29 | How many unique paths are there in a grid, with and without obstacles? |
| DS-29 | How do you find the minimum path sum in a grid? |
| DS-29 | How do you find the largest square of 1s in a matrix? |
| DS-29 | How do you compute the minimum path in a triangle with O(n) space? |
| DS-29 | How do you solve dungeon game, and why must you fill the table backwards? |
| DS-29 | How do you solve cherry pickup with two robots? |
| DS-29 | How do you reduce a 2D grid DP to a single row of memory? |
| DS-29 | How do you count paths that go out of bounds in at most k moves? |
| DS-29 | How do you find the minimum falling path sum? |
| DS-29 | How do you handle a grid DP when moves can go in all four directions? |
| DS-30 | What is the 0/1 knapsack recurrence, and why is it pseudo-polynomial? |
| DS-30 | How do you check whether an array can be partitioned into two equal-sum subsets? |
| DS-30 | How do you find the fewest coins to make an amount? |
| DS-30 | How do you count the number of ways to make an amount with coins? |
| DS-30 | Why does the loop order differ between 0/1 and unbounded knapsack in the 1D version? |
| DS-30 | How do you assign + and - signs to reach a target sum? |
| DS-30 | How do you minimise the last stone weight after smashing? |
| DS-30 | How do you handle a knapsack with two capacity dimensions (ones and zeroes)? |
| DS-30 | How does combination sum IV differ from coin change II? |
| DS-30 | How would you solve knapsack when the capacity is huge but values are small? |
| DS-31 | How do you compute the longest common subsequence of two strings? |
| DS-31 | How do you compute the edit distance between two strings? |
| DS-31 | How do you find the longest palindromic subsequence? |
| DS-31 | How do you count the distinct subsequences of s that equal t? |
| DS-31 | How do you check whether a string is an interleaving of two others? |
| DS-31 | How do you implement wildcard matching with ? and *? |
| DS-31 | How do you implement regular expression matching with . and *? |
| DS-31 | How do you find the shortest common supersequence? |
| DS-31 | How do you reduce LCS memory to O(min(m, n))? |
| DS-31 | How do you reconstruct the actual LCS string, not just its length? |
| DS-32 | How do you find the longest increasing subsequence in O(n log n)? |
| DS-32 | How does patience sorting relate to LIS? |
| DS-32 | How do you count the number of longest increasing subsequences? |
| DS-32 | How do you solve Russian doll envelopes? |
| DS-32 | How do you find the longest string chain? |
| DS-32 | How do you model stock buy-and-sell problems as a state machine? |
| DS-32 | How do you handle a cooldown or a transaction fee in the stock problems? |
| DS-32 | How do you find the maximum profit with at most k transactions? |
| DS-32 | How do you find the largest divisible subset? |
| DS-32 | How do you schedule jobs to maximise profit without overlaps? |
| DS-33 | What is interval DP, and how do you choose the iteration order? |
| DS-33 | How do you solve matrix chain multiplication? |
| DS-33 | How do you solve burst balloons, and why do you think about the last balloon? |
| DS-33 | How do you find the minimum cuts for palindrome partitioning? |
| DS-33 | How do you solve the stone game, and what does the DP value represent? |
| DS-33 | How do you decide whether player 1 can win (predict the winner)? |
| DS-33 | How do you find the minimum cost to cut a stick? |
| DS-33 | How do you solve the strange printer problem? |
| DS-33 | What is the time complexity of a typical interval DP, and why? |
| DS-33 | How do you find the minimum cost tree from leaf values? |
| DS-34 | How do you solve house robber on a tree? |
| DS-34 | What is rerooting, and how does it compute sum of distances for every node? |
| DS-34 | How do you place the minimum number of cameras to cover a binary tree? |
| DS-34 | What is bitmask DP, and when is n small enough for it? |
| DS-34 | How do you find the shortest path that visits all nodes? |
| DS-34 | How do you form the smallest team that covers all required skills? |
| DS-34 | What is digit DP, and what state does it carry? |
| DS-34 | How do you count numbers up to n with some digit property? |
| DS-34 | How do you count structurally unique BSTs? |
| DS-34 | How do you decide whether the first player can win a choosing game (can I win)? |
| DS-35 | How do you count the set bits in an integer, and in all numbers from 0 to n? |
| DS-35 | How do you find the single number when every other appears twice, and three times? |
| DS-35 | How do you add two integers without using + or -? |
| DS-35 | How do you check whether a number is a power of two? |
| DS-35 | How do you reverse the bits of a 32-bit integer? |
| DS-35 | How do you find the two numbers that appear once when all others appear twice? |
| DS-35 | How do you enumerate all subsets of a bitmask? |
| DS-35 | What does x & (x - 1) do, and where is it useful? |
| DS-35 | How do you compute the bitwise AND of a range of numbers? |
| DS-35 | How do you compute the total Hamming distance of all pairs? |
| DS-36 | How do you compute a^b mod m efficiently? |
| DS-36 | How do you find all primes up to n? |
| DS-36 | How do you rotate an n x n matrix in place? |
| DS-36 | How do you print a matrix in spiral order? |
| DS-36 | How do you set matrix rows and columns to zero in O(1) extra space? |
| DS-36 | How do you multiply two large numbers given as strings? |
| DS-36 | How do you pick an index with probability proportional to its weight? |
| DS-36 | How do you find the maximum number of points on a line? |
| DS-36 | How do you compute the game of life in place? |
| DS-36 | How do you convert a fraction to a recurring decimal string? |
| DS-37 | How does a segment tree answer range queries in O(log n)? |
| DS-37 | How does a Fenwick tree work, and how does it compare with a segment tree? |
| DS-37 | What is lazy propagation, and when do you need it? |
| DS-37 | How do you count the number of range sums within [lower, upper]? |
| DS-37 | How do you count smaller numbers after self with a Fenwick tree? |
| DS-37 | How would you implement a range module that adds, removes and queries ranges? |
| DS-37 | How do you find the maximum number of overlapping bookings (my calendar III)? |
| DS-37 | How do you build a segment tree in O(n)? |
| DS-37 | How would you handle range queries when values are huge (coordinate compression)? |
| DS-37 | When is a sparse table better than a segment tree? |
| DS-38 | How does the KMP prefix function work? |
| DS-38 | How does Rabin-Karp use rolling hashes, and how do you handle collisions? |
| DS-38 | What is the Z-function, and how is it used for pattern matching? |
| DS-38 | How do you find the shortest palindrome by adding characters to the front? |
| DS-38 | How do you find the longest duplicate substring? |
| DS-38 | How do you check whether a string is made of a repeated substring? |
| DS-38 | How do you find all repeated 10-letter DNA sequences? |
| DS-38 | How do you find the longest happy prefix? |
| DS-38 | What is the complexity of naive string matching versus KMP? |
| DS-38 | How would you implement strStr, and what edge cases matter? |
| DS-39 | How do you find bridges in a graph? |
| DS-39 | How do you find articulation points? |
| DS-39 | How does Tarjan's algorithm find strongly connected components? |
| DS-39 | How does Kosaraju's algorithm work? |
| DS-39 | How do you reconstruct an itinerary using all tickets (Eulerian path)? |
| DS-39 | When does an Eulerian path or circuit exist? |
| DS-39 | How do you find the minimum days to disconnect an island? |
| DS-39 | What is a condensation graph, and what is it useful for? |
| DS-39 | How do you find the critical connections in a network? |
| DS-39 | How do you construct a De Bruijn sequence (cracking the safe)? |
| DS-40 | How do you find the largest rectangle in a histogram? |
| DS-40 | How do you find the maximal rectangle of 1s in a binary matrix? |
| DS-40 | How do you compute the sum of subarray minimums? |
| DS-40 | How do you compute trapping rain water with a stack? |
| DS-40 | How do you detect a 132 pattern? |
| DS-40 | How do you count car fleets arriving at a destination? |
| DS-40 | How do you count the visible people in a queue? |
| DS-40 | How do you compute the maximum width ramp? |
| DS-40 | How do you use a monotonic deque for constrained subsequence sum? |
| DS-40 | How do you decide whether to keep an increasing or a decreasing monotonic stack? |
| DS-41 | How do you design an LRU cache with O(1) get and put? |
| DS-41 | How do you design an LFU cache with O(1) operations? |
| DS-41 | How would you make an LRU cache thread-safe, and what does locking cost? |
| DS-41 | How do you design a time-based key-value store? |
| DS-41 | How do you design a snapshot array? |
| DS-41 | How do you flatten a nested list with an iterator? |
| DS-41 | How do you design a hit counter or a logger rate limiter? |
| DS-41 | How do you design a data structure for all O(1) increment, decrement, getMax and getMin? |
| DS-41 | How do you design browser history with back and forward? |
| DS-41 | How do you design Twitter's follow and news feed as a class? |
| LD-1 | What are the four pillars of object-oriented programming? |
| LD-1 | How do virtual functions work in C++, and what is a vtable? |
| LD-1 | What is the difference between an abstract class and an interface in C++? |
| LD-1 | Why must a base class have a virtual destructor? |
| LD-1 | What is the difference between composition and inheritance, and when do you prefer each? |
| LD-1 | What is object slicing? |
| LD-1 | What is the difference between overloading and overriding? |
| LD-1 | What are the rule of three and the rule of five? |
| LD-1 | What is RAII, and why does it matter? |
| LD-1 | What does the override keyword protect against? |
| LD-2 | What does the single responsibility principle say, with an example of a violation? |
| LD-2 | What does the open-closed principle mean in practice? |
| LD-2 | What is the Liskov substitution principle, and what is the square-rectangle problem? |
| LD-2 | What is the interface segregation principle? |
| LD-2 | What is dependency inversion, and how does it relate to dependency injection? |
| LD-2 | How do SOLID principles make code easier to test? |
| LD-2 | Can you over-apply SOLID? Give an example. |
| LD-2 | Which SOLID principle does a large switch on type violate, and how do you fix it? |
| LD-2 | How do you explain SOLID to an interviewer with one design? |
| LD-2 | What are coupling and cohesion? |
| LD-3 | When would you use a factory method versus an abstract factory? |
| LD-3 | What problem does the builder pattern solve? |
| LD-3 | How do you implement a thread-safe singleton in C++? |
| LD-3 | Why is singleton often called an anti-pattern? |
| LD-3 | What is the prototype pattern? |
| LD-3 | How would you create different vehicle objects in a parking lot using a factory? |
| LD-3 | What is the difference between a factory and a constructor? |
| LD-3 | What is a fluent interface? |
| LD-3 | How do you test code that uses a singleton? |
| LD-3 | When is dependency injection better than a factory? |
| LD-4 | What does the adapter pattern do, with a real example? |
| LD-4 | How is the decorator pattern different from inheritance? |
| LD-4 | What is the composite pattern, and where is it used? |
| LD-4 | What is the facade pattern? |
| LD-4 | What kinds of proxy are there, and when do you use each? |
| LD-4 | What is the difference between adapter, decorator and proxy? |
| LD-4 | What is the bridge pattern? |
| LD-4 | What is the flyweight pattern? |
| LD-4 | How would you add logging to an existing class without changing it? |
| LD-4 | How would you model a file system with the composite pattern? |
| LD-5 | What is the strategy pattern, and how does it replace conditionals? |
| LD-5 | How does the observer pattern work, and what are its pitfalls? |
| LD-5 | How would you implement undo and redo with the command pattern? |
| LD-5 | What is the state pattern, and how is it different from strategy? |
| LD-5 | What is the iterator pattern? |
| LD-5 | What is the chain of responsibility pattern? |
| LD-5 | What is the template method pattern? |
| LD-5 | What is the mediator pattern? |
| LD-5 | How would you implement a vending machine with the state pattern? |
| LD-5 | How would you implement an event system with the observer pattern safely across threads? |
| LD-6 | What are the relationships in a UML class diagram? |
| LD-6 | What is the difference between aggregation and composition? |
| LD-6 | What does a sequence diagram show? |
| LD-6 | How do you show inheritance and interface implementation in UML? |
| LD-6 | What is multiplicity? |
| LD-6 | How detailed should a class diagram be in an interview? |
| LD-6 | What is the difference between association and dependency? |
| LD-6 | How do you draw an abstract class? |
| LD-6 | When is a state diagram useful? |
| LD-6 | How do you walk an interviewer through a diagram? |
| LD-7 | What is the difference between a process and a thread? |
| LD-7 | How does std::mutex work, and what is std::lock_guard? |
| LD-7 | How do condition variables work, and what is a spurious wakeup? |
| LD-7 | How do you implement a producer-consumer queue? |
| LD-7 | What is a deadlock, and how do you prevent it? |
| LD-7 | What is std::atomic, and when is it enough? |
| LD-7 | What is a thread pool, and why use one? |
| LD-7 | What is the difference between std::async and std::thread? |
| LD-7 | How do you make a singleton thread-safe? |
| LD-7 | What is a data race versus a race condition? |
| LD-8 | What classes would you define for a parking lot? |
| LD-8 | How do you handle different spot sizes and vehicle types? |
| LD-8 | How do you calculate parking fees flexibly? |
| LD-8 | How would you make parking and unparking thread-safe? |
| LD-8 | How do you find the nearest free spot efficiently? |
| LD-8 | How would you support multiple floors and entrances? |
| LD-8 | Which design patterns fit a parking lot? |
| LD-8 | How would you add electric vehicle charging spots? |
| LD-8 | How would you handle a lost ticket? |
| LD-8 | How do you test your parking lot design? |
| LD-9 | What classes would you define for an elevator system? |
| LD-9 | How do you decide which elevator serves a request? |
| LD-9 | What states does an elevator have? |
| LD-9 | What scheduling algorithms can an elevator use (SCAN, LOOK)? |
| LD-9 | How do you handle requests from inside and outside the elevator? |
| LD-9 | How would you simulate the system over time? |
| LD-9 | How do you handle emergencies and maintenance mode? |
| LD-9 | How would you make the controller thread-safe? |
| LD-9 | How would you extend the design for express elevators? |
| LD-9 | How do you minimise average wait time? |
| LD-10 | What classes would you define for tic-tac-toe on an n x n board? |
| LD-10 | How do you check for a winner in O(1) per move? |
| LD-10 | How would you design snake and ladder? |
| LD-10 | How do you make the game support multiple players? |
| LD-10 | How would you add an AI player? |
| LD-10 | How do you separate game rules from the board representation? |
| LD-10 | Which patterns fit a board game design? |
| LD-10 | How would you support undo? |
| LD-10 | How would you design chess moves for different pieces? |
| LD-10 | How do you test game logic? |
| LD-11 | What classes would you define for Splitwise? |
| LD-11 | How do you support equal, exact and percentage splits? |
| LD-11 | How do you compute who owes whom? |
| LD-11 | How do you simplify debts to minimise the number of transactions? |
| LD-11 | How do you handle rounding in splits? |
| LD-11 | How would you support groups? |
| LD-11 | How would you notify users of new expenses? |
| LD-11 | How do you store balances efficiently? |
| LD-11 | How would you handle multiple currencies? |
| LD-11 | How would you make it concurrent-safe? |
| LD-12 | What classes would you define for a movie ticket booking system? |
| LD-12 | How do you prevent two users from booking the same seat? |
| LD-12 | How do seat holds with timeouts work? |
| LD-12 | What is the difference between optimistic and pessimistic locking here? |
| LD-12 | How do you model shows, screens and seats? |
| LD-12 | How do you handle payment failure after a seat hold? |
| LD-12 | How would you support different seat pricing? |
| LD-12 | How do you search for shows? |
| LD-12 | How do you notify users? |
| LD-12 | How would you scale this design to many cinemas? |
| LD-13 | What rate limiting algorithms exist, and what are their trade-offs? |
| LD-13 | How do you implement a token bucket in C++? |
| LD-13 | How do you make a rate limiter thread-safe? |
| LD-13 | How do you rate limit per user? |
| LD-13 | What is the difference between fixed window and sliding window? |
| LD-13 | How do you design the rate limiter interface for extensibility? |
| LD-13 | How do you test a rate limiter that depends on time? |
| LD-13 | How do you handle bursts? |
| LD-13 | How would you make the limiter distributed? |
| LD-13 | What should the client see when rate limited? |
| LD-14 | How do you design a vending machine with the state pattern? |
| LD-14 | What states does an ATM have? |
| LD-14 | How do you handle cash dispensing with the fewest notes? |
| LD-14 | How do you manage inventory? |
| LD-14 | How do you handle refunds and cancellations? |
| LD-14 | How do you support multiple payment methods? |
| LD-14 | How do you make these designs thread-safe? |
| LD-14 | How would you log transactions? |
| LD-14 | How do you test state transitions? |
| LD-14 | What happens on a power failure mid-transaction? |
| LD-15 | How do you design a logging framework with levels and appenders? |
| LD-15 | How do you make logging thread-safe and fast? |
| LD-15 | How would you design an asynchronous logger? |
| LD-15 | How do you design a pub-sub system in-process? |
| LD-15 | How do you handle slow subscribers? |
| LD-15 | What delivery guarantees can a pub-sub system offer? |
| LD-15 | How do you filter messages by topic? |
| LD-15 | How would you configure logging at runtime? |
| LD-15 | Which patterns fit a logger and a pub-sub system? |
| LD-15 | How do you avoid losing logs on a crash? |
| SD-1 | What steps do you follow in a system design interview? |
| SD-1 | How do you clarify requirements, and what questions do you ask? |
| SD-1 | What are functional and non-functional requirements? |
| SD-1 | How do you choose which parts to deep-dive? |
| SD-1 | How do you handle an interviewer who changes requirements midway? |
| SD-1 | How much time should each step take in 45 minutes? |
| SD-1 | How do you present trade-offs clearly? |
| SD-1 | What mistakes make candidates fail system design? |
| SD-1 | How is a senior design answer different from a junior one? |
| SD-1 | How do you design an API in an interview? |
| SD-2 | How do you estimate QPS from daily active users? |
| SD-2 | How do you estimate storage for five years? |
| SD-2 | What are the latency numbers every engineer should know? |
| SD-2 | How do you estimate bandwidth? |
| SD-2 | How do you estimate the number of servers needed? |
| SD-2 | How do you estimate cache memory needed? |
| SD-2 | What is peak versus average traffic, and what multiplier do you use? |
| SD-2 | How do you round numbers for quick estimation? |
| SD-2 | How many seconds are in a day, and how does it help? |
| SD-2 | How do you estimate the storage for a photo-sharing service? |
| SD-3 | What happens when you type a URL into the browser? |
| SD-3 | How does DNS resolution work? |
| SD-3 | What is the difference between TCP and UDP? |
| SD-3 | What is the difference between HTTP/1.1, HTTP/2 and HTTP/3? |
| SD-3 | When would you choose REST, gRPC or GraphQL? |
| SD-3 | How do WebSockets work, and when would you use them? |
| SD-3 | What is long polling, and what are server-sent events? |
| SD-3 | How does HTTPS work? |
| SD-3 | What is an API gateway? |
| SD-3 | How do you version an API? |
| SD-4 | What does a load balancer do? |
| SD-4 | What is the difference between L4 and L7 load balancing? |
| SD-4 | What load balancing algorithms exist? |
| SD-4 | How do health checks work? |
| SD-4 | What are sticky sessions, and what problems do they cause? |
| SD-4 | How do you avoid the load balancer becoming a single point of failure? |
| SD-4 | What is a reverse proxy? |
| SD-4 | How does consistent hashing help load balancing? |
| SD-4 | What is global server load balancing? |
| SD-4 | How does a load balancer handle a slow backend? |
| SD-5 | What are cache-aside, write-through and write-back? |
| SD-5 | What eviction policies exist? |
| SD-5 | How do you keep a cache consistent with the database? |
| SD-5 | What is a cache stampede, and how do you prevent it? |
| SD-5 | What is a CDN, and when do you use one? |
| SD-5 | What should and should not be cached? |
| SD-5 | How do you choose a TTL? |
| SD-5 | What is the difference between Redis and Memcached? |
| SD-5 | How do you cache in multiple layers? |
| SD-5 | What is a hot key, and how do you handle it in a cache? |
| SD-6 | When do you choose SQL versus NoSQL? |
| SD-6 | How do database indexes work, and what do they cost? |
| SD-6 | What is the difference between B-tree and LSM-tree storage engines? |
| SD-6 | What is replication, and what is replication lag? |
| SD-6 | What are isolation levels? |
| SD-6 | What are ACID and BASE? |
| SD-6 | What is the difference between leader-follower and multi-leader replication? |
| SD-6 | How do you scale reads? |
| SD-6 | How do you scale writes? |
| SD-6 | What types of NoSQL databases exist? |
| SD-7 | What is sharding, and how do you choose a shard key? |
| SD-7 | What is consistent hashing? |
| SD-7 | What are virtual nodes? |
| SD-7 | What is a hot shard, and how do you fix it? |
| SD-7 | How do you rebalance shards without downtime? |
| SD-7 | How do you run a query that spans many shards? |
| SD-7 | What is range-based versus hash-based partitioning? |
| SD-7 | How do you handle joins across shards? |
| SD-7 | What is directory-based sharding? |
| SD-7 | How does Spanner split data? |
| SD-8 | What is the CAP theorem? |
| SD-8 | What is PACELC? |
| SD-8 | What consistency models exist? |
| SD-8 | What is a quorum, and how do R + W > N guarantee consistency? |
| SD-8 | How does Raft elect a leader? |
| SD-8 | How does Raft replicate the log? |
| SD-8 | What is Paxos, at a high level? |
| SD-8 | What is split brain, and how do you prevent it? |
| SD-8 | What is linearizability? |
| SD-8 | How does Google Spanner offer external consistency? |
| SD-9 | Why use a message queue? |
| SD-9 | What is the difference between a queue and a pub-sub topic? |
| SD-9 | How does Kafka work? |
| SD-9 | What are at-most-once, at-least-once and exactly-once delivery? |
| SD-9 | How do you handle poison messages? |
| SD-9 | How do consumer groups and partitions work in Kafka? |
| SD-9 | What is backpressure? |
| SD-9 | How do you preserve message ordering? |
| SD-9 | When would you choose RabbitMQ over Kafka? |
| SD-9 | What is a dead-letter queue? |
| SD-10 | What rate limiting algorithms exist, and what are their trade-offs? |
| SD-10 | How do you build a distributed rate limiter? |
| SD-10 | How do you use Redis for rate limiting? |
| SD-10 | How do you handle race conditions in a distributed rate limiter? |
| SD-10 | Where should rate limiting live in the architecture? |
| SD-10 | How do you rate limit by user, IP or API key? |
| SD-10 | What HTTP response and headers should a rate limiter return? |
| SD-10 | How do you handle clock skew? |
| SD-10 | How do you rate limit across data centres? |
| SD-10 | How does rate limiting differ from load shedding? |
| SD-11 | What problem does the Google File System solve, and what are its key design choices? |
| SD-11 | How does GFS handle a chunkserver failure? |
| SD-11 | What is MapReduce, and how does it handle failures? |
| SD-11 | What is Bigtable's data model? |
| SD-11 | How does Bigtable use SSTables, memtables and Bloom filters? |
| SD-11 | What is Spanner, and what is TrueTime? |
| SD-11 | How does Spanner provide globally consistent transactions? |
| SD-11 | What does Borg do, and how did it influence Kubernetes? |
| SD-11 | What is Chubby, and what is it used for? |
| SD-11 | How would you reference Google's systems in an interview without name-dropping? |
| SD-12 | How do you generate unique IDs in a distributed system? |
| SD-12 | How does Twitter's Snowflake ID work? |
| SD-12 | What are the pros and cons of UUIDs as database keys? |
| SD-12 | How do you handle clock going backwards in Snowflake? |
| SD-12 | What is a ticket server? |
| SD-12 | How do you make IDs roughly time-ordered? |
| SD-12 | How many IDs per second can Snowflake generate per node? |
| SD-12 | Why not use an auto-increment database ID? |
| SD-12 | What is ULID? |
| SD-12 | How do you generate short IDs for a URL shortener? |
| SD-13 | How do you generate short codes for a URL shortener? |
| SD-13 | Base62 counter versus hashing: what are the trade-offs? |
| SD-13 | How do you handle custom aliases? |
| SD-13 | Should the redirect be 301 or 302? |
| SD-13 | How do you scale reads for a URL shortener? |
| SD-13 | How do you handle expiry? |
| SD-13 | How do you collect analytics on clicks? |
| SD-13 | How do you prevent abuse? |
| SD-13 | What database would you choose, and why? |
| SD-13 | How do you estimate the storage for a URL shortener? |
| SD-14 | How does Dynamo partition data? |
| SD-14 | How does Dynamo handle replication and consistency? |
| SD-14 | What are vector clocks? |
| SD-14 | What is hinted handoff? |
| SD-14 | What is read repair and anti-entropy with Merkle trees? |
| SD-14 | How does gossip detect failures? |
| SD-14 | What is sloppy quorum? |
| SD-14 | How do you design a key-value store API? |
| SD-14 | How do you handle conflicting writes? |
| SD-14 | How does a single-node key-value store persist data? |
| SD-15 | How do you design one-to-one messaging? |
| SD-15 | How do WebSocket connections scale to millions of users? |
| SD-15 | How do you guarantee message delivery and ordering? |
| SD-15 | How do you implement online presence? |
| SD-15 | How do you design group chat? |
| SD-15 | How do you store message history? |
| SD-15 | How do you handle offline users and push notifications? |
| SD-15 | How do you support multiple devices per user? |
| SD-15 | How do you implement read receipts? |
| SD-15 | How would you add end-to-end encryption? |
| SD-16 | What is fan-out on write versus fan-out on read? |
| SD-16 | How do you handle celebrities with millions of followers? |
| SD-16 | How do you store the timeline? |
| SD-16 | How do you rank the feed? |
| SD-16 | How do you paginate a feed? |
| SD-16 | How do you cache timelines? |
| SD-16 | How do you handle deletes and edits? |
| SD-16 | How do you store the follow graph? |
| SD-16 | How do you estimate storage for tweets and media? |
| SD-16 | How do you make the feed feel real time? |
| SD-17 | How does video upload work at scale? |
| SD-17 | How does transcoding work, and why do you need multiple formats? |
| SD-17 | What is adaptive bitrate streaming? |
| SD-17 | How do CDNs serve video? |
| SD-17 | How do you store video metadata? |
| SD-17 | How do you count views at scale? |
| SD-17 | How do you handle resumable uploads? |
| SD-17 | How do you recommend videos at a high level? |
| SD-17 | How do you manage storage cost for rarely watched videos? |
| SD-17 | How do you handle live streaming? |
| SD-18 | How do you design search autocomplete? |
| SD-18 | How does a trie serve top-k suggestions quickly? |
| SD-18 | How do you collect and aggregate query frequencies? |
| SD-18 | How often do you rebuild the trie? |
| SD-18 | How do you cache suggestions? |
| SD-18 | How do you shard the trie? |
| SD-18 | How do you personalise suggestions? |
| SD-18 | How do you filter offensive suggestions? |
| SD-18 | How do you support multiple languages? |
| SD-18 | What latency target should autocomplete have, and how do you meet it? |
| SD-19 | How does a web crawler work? |
| SD-19 | What is the URL frontier? |
| SD-19 | How do you enforce politeness? |
| SD-19 | How do you avoid crawling duplicate URLs and content? |
| SD-19 | How do you distribute the crawler across machines? |
| SD-19 | How do you handle robots.txt? |
| SD-19 | How do you prioritise which pages to crawl? |
| SD-19 | How do you detect crawler traps? |
| SD-19 | How do you store crawled pages? |
| SD-19 | How do you recrawl for freshness? |
| SD-20 | How do you design file upload and download? |
| SD-20 | Why split files into chunks? |
| SD-20 | How do you sync files across devices? |
| SD-20 | How do you resolve conflicts when two devices edit a file? |
| SD-20 | How do you store metadata? |
| SD-20 | How do you deduplicate storage? |
| SD-20 | How do you share files with permissions? |
| SD-20 | How do you notify clients of changes? |
| SD-20 | How do you support version history? |
| SD-20 | How do you handle very large files? |
| SD-21 | How do you find nearby drivers? |
| SD-21 | What are geohash and quadtree, and how do they compare? |
| SD-21 | How do you handle frequent location updates? |
| SD-21 | How do you match riders with drivers? |
| SD-21 | How do you compute ETA? |
| SD-21 | How do you implement surge pricing? |
| SD-21 | How do you shard location data? |
| SD-21 | How do you handle a driver going offline? |
| SD-21 | How do you design nearby-places search like Google Maps? |
| SD-21 | What is Google S2 or Uber H3? |
| SD-22 | How do you design a multi-channel notification service? |
| SD-22 | How do you handle retries and failures? |
| SD-22 | How do you avoid duplicate notifications? |
| SD-22 | How do you respect user preferences and quiet hours? |
| SD-22 | How do you rate limit notifications per user? |
| SD-22 | How do you prioritise urgent notifications? |
| SD-22 | How do you track delivery and opens? |
| SD-22 | How do you send a notification to millions of users at once? |
| SD-22 | How do you template notifications? |
| SD-22 | How do you integrate with third-party providers such as APNs and FCM? |
| SD-23 | How do you design a metrics monitoring system? |
| SD-23 | What is a time-series database, and why is it used? |
| SD-23 | Push versus pull metrics collection: what are the trade-offs? |
| SD-23 | How do you downsample and retain metrics? |
| SD-23 | How do you design alerting rules? |
| SD-23 | How do you handle high-cardinality labels? |
| SD-23 | How do you query metrics fast? |
| SD-23 | How do you avoid alert fatigue? |
| SD-23 | How does Google monitor its systems (Borgmon, Monarch)? |
| SD-23 | How do you monitor the monitoring system? |
| SD-24 | How do you design a payment system? |
| SD-24 | What is idempotency, and how do you implement it for payments? |
| SD-24 | What is a double-entry ledger? |
| SD-24 | How do you reconcile payments with external providers? |
| SD-24 | How do you handle a payment that times out? |
| SD-24 | What is the saga pattern? |
| SD-24 | How do you avoid double charging? |
| SD-24 | How do you store money amounts? |
| SD-24 | How do you handle refunds? |
| SD-24 | How do you ensure auditability? |
| SD-25 | How does collaborative editing work? |
| SD-25 | What is operational transformation? |
| SD-25 | What is a CRDT, and how does it compare with OT? |
| SD-25 | How do you show other users' cursors? |
| SD-25 | How do you store document history? |
| SD-25 | How do you handle offline edits? |
| SD-25 | How do you scale to many editors on one document? |
| SD-25 | How do you implement comments and suggestions? |
| SD-25 | How do you handle permissions? |
| SD-25 | What latency is acceptable for collaborative editing? |
