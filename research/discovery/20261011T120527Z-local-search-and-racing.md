# Local search and racing — 2026-10-11T12:05:27Z

Added five native DRAFT concepts, bringing the maintained collection to 270.

| Record | Defining procedure |
| --- | --- |
| [AIMech:ParamILS](../../data/curated/ParamILS.yaml) | An iterated-local-search framework for algorithm configuration that searches finite parameter settings through one-parameter neighborhood moves, perturbations and random restarts, with a replaceable procedure for comparing configurations on target-algorithm runs. |
| [AIMech:BasicILS](../../data/curated/BasicILS.yaml) | A ParamILS algorithm-configuration method that compares candidate configurations using cost estimates on the same fixed number of target-algorithm runs, paired by problem instance and random seed. |
| [AIMech:FocusedILS](../../data/curated/FocusedILS.yaml) | A ParamILS algorithm-configuration method that adaptively extends paired evaluation prefixes until one configuration dominates the other, and allocates bonus evaluations to configurations that win the comparison. |
| [AIMech:RandomOnlineAggressiveRacing](../../data/curated/RandomOnlineAggressiveRacing.yaml) | An algorithm-configuration procedure that proposes uniformly random parameter settings and compares each challenger with an incumbent through adaptive evaluations on shared problem instances and random seeds, without fitting a predictive performance model. |
| [AIMech:FRace](../../data/curated/FRace.yaml) | A statistical racing method for configuring metaheuristics that evaluates a finite candidate set on shared problem-instance blocks and eliminates candidates judged worse through a Friedman rank test followed by comparisons with the best-ranked candidate. |

ParamILS is retained as the shared search framework; BasicILS and FocusedILS define different comparison procedures. ROAR uses random proposals with heuristic intensification, while F-Race eliminates a fixed candidate pool through rank tests. Source pseudocode, finite-budget and statistical limitations remain explicit.

Each record includes a documented AIO no-match assessment. The [finite calculation](configuration-racing-boundaries.py) checks source conventions and objective boundaries. The JSON ledger records source hashes, actual reading scopes, ignored-inclusive identity searches, AIO assessments and outstanding leads.

Review is adversarial author self-review. Discovery remains active.

Self-review [issue72](https://github.com/CultureBotAI/AIMech/issues/72) identified and corrected ROAR’s single-proposal wrapper versus the shared routine’s early-exit guard. The immutable initial review is retained; a successor disposition records validation of the fix.
