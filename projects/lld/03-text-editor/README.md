# 03 — Text Editor with undo/redo (Week 41)

**Topics:** LD-4 structural patterns, LD-5 behavioural patterns

The textbook command-pattern exercise, done properly: every edit is a `Command` that knows how
to undo itself, the `Editor` keeps two stacks, and a failed edit leaves no trace. Rendering is
a decorator chain.

## Requirements (what the tests check)

1. `insert` / `erase` edit the text; out-of-range throws `std::out_of_range`.
2. `undo` reverses edits newest first and returns false when there is nothing left.
3. `redo` replays undone edits; **any new edit clears the redo stack**.
4. A throwing edit changes neither the text nor the undo history.
5. `EraseCommand::undo` restores exactly what was removed.
6. 500 random edits undo cleanly back to the empty document.
7. `Bold(UpperCase(Plain))` renders `"hello"` as `"**HELLO**"`; line numbers as `"1: a\n2: b"`.

## Build

```bash
make test
```

## Design checklist

- [ ] Why is `removed_` stored in `EraseCommand` rather than recomputed in `undo`?
- [ ] Draw the two stacks after: insert, insert, undo, insert
- [ ] Decorator vs subclassing: how many classes would 3 independent formats need with inheritance?

## Extension (after green)

1. **Coalescing**: consecutive single-character inserts at adjacent positions undo as one word.
2. **Composite**: a `MacroCommand` made of commands; undo it as one step.
3. **Memory cap**: keep at most 1,000 undo steps (a deque, dropping the oldest).
