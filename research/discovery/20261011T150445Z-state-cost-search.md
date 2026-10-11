# State-cost search methods — 2026-10-11T15:04:45Z

Added three native DRAFT records, bringing the maintained collection to 316.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:FillAlgorithm](../../data/curated/FillAlgorithm.yaml) | An idealized finite constraint-satisfaction search algorithm that takes any strictly cost-reducing single-variable change when available and otherwise increases only the stored cost of the current non-solution assignment. |
| [AIMech:RealTimeAStar](../../data/curated/RealTimeAStar.yaml) | A real-time heuristic search algorithm that moves to a neighbor with minimum edge-cost-plus-heuristic estimate and stores the second-best such estimate at the state it leaves, using bounded lookahead or initial heuristics for previously unvisited states. |
| [AIMech:LearningRealTimeAStar](../../data/curated/LearningRealTimeAStar.yaml) | A real-time heuristic learning algorithm that moves to a minimum estimated path-cost neighbor, stores that minimum edge-cost-plus-heuristic value at the state it leaves, and retains learned state estimates across repeated problem-solving trials with the same goals. |

Fill and basic RTA* have bounded AIO no-match assessments; LRTA* has an explicit related match to MachineLearningTask. The records distinguish state-specific lifting, second-best backup and repeated-trial minimum-value learning. Guarantees retain their finite-space, reachability, heuristic and exploration conditions. The 1988 graph-correction sketch is distinct from the basic 1990 presentation.

The [finite examples](state-cost-search-boundaries.py) and JSON ledger document scope, evidence, actual reading, mapping and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 183 pending inspection leads.
