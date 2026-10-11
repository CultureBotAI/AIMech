# Neighborhood-search controls — 2026-10-11T14:27:03Z

Added three native DRAFT records, bringing the maintained collection to 307.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:HillClimbing](../../data/curated/HillClimbing.yaml) | A family of local-improvement search procedures that replaces a current solution with a strictly better neighbor and stops when no improving neighbor exists under the specified move set. |
| [AIMech:FastLocalSearch](../../data/curated/FastLocalSearch.yaml) | A neighborhood-search procedure that uses activation bits to scan selected subneighborhoods, deactivating unsuccessful ones and reactivating those affected by accepted improvements. |
| [AIMech:StrategicOscillation](../../data/curated/StrategicOscillation.yaml) | A search-control strategy that alternates search directions or regimes around selected boundaries, controlling excursions and returns to explore solutions beyond the region of a single one-direction search. |

The records distinguish strict local improvement, selective neighborhood scanning and deliberate boundary-relative excursions. All three have bounded AIO no-match assessments. The broad LocalSearch lead remains pending.

The [finite boundary examples](neighborhood-search-controls-boundaries.py) expose plateau, reactivation and move-ranking conventions. The JSON ledger records primary-source versions, actual reading scopes, identity checks and carried/new leads.

Adversarial author self-review is required. Discovery remains active with 179 pending inspection leads.

Issue #89 corrects the AIMA source access field to `documentation`, as required for official documentation. The source identity and inspected passage are unchanged.
