# GSAT reuse and randomized 2-SAT search — 2026-10-11T15:33:06Z

Added three native DRAFT records, bringing the maintained collection to 322.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:GSATClauseWeighting](../../data/curated/GSATClauseWeighting.yaml) | A GSAT extension that starts each clause with weight one, uses weighted clause counts to select flips, and increases the weights of clauses unsatisfied by the current assignment at the end of each search attempt. |
| [AIMech:GSATAveragingIn](../../data/curated/GSATAveragingIn.yaml) | A GSAT restart-initialization strategy that reuses agreements between earlier complete assignments, randomizes their differing positions, and periodically resets to a fresh random start. |
| [AIMech:Papadimitriou2SATRandomWalk](../../data/curated/Papadimitriou2SATRandomWalk.yaml) | A randomized 2-SAT search procedure that starts from any complete truth assignment and repeatedly selects an unsatisfied clause and flips a uniformly chosen literal’s variable until a satisfying assignment is reached or a selected move budget ends. |

The two GSAT extensions have bounded AIO no-match assessments. Papadimitriou’s walk has a related MarkovChain mapping supported by its explicit stochastic-process analysis, conditional on a state-based clause policy. The records distinguish terminal-state penalties, near-solution reuse and the scope of a 2-SAT move-count bound. Finite failure does not certify UNSAT.

The [finite examples](gsat-reuse-and-2sat-boundaries.py) and JSON ledger document scope, evidence, actual reading, mapping and carried/new leads. No benchmark performance is asserted.

Adversarial author self-review is required. Discovery remains active with 186 pending inspection leads.
