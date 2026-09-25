# Master Plan — 26 Weeks to FAANG SDE-II/III

**Start:** Mon 2026-05-18
**Target ready:** Sat 2026-11-15
**Total weeks:** 26
**Total hours:** ~494 (19h/week)

---

## Profile Snapshot

| Item | Value |
|------|-------|
| Age | 26 |
| Current role | Senior SWE @ Privafy, ~5.5 yrs |
| Day-to-day stack | Python, Go, K8s, Docker, gRPC, AWS, Robot Framework |
| Target level | SDE-II / SDE-III (L4/L5) |
| Target companies | Google (primary), Meta, Amazon, Microsoft, Atlassian |
| DSA language | C++ |
| DSA baseline | Rusty — needs 4-week ramp-up |
| Strong areas | Distributed systems, infra, scaling intuition (HLD-ready) |
| Weak areas | Recent DSA practice, LLD/OOD patterns, HLD vocabulary |

---

## Phase Overview

| Phase | Weeks | Dates | Hours | Theme | Outcome |
|-------|-------|-------|-------|-------|---------|
| **1. Foundations** | 1–4 | 2026-05-18 → 2026-06-14 | 76h | C++ STL + basic DSA | 60+ easy problems, complexity reflexes |
| **2. DSA Patterns** | 5–12 | 2026-06-15 → 2026-08-09 | 152h | All medium-tier patterns | 200+ problems, pattern recognition <3 min |
| **3. Advanced DSA + LLD** | 13–17 | 2026-08-10 → 2026-09-13 | 95h | Hard DSA + LLD fundamentals | 25 more problems, 8 LLD cases. **Mocks begin Wk 15.** |
| **4. System Design (HLD)** | 18–22 | 2026-09-14 → 2026-10-18 | 95h | HLD framework + 14 case studies | 14 written-up system designs |
| **5. Mocks + Behavioral** | 23–26 | 2026-10-19 → 2026-11-15 | 76h | Polish + 8-10 STAR + final mocks | Interview-ready, applications go live |

---

## Per-Phase Detail

Each phase has its own file with weekly breakdowns:

- `phase-1-foundations.md`
- `phase-2-dsa-patterns.md`
- `phase-3-advanced-dsa-lld.md`
- `phase-4-system-design.md`
- `phase-5-mocks-behavioral.md`

---

## What You're Being Measured On

By Nov 15, 2026 you should be able to honestly say yes to all of these:

**DSA**
- [ ] Solved ~290 LeetCode problems (60 E + 200 M + 30 H)
- [ ] Recognize the pattern of a new medium problem within 3 minutes
- [ ] Solve a fresh medium in 25-35 min start-to-clean-code
- [ ] Solve a fresh hard in 45-60 min with hints, 60-90 min without

**System Design (HLD)**
- [ ] 14 classic system designs written up in `notes/hld/`
- [ ] Can drive a 45-min HLD interview through FRs → NFRs → capacity → API → DB schema → scale-out → trade-offs without prompts
- [ ] Comfortable with: caching strategies, sharding, CAP, consistency models, message queues, CDN, load balancers, rate limiting

**LLD**
- [ ] 8-10 LLD problems coded end-to-end (Parking Lot, Splitwise, LRU, ATM, etc.)
- [ ] Apply SOLID without thinking about it
- [ ] Can explain Strategy, Factory, Observer, Singleton, Decorator, Adapter, Command, State patterns with use cases

**Core Subjects**
- [ ] OS: process/thread, scheduling, memory, paging, deadlocks, synchronization
- [ ] DBMS: SQL fluent, normalization, indexes, transactions/ACID, NoSQL vs SQL trade-offs
- [ ] CN: TCP/UDP, HTTP/HTTPS, DNS, TLS handshake (leverage gRPC/mTLS work)
- [ ] OOP: inheritance, polymorphism, abstraction, encapsulation, composition vs inheritance

**Behavioral / Googleyness**
- [ ] 8-10 STAR stories, each tagged to ≥2 leadership principles or Googleyness traits
- [ ] One scaling story (EDR simulator), one conflict story, one mistake story, one mentorship story minimum
- [ ] Can deliver a STAR answer in 90-120 seconds

**Mocks**
- [ ] 12 mock interviews completed
- [ ] Final 3 mocks rated ≥7/10 by the interviewer

---

## What the Coach Watches (and thresholds to react on)

| Metric | Watching for | Action if triggered |
|--------|--------------|----------------------|
| Weekly adherence | <60% for 2 consecutive weeks | Re-scope: extend current phase by 1 week |
| Problem accuracy on new pattern | <50% after 8 problems in that pattern | Add a remediation block: 3 more easy/medium of that pattern |
| Skipped reviews | >1 missed Sunday review | Hard-flag in next daily-log Reflection: "Why am I avoiding the review?" |
| Mock score trend | Flat or declining across 3 mocks | Identify root cause (DSA / HLD / LLD / behavioral) and concentrate next 2 weeks there |
| Sleep / energy <6/10 sustained | 5+ days in a row | Force a rest day mid-week. Plan adjusts down 20% next week. |

---

## What's Off the Table

These are explicitly **not** in scope:

- Competitive programming (Codeforces, CodeChef contests) — diminishing returns vs LC for FAANG
- Niche topics: heavy graph theory (Bellman-Ford / Floyd / max-flow), suffix arrays, advanced number theory — only touch if a target company asks
- Paid courses (resources are free-only)
- Cracking the Coding Interview book end-to-end — pick from it surgically when a topic comes up
- Premature webapp dashboard work — Track B starts week 5 at earliest

---

## Deferred Decisions (revisit at month-end)

- **Saturday block structure** — start with 9am-1pm continuous, switch to 2+2 split if energy flags
- **Adding paid resources** — if free-tier ceiling is hit (e.g., LC company-tagged), revisit LC Premium ($35/mo) at month 3
- **Application timing** — start applying Week 24 (2026-11-01) to get screens timed with peak readiness
- **Referrals** — collect Google/Meta/Amazon referral contacts during Phase 4, not before

---

## Phase Transitions

End of each phase, the coach asks:
1. Did you hit the phase goals? (yes / mostly / no)
2. Confidence level on phase outcomes (1-10)
3. Top 3 carry-over weaknesses
4. Adjust next phase, or proceed as planned?

If "no" or confidence <6, the **default is to extend by 1 week**, not to compress the next phase.
