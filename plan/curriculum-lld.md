# LLD Curriculum — Object-Oriented Design in C++

**Weeks 39–44.** Google does not run a separate LLD round for L4 the way Amazon or Flipkart do,
but it asks object-oriented design *inside* coding rounds: "design a parking lot class", "now
make the rate limiter thread-safe", "extend your iterator to skip nulls". The interviewer is
checking that the classes have one job each, that the interfaces would survive the next
requirement, and that you can reason about concurrency. Six weeks is proportionate to that.

**Output of every case study:** a class diagram (hand-drawn is fine, photograph it or use
text), the interfaces in C++ headers, one class fully implemented, and a paragraph on what
changes when requirement N+1 arrives.

---

## Topics

| # | Topic | Week | Note file | Tag |
|---|-------|------|-----------|-----|
| LD-1 | Object-oriented programming in C++ — classes, encapsulation, inheritance, polymorphism, virtual functions, abstract classes and interfaces | 39 | `notes/lld/ld-01-oop-cpp.md` | design |
| LD-2 | SOLID principles — single responsibility, open closed, Liskov substitution, interface segregation, dependency inversion | 39 | `notes/lld/ld-02-solid.md` | design |
| LD-3 | Creational design patterns — factory method, abstract factory, builder, singleton | 40 | `notes/lld/ld-03-creational-patterns.md` | design |
| LD-4 | Structural design patterns — adapter, decorator, composite, facade, proxy | 41 | `notes/lld/ld-04-structural-patterns.md` | design |
| LD-5 | Behavioral design patterns — strategy, observer, command, state, iterator, chain of responsibility | 41 | `notes/lld/ld-05-behavioral-patterns.md` | design |
| LD-6 | UML for interviews — class diagram, sequence diagram, relationships (association, aggregation, composition) | 40 | `notes/lld/ld-06-uml.md` | design |
| LD-7 | Concurrency in C++ — threads, mutex, condition variable, producer consumer, deadlock, thread-safe singleton | 42 | `notes/lld/ld-07-concurrency.md` | concurrency |
| LD-8 | Parking lot design — spots, vehicles, tickets, pricing strategy | 42 | `notes/lld/ld-08-parking-lot.md` | design |
| LD-9 | Elevator system design — elevator controller, request scheduling, state machine | 43 | `notes/lld/ld-09-elevator.md` | design |
| LD-10 | Game design — tic tac toe, snake and ladder, board and player abstractions | 43 | `notes/lld/ld-10-games.md` | design |
| LD-11 | Splitwise expense sharing design — users, groups, expenses, split strategies, balance simplification | 43 | `notes/lld/ld-11-splitwise.md` | design |
| LD-12 | Movie ticket booking design — shows, seats, seat locking, booking flow | 44 | `notes/lld/ld-12-ticket-booking.md` | design |
| LD-13 | Rate limiter low level design — token bucket, sliding window log, thread safety | 44 | `notes/lld/ld-13-rate-limiter.md` | design |
| LD-14 | Vending machine and ATM design — state pattern, inventory, cash dispensing | 44 | `notes/lld/ld-14-vending-atm.md` | design |
| LD-15 | Logging framework and pub sub design — log levels, appenders, observer, message broker | 44 | `notes/lld/ld-15-logger-pubsub.md` | design |

---

## Ten-step approach to a fresh LLD question

1. Clarify scope: which actors, which use cases are in, which are out (5 min).
2. List nouns → candidate classes; verbs → methods.
3. Pick the core entities and their relationships (has-a vs is-a).
4. Draw the class diagram.
5. Define interfaces first, implementations after.
6. Name the pattern where one clearly fits — never force one.
7. Walk one use case end to end through the objects (sequence diagram in words).
8. Implement the most interesting class in real C++.
9. Concurrency: what is shared, what locks it, what can deadlock.
10. Extension: add requirement N+1 and show which classes change (ideally one).

## Anti-patterns Google interviewers flag

- God class (`ParkingLotManager` that does everything)
- Inheritance for code reuse where composition fits
- Getters and setters for every field (anaemic model)
- A singleton for anything that is not genuinely one-per-process
- Ignoring thread safety when the question says "many users"
