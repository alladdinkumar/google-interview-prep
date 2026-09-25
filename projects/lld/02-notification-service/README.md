# 02 — Notification Service (Week 40)

**Topics:** LD-3 creational patterns, LD-6 UML · **Related design:** SD-22 notification system

Send one message to a user over email, SMS and push, with retries, opt-outs and delivery
events. Four patterns, each where it earns its place:

| Pattern | Where | Why here |
|---------|-------|----------|
| Builder | `Message::Builder` | A `Message` can never exist half-built or invalid |
| Factory | `ChannelFactory` | Callers ask for a type, not a concrete class |
| Strategy | `RetryPolicy` | Swap fixed retry for exponential backoff without touching the service |
| Observer | `DeliveryListener` | Metrics and audit logging subscribe without the service knowing them |

## Requirements (what the tests check)

1. `build()` throws `std::invalid_argument` without a recipient or a body; default priority is Normal.
2. `ChannelFactory::create(t)->type() == t` for every type.
3. `ExponentialBackoff(5, 100ms, 300ms)` waits 100, 200, 300, 300 ms before attempts 2–5.
4. A failing channel is retried up to the policy's attempts, with the sleeper called between tries.
5. Every attempt raises a `DeliveryEvent` with its attempt number and outcome.
6. Opted-out channels are skipped — unless the message is High priority.
7. A requested type with no registered channel fails silently: no attempt, no event.

## Build

```bash
make test
```

## Design checklist

- [ ] Class diagram in `notes/lld/ld-06-uml.md`, with the four patterns labelled
- [ ] `NotificationService` depends on `Channel` and `RetryPolicy` interfaces only (dependency inversion)
- [ ] Listener pointers: what happens if a listener is destroyed while registered? Document the rule.

## Extension (after green)

1. **Rate limit per user**: at most N notifications per minute; inject the clock.
2. **Async sending**: a worker thread and a queue; `send` returns immediately with a future.
3. **Deduplication**: the same (user, idempotency key) within 10 minutes is sent once.
