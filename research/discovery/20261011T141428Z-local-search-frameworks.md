# Local-search frameworks — 2026-10-11T14:14:28Z

Added three native DRAFT concepts, bringing the maintained collection to 304.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:TabuSearch](../../data/curated/TabuSearch.yaml) | A memory-guided optimization framework that steers a search trajectory by making selected moves temporarily inadmissible from search history, allowing non-improving moves and, where specified, aspiration-based overrides. |
| [AIMech:GuidedLocalSearch](../../data/curated/GuidedLocalSearch.yaml) | A local-search metaheuristic that repeatedly minimizes an objective augmented by feature penalties, increasing selected penalties at local minima to alter subsequent search while retaining solutions according to the original objective. |
| [AIMech:IteratedLocalSearch](../../data/curated/IteratedLocalSearch.yaml) | A metaheuristic that builds a single search trajectory among solutions returned by an embedded optimizer by perturbing the current accepted solution, rerunning that optimizer, and applying an acceptance criterion to the resulting candidate. |

The records distinguish memory-based move restrictions, selective feature penalties and perturbation followed by embedded optimization. All three carry bounded AIO no-match assessments; optional machine-learning applications do not establish a task or model identity.

The [finite calculations](local-search-frameworks-boundaries.py) check cycles, aspiration, feature-count and acceptance boundaries. The JSON ledger records exact source versions, actual reading scopes, ignored-inclusive identity searches and remaining leads.

Adversarial author self-review is required. Discovery remains active with 177 pending inspection leads and other unresolved dispositions.

Issue #87 corrects the Tabu source description: the scan contains a 2001 copyright footer, while its insertion date is not established. The article is from 1989.
