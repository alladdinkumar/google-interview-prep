# Phase 4 — System Design (HLD) (Weeks 18–22)

**Dates:** 2026-09-14 → 2026-10-18 (5 weeks)
**Budget:** ~95 hours (19h/week)
**Theme:** Master the HLD framework + walk through 14 classic system designs.

**This is where your Privafy experience pays off.** You've built distributed simulators, gRPC services, K8s deployments. The intuition is there — Phase 4 teaches you the *vocabulary* to articulate it in an interview.

---

## Phase Goals

- [ ] 14 system designs written up in `notes/hld/`
- [ ] HLD framework (FRs → NFRs → Capacity → API → DB → Scale-out → Trade-offs) automatic
- [ ] Comfortable with: caching, sharding, consistency models, CAP, message queues, CDN, LB, rate limiting
- [ ] 5 mocks done (Weeks 18, 19, 20, 21, 22) — mostly HLD
- [ ] DBMS deep topics done (sharding strategies, replication)

---

## The HLD Framework

Use this for every design, every time. ~45 min interview, split as:

1. **Requirements (5 min)** — FRs (what it does), NFRs (scale, latency, consistency, availability)
2. **Capacity estimation (3 min)** — users × actions/day × payload size → QPS + storage + bandwidth
3. **API design (5 min)** — top 4-6 endpoints with signatures
4. **DB design (7 min)** — schema, SQL vs NoSQL choice with reason, indexes
5. **High-level architecture (8 min)** — client → LB → service → cache → DB. Box-and-arrow diagram.
6. **Scale-out (10 min)** — caching layer, read replicas, sharding, message queue for async, CDN
7. **Trade-offs + bottlenecks (5 min)** — what you'd do differently at 100× scale, single points of failure
8. **Specific deep dive (2 min)** — interviewer-driven

Template lives in `notes/hld/_framework.md` (created next).

---

## Weekly Breakdown

### Week 18 — Framework + Building Blocks
**Hours: 19** | **🎯 Mock #4 (HLD)**

This week: zero new system designs. Master the building blocks.

- AM Mon: HLD framework template (`notes/hld/_framework.md`)
- AM Tue: Caching — read-through, write-through, write-back, write-around; cache invalidation; eviction (LRU/LFU); local vs distributed (`notes/hld/caching.md`)
- AM Wed: Sharding — by hash, by range, by geography; consistent hashing (`notes/hld/sharding.md`)
- AM Thu: CAP theorem + consistency models (eventual, strong, causal) (`notes/hld/cap.md`)
- AM Fri: Message queues — Kafka vs RabbitMQ vs SQS, async pattern (`notes/hld/queues.md`)
- PM Mon: Load balancers (L4 vs L7) + LB algos (round-robin, least-conn, weighted)
- PM Tue: CDN basics
- PM Wed: Rate limiting (token bucket, leaky bucket, fixed/sliding window)
- PM Thu: DB replication (master-slave, multi-master) + read replicas
- PM Fri: revision
- Sat: write the framework template + **Mock #4** (HLD-only)
- Sun: weekly review

Resource: Gaurav Sen system design playlist — https://www.youtube.com/@gkcs ; Concept&&Coding HLD — https://www.youtube.com/@ConceptandCoding ; ByteByteGo YouTube channel.

---

### Week 19 — TinyURL, Pastebin, Rate Limiter
**Designs: 3** | **Hours: 19** | **🎯 Mock #5 (HLD)**

Each design walked through end-to-end using the framework. Notes in `notes/hld/`.

- AM Mon: Design TinyURL (Bitly) — base62 encoding, key generation strategy, write-heavy vs read-heavy, cache strategy (`notes/hld/tinyurl.md`)
- AM Tue: Design Pastebin — paste storage, blob vs DB, expiry handling (`notes/hld/pastebin.md`)
- AM Wed: Design Rate Limiter — algorithm choice, distributed counter, Redis-based (`notes/hld/rate-limiter.md`)
- AM Thu-Fri: deep dive + alternative implementations + interviewer follow-ups
- PM: DBMS deep — sharding strategies, federation, denormalization
- Sat: review the 3 designs + **Mock #5**
- Sun: weekly review

