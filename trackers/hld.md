# HLD Tracker

System design case studies progress. Updated weekly during Phase 4.

---

## Building Blocks (Week 18)

| # | Topic | Note file | Studied | Notes written | Confidence (1-5) | Last revisited |
|---|-------|-----------|---------|---------------|-------------------|-----------------|
| 1 | HLD framework template | `_framework.md` | no | no | 1 | — |
| 2 | Caching strategies | `caching.md` | no | no | 1 | — |
| 3 | Sharding + consistent hashing | `sharding.md` | no | no | 1 | — |
| 4 | CAP + consistency models | `cap.md` | no | no | 1 | — |
| 5 | Message queues (Kafka/RabbitMQ/SQS) | `queues.md` | no | no | 1 | — |
| 6 | Load balancers (L4/L7) | `load-balancers.md` | no | no | 1 | — |
| 7 | CDN | `cdn.md` | no | no | 1 | — |
| 8 | Rate limiting | `rate-limiting.md` | no | no | 1 | — |
| 9 | DB replication | `db-replication.md` | no | no | 1 | — |
| 10 | SQL vs NoSQL | `sql-vs-nosql.md` | no | no | 1 | — |

---

## Case Studies (14 total)

A case study is **done** only when all 4 layers are drawn: Capacity / API / DB / Architecture.

| # | Design | Slug | Studied | Capacity | API | DB | Arch | Trade-offs | Confident (1-5) | Last revisited |
|---|--------|------|---------|----------|-----|-----|------|-----------|------------------|-----------------|
| 1 | TinyURL | `tinyurl.md` | no | — | — | — | — | — | 1 | — |
| 2 | Pastebin | `pastebin.md` | no | — | — | — | — | — | 1 | — |
| 3 | Rate Limiter (distributed) | `rate-limiter.md` | no | — | — | — | — | — | 1 | — |
| 4 | WhatsApp / Messenger | `whatsapp.md` | no | — | — | — | — | — | 1 | — |
| 5 | Twitter Feed | `twitter-feed.md` | no | — | — | — | — | — | 1 | — |
| 6 | Instagram | `instagram.md` | no | — | — | — | — | — | 1 | — |
| 7 | YouTube | `youtube.md` | no | — | — | — | — | — | 1 | — |
| 8 | Netflix | `netflix.md` | no | — | — | — | — | — | 1 | — |
| 9 | Distributed Cache | `distributed-cache.md` | no | — | — | — | — | — | 1 | — |
| 10 | Typeahead Search | `typeahead.md` | no | — | — | — | — | — | 1 | — |
| 11 | Uber | `uber.md` | no | — | — | — | — | — | 1 | — |
| 12 | Payment System | `payment.md` | no | — | — | — | — | — | 1 | — |
| 13 | Notification Service | `notifications.md` | no | — | — | — | — | — | 1 | — |
| 14 | BookMyShow | `bookmyshow-hld.md` | no | — | — | — | — | — | 1 | — |

---

## Deep-Dive Companions

| # | Topic | Note file | Studied | Confident |
|---|-------|-----------|---------|-----------|
| 1 | WebSocket vs LongPoll vs SSE | `_websocket.md` | no | 1 |
| 2 | HTTP/2 multiplexing | `_http2.md` | no | 1 |
| 3 | HTTP/3 / QUIC overview | `_http3.md` | no | 1 |
| 4 | gRPC architecture (your strength!) | `_grpc.md` | no | 3 (existing knowledge) |
| 5 | Distributed transactions (2PC, Saga) | `_distributed-txn.md` | no | 1 |
| 6 | Raft consensus (high-level) | `_raft.md` | no | 1 |
| 7 | Vector clocks / Lamport ts | `_vector-clocks.md` | no | 1 |
| 8 | DNS at scale (anycast, geo-DNS) | `_dns-scale.md` | no | 1 |
| 9 | LSM tree vs B-tree storage | `_lsm-btree.md` | no | 1 |
| 10 | Bloom filters | `_bloom-filter.md` | no | 1 |

---

## Mock HLD Performance

| Mock # | Date | Design asked | Got through | Bottleneck | Score (1-10) |
|--------|------|--------------|-------------|------------|--------------|
| #4 | — | — | — | — | — |
| #5 | — | — | — | — | — |
| #6 | — | — | — | — | — |
| #7 | — | — | — | — | — |
| #8 | — | — | — | — | — |
| #11 | — | — | — | — | — |

---

## Self-Assessment

End of Phase 4, can I do this without prompts?

- [ ] State assumptions upfront
- [ ] Quick capacity math (back-of-envelope) in 2-3 min
- [ ] Choose SQL vs NoSQL with explicit reason
- [ ] Design API with realistic endpoint signatures
- [ ] Draw a high-level architecture box-diagram
- [ ] Identify primary bottleneck (usually DB writes or hot cache)
- [ ] Discuss 2-3 trade-offs with the interviewer
- [ ] Handle "10× traffic" follow-up cleanly
