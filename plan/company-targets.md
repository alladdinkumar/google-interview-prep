# Company Targets — Interview Formats & Prep Emphasis

Your target tier (broad FAANG SDE-II/III, ~5.5 yrs exp). Five priority companies with their formats.

---

## Google (primary target)

**Level:** L4 (SDE-II) or L5 (SDE-III). Your experience fits L4 → stretch L5.

### Interview loop (typical, India)
1. **Phone screen** — 1 coding problem (medium), 45 min
2. **Onsite / virtual onsite** — 5 rounds, 45 min each:
   - Coding × 2 (medium-hard DSA)
   - System Design × 1 (HLD; only for L5+, light for L4)
   - LLD / OOD × 1 (sometimes folded into coding)
   - Googleyness & Leadership × 1 (behavioral)

### What Google emphasizes
- **Generalist DSA** — they ask broad topics; specialization doesn't help
- **Communication during coding** — "explain your thinking out loud" is non-negotiable
- **Code quality** — naming, edge cases, complexity stated upfront
- **Ambiguity tolerance** — questions deliberately under-specified; you must ask clarifying questions
- **Googleyness** — emotional intelligence > heroic ego

### Prep emphasis for you
- Code-quality habits in every solution (clean variable names, comment on intent, state O(n) up front)
- Practice asking 2-3 clarifying questions on EVERY problem from Week 5 onward
- Strong HLD framework (your strength — lean in here)
- Story 4 (conflict / disagree-and-commit) and Story 5 (failure) for Googleyness

### How to apply
- Direct: https://careers.google.com
- Referrals: ask current and former colleagues and college alumni at Google
- Recruiter contact: don't chase; respond if they reach out

---

## Meta (Facebook)

**Level:** E4 (~SDE-II) or E5 (~SDE-III). Heavily coding-weighted.

### Interview loop
1. **Phone screen** — 2 coding problems in 45 min (yes, two)
2. **Onsite** — 4-5 rounds, 45 min each:
   - Coding × 2 (medium-hard; expect 2 problems per round)
   - System Design × 1 (HLD, very common pattern: news feed / chat / social)
   - Behavioral × 1 ("Jedi" round — leadership / collaboration / impact)
   - Sometimes "Product Architecture" for senior levels

### What Meta emphasizes
- **Speed** — 2 problems in 45 min means ~20 min per problem (including bug-free implementation)
- **Optimal solutions** — they expect optimal, not "I'd refine this later"
- **Communication during coding** — same as Google
- **Behavioral signals** — Meta values "move fast", "be direct and respect your colleagues", "build social value", "live in the future"

### Prep emphasis for you
- Speed drills: in Phase 5, set 25-min timer on mediums, force optimal first
- Meta-tagged problems (LC company tag if you go Premium; or NeetCode "Meta" list)
- HLD: practice social/chat/feed designs (which are in Weeks 20-21 anyway)

### How to apply
- Direct: https://www.metacareers.com
- Referrals: LinkedIn search "Meta India" → connect

---

## Amazon

**Level:** SDE-II (L5) or SDE-III (L6). Heavy LP focus.

### Interview loop
1. **OA** — 2 coding problems (medium) + 1 work simulation (LP-style) — 90 min
2. **Phone screen** — 1 coding + LP questions, 45-60 min
3. **Onsite** — 5 rounds:
   - Coding × 2 (medium, LP-flavored)
   - System Design × 1 (HLD)
   - Bar Raiser × 1 (deep behavioral, harder LP questions)
   - Hiring Manager × 1 (mix of behavioral + technical depth)

### What Amazon emphasizes
- **Leadership Principles** — every answer should naturally weave in 1-2 LPs
- **Customer obsession** — even in coding, "would this approach handle X customer scenario?"
- **Working backwards** — design from the customer outcome
- **Bar Raiser** is brutal — they're looking for "above the bar" of current employees

### Prep emphasis for you
- LP coverage matrix — all 14 LPs should map to ≥1 of your stories
- Behavioral rehearsal: more than for any other company
- Story 4 (conflict — "disagree and commit"), Story 5 (failure — "learn and be curious"), Story 8 (standards — "insist on highest standards") are LP-heavy