---

### Week 20 — WhatsApp, Twitter, Instagram
**Designs: 3** | **Hours: 19** | **🎯 Mock #6 (HLD)**

These are the "design a chat / feed / social" canonical interviews.

- AM Mon-Tue: Design WhatsApp — connection management (long poll / WebSocket), message delivery (single device, group, multi-device), online/offline, push notifications (`notes/hld/whatsapp.md`)
- AM Wed-Thu: Design Twitter feed — fan-out on write vs read, celebrity problem, timeline service, tweet store (`notes/hld/twitter-feed.md`)
- AM Fri: Design Instagram — photo upload pipeline, CDN, news feed (overlap with Twitter), follow graph (`notes/hld/instagram.md`)
- PM each day: pick one specific deep-dive (e.g., "how does WhatsApp end-to-end encryption work at HLD level?")
- Sat: revise + **Mock #6**
- Sun: weekly review

---

### Week 21 — YouTube, Netflix, Distributed Cache, Search (Typeahead)
**Designs: 4** | **Hours: 19** | **🎯 Mock #7 (HLD)**

- AM Mon: Design YouTube — video upload pipeline, transcoding, storage tiering, CDN, recommendation system (HLD level) (`notes/hld/youtube.md`)
- AM Tue: Design Netflix — overlaps YouTube, focus on adaptive bitrate streaming, EDGE caching (`notes/hld/netflix.md`)
- AM Wed: Design Distributed Cache (Memcached/Redis Cluster) — consistent hashing, replication, hot key problem (`notes/hld/distributed-cache.md`)
- AM Thu: Design Search Typeahead — Trie at scale, prefix caching, ranking signals (`notes/hld/typeahead.md`)
- AM Fri: catch-up + deep dive on one
- PM each day: networking deep — gRPC architecture (use existing knowledge!), HTTP/2, HTTP/3
- Sat: revise + **Mock #7**
- Sun: weekly review

---

### Week 22 — Uber, Payment System, Notification Service, BookMyShow
**Designs: 4** | **Hours: 19** | **🎯 Mock #8 (HLD)**

- AM Mon: Design Uber — driver-rider matching, location updates (QuadTree / GeoHash), surge pricing (`notes/hld/uber.md`)
- AM Tue: Design Payment System — idempotency, double-spend prevention, distributed transactions / saga pattern (`notes/hld/payment.md`)
- AM Wed: Design Notification Service — multi-channel (push/email/SMS), retries, dedup, rate limiting per user (`notes/hld/notifications.md`)
- AM Thu: Design BookMyShow — seat-locking under concurrency (relates to Phase 3 LLD), payment integration, show search (`notes/hld/bookmyshow-hld.md`)
- AM Fri: catch-up + one more if time permits (Dropbox / Google Drive optional)
- PM each day: revise prior week's designs (spaced repetition)
- Sat: revise + **Mock #8 + Phase 4 retrospective**
- Sun: **Phase 4 retrospective + monthly review** (`reviews/monthly/2026-10.md`)

---

## Phase-4 Exit Criteria

Before Phase 5 (Mon 2026-10-19):

- [ ] 14 system designs written in `notes/hld/`
- [ ] Can drive a fresh HLD interview through the framework without prompts
- [ ] Comfortable explaining 5 caching strategies, 3 sharding approaches, CAP trade-offs
- [ ] 5 mocks done; latest 2 mocks rated ≥6/10
- [ ] DB sharding + replication notes done
- [ ] Adherence ≥65%

---

## Deep-Dive Companion Topics (sprinkled throughout phase 4)

These come up in interviewer follow-ups — be ready:

- gRPC vs REST (you live this — write a note)
- WebSocket vs long-polling vs SSE
- HTTP/2 multiplexing
- TLS handshake (you already know mTLS — easy)
- DNS at scale (anycast, geo-DNS)
- BGP basics (don't go deep)
- Consensus: Paxos / Raft (high-level intuition is enough)
- Vector clocks (one-paragraph understanding)
