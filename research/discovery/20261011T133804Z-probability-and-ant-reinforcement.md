# Probability and ant reinforcement — 2026-10-11T13:38:04Z

Added four native DRAFT concepts, bringing the maintained collection to 295.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:AntQ](../../data/curated/AntQ.yaml) | A family of cooperative ant-based optimization algorithms that learns shared edge desirabilities using Q-learning-inspired next-state estimates and delayed reinforcement from completed solutions. |
| [AIMech:PopulationBasedIncrementalLearning](../../data/curated/PopulationBasedIncrementalLearning.yaml) | An optimization method that samples candidate solutions from a probability-vector representation and incrementally moves that representation toward high-evaluation sampled solutions, with probability-vector mutation in its basic formulation. |
| [AIMech:RankBasedAntSystem](../../data/curated/RankBasedAntSystem.yaml) | An Ant System variant that weights pheromone deposits from a selected number of the current iteration’s best tours by rank and adds a separate reinforced contribution from the best-so-far tour. |
| [AIMech:ElitistAntSystem](../../data/curated/ElitistAntSystem.yaml) | An Ant System variant that retains the standard all-ant pheromone deposits and adds extra reinforcement to edges of the best-so-far tour after each construction cycle. |

Ant-Q uses a discounted next-value estimate; PBIL incrementally updates a sampling distribution; the ant variants distinguish rank-weighted deposits from all-ant deposits with extra archive reinforcement. Shared special cases do not erase the named method boundaries.

Ant-Q has a qualified related match to AIO Reinforcement Learning. The other three records have bounded AIO no-match assessments. The [finite calculations](probability-and-ant-reinforcement-boundaries.py) check the update distinctions. The JSON ledger preserves source versions, actual reading scopes, identity searches and outstanding leads.

Review is adversarial author self-review. Discovery remains active.
