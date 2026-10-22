# AIMech Skills

Native skills live in `.claude/skills/` and are exposed through `.agents/skills`.
Invoke them from an AIMech checkout. Each skill follows `CLAUDE.md`; none grants
permission to publish, run paid providers or rewrite generated records.

| Skill | Use | Saved result |
| --- | --- | --- |
| [aimech-add-record](../.claude/skills/aimech-add-record/SKILL.md) | Resolve identity, avoid duplicates, generate a missing pinned concept, or propose an unsupported addition | Generated record plus actual session history, or a clearly labeled proposal |
| [aimech-research-concept](../.claude/skills/aimech-research-concept/SKILL.md) | Investigate a concept's mechanism, applications, limitations and primary evidence | Timestamped evidence dossier |
| [aimech-discover-sources](../.claude/skills/aimech-discover-sources/SKILL.md) | Assess cohort coverage, source suitability and updates | Timestamped source assessment and integration handoff |
| [aimech-refresh-aio](../.claude/skills/aimech-refresh-aio/SKILL.md) | Assess or apply an explicitly scoped pinned AIO update | Migration proposal/accounting, saved reviews, and history for actual changes |
| [review-yaml-record](../.claude/skills/review-yaml-record/SKILL.md) | Assess an existing AIConcept | Timestamped structured YAML and rendered Markdown |
| [review-category](../.claude/skills/review-category/SKILL.md) | Review a cohort and retain/lump/split/defer its boundaries | Timestamped structured YAML and rendered Markdown |
| [aimech-resolve-reviews](../.claude/skills/aimech-resolve-reviews/SKILL.md) | Reassess findings and address supported fixes at their maintained owners | New structured successor reviews; earlier observations stay immutable |

`AIConcept` records currently reproduce the pinned AIO JSON. A trained model,
dataset or benchmark result is not automatically a new supported record type.
Research dossiers and source proposals support curation but do not replace the
[structured review contract](record-reviews.md) or imply scientific approval.

The resolution workflow explicitly verifies cross-review predecessor links;
the native bundle helper does not enforce that entire lineage. The refresh
workflow also compares ontology semantics beyond the importer's supported
projection. Passing bundle or import checks alone cannot establish those claims.
