# 05 — Splitwise (Week 43)

**Topics:** LD-11 Splitwise design, LD-10 games (same week) · **Related:** DS-16 heaps, DS-25 greedy

Expense sharing with three split strategies and debt simplification. Two traps an interviewer
waits for: money as `double` (never — integer paise), and rounding that loses a paisa.

## Requirements (what the tests check)

1. Equal split gives leftover paise one each to the first users: 100 / 3 → 34, 33, 33.
2. Exact split must sum to the amount; percent split must sum to 100 and round without loss.
3. Balances: positive is owed, negative owes; they always sum to zero.
4. Unknown users, duplicate users and non-positive amounts throw and change nothing.
5. `simplify()` settles a chain a→b→c with one payment c→a.
6. For 60 random expenses among 10 users, `simplify()` zeroes every balance in at most
   (non-zero users − 1) payments.

## Build

```bash
make test
```

## Design checklist

- [ ] Why integer paise? Show the `0.1 + 0.2` failure in your note.
- [ ] `simplify()`: greedy with two heaps (biggest creditor, biggest debtor). Why is it at most n−1 payments?
- [ ] Note: the truly minimal number of payments is NP-hard (subset-sum); say so if asked.

## Extension (after green)

1. **Groups** with their own balances, and a user in several groups.
2. **Expense history** with edit and delete, keeping balances consistent (think command pattern).
3. **Currencies**: store the currency per expense; settle per currency.
