# Problem Bank — every problem the plan schedules, verified

One row per problem. The planner links `LC-<number>` anywhere in a session to the row here:
the LeetCode page, a free alternative when LeetCode locks it behind Premium, the solution
videos in `problem-videos.md`, and the Gemini walkthrough prompts.

**How these were checked.** Every slug was looked up in LeetCode's own GraphQL API on
2026-09-25: the number, title and difficulty below are what LeetCode returned, not what was
remembered. Two candidate slugs did not exist and were dropped. Sixteen are Premium-only;
each has a **free alternative on LintCode**, found through LintCode's API and accepted only
when the title matched exactly and the problem was unlocked.

Order within a topic is teaching order — easier and more fundamental first. The phase files
schedule them in this order; the ones a phase does not schedule appear as extra practice under
their topic.

| # | Title | Difficulty | Topic | Slug | Free alternative |
|---|-------|------------|-------|------|------------------|
| LC-1480 | Running Sum of 1d Array | Easy | DS-1 | running-sum-of-1d-array | — |
| LC-1929 | Concatenation of Array | Easy | DS-1 | concatenation-of-array | — |
| LC-724 | Find Pivot Index | Easy | DS-1 | find-pivot-index | — |
| LC-283 | Move Zeroes | Easy | DS-1 | move-zeroes | — |
| LC-66 | Plus One | Easy | DS-1 | plus-one | — |
| LC-977 | Squares of a Sorted Array | Easy | DS-1 | squares-of-a-sorted-array | — |
| LC-217 | Contains Duplicate | Easy | DS-1 | contains-duplicate | — |
| LC-136 | Single Number | Easy | DS-1 | single-number | — |
| LC-169 | Majority Element | Easy | DS-1 | majority-element | — |
| LC-26 | Remove Duplicates from Sorted Array | Easy | DS-1 | remove-duplicates-from-sorted-array | — |
| LC-121 | Best Time to Buy and Sell Stock | Easy | DS-2 | best-time-to-buy-and-sell-stock | — |
| LC-53 | Maximum Subarray | Medium | DS-2 | maximum-subarray | — |
| LC-189 | Rotate Array | Medium | DS-2 | rotate-array | — |
| LC-268 | Missing Number | Easy | DS-2 | missing-number | — |
| LC-448 | Find All Numbers Disappeared in an Array | Easy | DS-2 | find-all-numbers-disappeared-in-an-array | — |
| LC-271 | Encode and Decode Strings | Medium | DS-3 | encode-and-decode-strings | https://www.lintcode.com/problem/659/ |
| LC-1 | Two Sum | Easy | DS-3 | two-sum | — |
| LC-242 | Valid Anagram | Easy | DS-3 | valid-anagram | — |
| LC-49 | Group Anagrams | Medium | DS-3 | group-anagrams | — |
| LC-347 | Top K Frequent Elements | Medium | DS-3 | top-k-frequent-elements | — |
| LC-128 | Longest Consecutive Sequence | Medium | DS-3 | longest-consecutive-sequence | — |
| LC-36 | Valid Sudoku | Medium | DS-3 | valid-sudoku | — |
| LC-387 | First Unique Character in a String | Easy | DS-3 | first-unique-character-in-a-string | — |
| LC-383 | Ransom Note | Easy | DS-3 | ransom-note | — |
| LC-205 | Isomorphic Strings | Easy | DS-3 | isomorphic-strings | — |
| LC-535 | Encode and Decode TinyURL | Medium | DS-3 | encode-and-decode-tinyurl | — |
| LC-380 | Insert Delete GetRandom O(1) | Medium | DS-3 | insert-delete-getrandom-o1 | — |
| LC-442 | Find All Duplicates in an Array | Medium | DS-3 | find-all-duplicates-in-an-array | — |
| LC-554 | Brick Wall | Medium | DS-3 | brick-wall | — |
| LC-929 | Unique Email Addresses | Easy | DS-3 | unique-email-addresses | — |
| LC-290 | Word Pattern | Easy | DS-3 | word-pattern | — |
| LC-454 | 4Sum II | Medium | DS-3 | 4sum-ii | — |
| LC-939 | Minimum Area Rectangle | Medium | DS-3 | minimum-area-rectangle | — |
| LC-303 | Range Sum Query - Immutable | Easy | DS-4 | range-sum-query-immutable | — |
| LC-238 | Product of Array Except Self | Medium | DS-4 | product-of-array-except-self | — |
| LC-560 | Subarray Sum Equals K | Medium | DS-4 | subarray-sum-equals-k | — |
| LC-525 | Contiguous Array | Medium | DS-4 | contiguous-array | — |
| LC-304 | Range Sum Query 2D - Immutable | Medium | DS-4 | range-sum-query-2d-immutable | — |
| LC-523 | Continuous Subarray Sum | Medium | DS-4 | continuous-subarray-sum | — |
| LC-974 | Subarray Sums Divisible by K | Medium | DS-4 | subarray-sums-divisible-by-k | — |
| LC-1094 | Car Pooling | Medium | DS-4 | car-pooling | — |
| LC-1109 | Corporate Flight Bookings | Medium | DS-4 | corporate-flight-bookings | — |
| LC-1248 | Count Number of Nice Subarrays | Medium | DS-4 | count-number-of-nice-subarrays | — |
| LC-1314 | Matrix Block Sum | Medium | DS-4 | matrix-block-sum | — |
| LC-1074 | Number of Submatrices That Sum to Target | Hard | DS-4 | number-of-submatrices-that-sum-to-target | — |
| LC-125 | Valid Palindrome | Easy | DS-5 | valid-palindrome | — |
| LC-167 | Two Sum II - Input Array Is Sorted | Medium | DS-5 | two-sum-ii-input-array-is-sorted | — |
| LC-15 | 3Sum | Medium | DS-5 | 3sum | — |
| LC-11 | Container With Most Water | Medium | DS-5 | container-with-most-water | — |
| LC-75 | Sort Colors | Medium | DS-5 | sort-colors | — |
| LC-27 | Remove Element | Easy | DS-5 | remove-element | — |
| LC-88 | Merge Sorted Array | Easy | DS-5 | merge-sorted-array | — |
| LC-881 | Boats to Save People | Medium | DS-5 | boats-to-save-people | — |
| LC-18 | 4Sum | Medium | DS-5 | 4sum | — |
| LC-42 | Trapping Rain Water | Hard | DS-5 | trapping-rain-water | — |
| LC-16 | 3Sum Closest | Medium | DS-5 | 3sum-closest | — |
| LC-31 | Next Permutation | Medium | DS-5 | next-permutation | — |
| LC-844 | Backspace String Compare | Easy | DS-5 | backspace-string-compare | — |
| LC-443 | String Compression | Medium | DS-5 | string-compression | — |
| LC-643 | Maximum Average Subarray I | Easy | DS-6 | maximum-average-subarray-i | — |
| LC-3 | Longest Substring Without Repeating Characters | Medium | DS-6 | longest-substring-without-repeating-characters | — |
| LC-424 | Longest Repeating Character Replacement | Medium | DS-6 | longest-repeating-character-replacement | — |
| LC-567 | Permutation in String | Medium | DS-6 | permutation-in-string | — |
| LC-209 | Minimum Size Subarray Sum | Medium | DS-6 | minimum-size-subarray-sum | — |
| LC-904 | Fruit Into Baskets | Medium | DS-6 | fruit-into-baskets | — |
| LC-1004 | Max Consecutive Ones III | Medium | DS-6 | max-consecutive-ones-iii | — |
| LC-992 | Subarrays with K Different Integers | Hard | DS-6 | subarrays-with-k-different-integers | — |
| LC-340 | Longest Substring with At Most K Distinct Characters | Medium | DS-6 | longest-substring-with-at-most-k-distinct-characters | https://www.lintcode.com/problem/386/ |
| LC-76 | Minimum Window Substring | Hard | DS-6 | minimum-window-substring | — |
| LC-239 | Sliding Window Maximum | Hard | DS-6 | sliding-window-maximum | — |
| LC-1423 | Maximum Points You Can Obtain from Cards | Medium | DS-6 | maximum-points-you-can-obtain-from-cards | — |
| LC-1493 | Longest Subarray of 1's After Deleting One Element | Medium | DS-6 | longest-subarray-of-1s-after-deleting-one-element | — |
| LC-1052 | Grumpy Bookstore Owner | Medium | DS-6 | grumpy-bookstore-owner | — |
| LC-1658 | Minimum Operations to Reduce X to Zero | Medium | DS-6 | minimum-operations-to-reduce-x-to-zero | — |
| LC-1838 | Frequency of the Most Frequent Element | Medium | DS-6 | frequency-of-the-most-frequent-element | — |
| LC-704 | Binary Search | Easy | DS-7 | binary-search | — |
| LC-35 | Search Insert Position | Easy | DS-7 | search-insert-position | — |
| LC-278 | First Bad Version | Easy | DS-7 | first-bad-version | — |
| LC-34 | Find First and Last Position of Element in Sorted Array | Medium | DS-7 | find-first-and-last-position-of-element-in-sorted-array | — |
| LC-74 | Search a 2D Matrix | Medium | DS-7 | search-a-2d-matrix | — |
| LC-153 | Find Minimum in Rotated Sorted Array | Medium | DS-7 | find-minimum-in-rotated-sorted-array | — |
| LC-33 | Search in Rotated Sorted Array | Medium | DS-7 | search-in-rotated-sorted-array | — |
| LC-162 | Find Peak Element | Medium | DS-7 | find-peak-element | — |
| LC-875 | Koko Eating Bananas | Medium | DS-7 | koko-eating-bananas | — |
| LC-1011 | Capacity To Ship Packages Within D Days | Medium | DS-7 | capacity-to-ship-packages-within-d-days | — |
| LC-981 | Time Based Key-Value Store | Medium | DS-7 | time-based-key-value-store | — |
| LC-410 | Split Array Largest Sum | Hard | DS-7 | split-array-largest-sum | — |
| LC-4 | Median of Two Sorted Arrays | Hard | DS-7 | median-of-two-sorted-arrays | — |
| LC-81 | Search in Rotated Sorted Array II | Medium | DS-7 | search-in-rotated-sorted-array-ii | — |
| LC-658 | Find K Closest Elements | Medium | DS-7 | find-k-closest-elements | — |
| LC-1482 | Minimum Number of Days to Make m Bouquets | Medium | DS-7 | minimum-number-of-days-to-make-m-bouquets | — |
| LC-1552 | Magnetic Force Between Two Balls | Medium | DS-7 | magnetic-force-between-two-balls | — |
| LC-378 | Kth Smallest Element in a Sorted Matrix | Medium | DS-7 | kth-smallest-element-in-a-sorted-matrix | — |
| LC-287 | Find the Duplicate Number | Medium | DS-7 | find-the-duplicate-number | — |
| LC-792 | Number of Matching Subsequences | Medium | DS-7 | number-of-matching-subsequences | — |
| LC-20 | Valid Parentheses | Easy | DS-8 | valid-parentheses | — |
| LC-155 | Min Stack | Medium | DS-8 | min-stack | — |
| LC-150 | Evaluate Reverse Polish Notation | Medium | DS-8 | evaluate-reverse-polish-notation | — |
| LC-739 | Daily Temperatures | Medium | DS-8 | daily-temperatures | — |
| LC-496 | Next Greater Element I | Easy | DS-8 | next-greater-element-i | — |
| LC-503 | Next Greater Element II | Medium | DS-8 | next-greater-element-ii | — |
| LC-735 | Asteroid Collision | Medium | DS-8 | asteroid-collision | — |
| LC-394 | Decode String | Medium | DS-8 | decode-string | — |
| LC-227 | Basic Calculator II | Medium | DS-8 | basic-calculator-ii | — |
| LC-402 | Remove K Digits | Medium | DS-8 | remove-k-digits | — |
| LC-901 | Online Stock Span | Medium | DS-8 | online-stock-span | — |
| LC-224 | Basic Calculator | Hard | DS-8 | basic-calculator | — |
| LC-71 | Simplify Path | Medium | DS-8 | simplify-path | — |
| LC-2390 | Removing Stars From a String | Medium | DS-8 | removing-stars-from-a-string | — |
| LC-1249 | Minimum Remove to Make Valid Parentheses | Medium | DS-8 | minimum-remove-to-make-valid-parentheses | — |
| LC-32 | Longest Valid Parentheses | Hard | DS-8 | longest-valid-parentheses | — |
| LC-346 | Moving Average from Data Stream | Easy | DS-9 | moving-average-from-data-stream | https://www.lintcode.com/problem/642/ |
| LC-232 | Implement Queue using Stacks | Easy | DS-9 | implement-queue-using-stacks | — |
| LC-225 | Implement Stack using Queues | Easy | DS-9 | implement-stack-using-queues | — |
| LC-933 | Number of Recent Calls | Easy | DS-9 | number-of-recent-calls | — |
| LC-622 | Design Circular Queue | Medium | DS-9 | design-circular-queue | — |
| LC-862 | Shortest Subarray with Sum at Least K | Hard | DS-9 | shortest-subarray-with-sum-at-least-k | — |
| LC-1696 | Jump Game VI | Medium | DS-9 | jump-game-vi | — |
| LC-206 | Reverse Linked List | Easy | DS-10 | reverse-linked-list | — |
| LC-21 | Merge Two Sorted Lists | Easy | DS-10 | merge-two-sorted-lists | — |
| LC-141 | Linked List Cycle | Easy | DS-10 | linked-list-cycle | — |
| LC-876 | Middle of the Linked List | Easy | DS-10 | middle-of-the-linked-list | — |
| LC-234 | Palindrome Linked List | Easy | DS-10 | palindrome-linked-list | — |
| LC-19 | Remove Nth Node From End of List | Medium | DS-10 | remove-nth-node-from-end-of-list | — |
| LC-143 | Reorder List | Medium | DS-10 | reorder-list | — |
| LC-2 | Add Two Numbers | Medium | DS-10 | add-two-numbers | — |
| LC-142 | Linked List Cycle II | Medium | DS-10 | linked-list-cycle-ii | — |
| LC-160 | Intersection of Two Linked Lists | Easy | DS-10 | intersection-of-two-linked-lists | — |
| LC-138 | Copy List with Random Pointer | Medium | DS-10 | copy-list-with-random-pointer | — |
| LC-92 | Reverse Linked List II | Medium | DS-10 | reverse-linked-list-ii | — |
| LC-148 | Sort List | Medium | DS-10 | sort-list | — |
| LC-25 | Reverse Nodes in k-Group | Hard | DS-10 | reverse-nodes-in-k-group | — |
| LC-23 | Merge k Sorted Lists | Hard | DS-10 | merge-k-sorted-lists | — |
| LC-328 | Odd Even Linked List | Medium | DS-10 | odd-even-linked-list | — |
| LC-61 | Rotate List | Medium | DS-10 | rotate-list | — |
| LC-82 | Remove Duplicates from Sorted List II | Medium | DS-10 | remove-duplicates-from-sorted-list-ii | — |
| LC-24 | Swap Nodes in Pairs | Medium | DS-10 | swap-nodes-in-pairs | — |
| LC-509 | Fibonacci Number | Easy | DS-11 | fibonacci-number | — |
| LC-50 | Pow(x, n) | Medium | DS-11 | powx-n | — |
| LC-215 | Kth Largest Element in an Array | Medium | DS-11 | kth-largest-element-in-an-array | — |
| LC-912 | Sort an Array | Medium | DS-11 | sort-an-array | — |
| LC-315 | Count of Smaller Numbers After Self | Hard | DS-11 | count-of-smaller-numbers-after-self | — |
| LC-241 | Different Ways to Add Parentheses | Medium | DS-11 | different-ways-to-add-parentheses | — |
| LC-493 | Reverse Pairs | Hard | DS-11 | reverse-pairs | — |
| LC-451 | Sort Characters By Frequency | Medium | DS-12 | sort-characters-by-frequency | — |
| LC-179 | Largest Number | Medium | DS-12 | largest-number | — |
| LC-274 | H-Index | Medium | DS-12 | h-index | — |
| LC-791 | Custom Sort String | Medium | DS-12 | custom-sort-string | — |
| LC-324 | Wiggle Sort II | Medium | DS-12 | wiggle-sort-ii | — |
| LC-164 | Maximum Gap | Medium | DS-12 | maximum-gap | — |
| LC-833 | Find And Replace in String | Medium | DS-12 | find-and-replace-in-string | — |
| LC-1229 | Meeting Scheduler | Medium | DS-12 | meeting-scheduler | https://www.lintcode.com/problem/3653/ |
| LC-104 | Maximum Depth of Binary Tree | Easy | DS-13 | maximum-depth-of-binary-tree | — |
| LC-226 | Invert Binary Tree | Easy | DS-13 | invert-binary-tree | — |
| LC-100 | Same Tree | Easy | DS-13 | same-tree | — |
| LC-101 | Symmetric Tree | Easy | DS-13 | symmetric-tree | — |
| LC-94 | Binary Tree Inorder Traversal | Easy | DS-13 | binary-tree-inorder-traversal | — |
| LC-102 | Binary Tree Level Order Traversal | Medium | DS-13 | binary-tree-level-order-traversal | — |
| LC-199 | Binary Tree Right Side View | Medium | DS-13 | binary-tree-right-side-view | — |
| LC-543 | Diameter of Binary Tree | Easy | DS-13 | diameter-of-binary-tree | — |
| LC-110 | Balanced Binary Tree | Easy | DS-13 | balanced-binary-tree | — |
| LC-572 | Subtree of Another Tree | Easy | DS-13 | subtree-of-another-tree | — |
| LC-103 | Binary Tree Zigzag Level Order Traversal | Medium | DS-13 | binary-tree-zigzag-level-order-traversal | — |
| LC-1448 | Count Good Nodes in Binary Tree | Medium | DS-13 | count-good-nodes-in-binary-tree | — |
| LC-366 | Find Leaves of Binary Tree | Medium | DS-13 | find-leaves-of-binary-tree | https://www.lintcode.com/problem/650/ |
| LC-662 | Maximum Width of Binary Tree | Medium | DS-13 | maximum-width-of-binary-tree | — |
| LC-987 | Vertical Order Traversal of a Binary Tree | Hard | DS-13 | vertical-order-traversal-of-a-binary-tree | — |
| LC-111 | Minimum Depth of Binary Tree | Easy | DS-13 | minimum-depth-of-binary-tree | — |
| LC-145 | Binary Tree Postorder Traversal | Easy | DS-13 | binary-tree-postorder-traversal | — |
| LC-958 | Check Completeness of a Binary Tree | Medium | DS-13 | check-completeness-of-a-binary-tree | — |
| LC-222 | Count Complete Tree Nodes | Medium | DS-13 | count-complete-tree-nodes | — |
| LC-112 | Path Sum | Easy | DS-14 | path-sum | — |
| LC-113 | Path Sum II | Medium | DS-14 | path-sum-ii | — |
| LC-236 | Lowest Common Ancestor of a Binary Tree | Medium | DS-14 | lowest-common-ancestor-of-a-binary-tree | — |
| LC-105 | Construct Binary Tree from Preorder and Inorder Traversal | Medium | DS-14 | construct-binary-tree-from-preorder-and-inorder-traversal | — |
| LC-114 | Flatten Binary Tree to Linked List | Medium | DS-14 | flatten-binary-tree-to-linked-list | — |
| LC-437 | Path Sum III | Medium | DS-14 | path-sum-iii | — |
| LC-863 | All Nodes Distance K in Binary Tree | Medium | DS-14 | all-nodes-distance-k-in-binary-tree | — |
| LC-124 | Binary Tree Maximum Path Sum | Hard | DS-14 | binary-tree-maximum-path-sum | — |
| LC-297 | Serialize and Deserialize Binary Tree | Hard | DS-14 | serialize-and-deserialize-binary-tree | — |
| LC-116 | Populating Next Right Pointers in Each Node | Medium | DS-14 | populating-next-right-pointers-in-each-node | — |
| LC-129 | Sum Root to Leaf Numbers | Medium | DS-14 | sum-root-to-leaf-numbers | — |
| LC-106 | Construct Binary Tree from Inorder and Postorder Traversal | Medium | DS-14 | construct-binary-tree-from-inorder-and-postorder-traversal | — |
| LC-1110 | Delete Nodes And Return Forest | Medium | DS-14 | delete-nodes-and-return-forest | — |
| LC-2096 | Step-By-Step Directions From a Binary Tree Node to Another | Medium | DS-14 | step-by-step-directions-from-a-binary-tree-node-to-another | — |
| LC-979 | Distribute Coins in Binary Tree | Medium | DS-14 | distribute-coins-in-binary-tree | — |
| LC-1372 | Longest ZigZag Path in a Binary Tree | Medium | DS-14 | longest-zigzag-path-in-a-binary-tree | — |
| LC-700 | Search in a Binary Search Tree | Easy | DS-15 | search-in-a-binary-search-tree | — |
| LC-701 | Insert into a Binary Search Tree | Medium | DS-15 | insert-into-a-binary-search-tree | — |
| LC-98 | Validate Binary Search Tree | Medium | DS-15 | validate-binary-search-tree | — |
| LC-235 | Lowest Common Ancestor of a Binary Search Tree | Medium | DS-15 | lowest-common-ancestor-of-a-binary-search-tree | — |
| LC-230 | Kth Smallest Element in a BST | Medium | DS-15 | kth-smallest-element-in-a-bst | — |
| LC-450 | Delete Node in a BST | Medium | DS-15 | delete-node-in-a-bst | — |
| LC-108 | Convert Sorted Array to Binary Search Tree | Easy | DS-15 | convert-sorted-array-to-binary-search-tree | — |
| LC-173 | Binary Search Tree Iterator | Medium | DS-15 | binary-search-tree-iterator | — |
| LC-99 | Recover Binary Search Tree | Medium | DS-15 | recover-binary-search-tree | — |
| LC-653 | Two Sum IV - Input is a BST | Easy | DS-15 | two-sum-iv-input-is-a-bst | — |
| LC-669 | Trim a Binary Search Tree | Medium | DS-15 | trim-a-binary-search-tree | — |
| LC-1382 | Balance a Binary Search Tree | Medium | DS-15 | balance-a-binary-search-tree | — |
| LC-220 | Contains Duplicate III | Hard | DS-15 | contains-duplicate-iii | — |
| LC-703 | Kth Largest Element in a Stream | Easy | DS-16 | kth-largest-element-in-a-stream | — |
| LC-1046 | Last Stone Weight | Easy | DS-16 | last-stone-weight | — |
| LC-973 | K Closest Points to Origin | Medium | DS-16 | k-closest-points-to-origin | — |
| LC-621 | Task Scheduler | Medium | DS-16 | task-scheduler | — |
| LC-767 | Reorganize String | Medium | DS-16 | reorganize-string | — |
| LC-373 | Find K Pairs with Smallest Sums | Medium | DS-16 | find-k-pairs-with-smallest-sums | — |
| LC-295 | Find Median from Data Stream | Hard | DS-16 | find-median-from-data-stream | — |
| LC-502 | IPO | Hard | DS-16 | ipo | — |
| LC-632 | Smallest Range Covering Elements from K Lists | Hard | DS-16 | smallest-range-covering-elements-from-k-lists | — |
| LC-1834 | Single-Threaded CPU | Medium | DS-16 | single-threaded-cpu | — |
| LC-692 | Top K Frequent Words | Medium | DS-16 | top-k-frequent-words | — |
| LC-1642 | Furthest Building You Can Reach | Medium | DS-16 | furthest-building-you-can-reach | — |
| LC-1383 | Maximum Performance of a Team | Hard | DS-16 | maximum-performance-of-a-team | — |
| LC-857 | Minimum Cost to Hire K Workers | Hard | DS-16 | minimum-cost-to-hire-k-workers | — |
| LC-407 | Trapping Rain Water II | Hard | DS-16 | trapping-rain-water-ii | — |
| LC-78 | Subsets | Medium | DS-17 | subsets | — |
| LC-90 | Subsets II | Medium | DS-17 | subsets-ii | — |
| LC-46 | Permutations | Medium | DS-17 | permutations | — |
| LC-47 | Permutations II | Medium | DS-17 | permutations-ii | — |
| LC-77 | Combinations | Medium | DS-17 | combinations | — |
| LC-39 | Combination Sum | Medium | DS-17 | combination-sum | — |
| LC-40 | Combination Sum II | Medium | DS-17 | combination-sum-ii | — |
| LC-17 | Letter Combinations of a Phone Number | Medium | DS-17 | letter-combinations-of-a-phone-number | — |
| LC-22 | Generate Parentheses | Medium | DS-17 | generate-parentheses | — |
| LC-93 | Restore IP Addresses | Medium | DS-17 | restore-ip-addresses | — |
| LC-216 | Combination Sum III | Medium | DS-17 | combination-sum-iii | — |
| LC-784 | Letter Case Permutation | Medium | DS-17 | letter-case-permutation | — |
| LC-526 | Beautiful Arrangement | Medium | DS-17 | beautiful-arrangement | — |
| LC-79 | Word Search | Medium | DS-18 | word-search | — |
| LC-131 | Palindrome Partitioning | Medium | DS-18 | palindrome-partitioning | — |
| LC-51 | N-Queens | Hard | DS-18 | n-queens | — |
| LC-52 | N-Queens II | Hard | DS-18 | n-queens-ii | — |
| LC-37 | Sudoku Solver | Hard | DS-18 | sudoku-solver | — |
| LC-698 | Partition to K Equal Sum Subsets | Medium | DS-18 | partition-to-k-equal-sum-subsets | — |
| LC-140 | Word Break II | Hard | DS-18 | word-break-ii | — |
| LC-282 | Expression Add Operators | Hard | DS-18 | expression-add-operators | — |
| LC-473 | Matchsticks to Square | Medium | DS-18 | matchsticks-to-square | — |
| LC-980 | Unique Paths III | Hard | DS-18 | unique-paths-iii | — |
| LC-301 | Remove Invalid Parentheses | Hard | DS-18 | remove-invalid-parentheses | — |
| LC-733 | Flood Fill | Easy | DS-19 | flood-fill | — |
| LC-200 | Number of Islands | Medium | DS-19 | number-of-islands | — |
| LC-695 | Max Area of Island | Medium | DS-19 | max-area-of-island | — |
| LC-133 | Clone Graph | Medium | DS-19 | clone-graph | — |
| LC-547 | Number of Provinces | Medium | DS-19 | number-of-provinces | — |
| LC-130 | Surrounded Regions | Medium | DS-19 | surrounded-regions | — |
| LC-417 | Pacific Atlantic Water Flow | Medium | DS-19 | pacific-atlantic-water-flow | — |
| LC-1971 | Find if Path Exists in Graph | Easy | DS-19 | find-if-path-exists-in-graph | — |
| LC-785 | Is Graph Bipartite? | Medium | DS-19 | is-graph-bipartite | — |
| LC-841 | Keys and Rooms | Medium | DS-19 | keys-and-rooms | — |
| LC-1254 | Number of Closed Islands | Medium | DS-19 | number-of-closed-islands | — |
| LC-490 | The Maze | Medium | DS-19 | the-maze | https://www.lintcode.com/problem/787/ |
| LC-827 | Making A Large Island | Hard | DS-19 | making-a-large-island | — |
| LC-997 | Find the Town Judge | Easy | DS-19 | find-the-town-judge | — |
| LC-1020 | Number of Enclaves | Medium | DS-19 | number-of-enclaves | — |
| LC-1905 | Count Sub Islands | Medium | DS-19 | count-sub-islands | — |
| LC-2101 | Detonate the Maximum Bombs | Medium | DS-19 | detonate-the-maximum-bombs | — |
| LC-934 | Shortest Bridge | Medium | DS-19 | shortest-bridge | — |
| LC-994 | Rotting Oranges | Medium | DS-20 | rotting-oranges | — |
| LC-542 | 01 Matrix | Medium | DS-20 | 01-matrix | — |
| LC-1091 | Shortest Path in Binary Matrix | Medium | DS-20 | shortest-path-in-binary-matrix | — |
| LC-752 | Open the Lock | Medium | DS-20 | open-the-lock | — |
| LC-127 | Word Ladder | Hard | DS-20 | word-ladder | — |
| LC-286 | Walls and Gates | Medium | DS-20 | walls-and-gates | https://www.lintcode.com/problem/663/ |
| LC-909 | Snakes and Ladders | Medium | DS-20 | snakes-and-ladders | — |
| LC-1162 | As Far from Land as Possible | Medium | DS-20 | as-far-from-land-as-possible | — |
| LC-1293 | Shortest Path in a Grid with Obstacles Elimination | Hard | DS-20 | shortest-path-in-a-grid-with-obstacles-elimination | — |
| LC-433 | Minimum Genetic Mutation | Medium | DS-20 | minimum-genetic-mutation | — |
| LC-815 | Bus Routes | Hard | DS-20 | bus-routes | — |
| LC-1306 | Jump Game III | Medium | DS-20 | jump-game-iii | — |
| LC-1926 | Nearest Exit from Entrance in Maze | Medium | DS-20 | nearest-exit-from-entrance-in-maze | — |
| LC-773 | Sliding Puzzle | Hard | DS-20 | sliding-puzzle | — |
| LC-864 | Shortest Path to Get All Keys | Hard | DS-20 | shortest-path-to-get-all-keys | — |
| LC-207 | Course Schedule | Medium | DS-21 | course-schedule | — |
| LC-210 | Course Schedule II | Medium | DS-21 | course-schedule-ii | — |
| LC-802 | Find Eventual Safe States | Medium | DS-21 | find-eventual-safe-states | — |
| LC-310 | Minimum Height Trees | Medium | DS-21 | minimum-height-trees | — |
| LC-2050 | Parallel Courses III | Hard | DS-21 | parallel-courses-iii | — |
| LC-329 | Longest Increasing Path in a Matrix | Hard | DS-21 | longest-increasing-path-in-a-matrix | — |
| LC-269 | Alien Dictionary | Hard | DS-21 | alien-dictionary | https://www.lintcode.com/problem/892/ |
| LC-1203 | Sort Items by Groups Respecting Dependencies | Hard | DS-21 | sort-items-by-groups-respecting-dependencies | — |
| LC-1462 | Course Schedule IV | Medium | DS-21 | course-schedule-iv | — |
| LC-2115 | Find All Possible Recipes from Given Supplies | Medium | DS-21 | find-all-possible-recipes-from-given-supplies | — |
| LC-1857 | Largest Color Value in a Directed Graph | Hard | DS-21 | largest-color-value-in-a-directed-graph | — |
| LC-261 | Graph Valid Tree | Medium | DS-22 | graph-valid-tree | https://www.lintcode.com/problem/178/ |
| LC-323 | Number of Connected Components in an Undirected Graph | Medium | DS-22 | number-of-connected-components-in-an-undirected-graph | https://www.lintcode.com/problem/3651/ |
| LC-684 | Redundant Connection | Medium | DS-22 | redundant-connection | — |
| LC-721 | Accounts Merge | Medium | DS-22 | accounts-merge | — |
| LC-1319 | Number of Operations to Make Network Connected | Medium | DS-22 | number-of-operations-to-make-network-connected | — |
| LC-947 | Most Stones Removed with Same Row or Column | Medium | DS-22 | most-stones-removed-with-same-row-or-column | — |
| LC-990 | Satisfiability of Equality Equations | Medium | DS-22 | satisfiability-of-equality-equations | — |
| LC-1202 | Smallest String With Swaps | Medium | DS-22 | smallest-string-with-swaps | — |
| LC-778 | Swim in Rising Water | Hard | DS-22 | swim-in-rising-water | — |
| LC-399 | Evaluate Division | Medium | DS-22 | evaluate-division | — |
| LC-1061 | Lexicographically Smallest Equivalent String | Medium | DS-22 | lexicographically-smallest-equivalent-string | — |
| LC-839 | Similar String Groups | Hard | DS-22 | similar-string-groups | — |
| LC-959 | Regions Cut By Slashes | Medium | DS-22 | regions-cut-by-slashes | — |
| LC-743 | Network Delay Time | Medium | DS-23 | network-delay-time | — |
| LC-1514 | Path with Maximum Probability | Medium | DS-23 | path-with-maximum-probability | — |
| LC-787 | Cheapest Flights Within K Stops | Medium | DS-23 | cheapest-flights-within-k-stops | — |
| LC-1631 | Path With Minimum Effort | Medium | DS-23 | path-with-minimum-effort | — |
| LC-1334 | Find the City With the Smallest Number of Neighbors at a Threshold Distance | Medium | DS-23 | find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance | — |
| LC-1976 | Number of Ways to Arrive at Destination | Medium | DS-23 | number-of-ways-to-arrive-at-destination | — |
| LC-1368 | Minimum Cost to Make at Least One Valid Path in a Grid | Hard | DS-23 | minimum-cost-to-make-at-least-one-valid-path-in-a-grid | — |
| LC-2045 | Second Minimum Time to Reach Destination | Hard | DS-23 | second-minimum-time-to-reach-destination | — |
| LC-882 | Reachable Nodes In Subdivided Graph | Hard | DS-23 | reachable-nodes-in-subdivided-graph | — |
| LC-2203 | Minimum Weighted Subgraph With the Required Paths | Hard | DS-23 | minimum-weighted-subgraph-with-the-required-paths | — |
| LC-1584 | Min Cost to Connect All Points | Medium | DS-24 | min-cost-to-connect-all-points | — |
| LC-1135 | Connecting Cities With Minimum Cost | Medium | DS-24 | connecting-cities-with-minimum-cost | https://www.lintcode.com/problem/3672/ |
| LC-1489 | Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree | Hard | DS-24 | find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree | — |
| LC-1579 | Remove Max Number of Edges to Keep Graph Fully Traversable | Hard | DS-24 | remove-max-number-of-edges-to-keep-graph-fully-traversable | — |
| LC-1697 | Checking Existence of Edge Length Limited Paths | Hard | DS-24 | checking-existence-of-edge-length-limited-paths | — |
| LC-455 | Assign Cookies | Easy | DS-25 | assign-cookies | — |
| LC-860 | Lemonade Change | Easy | DS-25 | lemonade-change | — |
| LC-55 | Jump Game | Medium | DS-25 | jump-game | — |
| LC-45 | Jump Game II | Medium | DS-25 | jump-game-ii | — |
| LC-134 | Gas Station | Medium | DS-25 | gas-station | — |
| LC-846 | Hand of Straights | Medium | DS-25 | hand-of-straights | — |
| LC-763 | Partition Labels | Medium | DS-25 | partition-labels | — |
| LC-135 | Candy | Hard | DS-25 | candy | — |
| LC-452 | Minimum Number of Arrows to Burst Balloons | Medium | DS-25 | minimum-number-of-arrows-to-burst-balloons | — |
| LC-406 | Queue Reconstruction by Height | Medium | DS-25 | queue-reconstruction-by-height | — |
| LC-678 | Valid Parenthesis String | Medium | DS-25 | valid-parenthesis-string | — |
| LC-1326 | Minimum Number of Taps to Open to Water a Garden | Hard | DS-25 | minimum-number-of-taps-to-open-to-water-a-garden | — |
| LC-1710 | Maximum Units on a Truck | Easy | DS-25 | maximum-units-on-a-truck | — |
| LC-1029 | Two City Scheduling | Medium | DS-25 | two-city-scheduling | — |
| LC-1007 | Minimum Domino Rotations For Equal Row | Medium | DS-25 | minimum-domino-rotations-for-equal-row | — |
| LC-826 | Most Profit Assigning Work | Medium | DS-25 | most-profit-assigning-work | — |
| LC-1647 | Minimum Deletions to Make Character Frequencies Unique | Medium | DS-25 | minimum-deletions-to-make-character-frequencies-unique | — |
| LC-316 | Remove Duplicate Letters | Medium | DS-25 | remove-duplicate-letters | — |
| LC-330 | Patching Array | Hard | DS-25 | patching-array | — |
| LC-252 | Meeting Rooms | Easy | DS-26 | meeting-rooms | https://www.lintcode.com/problem/920/ |
| LC-253 | Meeting Rooms II | Medium | DS-26 | meeting-rooms-ii | https://www.lintcode.com/problem/919/ |
| LC-56 | Merge Intervals | Medium | DS-26 | merge-intervals | — |
| LC-57 | Insert Interval | Medium | DS-26 | insert-interval | — |
| LC-435 | Non-overlapping Intervals | Medium | DS-26 | non-overlapping-intervals | — |
| LC-986 | Interval List Intersections | Medium | DS-26 | interval-list-intersections | — |
| LC-729 | My Calendar I | Medium | DS-26 | my-calendar-i | — |
| LC-731 | My Calendar II | Medium | DS-26 | my-calendar-ii | — |
| LC-1851 | Minimum Interval to Include Each Query | Hard | DS-26 | minimum-interval-to-include-each-query | — |
| LC-759 | Employee Free Time | Hard | DS-26 | employee-free-time | https://www.lintcode.com/problem/850/ |
| LC-218 | The Skyline Problem | Hard | DS-26 | the-skyline-problem | — |
| LC-1288 | Remove Covered Intervals | Medium | DS-26 | remove-covered-intervals | — |
| LC-2406 | Divide Intervals Into Minimum Number of Groups | Medium | DS-26 | divide-intervals-into-minimum-number-of-groups | — |
| LC-1353 | Maximum Number of Events That Can Be Attended | Medium | DS-26 | maximum-number-of-events-that-can-be-attended | — |
| LC-352 | Data Stream as Disjoint Intervals | Hard | DS-26 | data-stream-as-disjoint-intervals | — |
| LC-208 | Implement Trie (Prefix Tree) | Medium | DS-27 | implement-trie-prefix-tree | — |
| LC-211 | Design Add and Search Words Data Structure | Medium | DS-27 | design-add-and-search-words-data-structure | — |
| LC-648 | Replace Words | Medium | DS-27 | replace-words | — |
| LC-720 | Longest Word in Dictionary | Medium | DS-27 | longest-word-in-dictionary | — |
| LC-1268 | Search Suggestions System | Medium | DS-27 | search-suggestions-system | — |
| LC-677 | Map Sum Pairs | Medium | DS-27 | map-sum-pairs | — |
| LC-421 | Maximum XOR of Two Numbers in an Array | Medium | DS-27 | maximum-xor-of-two-numbers-in-an-array | — |
| LC-212 | Word Search II | Hard | DS-27 | word-search-ii | — |
| LC-1032 | Stream of Characters | Hard | DS-27 | stream-of-characters | — |
| LC-336 | Palindrome Pairs | Hard | DS-27 | palindrome-pairs | — |
| LC-472 | Concatenated Words | Hard | DS-27 | concatenated-words | — |
| LC-70 | Climbing Stairs | Easy | DS-28 | climbing-stairs | — |
| LC-746 | Min Cost Climbing Stairs | Easy | DS-28 | min-cost-climbing-stairs | — |
| LC-198 | House Robber | Medium | DS-28 | house-robber | — |
| LC-213 | House Robber II | Medium | DS-28 | house-robber-ii | — |
| LC-91 | Decode Ways | Medium | DS-28 | decode-ways | — |
| LC-139 | Word Break | Medium | DS-28 | word-break | — |
| LC-152 | Maximum Product Subarray | Medium | DS-28 | maximum-product-subarray | — |
| LC-279 | Perfect Squares | Medium | DS-28 | perfect-squares | — |
| LC-740 | Delete and Earn | Medium | DS-28 | delete-and-earn | — |
| LC-5 | Longest Palindromic Substring | Medium | DS-28 | longest-palindromic-substring | — |
| LC-647 | Palindromic Substrings | Medium | DS-28 | palindromic-substrings | — |
| LC-2140 | Solving Questions With Brainpower | Medium | DS-28 | solving-questions-with-brainpower | — |
| LC-983 | Minimum Cost For Tickets | Medium | DS-28 | minimum-cost-for-tickets | — |
| LC-1155 | Number of Dice Rolls With Target Sum | Medium | DS-28 | number-of-dice-rolls-with-target-sum | — |
| LC-1220 | Count Vowels Permutation | Hard | DS-28 | count-vowels-permutation | — |
| LC-62 | Unique Paths | Medium | DS-29 | unique-paths | — |
| LC-63 | Unique Paths II | Medium | DS-29 | unique-paths-ii | — |
| LC-64 | Minimum Path Sum | Medium | DS-29 | minimum-path-sum | — |
| LC-120 | Triangle | Medium | DS-29 | triangle | — |
| LC-221 | Maximal Square | Medium | DS-29 | maximal-square | — |
| LC-931 | Minimum Falling Path Sum | Medium | DS-29 | minimum-falling-path-sum | — |
| LC-1463 | Cherry Pickup II | Hard | DS-29 | cherry-pickup-ii | — |
| LC-174 | Dungeon Game | Hard | DS-29 | dungeon-game | — |
| LC-576 | Out of Boundary Paths | Medium | DS-29 | out-of-boundary-paths | — |
| LC-1301 | Number of Paths with Max Score | Hard | DS-29 | number-of-paths-with-max-score | — |
| LC-741 | Cherry Pickup | Hard | DS-29 | cherry-pickup | — |
| LC-416 | Partition Equal Subset Sum | Medium | DS-30 | partition-equal-subset-sum | — |
| LC-494 | Target Sum | Medium | DS-30 | target-sum | — |
| LC-1049 | Last Stone Weight II | Medium | DS-30 | last-stone-weight-ii | — |
| LC-474 | Ones and Zeroes | Medium | DS-30 | ones-and-zeroes | — |
| LC-322 | Coin Change | Medium | DS-30 | coin-change | — |
| LC-518 | Coin Change II | Medium | DS-30 | coin-change-ii | — |
| LC-377 | Combination Sum IV | Medium | DS-30 | combination-sum-iv | — |
| LC-879 | Profitable Schemes | Hard | DS-30 | profitable-schemes | — |
| LC-1043 | Partition Array for Maximum Sum | Medium | DS-30 | partition-array-for-maximum-sum | — |
| LC-956 | Tallest Billboard | Hard | DS-30 | tallest-billboard | — |
| LC-1143 | Longest Common Subsequence | Medium | DS-31 | longest-common-subsequence | — |
| LC-72 | Edit Distance | Medium | DS-31 | edit-distance | — |
| LC-516 | Longest Palindromic Subsequence | Medium | DS-31 | longest-palindromic-subsequence | — |
| LC-583 | Delete Operation for Two Strings | Medium | DS-31 | delete-operation-for-two-strings | — |
| LC-1312 | Minimum Insertion Steps to Make a String Palindrome | Hard | DS-31 | minimum-insertion-steps-to-make-a-string-palindrome | — |
| LC-115 | Distinct Subsequences | Hard | DS-31 | distinct-subsequences | — |
| LC-97 | Interleaving String | Medium | DS-31 | interleaving-string | — |
| LC-1092 | Shortest Common Supersequence  | Hard | DS-31 | shortest-common-supersequence | — |
| LC-44 | Wildcard Matching | Hard | DS-31 | wildcard-matching | — |
| LC-10 | Regular Expression Matching | Hard | DS-31 | regular-expression-matching | — |
| LC-718 | Maximum Length of Repeated Subarray | Medium | DS-31 | maximum-length-of-repeated-subarray | — |
| LC-1035 | Uncrossed Lines | Medium | DS-31 | uncrossed-lines | — |
| LC-712 | Minimum ASCII Delete Sum for Two Strings | Medium | DS-31 | minimum-ascii-delete-sum-for-two-strings | — |
| LC-87 | Scramble String | Hard | DS-31 | scramble-string | — |
| LC-300 | Longest Increasing Subsequence | Medium | DS-32 | longest-increasing-subsequence | — |
| LC-673 | Number of Longest Increasing Subsequence | Medium | DS-32 | number-of-longest-increasing-subsequence | — |
| LC-368 | Largest Divisible Subset | Medium | DS-32 | largest-divisible-subset | — |
| LC-1048 | Longest String Chain | Medium | DS-32 | longest-string-chain | — |
| LC-354 | Russian Doll Envelopes | Hard | DS-32 | russian-doll-envelopes | — |
| LC-309 | Best Time to Buy and Sell Stock with Cooldown | Medium | DS-32 | best-time-to-buy-and-sell-stock-with-cooldown | — |
| LC-123 | Best Time to Buy and Sell Stock III | Hard | DS-32 | best-time-to-buy-and-sell-stock-iii | — |
| LC-188 | Best Time to Buy and Sell Stock IV | Hard | DS-32 | best-time-to-buy-and-sell-stock-iv | — |
| LC-646 | Maximum Length of Pair Chain | Medium | DS-32 | maximum-length-of-pair-chain | — |
| LC-714 | Best Time to Buy and Sell Stock with Transaction Fee | Medium | DS-32 | best-time-to-buy-and-sell-stock-with-transaction-fee | — |
| LC-1027 | Longest Arithmetic Subsequence | Medium | DS-32 | longest-arithmetic-subsequence | — |
| LC-1235 | Maximum Profit in Job Scheduling | Hard | DS-32 | maximum-profit-in-job-scheduling | — |
| LC-1039 | Minimum Score Triangulation of Polygon | Medium | DS-33 | minimum-score-triangulation-of-polygon | — |
| LC-1547 | Minimum Cost to Cut a Stick | Hard | DS-33 | minimum-cost-to-cut-a-stick | — |
| LC-312 | Burst Balloons | Hard | DS-33 | burst-balloons | — |
| LC-132 | Palindrome Partitioning II | Hard | DS-33 | palindrome-partitioning-ii | — |
| LC-664 | Strange Printer | Hard | DS-33 | strange-printer | — |
| LC-877 | Stone Game | Medium | DS-33 | stone-game | — |
| LC-486 | Predict the Winner | Medium | DS-33 | predict-the-winner | — |
| LC-1130 | Minimum Cost Tree From Leaf Values | Medium | DS-33 | minimum-cost-tree-from-leaf-values | — |
| LC-1140 | Stone Game II | Medium | DS-33 | stone-game-ii | — |
| LC-375 | Guess Number Higher or Lower II | Medium | DS-33 | guess-number-higher-or-lower-ii | — |
| LC-546 | Remove Boxes | Hard | DS-33 | remove-boxes | — |
| LC-337 | House Robber III | Medium | DS-34 | house-robber-iii | — |
| LC-968 | Binary Tree Cameras | Hard | DS-34 | binary-tree-cameras | — |
| LC-96 | Unique Binary Search Trees | Medium | DS-34 | unique-binary-search-trees | — |
| LC-834 | Sum of Distances in Tree | Hard | DS-34 | sum-of-distances-in-tree | — |
| LC-464 | Can I Win | Medium | DS-34 | can-i-win | — |
| LC-847 | Shortest Path Visiting All Nodes | Hard | DS-34 | shortest-path-visiting-all-nodes | — |
| LC-1125 | Smallest Sufficient Team | Hard | DS-34 | smallest-sufficient-team | — |
| LC-1434 | Number of Ways to Wear Different Hats to Each Other | Hard | DS-34 | number-of-ways-to-wear-different-hats-to-each-other | — |
| LC-357 | Count Numbers with Unique Digits | Medium | DS-34 | count-numbers-with-unique-digits | — |
| LC-902 | Numbers At Most N Given Digit Set | Hard | DS-34 | numbers-at-most-n-given-digit-set | — |
| LC-2246 | Longest Path With Different Adjacent Characters | Hard | DS-34 | longest-path-with-different-adjacent-characters | — |
| LC-1349 | Maximum Students Taking Exam | Hard | DS-34 | maximum-students-taking-exam | — |
| LC-2376 | Count Special Integers | Hard | DS-34 | count-special-integers | — |
| LC-191 | Number of 1 Bits | Easy | DS-35 | number-of-1-bits | — |
| LC-338 | Counting Bits | Easy | DS-35 | counting-bits | — |
| LC-190 | Reverse Bits | Easy | DS-35 | reverse-bits | — |
| LC-371 | Sum of Two Integers | Medium | DS-35 | sum-of-two-integers | — |
| LC-137 | Single Number II | Medium | DS-35 | single-number-ii | — |
| LC-260 | Single Number III | Medium | DS-35 | single-number-iii | — |
| LC-201 | Bitwise AND of Numbers Range | Medium | DS-35 | bitwise-and-of-numbers-range | — |
| LC-318 | Maximum Product of Word Lengths | Medium | DS-35 | maximum-product-of-word-lengths | — |
| LC-231 | Power of Two | Easy | DS-35 | power-of-two | — |
| LC-461 | Hamming Distance | Easy | DS-35 | hamming-distance | — |
| LC-477 | Total Hamming Distance | Medium | DS-35 | total-hamming-distance | — |
| LC-1318 | Minimum Flips to Make a OR b Equal to c | Medium | DS-35 | minimum-flips-to-make-a-or-b-equal-to-c | — |
| LC-204 | Count Primes | Medium | DS-36 | count-primes | — |
| LC-202 | Happy Number | Easy | DS-36 | happy-number | — |
| LC-1071 | Greatest Common Divisor of Strings | Easy | DS-36 | greatest-common-divisor-of-strings | — |
| LC-48 | Rotate Image | Medium | DS-36 | rotate-image | — |
| LC-54 | Spiral Matrix | Medium | DS-36 | spiral-matrix | — |
| LC-73 | Set Matrix Zeroes | Medium | DS-36 | set-matrix-zeroes | — |
| LC-43 | Multiply Strings | Medium | DS-36 | multiply-strings | — |
| LC-166 | Fraction to Recurring Decimal | Medium | DS-36 | fraction-to-recurring-decimal | — |
| LC-372 | Super Pow | Medium | DS-36 | super-pow | — |
| LC-528 | Random Pick with Weight | Medium | DS-36 | random-pick-with-weight | — |
| LC-2013 | Detect Squares | Medium | DS-36 | detect-squares | — |
| LC-149 | Max Points on a Line | Hard | DS-36 | max-points-on-a-line | — |
| LC-482 | License Key Formatting | Easy | DS-36 | license-key-formatting | — |
| LC-168 | Excel Sheet Column Title | Easy | DS-36 | excel-sheet-column-title | — |
| LC-1041 | Robot Bounded In Circle | Medium | DS-36 | robot-bounded-in-circle | — |
| LC-289 | Game of Life | Medium | DS-36 | game-of-life | — |
| LC-593 | Valid Square | Medium | DS-36 | valid-square | — |
| LC-68 | Text Justification | Hard | DS-36 | text-justification | — |
| LC-307 | Range Sum Query - Mutable | Medium | DS-37 | range-sum-query-mutable | — |
| LC-327 | Count of Range Sum | Hard | DS-37 | count-of-range-sum | — |
| LC-732 | My Calendar III | Hard | DS-37 | my-calendar-iii | — |
| LC-715 | Range Module | Hard | DS-37 | range-module | — |
| LC-699 | Falling Squares | Hard | DS-37 | falling-squares | — |
| LC-1649 | Create Sorted Array through Instructions | Hard | DS-37 | create-sorted-array-through-instructions | — |
| LC-2407 | Longest Increasing Subsequence II | Hard | DS-37 | longest-increasing-subsequence-ii | — |
| LC-2179 | Count Good Triplets in an Array | Hard | DS-37 | count-good-triplets-in-an-array | — |
| LC-28 | Find the Index of the First Occurrence in a String | Easy | DS-38 | find-the-index-of-the-first-occurrence-in-a-string | — |
| LC-459 | Repeated Substring Pattern | Easy | DS-38 | repeated-substring-pattern | — |
| LC-187 | Repeated DNA Sequences | Medium | DS-38 | repeated-dna-sequences | — |
| LC-214 | Shortest Palindrome | Hard | DS-38 | shortest-palindrome | — |
| LC-1392 | Longest Happy Prefix | Hard | DS-38 | longest-happy-prefix | — |
| LC-1044 | Longest Duplicate Substring | Hard | DS-38 | longest-duplicate-substring | — |
| LC-2223 | Sum of Scores of Built Strings | Hard | DS-38 | sum-of-scores-of-built-strings | — |
| LC-796 | Rotate String | Easy | DS-38 | rotate-string | — |
| LC-1408 | String Matching in an Array | Easy | DS-38 | string-matching-in-an-array | — |
| LC-1316 | Distinct Echo Substrings | Hard | DS-38 | distinct-echo-substrings | — |
| LC-1192 | Critical Connections in a Network | Hard | DS-39 | critical-connections-in-a-network | — |
| LC-332 | Reconstruct Itinerary | Hard | DS-39 | reconstruct-itinerary | — |
| LC-753 | Cracking the Safe | Hard | DS-39 | cracking-the-safe | — |
| LC-2097 | Valid Arrangement of Pairs | Hard | DS-39 | valid-arrangement-of-pairs | — |
| LC-1568 | Minimum Number of Days to Disconnect Island | Hard | DS-39 | minimum-number-of-days-to-disconnect-island | — |
| LC-84 | Largest Rectangle in Histogram | Hard | DS-40 | largest-rectangle-in-histogram | — |
| LC-85 | Maximal Rectangle | Hard | DS-40 | maximal-rectangle | — |
| LC-907 | Sum of Subarray Minimums | Medium | DS-40 | sum-of-subarray-minimums | — |
| LC-456 | 132 Pattern | Medium | DS-40 | 132-pattern | — |
| LC-853 | Car Fleet | Medium | DS-40 | car-fleet | — |
| LC-1944 | Number of Visible People in a Queue | Hard | DS-40 | number-of-visible-people-in-a-queue | — |
| LC-1425 | Constrained Subsequence Sum | Hard | DS-40 | constrained-subsequence-sum | — |
| LC-1499 | Max Value of Equation | Hard | DS-40 | max-value-of-equation | — |
| LC-1475 | Final Prices With a Special Discount in a Shop | Easy | DS-40 | final-prices-with-a-special-discount-in-a-shop | — |
| LC-962 | Maximum Width Ramp | Medium | DS-40 | maximum-width-ramp | — |
| LC-975 | Odd Even Jump | Hard | DS-40 | odd-even-jump | — |
| LC-1793 | Maximum Score of a Good Subarray | Hard | DS-40 | maximum-score-of-a-good-subarray | — |
| LC-359 | Logger Rate Limiter | Easy | DS-41 | logger-rate-limiter | https://www.lintcode.com/problem/3620/ |
| LC-362 | Design Hit Counter | Medium | DS-41 | design-hit-counter | https://www.lintcode.com/problem/3662/ |
| LC-146 | LRU Cache | Medium | DS-41 | lru-cache | — |
| LC-706 | Design HashMap | Easy | DS-41 | design-hashmap | — |
| LC-355 | Design Twitter | Medium | DS-41 | design-twitter | — |
| LC-341 | Flatten Nested List Iterator | Medium | DS-41 | flatten-nested-list-iterator | — |
| LC-281 | Zigzag Iterator | Medium | DS-41 | zigzag-iterator | https://www.lintcode.com/problem/540/ |
| LC-284 | Peeking Iterator | Medium | DS-41 | peeking-iterator | — |
| LC-1146 | Snapshot Array | Medium | DS-41 | snapshot-array | — |
| LC-460 | LFU Cache | Hard | DS-41 | lfu-cache | — |
| LC-432 | All O`one Data Structure | Hard | DS-41 | all-oone-data-structure | — |
| LC-1472 | Design Browser History | Medium | DS-41 | design-browser-history | — |
| LC-2034 | Stock Price Fluctuation  | Medium | DS-41 | stock-price-fluctuation | — |
| LC-2353 | Design a Food Rating System | Medium | DS-41 | design-a-food-rating-system | — |
| LC-705 | Design HashSet | Easy | DS-41 | design-hashset | — |
| LC-1396 | Design Underground System | Medium | DS-41 | design-underground-system | — |
| LC-1797 | Design Authentication Manager | Medium | DS-41 | design-authentication-manager | — |
| LC-895 | Maximum Frequency Stack | Hard | DS-41 | maximum-frequency-stack | — |
| LC-2502 | Design Memory Allocator | Medium | DS-41 | design-memory-allocator | — |
| LC-855 | Exam Room | Medium | DS-41 | exam-room | — |
