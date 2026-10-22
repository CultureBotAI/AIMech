---
name: stats-report
description: "Generate reproducible corpus, source, grounding, and data-quality statistics from the current AIMech corpus."
category: reporting
requires_database: false
requires_internet: false
version: 1.0.0
tags: [reporting, statistics, metrics, corpus]
---

# Statistics report

Use this skill for current AIMech repository counts, README statistics,
publication summaries, or before/after measurements for an import or curation
batch.

## Commands

```bash
just check-source
just validate
just check
```

Run `just check-source` and `just validate` (`uv run --locked aimech validate`) to verify live concept counts across `data/aio/*.yaml` and `data/curated/*.yaml`.

Never copy a hardcoded record count from skill prose: always derive counts at
run time because the corpus changes continuously.

## Verification

- Record the exact command and git commit used for published figures.
- Do not hand-edit generated statistics tables or JSON/Markdown reports and present them as a fresh run.
- Run `just validate` alongside reporting commands when summarizing corpus health.
