# Temporal prediction and routing — 2026-10-11T14:03:15Z

Added three native DRAFT concepts, bringing the maintained collection to 301.

| Record | Defining mechanism |
| --- | --- |
| [AIMech:TemporalDifferenceLearning](../../data/curated/TemporalDifferenceLearning.yaml) | A family of prediction-learning methods that assign temporal credit using discrepancies between successive, recursively related predictions of future outcomes, with intervening costs or rewards included when the target is cumulative. |
| [AIMech:Sarsa](../../data/curated/Sarsa.yaml) | An on-policy temporal-difference control algorithm that updates the current state-action value toward the observed reward plus the discounted estimated value of the next action selected by the same behavior policy. |
| [AIMech:QRouting](../../data/curated/QRouting.yaml) | A distributed adaptive packet-routing algorithm that learns destination-specific delivery-time estimates by combining observed local queue and transmission delays with a neighboring node’s estimate of remaining delivery time. |

The records distinguish a prediction family, an on-policy control algorithm and adaptive packet routing. TD fixed-weight equivalence is kept separate from online parameter timing; Sarsa uses the selected next action; Q-routing minimizes local cost estimates and can leave unused alternatives stale.

All three have qualified related matches to AIO Reinforcement Learning. The Sarsa sources disagree on naming chronology, which remains explicit. The [finite calculations](temporal-prediction-and-routing-boundaries.py) check mechanism boundaries. The JSON ledger records actual reading scopes, source versions, access failures and ignored-inclusive identity searches.

Adversarial author self-review is required. Discovery remains active with 175 pending inspection leads and other unresolved dispositions.

Review issue #85 corrected the TD evidence graph by linking its control-application scope claim to the inspected author-book section. The original partial review is retained.
