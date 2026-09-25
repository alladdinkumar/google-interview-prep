# LLD Curriculum — OOP, Design Patterns, Machine Coding

**Total LLD problems:** 8-10 across Weeks 15-17 (Phase 3).
**Coding language:** C++ (alternative: Python if cleaner for the problem).
**Goal:** SOLID becomes reflexive. You can map a problem to its dominant design pattern in <2 min.

---

## Foundation (Week 15)

### SOLID Principles
- **S** ingle Responsibility — one reason to change
- **O** pen/Closed — open for extension, closed for modification
- **L** iskov Substitution — derived classes substitutable for base
- **I** nterface Segregation — many small interfaces > one fat one
- **D** ependency Inversion — depend on abstractions, not concretions

Note file: `notes/lld/solid.md` with one C++ example per principle (good and bad).

### Top 10 Design Patterns

| # | Pattern | Category | Note file | When to use |
|---|---------|----------|-----------|-------------|
| 1 | Strategy | Behavioral | `strategy.md` | Switch algorithms at runtime (e.g., payment processors) |
| 2 | Factory | Creational | `factory.md` | Create objects without specifying exact class (Logger types) |
| 3 | Abstract Factory | Creational | `abstract-factory.md` | Families of related objects (UI themes) |
| 4 | Singleton | Creational | `singleton.md` | Single shared instance (config, logger) — **thread-safe variant only!** |
| 5 | Observer | Behavioral | `observer.md` | Pub-sub, event listeners (notifications) |
| 6 | Decorator | Structural | `decorator.md` | Add behaviors dynamically (pizza toppings, stream filters) |
| 7 | Adapter | Structural | `adapter.md` | Make incompatible interfaces work together |
| 8 | Command | Behavioral | `command.md` | Encapsulate request as object (undo/redo) |
| 9 | State | Behavioral | `state.md` | Behavior changes with internal state (ATM, vending machine) |
| 10 | Template Method | Behavioral | `template-method.md` | Skeleton in base, steps overridden in derived |

**Bonus (encountered in problems, learn on the fly):** Builder (StringBuilder-style), Iterator, Chain of Responsibility, Composite, Proxy, Facade, Flyweight.

Resource: https://refactoring.guru/design-patterns (best free site). Browse one pattern at a time, read the intent + C++ example.

---

## 8 Core LLD Problems (Weeks 15-17)

For each, deliverable in `notes/lld/<slug>.md` is:
1. Requirements list (functional + non-functional)
2. Entities / classes (UML-style box list)
3. Relationships (composition, inheritance, association)
4. Sequence diagram for 1 core flow
5. SOLID violations avoided (explicit list)
6. Design patterns applied
7. Code (C++ headers + key method bodies; doesn't have to be complete)

| # | Problem | Slug | Patterns to apply | Week |
|---|---------|------|-------------------|------|
| 1 | Parking Lot | `parking-lot.md` | Strategy (parking spot allocation), Factory (Vehicle), Singleton (ParkingLot manager) | 15 |
| 2 | Splitwise | `splitwise.md` | Observer (notify users), Strategy (split equally/unequally/percentage) | 16 |
| 3 | Snake & Ladder | `snake-ladder.md` | Template Method (turn flow), State (game state) | 16 |
| 4 | LRU Cache | `lru-cache.md` | Composite (DLL + HashMap), no specific pattern but interface clean | 16 |
| 5 | LFU Cache | `lfu-cache.md` | Same as LRU + frequency tracking | 16 |
| 6 | ATM | `atm.md` | State (states: idle, authenticated, dispensing, transaction), Chain of Responsibility (cash dispenser) | 17 |
| 7 | Logger / Logging Framework | `logger.md` | Singleton (Logger), Strategy (Console/File/Network handlers), Chain of Responsibility (log levels) | 17 |
| 8 | Tic-Tac-Toe (N×N generalization) | `tic-tac-toe.md` | Strategy (win-check), State (game phases) | 17 |

### Stretch (Sat Week 17 buffer)
| # | Problem | Slug | Patterns |
|---|---------|------|----------|
| 9 | Movie Ticket Booking | `bookmyshow.md` | Observer (notifications), Strategy (seat allocation), seat-locking concurrency |
| 10 | Vending Machine | `vending-machine.md` | State (idle → selected → paid → dispensing → idle), Strategy (payment) |
| 11 | Elevator System | `elevator.md` | Strategy (elevator selection algorithm), State (moving/idle/maintenance) |
| 12 | Chess | `chess.md` | Strategy (move validation per piece), Iterator (piece collection) |

Pick **one** stretch problem if you finish core 8 ahead. Don't try to do all 12.

---

## How to Approach a Fresh LLD Problem (10-step framework)

1. **Clarify requirements** (3-5 min). Functional ("what does it do") + non-functional ("concurrent? scale? persistence?"). Ask explicitly.
2. **List entities / objects.** Just nouns. Don't worry about methods yet.
3. **Group entities into classes.** Identify "is-a" (inheritance) vs "has-a" (composition).
4. **Add methods.** What does each class *do*? Don't expose internal state.
5. **Identify the dominant design pattern.** What's the most variable axis? That's usually Strategy. What's created in multiple ways? Factory. Etc.
6. **Apply SOLID.** Each class one responsibility. Open for extension where future variation likely.
7. **Draw class diagram.** (Box + arrows. ASCII is fine. Excalidraw better.)
8. **Walk through 1 core flow** — sequence diagram in words: "User does X → calls Y → Z."
9. **Handle concurrency** (if non-functional asks for it). Where's the shared state? What's the locking strategy?
10. **Code skeletons.** Headers + 1-2 critical methods. Interviewer rarely needs full implementation.

---

## Common Anti-Patterns to Avoid

- **God class** — one class doing 5 things. Smell it, split it.
- **Public mutable state** — exposes internals. Use accessors or, better, immutable objects.
- **Concrete dependencies** — `new ConcreteThing()` instead of `IThing`. Inject instead.
- **Magic numbers / strings** — make them constants or enums.
- **Forgetting concurrency** — if interviewer says "multiple users," and your design has no locks, that's a fail.
- **Singleton everywhere** — Singleton is a code smell when overused. Use it for genuinely-global things only (config, logger).

---

## Resources

| Resource | Type | URL |
|----------|------|-----|
| Refactoring Guru — Design Patterns | Text | https://refactoring.guru/design-patterns |
| Concept&&Coding LLD playlist | Video | https://www.youtube.com/@ConceptandCoding |
| Soumyajit Bhattacharya (Coding Soumya) LLD | Video | https://www.youtube.com/c/CodingSoumya |
| Gaurav Sen LLD videos | Video | https://www.youtube.com/@gkcs |
| Coding Decoded LLD (some) | Video | YouTube search |
| LLD interview github repos | Code | Search github "low-level-design" |

---

## Tracking

`trackers/lld.md` has one row per LLD problem:

| Problem | Notes file | Diagram drawn | SOLID applied | Patterns identified | Code skeleton | Confident (1-5) |
|---------|------------|---------------|---------------|---------------------|---------------|-----------------|
| Parking Lot | parking-lot.md | y | y | Strategy, Factory, Singleton | partial | 3 |
| ... | | | | | | |

You re-rate confidence weekly. Anything <3 stays in `trackers/weak-areas.md` until re-done.
