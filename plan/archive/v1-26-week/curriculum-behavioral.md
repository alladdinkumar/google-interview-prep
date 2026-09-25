# Behavioral Curriculum — STAR Stories + Googleyness + Leadership Principles

**Goal:** 8-10 STAR stories, each ≤2 min spoken, each mapped to ≥2 leadership principles or Googleyness traits.

**When:** Sprinkled throughout the 26 weeks (15 min/day "story refine" slot in daily logs), but the *bulk* happens in Phase 5 Week 23.

**Why this matters:** Google's Googleyness and Amazon's LP rounds *eliminate* candidates who can't articulate impact and judgment. DSA gets you the screen; behavioral gets you the offer.

---

## STAR Format Refresher

| Letter | Meaning | Time | Example phrase to start |
|--------|---------|------|--------------------------|
| **S** | Situation | 15 sec | "At Privafy, we were running an EDR fleet test at 12K simulated clients..." |
| **T** | Task | 15 sec | "...and my task was to identify why throughput plateaued at ~80K events/sec when the target was 120K." |
| **A** | Action | 60-75 sec | "I instrumented the simulator, profiled the hot path..." (be specific, use "I" not "we") |
| **R** | Result + Learning | 20 sec | "We hit 120K events/sec. Key learning: lock contention isn't always the obvious bottleneck." |

**Total: 90-120 sec.** Anything longer = trim. Anything under 60 sec = add detail.

---

## 10 Story Slots — Based on Your Resume

Each slot is a *type* of story Google/FAANG asks for. You need at least one strong example for each.

