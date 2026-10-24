# Discovery Report: Round 370 — Adaptive Non-Monotone Threshold Sampling for Low-Adaptivity Submodular Maximization

- **Timestamp**: `2026-10-19T07:33:00Z`
- **Selected Concept**: `AIMech:AdaptiveNonMonotoneThresholdSamplingSubmodularMaximization` (*Adaptive Non-Monotone Threshold Sampling for Low-Adaptivity Submodular Maximization*)
- **Record Path**: `data/curated/AdaptiveNonMonotoneThresholdSamplingSubmodularMaximization.yaml`
- **Primary Source**: Matthew Fahrbach, Vahab Mirrokni, Morteza Zadimoghaddam — *Non-monotone Submodular Maximization with Nearly Optimal Adaptivity and Query Complexity* (`https://proceedings.mlr.press/v97/fahrbach19a.html`).

## Identity & Boundary Resolution

Distinct from AIMech:AmortizedFilteringForLogarithmicAdaptivitySubmodularMaximization (Round 360, Balkanski, Rubinstein, & Singer 2019) and AIMech:ParallelGreedySubmodularMaximizationInLogarithmicAdaptivityAndNearlyLinearTime (Round 362, Ene & Nguyen 2019), which require monotone submodular objectives where adding an eps-fraction of below-threshold elements cannot reduce objective value, whereas NON-MONOTONE-THRESHOLD-SAMPLING enforces early candidate-pool termination |A| < c_3 * k (to bound element inclusion probability <= 1/c_3 for Lemma 2.1), adds prefix post-filtering (to prevent negative-marginal elements from degrading S'), and couples threshold sampling with unconstrained maximization and uniform downsampling when |A| < c_3 * k.

## Constructed Boundary & Regime Verification

```text
[PASS] Adaptive Non-Monotone Threshold Sampling boundaries verified: post-filtered f(S')=8.00 >= tau*|S'|=3.00 (unfiltered=3.50), Thm 3.1 ratio=0.02619 (11/420), Thm 3.2 ratio=0.03957
```
