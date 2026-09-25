# LLD Tracker

Low-level design / OOD / machine coding progress. Updated weekly during Phase 3.

---

## Foundations (Week 15)

### SOLID
| Principle | Note written | Examples coded | Confident (1-5) |
|-----------|--------------|----------------|------------------|
| S — Single Responsibility | no | 0 | 1 |
| O — Open/Closed | no | 0 | 1 |
| L — Liskov Substitution | no | 0 | 1 |
| I — Interface Segregation | no | 0 | 1 |
| D — Dependency Inversion | no | 0 | 1 |

### Top 10 Design Patterns

| # | Pattern | Category | Note written | C++ example coded | Confident (1-5) | Last revisited |
|---|---------|----------|--------------|---------------------|------------------|-----------------|
| 1 | Strategy | Behavioral | no | no | 1 | — |
| 2 | Factory | Creational | no | no | 1 | — |
| 3 | Abstract Factory | Creational | no | no | 1 | — |
| 4 | Singleton (thread-safe) | Creational | no | no | 1 | — |
| 5 | Observer | Behavioral | no | no | 1 | — |
| 6 | Decorator | Structural | no | no | 1 | — |
| 7 | Adapter | Structural | no | no | 1 | — |
| 8 | Command | Behavioral | no | no | 1 | — |
| 9 | State | Behavioral | no | no | 1 | — |
| 10 | Template Method | Behavioral | no | no | 1 | — |

---

## Core LLD Problems (8 — Phase 3)

For each, "done" = class diagram + SOLID applied + patterns identified + at least skeleton code.

| # | Problem | Slug | Wk | Diagram | SOLID | Patterns | Code | Concurrency considered | Confident (1-5) |
|---|---------|------|----|---------|-------|----------|------|------------------------|------------------|
| 1 | Parking Lot | `parking-lot.md` | 15 | no | no | — | no | n/a | 1 |
| 2 | Splitwise | `splitwise.md` | 16 | no | no | — | no | n/a | 1 |
| 3 | Snake & Ladder | `snake-ladder.md` | 16 | no | no | — | no | n/a | 1 |
| 4 | LRU Cache | `lru-cache.md` | 16 | no | no | — | no | yes/no | 1 |
| 5 | LFU Cache | `lfu-cache.md` | 16 | no | no | — | no | yes/no | 1 |
| 6 | ATM | `atm.md` | 17 | no | no | — | no | n/a | 1 |
| 7 | Logger | `logger.md` | 17 | no | no | — | no | yes/no | 1 |
| 8 | Tic-Tac-Toe (N×N) | `tic-tac-toe.md` | 17 | no | no | — | no | n/a | 1 |

---

## Stretch LLD Problems (only if ahead)

| # | Problem | Slug | Done | Confident |
|---|---------|------|------|-----------|
| 9 | BookMyShow / Movie booking | `bookmyshow-lld.md` | no | 1 |
| 10 | Vending Machine | `vending-machine.md` | no | 1 |
| 11 | Elevator | `elevator.md` | no | 1 |
| 12 | Chess | `chess.md` | no | 1 |

---

## Mock LLD Performance

| Mock # | Date | Problem | Time to working design | Code quality | Score (1-10) |
|--------|------|---------|------------------------|--------------|--------------|
| (none yet) | — | — | — | — | — |

---

## Self-Assessment

End of Phase 3, can I do this without thinking?

- [ ] Recognize dominant design pattern in <2 min on a fresh problem
- [ ] Draw class diagram in 5-7 min
- [ ] Identify SOLID violations in someone else's design
- [ ] Code a thread-safe Singleton from memory
- [ ] Code an LRU cache from memory
- [ ] Apply Strategy pattern without effort
- [ ] Identify concurrency hotspots and choose locking strategy