| # | Slot | Possible story from your background | LPs / Googleyness tags |
|---|------|-------------------------------------|--------------------------|
| 1 | **Massive scaling / impact** | EDR simulator @ 12K clients / 120K events/sec | Deliver Results, Think Big, Bias for Action |
| 2 | **Ambiguous problem, you defined it** | Building telemetry validation framework from scratch | Comfort with Ambiguity (Googleyness), Invent and Simplify |
| 3 | **Technical depth / debugging** | Diagnosing a tricky network policy bug or telemetry inconsistency | Dive Deep, Are Right A Lot |
| 4 | **Conflict / pushback / disagreement** | Disagreement with a PM or engineer over an approach where you held your ground (or where you conceded with data) | Have Backbone; Disagree and Commit, Earn Trust |
| 5 | **Failure / mistake you owned** | A test that missed a regression, an infra outage you caused, a bad design call | Ownership, Learn and Be Curious |
| 6 | **Mentorship / hiring** | Onboarding a junior, reviewing PRs, building team-internal docs | Hire and Develop the Best |
| 7 | **Cross-team / customer-facing** | Working with cloud team on AWS provisioning, or with product on requirements | Customer Obsession, Earn Trust |
| 8 | **Process / standards improvement** | Setting up Jenkins regression pipelines, introducing automated reporting | Insist on Highest Standards, Frugality |
| 9 | **Learning / curiosity outside scope** | Picking up Go from scratch, learning Kubernetes for a project | Learn and Be Curious |
| 10 | **Long-term commitment / persistence** | A multi-quarter project (EDR simulator's evolution) | Bias for Action, Deliver Results |

**Layout per story:**

Create `notes/behavioral/stories/01-edr-scaling.md` (etc.) with this template:

```markdown
# Story 01 — EDR Simulator Scaling to 12K Clients

## Tags
- Amazon LPs: Deliver Results, Think Big, Bias for Action
- Googleyness: Comfort with ambiguity, Action over perfection

## Situation (~15 sec spoken)
[3-4 sentences max]

## Task (~15 sec)
[What specifically were you responsible for? Use "I" or "my team and I — I owned the X part."]

## Action (~60-75 sec)
[4-6 short paragraphs OR 4-6 bullets. Specific tools, specific decisions, specific trade-offs. Use "I" liberally — they want to know what YOU did.]

## Result (~20 sec)
[Concrete number if possible. "Throughput went from 80K to 120K events/sec, project shipped 2 weeks ahead of schedule."]

## Learning
[One sentence. What would you do differently? What's the takeaway?]

## Common follow-up questions
- "What was the riskiest decision?"
- "What did you do when X went wrong?"
- "Who else was involved and how did you split work?"
- "What metrics did you track to verify success?"

## My answers to follow-ups (notes)
[Bullets — don't memorize sentences, memorize the bones.]

## Time check
- Last rehearsed out loud: 2026-MM-DD
- Measured time: M:SS
- Target: 90-120 sec
```

---

## Coverage Matrix

Track in `trackers/behavioral.md`. Each row is a leadership principle or Googleyness trait. Each column is a story. ✓ = covered.

Sample:

| Principle / Trait | Story 1 (EDR scale) | Story 2 (Telemetry) | Story 3 (Bug) | ... | Coverage count |
|-------------------|---------------------|---------------------|---------------|-----|----------------|
| Deliver Results | ✓ | | ✓ | | 2 |
| Ownership | | ✓ | | | 1 |
| Dive Deep | | | ✓ | | 1 |
| Bias for Action | ✓ | ✓ | | | 2 |
| ... | | | | | |

**Goal: every leadership principle covered by ≥1 story.** Aim for ≥80% of LPs.

---

## Amazon Leadership Principles (the 16, condensed)

You should know what each means. You don't need a story for each, but you should be able to recognize which principle the interviewer's question is testing.

1. Customer Obsession
2. Ownership
3. Invent and Simplify
4. Are Right, A Lot
5. Learn and Be Curious
6. Hire and Develop the Best
7. Insist on the Highest Standards
8. Think Big
9. Bias for Action
10. Frugality
11. Earn Trust
12. Dive Deep
13. Have Backbone; Disagree and Commit
14. Deliver Results
15. Strive to be Earth's Best Employer
16. Success and Scale Bring Broad Responsibility

Note: Amazon's 15 + 16 are newer and less common in interviews. Don't sweat them.

---

## Googleyness Traits

Google's term is "Googleyness." It's not a formal list but distilled to:

- **Comfort with ambiguity** — can you make progress without complete specs?
- **Bias toward action** — do you ship or do you analysis-paralyze?
- **Intellectual humility** — can you say "I don't know" and "I was wrong"?
- **Collaboration** — do you build people up or up-stage them?
- **Push back constructively** — do you disagree without being a jerk?
- **Owning failure** — do you say "I screwed up" or "the team's plan was wrong"?

Each story should naturally lean toward 1-2 of these. Tag explicitly.

---

## Behavioral Round Mechanics

A typical behavioral round (45 min):
- 5 min: Greetings, "tell me about yourself" (2-min intro)
- 30 min: 3-4 behavioral questions, ~7-10 min each (90-120 sec STAR + 4-6 min follow-up)
- 5 min: your questions to interviewer
- 5 min: closing

**Common openers:**
- "Tell me about a time when you... [had to deal with X]"
- "Walk me through a project you're most proud of."
- "Describe a conflict you had with a teammate."
- "Tell me about a time you failed."
- "Describe a time you had to learn something new quickly."

**The "tell me about yourself" answer (2 min):**
1. Where you are now (Privafy, ~5.5 yrs, senior SWE)
2. What you do (one-line summary of biggest scope: "build automation + simulators for EDR systems that exercise 50K+ container fleets")
3. Key recent achievement (one bullet, ideally the EDR scaling story headline)
4. Why this company / role (1 sentence — researched per interview)

Don't recite resume bullet points. Tell a story.

---

## Rehearsal Plan (mostly Week 23 + spaced repetition)

- Phase 1-3: 15 min/day "story refine" in daily log (refine one slot, don't all)
- Phase 4: rotate stories — pick 1 to rehearse out loud each day
- Phase 5 Week 23: full draft + first rehearsal of all 10
- Phase 5 Weeks 24-26: rotate (each story rehearsed ≥3× before interview week)
- **Record yourself.** Listen back. You'll catch verbal tics ("um", "kind of", "I guess") that interviewers notice.

---

## Anti-Patterns

- **"We" everywhere** — interviewer is hiring YOU, not your team. Use "I did X, the team did Y."
- **No metric in the Result** — "we shipped it" is weak. "We hit 120K events/sec, 50% above target" is strong.
- **Rambling without structure** — STAR isn't optional. The interviewer is taking notes — make their job easy.
- **No failure story** — everyone has them. Pretending you don't = red flag.
- **Spinning a failure as a "humblebrag"** — "My biggest weakness is I work too hard." Don't.
- **Generic answers** — "I always communicate well." Show, don't tell. Give an example.

---

## Resources

- Amazon LP guide — https://www.amazon.jobs/en/principles
- Jeff H Sipe interview prep YouTube — https://www.youtube.com/@JeffHSipe
- "Cracking the Behavioral Interview" articles on Interviewing.io blog
- "Tell Me About Yourself" mock answers — interviewing.io blog
- For Googleyness: "Work Rules!" by Laszlo Bock (skim, don't read end-to-end)
