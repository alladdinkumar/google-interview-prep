# Phase 3 — Advanced DSA + LLD Start (Weeks 13–17)

**Dates:** 2026-08-10 → 2026-09-13 (5 weeks)
**Budget:** ~95 hours (19h/week)
**Theme:** Cover hard-tier DSA topics. Start LLD fundamentals. **Mocks begin Week 15.**

---

## Phase Goals

- [ ] 25 more DSA problems (focus on harder patterns)
- [ ] Tries + advanced strings + advanced DP + segment trees covered
- [ ] 8 LLD problems coded end-to-end
- [ ] SOLID + 10 design patterns understood and articulable
- [ ] 3 mocks done (Weeks 15, 16, 17)
- [ ] Networking notes done (TCP/IP, HTTP, DNS, TLS — leverage gRPC/mTLS work)

---

## Weekly Breakdown

### Week 13 — Tries + Advanced Strings
**Problems: 12** | **Hours: 19**

Trie operations (insert, search, prefix). Trie applications (autocomplete, word search II).

Advanced string: KMP algorithm (longest proper prefix-suffix), Rabin-Karp (rolling hash), Z-algorithm.

- AM: 2-3 trie/string problems/day
- PM Mon: Trie implementation in C++ (`notes/dsa/trie.md`)
- PM Tue: KMP derivation (`notes/dsa/kmp.md`)
- PM Wed: CN — HTTPS/TLS handshake (use existing mTLS knowledge!)
- PM Thu: CN — load balancers (L4 vs L7), proxies (forward vs reverse)
- PM Fri: revision
- Sat: 1 hard — Word Search II (Trie + DFS)
- Sun: weekly review

---

### Week 14 — Segment Trees + Fenwick + Advanced DP
**Problems: 12** | **Hours: 19**

Segment tree (point update, range query, lazy propagation light). Fenwick tree (BIT). Advanced DP: tree DP (LIS on tree, House Robber III), digit DP (count numbers with property), bitmask DP (TSP light, Partition to K Subsets).

- AM: 2-3 problems/day
- PM Mon: Segment tree template (`notes/dsa/segment-tree.md`)
- PM Tue: BIT template (`notes/dsa/fenwick.md`)
- PM Wed: tree DP (`notes/dsa/tree-dp.md`)
- PM Thu: bitmask DP (`notes/dsa/bitmask-dp.md`)
- PM Fri: revision
- Sat: 1 hard segment tree problem (Range Sum Query - Mutable)
- Sun: weekly review

---

### Week 15 — LLD: OOP + SOLID + Top 10 Design Patterns
**Problems: 1 LLD (Parking Lot)** | **Hours: 19** | **🎯 Mock #1**

LLD foundations week. **No DSA quota — this week is OOP / patterns / SOLID.**

- AM Mon: SOLID principles deep dive (`notes/lld/solid.md`)
- AM Tue: Strategy + Factory patterns (`notes/lld/strategy.md`, `notes/lld/factory.md`)
- AM Wed: Singleton (thread-safe!) + Observer (`notes/lld/singleton.md`, `notes/lld/observer.md`)
- AM Thu: Decorator + Adapter (`notes/lld/decorator.md`, `notes/lld/adapter.md`)
- AM Fri: Command + State + Template Method (3 notes files)
- PM each day: code patterns in C++ (small reference snippets in notes)
- **Saturday: LLD problem #1 — Parking Lot.** Design classes, draw class diagram, code core flows. (`notes/lld/parking-lot.md`)
- **Sat afternoon (last 30 min): Mock #1** — schedule with Pramp or peer. Coding round level. Log to `trackers/mocks.md`.
- Sun: weekly review

Resource: Concept&&Coding LLD playlist — https://www.youtube.com/@ConceptandCoding ; Refactoring Guru patterns — https://refactoring.guru/design-patterns

---

### Week 16 — LLD Case Studies: Splitwise, Snake & Ladder, LRU/LFU Cache
**Problems: 3 LLD** | **Hours: 19** | **🎯 Mock #2**

- AM Mon: Splitwise design (`notes/lld/splitwise.md`) — entities (User, Group, Expense, Balance), settle algorithm
- AM Tue: Splitwise coding (in C++, core classes)
- AM Wed: Snake & Ladder (`notes/lld/snake-ladder.md`) — entities (Board, Die, Player, Game), turn loop
- AM Thu: LRU cache (`notes/lld/lru-cache.md`) — DLL + hashmap, then code in C++
- AM Fri: LFU cache (`notes/lld/lfu-cache.md`)
- PM each day: design patterns review + code completion
- Sat: extend LRU to thread-safe LRU (use std::mutex / shared_mutex) + **Mock #2**
- Sun: weekly review

---

### Week 17 — LLD Case Studies: ATM, Logger, Tic-Tac-Toe, BookMyShow
**Problems: 4 LLD** | **Hours: 19** | **🎯 Mock #3**

- AM Mon: ATM design + state pattern (`notes/lld/atm.md`)
- AM Tue: Logging framework — observer + strategy (`notes/lld/logger.md`)
- AM Wed: Tic-Tac-Toe + extension to N×N (`notes/lld/tic-tac-toe.md`)
- AM Thu: BookMyShow / Movie ticket booking — concurrency for seat-locking (`notes/lld/bookmyshow.md`)
- AM Fri: catch-up day + redo any incomplete LLD
- PM each day: revision of design patterns + dry-running concurrent scenarios
- Sat: pick one of {Vending Machine, Elevator, Chess} and code it + **Mock #3**
- Sun: **Weekly + Phase 3 retrospective**

---

## Phase-3 Exit Criteria

Before Phase 4 (Mon 2026-09-14):

- [ ] 25 advanced DSA problems done
- [ ] 8 LLD problems coded with class diagrams in notes
- [ ] SOLID + 10 design patterns articulable with use cases
- [ ] Networking notes (TCP/HTTP/TLS/DNS) filed
- [ ] 3 mocks done with feedback logged in `trackers/mocks.md`
- [ ] Adherence ≥65%

---

## Mock Interview Setup

Starting Week 15, every Saturday afternoon you do 1 mock interview.

**Where to find mocks (free options):**
- **Pramp** (https://www.pramp.com) — free peer mocks, schedule slot
- **Interviewing.io** — free credits for first mock with FAANG engineers
- **Find a buddy:** post on r/leetcode or r/cscareerquestions for a study partner
- **DSA-coach.com** or **Exponent** — sometimes have free trials

**Mock rotation across 12 mocks (Weeks 15-26):**
- Coding mocks: 6 total (Weeks 15, 16, 17, 19, 21, 24)
- HLD mocks: 4 total (Weeks 18, 20, 22, 25)
- LLD mocks: 1 total (Week 23)
- Behavioral mock: 1 total (Week 26)

After each mock, fill in `trackers/mocks.md` with score (1-10), top 3 weaknesses, action items.
