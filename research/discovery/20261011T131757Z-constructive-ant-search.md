# Constructive ant search — 2026-10-11T13:17:57Z

Added three native DRAFT concepts, bringing the maintained collection to 291.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:AntSystem](../../data/curated/AntSystem.yaml) | A constructive combinatorial optimization method in which artificial ants sample solution components using shared pheromone trails and problem-specific heuristic information, then modify those trails through reinforcement and evaporation. |
| [AIMech:AntColonySystem](../../data/curated/AntColonySystem.yaml) | An ant-colony optimization algorithm that combines a greedy-or-proportional construction rule, local pheromone updates during construction, and global pheromone updates restricted to a selected best tour. |
| [AIMech:MaxMinAntSystem](../../data/curated/MaxMinAntSystem.yaml) | An ant-colony optimization algorithm that reinforces solution components from a single selected best ant per iteration, constrains pheromone trails between lower and upper limits, and initializes trails high to encourage early exploration. |

The records distinguish all-ant ant-cycle deposits, ACS construction and local/global updates, and MAX–MIN single-best reinforcement with trail bounds. The source conventions and appendix ambiguities are explicit.

All three records have bounded AIO no-match assessments. The [finite calculations](ant-search-boundaries.py) check update conventions and support/convergence boundaries. The JSON ledger preserves source versions, actual reading scopes, identity searches and outstanding leads.

Review is adversarial author self-review. Discovery remains active.

Review issue [80](https://github.com/CultureBotAI/AIMech/issues/80) led to explicit TSP/unit-exponent assumptions and the corrected lower-bound equation locator. The finite calculation now distinguishes alpha=1 from alpha=2.
