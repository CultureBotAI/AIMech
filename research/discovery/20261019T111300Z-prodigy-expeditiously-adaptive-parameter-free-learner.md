# Discovery Report: Round 590 — Prodigy (Expeditiously Adaptive Parameter-Free Optimization)

- **Timestamp**: `2026-10-19T11:13:00Z`
- **Selected Concept**: `AIMech:ProdigyExpeditiouslyAdaptiveParameterFreeOptimization` (*Prodigy (Expeditiously Adaptive Parameter-Free Optimization)*)
- **Record Path**: `data/curated/ProdigyExpeditiouslyAdaptiveParameterFreeOptimization.yaml`
- **Primary Source**: Konstantin Mishchenko, Aaron Defazio — *Prodigy: An Expeditiously Adaptive Parameter-Free Learner* (`https://dblp.org/rec/conf/icml/MishchenkoD24`).

## Identity & Boundary Resolution

Distinct from standard D-Adaptation in that Prodigy weights each historical squared gradient norm in the step-size denominator by d_i^2 rather than unweighted ||g_i||^2, yielding a provably larger step size d_k^2 / sqrt(sum_{i=0}^k d_i^2 ||g_i||^2) >= d_k / sqrt(sum_{i=0}^k ||g_i||^2) and reducing the dependence on the initial distance underestimate D / d_0 from O(log(D / d_0)) to the optimal O(sqrt(log(D / d_0))). Distinct from DoG in that Prodigy estimates D via a dual lower bound d_hat_{k+1} rather than the maximum iterate displacement max_{i<=k} ||x_i - x_0|| and naturally supports coordinatewise Adam preconditioning.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 590 Prodigy verified: lemma1=(0.1031<=1.7608), d_prodigy=2.5403>d_dadapt=0.0004, loss_prodigy=1.7097<loss_dadapt=4.9996
```
