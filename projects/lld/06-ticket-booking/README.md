# 06 — Movie Ticket Booking with seat holds (Week 44)

**Topics:** LD-12 ticket booking, LD-13 rate limiter, LD-14 state, LD-15 pub-sub · **Related design:** SD-24 payments

The part of BookMyShow that interviews actually probe: two people click the same seat at the
same moment. Seats are *held* (all or nothing) while payment runs, then *confirmed*; holds
expire so an abandoned checkout does not block a seat forever.

## Requirements (what the tests check)

1. hold → confirm books seats permanently; booked seats never reappear.
2. A hold is all-or-nothing: if any seat is taken, none are held.
3. Out-of-range seats and unknown shows are reported, not thrown; duplicate shows throw.
4. A hold stops blocking at exactly `start + holdSeconds`; an expired hold cannot be confirmed.
5. `release` works once; a released hold cannot be confirmed.
6. `available` is sorted by (row, col).
7. 16 threads race for 100 seats: exactly 100 confirmed bookings, each seat once.

## Build

```bash
make test
```

## Design checklist

- [ ] Seat states: free → held(holdId, expiry) → booked; draw the state diagram (LD-14)
- [ ] Where would optimistic locking (a version per seat) replace your mutex, and what changes?
- [ ] How does a hold expire without a timer thread? (lazily, when `now` is compared)

## Extension (after green)

1. **Per-show locks**, so two shows never contend.
2. **Notifications**: publish HoldExpired and Booked events to subscribers (LD-15 pub-sub).
3. **Rate limit** holds per user with a token bucket (LD-13), to stop one user hoarding seats.
