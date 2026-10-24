# Discovery Report: Round 536 — Election Coding for Byzantine-Robust SignSGD with Majority Vote

- **Timestamp**: `2026-10-19T10:19:00Z`
- **Selected Concept**: `AIMech:ElectionCodingForByzantineRobustSignSgd` (*Election Coding for Byzantine-Robust SignSGD with Majority Vote*)
- **Record Path**: `data/curated/ElectionCodingForByzantineRobustSignSgd.yaml`
- **Primary Source**: Jy-yong Sohn, Dong-Jun Han, Beongjun Choi, Jaekyun Moon — *Election Coding for Distributed Learning: Protecting SignSGD against Byzantine Attacks* (`https://dblp.org/rec/conf/nips/SohnHCM20.xml`).

## Identity & Boundary Resolution

Distinct from uncoded SignSGD with Majority Vote (AIMech:SignSgdCompressedOptimisationWithMajorityVote, which corresponds to G = I_n with redundancy r = 1 and fails whenever Byzantine flips exceed the margin of the majority vote), from DRACO (AIMech:DracoByzantineResilientDistributedTrainingViaRedundantGradients, which uses cyclic/fractional repetition codes over real-valued full-precision gradients with linear redundancy r = 2b + 1), and from DETOX (AIMech:DetoxRedundancyBasedHierarchicalByzantineRobustGradientAggregation, which combines group majority filtering with full-precision geometric median / Krum aggregation). Election Coding (Sohn et al., NeurIPS 2020 / arXiv:1910.06093, Section 2.2, pp. 3-7) preserves 1-bit worker-to-master and master-to-worker communication while providing two explicit code families: (1) Random Bernoulli Codes where G_{ij} ~ Bern(p) with p = Theta(sqrt(log(n)/n)), achieving vanishing global sign estimation error P(hat{mu} != sign(g)) < 1/Delta (Lemma 1 & Theorem 1) and O(1/sqrt(T)) non-convex convergence (Theorem 2); and (2) Deterministic Algebraic Codes (Algorithm 1, Lemma 2, & Theorem 3) with block structure [I_s, 0; 0, A; 1_{(n-s-L) x n}] where s = (n-1)/2 - b and L = floor((n-(2b+1))/(2(b+1))) + 1, guaranteeing exact majority recovery P(hat{mu} != mu) = 0 under any b < floor(n/2) Byzantine bit-flip attacks.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 536 Election Coding verified: r(5,1)=3.80, r(7,2)=5.8571, r(9,2)=6.7778, P(hat_mu != mu)=0 across all 2^n states
```