### How to apply
- Direct: https://amazon.jobs
- Phone screens with Amazon recruiters are aggressive — ready when you apply

---

## Microsoft

**Level:** SDE-II (60) or Senior SDE (63-64). More relaxed interview vs FAANG.

### Interview loop
1. **OA / Phone screen** — 1-2 coding problems, 45 min
2. **Onsite** — 4-5 rounds:
   - Coding × 2-3 (medium DSA)
   - System Design × 1 (HLD; sometimes lighter than Google/Meta)
   - "As Appropriate" (AA) — final round with senior manager, mix of behavioral and deep technical

### What Microsoft emphasizes
- **Fundamentals** — OS / DBMS / OOP come up more than at Google
- **Polite collaboration** — Microsoft culture is "growth mindset" (Satya-era)
- **Real product thinking** — they often ask "how would you design feature X within Y product?"

### Prep emphasis for you
- Core subjects matter more here (use Phase 2's core-subjects work as direct prep)
- OOP / OS questions can appear inside coding rounds — "implement Singleton with thread-safety", "explain virtual function dispatch"

### How to apply
- Direct: https://careers.microsoft.com
- LinkedIn referrals work well

---

## Atlassian

**Level:** Senior SWE (P40) or Principal SWE (P50). Heavy LLD / machine coding.

### Interview loop
1. **OA** — 1 medium DSA, 60 min (often via Codility / HackerRank)
2. **Onsite** — 4 rounds:
   - **Machine coding (LLD)** — 90-min round to build a small system end-to-end; **this is Atlassian's signature round**
   - System Design × 1 (HLD)
   - Behavioral × 1 (values-aligned)
   - Technical deep dive × 1 (CS fundamentals + previous projects)

### What Atlassian emphasizes
- **LLD execution** — 90-min round means you must design + code a working system. Common: parking lot, splitwise-style, file storage system
- **Atlassian values** — "Open Company, No Bullshit", "Build with Heart and Balance", "Don't #@!% the Customer", "Play, as a Team", "Be the Change You Seek"
- **Past project deep dive** — they drill 30-60 min on one past project

### Prep emphasis for you
- LLD is **critical** — Atlassian rounds are won/lost in LLD
- Your Phase 3 LLD week is more important than for other companies
- Past project deep dive: rehearse 1-2 deep technical stories with diagrams (a system you built end to end, with its numbers, is ideal)

### How to apply
- Direct: https://www.atlassian.com/company/careers
- Bangalore office is hiring; good fit for you

---

## Comparison Matrix

| Aspect | Google | Meta | Amazon | Microsoft | Atlassian |
|--------|--------|------|--------|-----------|-----------|
| Coding rounds | 2 | 2 (2 Qs each) | 2 | 2-3 | 1 |
| HLD weight | High | High | Medium-High | Medium | Medium |
| LLD weight | Medium | Low | Low | Low | **Very High** |
| Behavioral weight | High (Googleyness) | Medium | **Very High (LPs)** | Medium | High (values) |
| Core CS subjects | Medium | Low | Low | **High** | Medium |
| Speed emphasis | Medium | **High** | Medium | Medium | Medium |
| Ambiguity in problems | **High** | Medium | Medium | Low | Medium |

---

## Application Sequencing (Phase 5)

Don't apply to all 5 the same day. Sequence by:

1. **Week 24 (warm-up tier):** Microsoft + Atlassian (easier ramp, lower stakes, good first interview experience)
2. **Week 25 (mid-tier):** Amazon (LP-heavy — uses your behavioral prep)
3. **Week 26 (top tier):** Meta + Google (when you've already done 1-2 real interviews and learned what to fix)

This gives you 1-2 "rehearsal" real interviews before the dream-company shots.

---

## Secondary / Stretch Companies (apply if time)

- **Apple** — coding-heavy, design rounds for senior; iOS bias
- **Netflix** — small loop, very senior-heavy bar; only apply if confident
- **Uber India** — strong India presence, design-heavy
- **Razorpay** — Indian fintech, modern stack, asks DSA + system design + behavioral
- **Flipkart** — DSA-heavy + LLD; large hiring
- **Walmart Labs** — DSA + HLD; relaxed culture
- **Salesforce** — Java-leaning but C++ ok; medium difficulty
