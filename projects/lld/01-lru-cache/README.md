# 01 — LRU Cache library (Week 39)

**Topics:** LD-1 OOP in C++, LD-2 SOLID · **Related problem:** LC-146 LRU Cache

A generic `LRUCache<K, V>` with O(1) `get` and `put`, eviction when full, and an eviction
listener. Small on purpose: the point of week 39 is writing a class an interviewer would call
clean — a narrow public interface, invariants that hold after every call, no leaks.

## Requirements (what the tests check)

1. `LRUCache(0)` throws `std::invalid_argument`.
2. `get` returns the value and makes the key most recently used; absent → `std::nullopt`.
3. `put` inserts or overwrites; overwriting is a use. A full cache evicts its least recently
   used entry before inserting a new key.
4. `contains` does **not** change recency. `erase` removes without notifying listeners.
5. Every eviction calls each registered listener with the evicted key and value.
6. Behaves exactly like a naive reference model over 20,000 random operations.
7. A million operations finish in well under five seconds — every operation O(1).

## Build

```bash
make test      # 0/8 until you implement src/lru_cache.h
```

## Design checklist

- [ ] Class diagram in your LD-1 note: which member owns the recency order, which the lookup
- [ ] Every public method documented with its complexity
- [ ] No raw `new`/`delete`
- [ ] The listener cannot corrupt the cache (what if it calls `put` from inside the callback?)

## Extension (after green)

1. **TTL.** Entries expire `ttl` after their last write. Inject the clock
   (`std::function<Clock::time_point()>`) so tests stay deterministic.
2. **Thread safety.** Wrap with a mutex; then shard into 16 independent caches by
   `hash(key) % 16` and measure the throughput difference with 8 threads.
3. Write three lines: what you would change, what an interviewer would push on, time taken.
