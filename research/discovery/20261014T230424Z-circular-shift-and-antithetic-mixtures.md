# Circular shifts and antithetic mixtures — 2026-10-14T23:04:24Z

Three finite DRAFT transition constructions were created with related AIO Markov Chain mappings.

## Circular weight-shift sampler

`AIMech:CircularWeightShiftSampler` — `data/curated/CircularWeightShiftSampler.yaml`

A finite-state Markov transition construction that partitions a circle into intervals with target-weight lengths and derives each transition from the overlap of a positively shifted current-state interval with destination intervals.

## Upward-downward nested antithetic mixture

`AIMech:UpwardDownwardNestedAntitheticMixture` — `data/curated/UpwardDownwardNestedAntitheticMixture.yaml`

A finite conditional Markov update that chooses with equal probability between complete upward and downward nested antithetic modification kernels for the same target distribution.

## Upward-downward shifted tower mixture

`AIMech:UpwardDownwardShiftedTowerMixture` — `data/curated/UpwardDownwardShiftedTowerMixture.yaml`

A finite conditional Markov update that equally mixes maximum-shift tower kernels built from paired upward and downward cyclic state orders, making their stationary flows symmetric.

## Evidence and scope

The circular construction uses positive finite weights, one consistent order and an explicit shift orientation; maximum and half shifts are contained policies. UDNAM chooses between complete upward and downward NAM components. UDST chooses between maximum-shift components with paired reverse-tail orders, including ties.

The two mixtures use a constant fair component choice at each local update. Mixture, sequential composition, state-dependent selection and global scan schedules are kept distinct. Invariance does not establish irreducibility, aperiodicity or efficiency.

Tower evidence includes separately pinned Suwa2010 arXiv v2, Suwa2022 v1 and Suwa2023 v2 PDFs plus selected Neal2024 methods. Mixture claims cite only Neal2024. Version dates, Suwa2010 cover/margin inconsistency, opposite shift conventions, Neal Algorithm 6 shortcut and Algorithm 7 closed-endpoint caveats are retained without asserting an author erratum.

Two original exact-rational calculators are copied byte-for-byte. The mixture calculator reads the unchanged existing NAM sibling and new tower sibling with fixed hashes. Original scripts/results, first expanded executions, rerun receipts and derivations are embedded; no failed run or correction event is invented. These are bounded curator checks, not author software or general theorem replication.

All 1152 current canonical identities were refreshed and four whole checkouts searched including ignored and hidden files. The 895 prior main frontier entries gain three actual leaves, totaling 898; all 393 nested entries remain unchanged. Existing family owners remain partial.

Full structured ledger: `research/discovery/20261014T230424Z-circular-shift-and-antithetic-mixtures.json`

Root and supporting agents belong to the same author workflow. Actual saved reviews, full gates and publication remain separate later work.
