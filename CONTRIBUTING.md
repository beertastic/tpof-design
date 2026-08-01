# Production Documentation Workflow

**First, once per clone:**

```bash
git config core.hooksPath tools/hooks
```

Without it, `REPO-STATE.md` stops being stamped, and a connected AI agent loses
its only way to tell current files from cached ones. See [`AGENTS.md`](AGENTS.md).

## Status values

- `Concept` — exploratory and not canonical
- `Draft` — written for review
- `Approved` — canonical for production
- `Superseded` — retained for history but no longer active

## Review checklist

- Consistent with the Production Design Bible
- Function is visible in costume, prop, and environment choices
- Avoids unintentional Earth-historical shorthand
- Uses practical, manufacturable construction
- Records unresolved questions explicitly
- Includes version and revision history

## Branch naming

- `character/<name>`
- `faction/<name>`
- `prop/<name>`
- `location/<name>`
- `design/<topic>`
