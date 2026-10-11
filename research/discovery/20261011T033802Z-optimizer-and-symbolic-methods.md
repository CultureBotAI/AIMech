# Optimizer and symbolic-method discovery — 2026-10-11T03:38:02Z

Added AMSGrad, AdamNC, A-star search and the original STRIPS planning procedure; enriched Adafactor with its original paper and Adam with scoped counterexample evidence. The native collection now has 60 DRAFT concepts.

A-star and STRIPS use explicit no-match assessments because the inspected AIO classes do not provide convincing counterparts. The schema now validates this assessment as an exclusive alternative to positive mappings, requiring search scope and rejected targets. Source-pin, identity and claim-evidence requirements remain in force.

| Record | Disposition |
| --- | --- |
| [AIMech:AMSGrad](../../data/curated/AMSGrad.yaml) | added |
| [AIMech:AdamNC](../../data/curated/AdamNC.yaml) | added |
| [AIMech:AStarSearch](../../data/curated/AStarSearch.yaml) | added |
| [AIMech:STRIPSPlanning](../../data/curated/STRIPSPlanning.yaml) | added |
| [AIMech:Adafactor](../../data/curated/Adafactor.yaml) | evidence_enriched |
| [AIMech:Adam](../../data/curated/Adam.yaml) | limitation_evidence_added |

The A-star PDF has no usable text layer. Rendered pages and OCR were used, with the algorithm and evaluation function checked visually. AMSGrad/AdamNC and Adafactor equations and STRIPS operator/search pages were also inspected visually.

Adam's counterexample is preserved with its fixed-coefficient condition and analyzed setting. It is not a universal claim about every Adam implementation or training task.

Primary reinforcement-learning papers and symbolic-method neighbors remain on the frontier, alongside previous generative, graph, interpretation and architecture leads. This round found new concepts and does not establish saturation. The JSON companion records queries, exact source hashes, reading provenance and each disposition.
