# Core Subjects Tracker

OS / DBMS / CN / OOP. Updated weekly.

---

## Operating Systems

| # | Topic | Note file | Studied | Notes written | Confident (1-5) | Last revisited |
|---|-------|-----------|---------|----------------|------------------|-----------------|
| 1 | Intro + OS structures | `os-01-intro.md` | no | no | 1 | — |
| 2 | Process vs Thread, PCB, context switch | `os-02-process-thread.md` | no | no | 1 | — |
| 3 | CPU scheduling (FCFS, SJF, RR, MLFQ) | `os-03-scheduling.md` | no | no | 1 | — |
| 4 | Synchronization (mutex, semaphore, monitors) | `os-04-sync.md` | no | no | 1 | — |
| 5 | Classic sync problems | `os-05-classic-sync.md` | no | no | 1 | — |
| 6 | Deadlocks (4 conditions, Banker's) | `os-06-deadlocks.md` | no | no | 1 | — |
| 7 | Memory management | `os-07-memory.md` | no | no | 1 | — |
| 8 | Virtual memory, paging, page replacement | `os-08-virtual-memory.md` | no | no | 1 | — |
| 9 | File systems, inodes | `os-09-filesystems.md` | no | no | 1 | — |
| 10 | I/O + disk scheduling | `os-10-io-disk.md` | no | no | 1 | — |

---

## DBMS

| # | Topic | Note file | Studied | Notes written | Confident (1-5) | Last revisited |
|---|-------|-----------|---------|----------------|------------------|-----------------|
| 1 | Intro to DBMS | `dbms-01-intro.md` | no | no | 1 | — |
| 2 | ER model, ER diagrams | `dbms-02-er.md` | no | no | 1 | — |
| 3 | Relational model, keys | `dbms-03-relational.md` | no | no | 1 | — |
| 4 | SQL basics + DDL/DML/DCL/TCL | `dbms-04-sql.md` | no | no | 1 | — |
| 5 | Joins | `dbms-05-joins.md` | no | no | 1 | — |
| 6 | Normalization (1NF–BCNF) | `dbms-06-normalization.md` | no | no | 1 | — |
| 7 | Indexes (B-tree vs Hash, clustered) | `dbms-07-indexes.md` | no | no | 1 | — |
| 8 | Transactions + ACID | `dbms-08-acid.md` | no | no | 1 | — |
| 9 | Isolation levels + anomalies | `dbms-09-isolation.md` | no | no | 1 | — |
| 10 | NoSQL types + when to use | `dbms-10-nosql.md` | no | no | 1 | — |

### SQL Practice
- LeetCode SQL 50 completed: 0 / 50
- SQLZoo modules completed: 0 / 9

---

## Computer Networks

(Head start — you use gRPC + mTLS + HAProxy daily)

| # | Topic | Note file | Studied | Notes written | Confident (1-5) | Last revisited |
|---|-------|-----------|---------|----------------|------------------|-----------------|
| 1 | OSI / TCP-IP layers | `cn-01-layers.md` | no | no | 2 | — |
| 2 | HTTP — request, response, status, methods | `cn-02-http.md` | no | no | 3 | — |
| 3 | TCP vs UDP, handshake, congestion | `cn-03-tcp-udp.md` | no | no | 2 | — |
| 4 | DNS (recursive vs iterative, anycast, geo-DNS) | `cn-04-dns.md` | no | no | 2 | — |
| 5 | HTTPS / TLS handshake (mTLS — your strength!) | `cn-05-tls.md` | no | no | 3 | — |
| 6 | Load balancers + proxies | `cn-06-lb-proxy.md` | no | no | 3 | — |
| 7 | HTTP/2 multiplexing, HTTP/3 (QUIC) | `cn-07-http2-3.md` | no | no | 1 | — |
| 8 | WebSocket vs SSE vs Long Poll | `cn-08-websocket.md` | no | no | 1 | — |

---

## OOP

| # | Topic | Note file | Studied | Notes written | Confident (1-5) | Last revisited |
|---|-------|-----------|---------|----------------|------------------|-----------------|
| 1 | 4 pillars | `oop-01-pillars.md` | no | no | 3 | — |
| 2 | Composition vs inheritance | `oop-02-composition.md` | no | no | 2 | — |
| 3 | Abstract classes vs interfaces (C++) | `oop-03-abstract-vs-interface.md` | no | no | 2 | — |
| 4 | Virtual functions + vtable | `oop-04-virtual.md` | no | no | 2 | — |
| 5 | C++ special member functions (move/copy) | `oop-05-cpp-special.md` | no | no | 2 | — |
| 6 | Diamond problem + virtual inheritance | `oop-06-diamond.md` | no | no | 1 | — |

---

## Interviewer-Favorite Questions Drill

Mark "rehearsed" when you can explain it cleanly out loud in <60 sec.

### OS
- [ ] Process vs thread — concrete example
- [ ] How does paging work? Walk through a memory access
- [ ] What happens on a page fault?
- [ ] Producer-consumer with a single mutex — what's wrong?
- [ ] Deadlock conditions + how to break each

### DBMS
- [ ] SQL vs NoSQL — when to pick which
- [ ] ACID with concrete bank-transfer example
- [ ] Read Committed vs Serializable trade-off
- [ ] Index on a high-cardinality vs low-cardinality column
- [ ] B-tree index lookup walkthrough

### CN
- [ ] What happens when I type google.com and press enter
- [ ] TCP vs UDP — when UDP?
- [ ] TLS handshake walkthrough
- [ ] HTTPS MITM protection
- [ ] HTTP/2 multiplexing benefit
- [ ] WebSocket vs polling

### OOP
- [ ] Polymorphism with real example
- [ ] Composition over inheritance — why?
- [ ] Diamond problem
- [ ] vtable
- [ ] Abstract classes — why use them?
