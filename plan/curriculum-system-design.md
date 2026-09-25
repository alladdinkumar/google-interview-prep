# System Design Curriculum — Google-scale HLD

**Weeks 45–56.** At L4 Google often runs one system design round; at L5 it is certain and
weighted heavily. Your day job (K8s, gRPC, AWS, distributed telemetry) is a real advantage
here — the work is turning intuition into the interview's vocabulary and structure, and
knowing Google's own systems well enough to reference them (GFS, Bigtable, Spanner, Borg,
MapReduce) without name-dropping.

**Output of every case study:** requirements (functional + non-functional with numbers), a
capacity estimate, the API, the data model, the high-level diagram, two deep dives, and the
bottleneck you would fix next. Written in `notes/system-design/`.

---

## Topics

| # | Topic | Week | Note file | Tag |
|---|-------|------|-----------|-----|
| SD-1 | System design interview framework — requirements, estimation, API design, data model, high level design, deep dive, trade-offs | 45 | `notes/system-design/sd-01-framework.md` | design |
| SD-2 | Back of the envelope estimation — QPS, storage, bandwidth, latency numbers every programmer should know | 45 | `notes/system-design/sd-02-estimation.md` | design |
| SD-3 | Networking and APIs for system design — DNS, HTTP, TCP vs UDP, WebSockets, REST vs gRPC, long polling | 46 | `notes/system-design/sd-03-networking-apis.md` | design |
| SD-4 | Load balancing — L4 vs L7 load balancer, round robin, least connections, health checks, reverse proxy | 46 | `notes/system-design/sd-04-load-balancing.md` | design |
| SD-5 | Caching — cache aside, write through, write back, eviction policies, CDN, cache invalidation | 47 | `notes/system-design/sd-05-caching.md` | design |
| SD-6 | Databases — SQL vs NoSQL, indexing, B-tree vs LSM tree, replication, read replicas, transactions and isolation | 47 | `notes/system-design/sd-06-databases.md` | design |
| SD-7 | Sharding and consistent hashing — partitioning strategies, hot keys, rebalancing, virtual nodes | 48 | `notes/system-design/sd-07-sharding.md` | design |
| SD-8 | CAP theorem and consensus — consistency models, quorum, leader election, Raft, Paxos | 48 | `notes/system-design/sd-08-cap-consensus.md` | design |
| SD-9 | Message queues and streaming — Kafka, pub sub, delivery semantics, backpressure | 49 | `notes/system-design/sd-09-queues-streaming.md` | design |
| SD-10 | Rate limiting — token bucket, leaky bucket, fixed window, sliding window, distributed rate limiter | 49 | `notes/system-design/sd-10-rate-limiting.md` | design |
| SD-11 | Google infrastructure papers — Google File System, MapReduce, Bigtable, Spanner, Borg | 50 | `notes/system-design/sd-11-google-papers.md` | design |
| SD-12 | Unique ID generation — Snowflake IDs, UUID, ticket servers, clock skew | 49 | `notes/system-design/sd-12-unique-ids.md` | design |
| SD-13 | Design a URL shortener — key generation, base62 encoding, redirection, analytics | 51 | `notes/system-design/sd-13-url-shortener.md` | design |
| SD-14 | Design a distributed key value store — Dynamo, partitioning, replication, vector clocks, gossip | 51 | `notes/system-design/sd-14-key-value-store.md` | design |
| SD-15 | Design a chat system — WhatsApp, WebSocket connections, message delivery, presence, group chat | 52 | `notes/system-design/sd-15-chat.md` | design |
| SD-16 | Design a news feed — Twitter timeline, fan out on write vs read, celebrity problem, ranking | 52 | `notes/system-design/sd-16-news-feed.md` | design |
| SD-17 | Design YouTube video streaming — upload pipeline, transcoding, adaptive bitrate, CDN | 53 | `notes/system-design/sd-17-youtube.md` | design |
| SD-18 | Design search autocomplete — typeahead, trie at scale, top K queries, data collection pipeline | 53 | `notes/system-design/sd-18-autocomplete.md` | design |
| SD-19 | Design a web crawler — URL frontier, politeness, deduplication, distributed crawling | 54 | `notes/system-design/sd-19-web-crawler.md` | design |
| SD-20 | Design Google Drive file storage — Dropbox, chunking, sync, conflict resolution, metadata | 54 | `notes/system-design/sd-20-google-drive.md` | design |
| SD-21 | Design a proximity service — Uber, Google Maps nearby, geohash, quadtree, location updates | 55 | `notes/system-design/sd-21-proximity.md` | design |
| SD-22 | Design a notification system — push, email, SMS, retries, deduplication, user preferences | 55 | `notes/system-design/sd-22-notifications.md` | design |
| SD-23 | Design a metrics monitoring and alerting system — time series database, aggregation, alerting | 56 | `notes/system-design/sd-23-metrics-monitoring.md` | design |
| SD-24 | Design a payment system — idempotency, double entry ledger, reconciliation, distributed transactions | 56 | `notes/system-design/sd-24-payments.md` | design |
| SD-25 | Design Google Docs collaborative editing — operational transformation, CRDT, real time sync | 56 | `notes/system-design/sd-25-google-docs.md` | design |

---

## The 45-minute shape

| Minutes | Step | What the interviewer is checking |
|---------|------|----------------------------------|
| 0–5 | Functional + non-functional requirements, with numbers | You scope before you build |
| 5–10 | Estimation: QPS, storage, bandwidth | You know where the scale actually is |
| 10–15 | API + data model | Clean contracts, sensible keys |
| 15–30 | High-level diagram, one request traced through it | It works end to end |
| 30–42 | Two deep dives the interviewer picks | Depth, trade-offs named out loud |
| 42–45 | Bottlenecks, failure modes, what's next | Judgment |

## Follow-ups to expect (be ready for every one)

- What happens when this node dies? This data centre?
- How do you make this idempotent?
- Where's the hot key, and what do you do about it?
- Strong or eventual consistency here — and what does the user see?
- How would you roll this out without downtime?
