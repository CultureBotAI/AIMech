# Discovery Report: Round 368 — Measured Continuous Greedy Algorithm for Constrained Monotone and Non-Monotone Submodular Maximization

- **Timestamp**: `2026-10-19T07:31:00Z`
- **Selected Concept**: `AIMech:MeasuredContinuousGreedySubmodularMaximization` (*Measured Continuous Greedy Algorithm for Constrained Monotone and Non-Monotone Submodular Maximization*)
- **Record Path**: `data/curated/MeasuredContinuousGreedySubmodularMaximization.yaml`
- **Primary Source**: Moran Feldman, Joseph (Seffi) Naor, Roy Schwartz — *A Unified Continuous Greedy Algorithm for Submodular Maximization* (`https://doi.org/10.1109/FOCS.2011.46`).

## Identity & Boundary Resolution

Distinct from AIMech:ContinuousGreedyAndMultilinearExtensionForMatroidSubmodularMaximization (Round 349, Calinescu et al. 2011), which updates y_e(t + delta) = y_e(t) + delta * I_e(t) without the (1 - y_e(t)) damping factor—causing coordinates to reach 1 too quickly and failing on non-monotone submodular functions where F(y(t) vee 1_{OPT}) requires bounding max_e y_e(t) <= 1 - e^{-t} via Lemma III.5—and which cannot run past stopping time T = 1 on high-density monotone packing polytopes.

## Constructed Boundary & Regime Verification

```text
[PASS] Measured Continuous Greedy boundaries verified: OPT=6.40, F(y(1))=4.2436 >= (1/e)*OPT=2.3544, max_e y_e(1)=0.6329 <= 1-1/e=0.6321, 2-player SW ratio=0.75
```
