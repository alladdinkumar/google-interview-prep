# HLD Curriculum — System Design

**Total case studies:** 14 designs across Phase 4 (Weeks 18-22).
**Framework:** FRs → NFRs → Capacity → API → DB → High-Level Arch → Scale-out → Trade-offs.

---

## Building Blocks (Week 18 — before any case study)

You must internalize these before tackling case studies. Each one gets its own note file under `notes/hld/`.

| # | Topic | Note file | Resource |
|---|-------|-----------|----------|
| 1 | HLD framework template | `_framework.md` | (you write this) |
| 2 | Caching (read/write strategies, eviction, distributed) | `caching.md` | ByteByteGo + Gaurav Sen |
| 3 | Sharding + consistent hashing | `sharding.md` | Gaurav Sen consistent hashing video |
| 4 | CAP theorem + consistency models | `cap.md` | Arpit Bhayani CAP video |
| 5 | Message queues (Kafka / RabbitMQ / SQS) | `queues.md` | Gaurav Sen Kafka video |
| 6 | Load balancers (L4/L7) + algorithms | `load-balancers.md` | ByteByteGo |
| 7 | CDN basics | `cdn.md` | ByteByteGo CDN |
| 8 | Rate limiting (4 algorithms) | `rate-limiting.md` | System Design Interview Vol 1 ch 4 |
| 9 | DB replication + read replicas | `db-replication.md` | Gaurav Sen |
| 10 | SQL vs NoSQL — when to pick which | `sql-vs-nosql.md` | ByteByteGo |

**Don't skip this.** Case studies feel hard when you don't have the vocabulary. Get the vocabulary first.

---

## 14 Case Studies (Weeks 19-22)

Each case study walks through the full framework. Output: one markdown file in `notes/hld/<slug>.md` with diagrams (ASCII or excalidraw export) + design write-up.

### Week 19 — URL Shortener Family (3 designs)

| # | Design | Slug | Key challenges |
|---|--------|------|----------------|
| 1 | TinyURL | `tinyurl.md` | Key generation (base62 + counter vs hash), read-heavy cache, custom alias |
| 2 | Pastebin | `pastebin.md` | Blob storage choice, expiry, syntax highlighting (out of scope), abuse prevention |
| 3 | Rate Limiter (distributed) | `rate-limiter.md` | Token bucket vs sliding window, Redis-based counter, race conditions |

### Week 20 — Chat / Feed / Social (3 designs)

| # | Design | Slug | Key challenges |
|---|--------|------|----------------|
| 4 | WhatsApp / Messenger | `whatsapp.md` | WebSocket connection mgmt, group fan-out, online/offline, push notifications, multi-device |
| 5 | Twitter Feed | `twitter-feed.md` | Fan-out on write vs read, celebrity problem, timeline service, hot tweets |
| 6 | Instagram | `instagram.md` | Photo upload pipeline, CDN, news feed (reuse Twitter), follow graph at scale |

### Week 21 — Streaming / Caching / Search (4 designs)

| # | Design | Slug | Key challenges |
|---|--------|------|----------------|
| 7 | YouTube | `youtube.md` | Upload pipeline, transcoding, adaptive bitrate, storage tiering, CDN |
| 8 | Netflix | `netflix.md` | Reuse YouTube, focus on edge caching, content discovery, recommendation HLD |
| 9 | Distributed Cache (Memcached/Redis Cluster) | `distributed-cache.md` | Consistent hashing, replication, hot key problem, eviction policies |
| 10 | Typeahead Suggestion (Search autocomplete) | `typeahead.md` | Trie at scale, prefix caching, ranking signals, distributed Trie |

### Week 22 — Marketplaces / Financial / Notifications (4 designs)

| # | Design | Slug | Key challenges |
|---|--------|------|----------------|
| 11 | Uber / Lyft | `uber.md` | Driver-rider matching, geo-indexing (QuadTree/GeoHash/H3), surge pricing |
| 12 | Payment System | `payment.md` | Idempotency keys, double-spend, distributed transactions (saga), fraud check |
| 13 | Notification Service | `notifications.md` | Multi-channel fanout, retries with backoff, dedup, per-user rate limits |
| 14 | BookMyShow / Ticketmaster | `bookmyshow-hld.md` | Seat-locking under concurrency, payment flow, search/filter |

---

## Optional / Stretch Designs

If you finish early, pick from:
- Dropbox / Google Drive (file sync, conflict resolution)
- Web Crawler
- Distributed File System (GFS / HDFS overview)
- Ad-click event aggregation pipeline
- Stock exchange order book
- Slack
- Zoom (real-time video)
- Reddit (read-heavy, comments tree)

Don't force these in if you're behind on the core 14.

---

## Free Resources (Primary)

| Resource | Type | URL | Notes |
|----------|------|-----|-------|
| Gaurav Sen YouTube | Video | https://www.youtube.com/@gkcs | Single best free HLD source. Watch in order. |
| Concept&&Coding HLD | Video | https://www.youtube.com/@ConceptandCoding | Indian-instructor-friendly, complements Gaurav |
| ByteByteGo YouTube | Video | https://www.youtube.com/@ByteByteGo | 6-min animated explainers |
| Arpit Bhayani System Design | Video | https://www.youtube.com/@ArpitBhayani | Deep technical, great for follow-ups |
| Hello Interview System Design | Video | https://www.youtube.com/@hello_interview | Mock-interview style walkthroughs |
| System Design Primer (donnemartin) | Text | https://github.com/donnemartin/system-design-primer | Free comprehensive text reference |
| High Scalability blog | Text | http://highscalability.com | Real-world architectures |

---

## Deep-Dive Companions (read alongside case studies)

These come up as interviewer follow-ups:

- **WebSocket vs Long Poll vs SSE** — connection management deep dive
- **HTTP/2 multiplexing** vs HTTP/1.1 head-of-line blocking
- **gRPC** (you already know this — write a note!) — protobuf, streaming RPC, mTLS
- **Distributed transactions** — 2PC, 3PC, Saga pattern
- **Consensus** — Raft (one-paragraph), Paxos (acknowledge it exists)
- **Vector clocks + Lamport timestamps** (one paragraph each, just enough)
- **DNS at scale** — anycast, geo-DNS, DNS load balancing
- **Storage engines** — LSM tree (Cassandra, RocksDB) vs B-tree (MySQL, Postgres)

---

## Tracking

Each completed case study gets a row in `trackers/hld.md`:

| Design | Notes file | Drew capacity | Drew API | Drew DB | Drew arch | Confident (1-5) | Last revisited |
|--------|------------|---------------|----------|---------|-----------|-----------------|----------------|
| TinyURL | tinyurl.md | y | y | y | y | 4 | 2026-09-20 |
| ... | | | | | | | |

A case study isn't "done" until all 4 layers (capacity / API / DB / arch) are drawn or written.

---

## Common Interviewer Follow-ups (be ready)

- "What if 10× traffic tomorrow?" → identify hottest tier, scale it
- "What if a shard goes down?" → replication, fallback to nearest replica
- "What's your bottleneck?" → name it explicitly: usually DB write throughput
- "How do you handle hot keys?" → request coalescing, replicate hot key to multiple shards, client-side caching
- "How do you ensure exactly-once?" → idempotency key + dedup window
- "What's the read:write ratio assumption?" → state it upfront in capacity section

Practice answering these. They're not unfair — they're testing depth.
