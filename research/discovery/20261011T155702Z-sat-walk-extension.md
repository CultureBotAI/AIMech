# SAT random-walk extensions and indifferent history search — 2026-10-11T15:57:02Z

Added three native DRAFT records, bringing the maintained collection to 328.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:NoveltyPlus](../../data/curated/NoveltyPlus.yaml) | A Novelty extension that, at each SAT search step, chooses a random variable from a randomly selected unsatisfied clause with a fixed walk probability and otherwise uses Novelty’s recency-conditioned best/second-best selector. |
| [AIMech:RNoveltyPlus](../../data/curated/RNoveltyPlus.yaml) | The 1999 R-Novelty extension that replaces its periodic random override with a fixed per-step probability of a random clause-variable flip and otherwise uses the recency- and score-gap-dependent R-Novelty selector. |
| [AIMech:IHSAT](../../data/curated/IHSAT.yaml) | A GenSAT variant that chooses the least recently flipped variable among all flips that do not decrease the satisfied-clause count, or among all variables when no nondecreasing flip exists. |

All three records have bounded AIO no-match assessments. The plus methods use a separate per-step random-walk probability; the1999 R-Novelty+ removes the periodic override, and the2004 plus convention remains distinct. Their asymptotic guarantee requires a fixed positive walk probability and gives no finite UNSAT certificate. IHSAT selects by age among all nondecreasing moves, or all moves if every gain is negative.

The [finite examples](sat-walk-extension-boundaries.py) and JSON ledger document scope, evidence, actual reading, mapping and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 186 pending inspection leads.
