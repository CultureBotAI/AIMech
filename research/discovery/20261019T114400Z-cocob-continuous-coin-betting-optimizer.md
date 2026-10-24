# Discovery Report: Round 621 — Continuous Coin Betting Optimizer

- **Timestamp**: `2026-10-19T11:44:00Z`
- **Selected Concept**: `AIMech:CocobContinuousCoinBettingOptimizer` (*Continuous Coin Betting Optimizer*)
- **Record Path**: `data/curated/CocobContinuousCoinBettingOptimizer.yaml`
- **Primary Source**: Francesco Orabona, Tatiana Tommasi — *Training Deep Networks without Learning Rates Through Coin Betting* (`https://dblp.org/rec/conf/nips/OrabonaT17`).

## Identity & Boundary Resolution

Distinct from adaptive learning-rate algorithms (AdaGrad, RMSProp, Adam, AdaDelta) that scale updates by a tuned base learning rate eta and from second-order or curvature-based tuners (YellowFin): COCOB eliminates the learning rate hyperparameter entirely by mapping iterate offsets w_{t,i} - w_{1,i} to bets proportional to accumulated gambler wealth L_i + Reward_{t,i} under Fenchel duality.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 621 COCOB verified: scale_err=4.44e-16, lemma2_rat=1.0007>=1, wealth_rat=1.1859>=1, fenchel_rat=1.2965<=1, thm1_rat=0.2099<=1, abs_subopt=0.4291, bp_err=0.0192
```
