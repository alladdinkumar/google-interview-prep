# Core Subjects Curriculum — OS, DBMS, CN, OOP

These get sprinkled into evening sessions and PM slots throughout Phases 1-3. They're not the main event — but Indian product cos (Atlassian, Razorpay, Flipkart) and Microsoft love asking them. Google asks them less but they show up in coding round trivia.

**Time budget:** ~2-3 hours/week during Phases 1-3 (mostly PM Wed/Thu slots). ~40 hours total.

---

## Operating Systems (Phases 1-2)

### Topics

| # | Topic | When | Note file | Resource |
|---|-------|------|-----------|----------|
| 1 | Intro, OS structures, monolithic vs microkernel | Week 1 | `notes/core/os-01-intro.md` | Galvin Ch 1-2 / Neso Academy |
| 2 | Process vs thread, PCB, context switching | Week 1 | `notes/core/os-02-process-thread.md` | Galvin Ch 3 / GFG |
| 3 | CPU scheduling (FCFS, SJF, RR, Priority, MLFQ) | Week 1 | `notes/core/os-03-scheduling.md` | Galvin Ch 5 |
| 4 | Synchronization (mutex, semaphore, monitors, condition variables) | Week 2 | `notes/core/os-04-sync.md` | Galvin Ch 6 |
| 5 | Classic problems (producer-consumer, readers-writers, dining philosophers) | Week 2 | `notes/core/os-05-classic-sync.md` | Galvin Ch 6 |
| 6 | Deadlocks (4 conditions, prevention/avoidance/detection/recovery, Banker's algo) | Week 2 | `notes/core/os-06-deadlocks.md` | Galvin Ch 7 |
| 7 | Memory management (contiguous, paging, segmentation) | Week 4 | `notes/core/os-07-memory.md` | Galvin Ch 8 |
| 8 | Virtual memory (paging, page table, TLB, page replacement: FIFO/LRU/Optimal/LFU) | Week 6 | `notes/core/os-08-virtual-memory.md` | Galvin Ch 9 |
| 9 | File systems (inodes, allocation methods, directory structure) | Week 8 | `notes/core/os-09-filesystems.md` | Galvin Ch 10-11 |
| 10 | I/O systems, disk scheduling (FCFS, SSTF, SCAN, C-SCAN, LOOK) | Week 10 | `notes/core/os-10-io-disk.md` | Galvin Ch 12 |

**Interview-favorite questions** (rehearse the explanation, don't just read):
- "Process vs thread — give me a concrete example where you'd use which."
- "How does paging work? Walk me through a memory access."
- "Producer-consumer with a single mutex — what's wrong with it?"
- "Deadlock conditions and how to break each one."
- "What happens on a page fault?"

**Resources (free):**
- Neso Academy OS playlist — https://www.youtube.com/playlist?list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O
- Galvin OS textbook (free PDF available)
- GFG OS quiz section

---

## DBMS (Phase 2, Week 7-10)

### Topics

| # | Topic | When | Note file | Resource |
|---|-------|------|-----------|----------|
| 1 | Intro to DBMS, DBMS vs file system | Wk 7 | `notes/core/dbms-01-intro.md` | Korth Ch 1 |
| 2 | ER model, ER diagrams, cardinality | Wk 7 | `notes/core/dbms-02-er.md` | Korth Ch 7 |
| 3 | Relational model, keys (primary/candidate/foreign) | Wk 7 | `notes/core/dbms-03-relational.md` | Korth Ch 2 |
| 4 | SQL basics — DDL, DML, DCL, TCL | Wk 8 | `notes/core/dbms-04-sql.md` | SQLZoo (interactive practice) |
| 5 | Joins (inner, left, right, full, self, cross) | Wk 8 | `notes/core/dbms-05-joins.md` | SQLZoo |
| 6 | Normalization (1NF, 2NF, 3NF, BCNF, 4NF) | Wk 8 | `notes/core/dbms-06-normalization.md` | Korth Ch 8 |
| 7 | Indexes — B-tree vs Hash, clustered vs non-clustered, when to index | Wk 8 | `notes/core/dbms-07-indexes.md` | GFG |
| 8 | Transactions + ACID | Wk 9 | `notes/core/dbms-08-acid.md` | Korth Ch 14 |
| 9 | Isolation levels (Read Uncommitted, Read Committed, Repeatable Read, Serializable) + anomalies | Wk 9 | `notes/core/dbms-09-isolation.md` | GFG / use case in interviews |
| 10 | NoSQL — Document (Mongo), Key-Value (Redis), Column (Cassandra), Graph (Neo4j); when to pick which | Wk 10 | `notes/core/dbms-10-nosql.md` | ByteByteGo |

**Interview-favorite questions:**
- "Difference between SQL and NoSQL — when would you pick each?"
- "Explain ACID with a concrete bank-transfer example."
- "What's the trade-off between Read Committed and Serializable?"
- "What happens to an index on a column with many duplicate values?"
- "Walk me through how a B-tree index lookup works."

**Resources:**
- Korth DBMS textbook (free PDF)
- Gate Smashers DBMS playlist — https://www.youtube.com/@GateSmashers
- SQLZoo for practice — https://sqlzoo.net
- Free LeetCode SQL problems (50 problems)

---

## Computer Networks (Phase 2-3, Week 11-13)

You have a head start here — gRPC, mTLS, HAProxy, K8s networking are all in your day job. Focus on the **vocabulary and theory** to articulate what you already do.

### Topics

| # | Topic | When | Note file | Notes |
|---|-------|------|-----------|-------|
| 1 | OSI / TCP-IP model layers | Wk 11 | `notes/core/cn-01-layers.md` | One-paragraph each layer |
| 2 | HTTP/1.1 request-response, status codes, methods | Wk 11 | `notes/core/cn-02-http.md` | You know this; just write it down |
| 3 | TCP vs UDP, handshake, congestion control overview | Wk 11 | `notes/core/cn-03-tcp-udp.md` | Galvin / Tanenbaum |
| 4 | DNS — how it works, recursive vs iterative, anycast, geo-DNS | Wk 11 | `notes/core/cn-04-dns.md` | ByteByteGo DNS |
| 5 | HTTPS / TLS handshake (you know mTLS — use that!) | Wk 13 | `notes/core/cn-05-tls.md` | Cloudflare blog explainer |
| 6 | Load balancers, proxies (forward vs reverse) | Wk 13 | `notes/core/cn-06-lb-proxy.md` | overlaps with HLD week 18 |
| 7 | HTTP/2 multiplexing, HTTP/3 (QUIC) | Wk 13 | `notes/core/cn-07-http2-3.md` | Cloudflare blog |
| 8 | WebSocket vs SSE vs Long Poll | Wk 13 | `notes/core/cn-08-websocket.md` | Hello Interview video |

**Interview-favorite questions:**
- "What happens when I type google.com and press enter?" (the classic — walk through it)
- "Difference between TCP and UDP — when would you use UDP?"
- "Walk me through the TLS handshake."
- "How does HTTPS protect against MITM?"
- "What's HTTP/2's multiplexing solving?"
- "When would you choose WebSocket over polling?"

**Resources:**
- Cloudflare Learning Center — https://www.cloudflare.com/learning/
- Computerphile videos
- Tanenbaum Computer Networks (reference, don't read end-to-end)
- ByteByteGo videos for visual

---

## OOP (Phase 1 Week 3, ongoing)

This is mostly refresh. You use OOP daily, just need to articulate.

### Topics

| # | Topic | Note file |
|---|-------|-----------|
| 1 | 4 pillars: encapsulation, abstraction, inheritance, polymorphism | `notes/core/oop-01-pillars.md` |
| 2 | Composition vs inheritance ("favor composition") | `notes/core/oop-02-composition.md` |
| 3 | Abstract classes vs interfaces (in C++ context) | `notes/core/oop-03-abstract-vs-interface.md` |
| 4 | Virtual functions, vtable, runtime polymorphism in C++ | `notes/core/oop-04-virtual.md` |
| 5 | Constructor types, copy semantics, move semantics in C++ | `notes/core/oop-05-cpp-special.md` |
| 6 | Diamond problem + virtual inheritance | `notes/core/oop-06-diamond.md` |

**Interview-favorite questions:**
- "What's polymorphism — give a real example?"
- "When would you prefer composition over inheritance?"
- "What's the diamond problem and how does C++ solve it?"
- "What's a vtable?"
- "Why use abstract classes?"

---

## Tracking

`trackers/core-subjects.md` is a simple checklist:

```
## OS
- [ ] 01 Intro
- [ ] 02 Process vs Thread
...

## DBMS
- [ ] 01 Intro
...

## CN
- [ ] 01 Layers
...

## OOP
- [ ] 01 Pillars
...
```

Plus a "Last revisited" date per topic. Spaced-repetition: anything not revisited in 21+ days gets flagged for a 15-min refresh.
