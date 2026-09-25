# Topic Lectures — the search phrase behind every topic's videos

One row per curriculum topic. The phrase is what `webapp/tools/build_videos.py` searches
YouTube with; the videos it finds, scores and verifies land in `topic-videos.md`. **The phrase
is the valuable part**: improve one, re-run that topic (`python webapp/tools/build_videos.py
DS-6`), and the topic gets better videos.

Write phrases the way you would type them into YouTube. Avoid apostrophes and symbols
(`Dijkstra's` → `Dijkstra algorithm`); they tokenise badly.

The planner never links a channel page or a playlist from a topic row — only individual
videos. The one fallback, used only if every video for a topic were taken down, is a plain
YouTube search for this phrase.

| # | Search phrase |
|---|---------------|
| DS-1 | C++ STL tutorial for competitive programming vector map set priority queue |
| DS-2 | time and space complexity analysis big O for coding interviews |
| DS-3 | arrays and hashing hashmap coding interview pattern |
| DS-4 | prefix sum technique subarray sum equals k |
| DS-5 | two pointers technique coding interview pattern |
| DS-6 | sliding window technique fixed and variable size |
| DS-7 | binary search on answer pattern lower bound rotated array |
| DS-8 | monotonic stack next greater element pattern |
| DS-9 | monotonic deque sliding window maximum queue implementation |
| DS-10 | linked list interview patterns reversal fast slow pointers |
| DS-11 | divide and conquer merge sort quickselect explained |
| DS-12 | custom comparator sorting counting sort bucket sort interview |
| DS-13 | binary tree traversals inorder preorder postorder level order |
| DS-14 | lowest common ancestor binary tree path sum construct tree |
| DS-15 | binary search tree insert delete validate BST |
| DS-16 | heap priority queue top k elements pattern |
| DS-17 | backtracking subsets permutations combinations template |
| DS-18 | N queens sudoku solver word search backtracking |
| DS-19 | graph DFS BFS connected components number of islands |
| DS-20 | multi source BFS shortest path unweighted grid 0-1 BFS |
| DS-21 | topological sort Kahn algorithm course schedule |
| DS-22 | union find disjoint set path compression union by rank |
| DS-23 | Dijkstra algorithm Bellman Ford Floyd Warshall shortest path |
| DS-24 | minimum spanning tree Kruskal Prim algorithm |
| DS-25 | greedy algorithms interview problems jump game gas station |
| DS-26 | merge intervals meeting rooms sweep line pattern |
| DS-27 | trie data structure implementation prefix tree |
| DS-28 | dynamic programming 1D memoization tabulation house robber |
| DS-29 | grid dynamic programming unique paths minimum path sum |
| DS-30 | 0 1 knapsack unbounded knapsack coin change dynamic programming |
| DS-31 | longest common subsequence edit distance dynamic programming on strings |
| DS-32 | longest increasing subsequence binary search patience sorting |
| DS-33 | matrix chain multiplication burst balloons interval dynamic programming |
| DS-34 | dynamic programming on trees bitmask dp digit dp |
| DS-35 | bit manipulation tricks for coding interviews XOR |
| DS-36 | math for coding interviews GCD modular exponentiation sieve |
| DS-37 | segment tree range query point update fenwick tree |
| DS-38 | KMP algorithm Z algorithm Rabin Karp string matching |
| DS-39 | Tarjan algorithm bridges articulation points strongly connected components |
| DS-40 | largest rectangle in histogram trapping rain water monotonic stack |
| DS-41 | LRU cache design data structure implementation |
| AL-1 | asymptotic notation big O omega theta explained |
| AL-2 | dynamic array amortized analysis vector doubling |
| AL-3 | hash table collision resolution chaining open addressing load factor |
| AL-4 | master theorem recurrence relations recursion tree method |
| AL-5 | binary search algorithm correctness invariant |
| AL-6 | how strings are stored in memory character encoding UTF-8 |
| AL-7 | stack and queue data structure implementation array linked list |
| AL-8 | doubly linked list circular linked list skip list |
| AL-9 | sorting algorithms comparison merge sort quick sort heap sort stability |
| AL-10 | comparison sort lower bound counting sort radix sort |
| AL-11 | binary tree properties complete full perfect binary tree |
| AL-12 | AVL tree rotations red black tree |
| AL-13 | B tree and B+ tree data structure explained |
| AL-14 | binary heap heapify build heap heap sort |
| AL-15 | backtracking state space tree time complexity |
| AL-16 | graph representation adjacency list adjacency matrix |
| AL-17 | depth first search breadth first search algorithm explained |
| AL-18 | directed acyclic graph topological ordering strongly connected components |
| AL-19 | disjoint set union by rank path compression inverse ackermann |
| AL-20 | Dijkstra algorithm proof negative edges Bellman Ford |
| AL-21 | minimum spanning tree cut property proof |
| AL-22 | greedy algorithm exchange argument activity selection Huffman coding |
| AL-23 | suffix array suffix tree trie explained |
| AL-24 | amortized analysis aggregate accounting potential method |
| AL-25 | dynamic programming optimal substructure overlapping subproblems |
| AL-26 | knapsack problem dynamic programming longest common subsequence explained |
| AL-27 | two's complement bitwise operations bit shifts |
| AL-28 | number theory GCD extended euclidean modular inverse sieve |
| AL-29 | permutations combinations probability expected value for programmers |
| AL-30 | randomized algorithms reservoir sampling Fisher Yates shuffle quickselect |
| AL-31 | sparse table square root decomposition range minimum query |
| AL-32 | KMP algorithm prefix function explained |
| AL-33 | max flow min cut Ford Fulkerson Edmonds Karp |
| AL-34 | computational geometry cross product convex hull |
| AL-35 | P vs NP NP complete NP hard explained |
| AL-36 | Bloom filter count min sketch HyperLogLog |
| AL-37 | external merge sort memory hierarchy cache locality |
| AL-38 | concurrent data structures locks lock free queue |
| LD-1 | object oriented programming C++ polymorphism virtual functions |
| LD-2 | SOLID principles explained with examples |
| LD-3 | factory builder singleton design pattern |
| LD-4 | adapter decorator composite facade proxy design pattern |
| LD-5 | strategy observer command state design pattern |
| LD-6 | UML class diagram sequence diagram tutorial |
| LD-7 | C++ multithreading mutex condition variable producer consumer |
| LD-8 | parking lot low level design |
| LD-9 | elevator system low level design |
| LD-10 | tic tac toe low level design |
| LD-11 | splitwise low level design |
| LD-12 | movie ticket booking system low level design |
| LD-13 | rate limiter low level design token bucket |
| LD-14 | vending machine low level design state pattern |
| LD-15 | logging framework low level design |
| SD-1 | how to approach system design interview requirements estimation high level deep dive |
| SD-2 | back of the envelope estimation system design |
| SD-3 | REST vs gRPC vs WebSockets system design |
| SD-4 | load balancer explained system design |
| SD-5 | caching strategies system design cache invalidation |
| SD-6 | SQL vs NoSQL database indexing replication system design |
| SD-7 | consistent hashing database sharding |
| SD-8 | CAP theorem Raft consensus algorithm |
| SD-9 | Kafka message queue system design |
| SD-10 | rate limiting algorithms token bucket sliding window |
| SD-11 | Google File System GFS paper Bigtable Spanner MapReduce explained |
| SD-12 | distributed unique ID generator snowflake |
| SD-13 | design URL shortener system design interview |
| SD-14 | design key value store Dynamo system design |
| SD-15 | design chat system WhatsApp system design |
| SD-16 | design Twitter news feed system design |
| SD-17 | YouTube video streaming architecture transcoding adaptive bitrate CDN |
| SD-18 | design search autocomplete typeahead system design |
| SD-19 | design web crawler system design |
| SD-20 | design Google Drive Dropbox system design |
| SD-21 | design Uber proximity service geohash quadtree |
| SD-22 | design notification system system design |
| SD-23 | design metrics monitoring alerting system |
| SD-24 | payment system architecture idempotency ledger reconciliation |
| SD-25 | design Google Docs collaborative editing operational transformation |
| BH-1 | Googleyness and leadership interview |
| BH-2 | STAR method behavioral interview answers |
| BH-3 | tell me about a time you had a conflict behavioral interview |
| BH-4 | tell me about a time you failed behavioral interview |
| BH-5 | tell me about yourself software engineer interview |
| IC-1 | Google software engineer interview process |
| IC-2 | think out loud during coding interview communication clarifying questions |
| IC-3 | Google coding interview in Google Docs tips |
| IC-4 | software engineer resume tips referral FAANG |
| IC-5 | mock coding interview Google software engineer |
| IC-6 | software engineer offer negotiation team matching Google |
