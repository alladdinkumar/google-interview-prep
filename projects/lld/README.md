# LLD Projects — designs that compile, run and are tested

The six Saturday projects of Weeks 39–44. Each one is a small C++17 library with the
**interface already written** and every method a stub that throws `not implemented`. The
tests compile and run from day one and report `0/N passed`; you implement until they are all
green, then do the extension in the project's README.

This is the difference between reading about the observer pattern and having written one that
survives eight threads.

| Week | Project | Patterns and skills | Tests |
|------|---------|---------------------|-------|
| 39 | [`01-lru-cache`](01-lru-cache/) | Templates, RAII, interface design, eviction listener (observer) | 8 |
| 40 | [`02-notification-service`](02-notification-service/) | Factory, builder, strategy (retry), observer (delivery events) | 8 |
| 41 | [`03-text-editor`](03-text-editor/) | Command (undo/redo), decorator (rendering) | 8 |
| 42 | [`04-parking-lot`](04-parking-lot/) | Strategy (allocation, pricing), thread safety with a mutex | 8 |
| 43 | [`05-splitwise`](05-splitwise/) | Strategy (splits), integer money, debt simplification (greedy + heaps) | 8 |
| 44 | [`06-ticket-booking`](06-ticket-booking/) | Seat holds with expiry, concurrency: exactly one winner per seat | 8 |

## Running one

```bash
cd projects/lld/01-lru-cache
make test
```

**Compiler.** C++17 with `std::thread`: g++ 9+ or clang 10+. On Windows install MSYS2 and
`pacman -S mingw-w64-ucrt-x86_64-gcc make`, or use WSL. The MinGW.org g++ 6.3 that is on
this machine today is too old (no `std::thread`, partial C++17).

**CI.** `.github/workflows/projects.yml` builds every project on each push to `projects/` with
g++ 13 on Ubuntu and prints each score. A project that does not compile fails the run; failing
tests do not, because unimplemented stubs are the starting state.

## Rules

- Do not edit `tests.cpp` to make a test pass. Add tests, never remove them.
- Keep the public interface in `src/*.h`; add private helpers freely.
- When all tests pass, write three lines at the bottom of the README: what you would change,
  what an interviewer would push on, how long it took.
