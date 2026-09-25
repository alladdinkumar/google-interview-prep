# 04 — Parking Lot, thread-safe (Week 42)

**Topics:** LD-7 concurrency in C++, LD-8 parking lot design

The most-asked LLD question, taken one step past the whiteboard: it has to be correct when eight
gates park cars at the same moment.

## Requirements (what the tests check)

1. Fitting: motorcycles fit any spot (smallest first), cars Medium/Large, trucks Large only.
2. Pricing: first 15 minutes free, then per **started** hour — motorcycle ₹20, car ₹50, truck ₹100 (in paise).
3. Allocation: smallest fitting size, then lowest floor, then lowest index.
4. A full lot, or a plate that is already inside, gets `nullopt`.
5. `unpark` returns the fee and frees the spot; unknown, reused or time-travelling tickets throw.
6. Ticket ids are unique and increasing.
7. 8 threads × 100 cars into 400 spots: exactly 400 park, no spot is handed out twice.

## Build

```bash
make test
```

## Design checklist

- [ ] Where does the lock live, and what is its critical section? Keep pricing outside it.
- [ ] How do you find a free spot faster than scanning every spot? (a set per size, ordered)
- [ ] Class diagram with the two strategies in `notes/lld/ld-08-parking-lot.md`

## Extension (after green)

1. **Per-floor locks** so two floors never contend; prove no double allocation still holds.
2. **EV spots**: a new spot size and a charging fee, added without editing `ParkingLot` (open-closed).
3. **Display boards**: an observer notified with free counts per floor after every change.
