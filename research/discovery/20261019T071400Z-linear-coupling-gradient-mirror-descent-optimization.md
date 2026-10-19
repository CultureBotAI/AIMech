# Discovery Report: Round 351 — Linear Coupling of Gradient and Mirror Descent for First-Order Optimization

- **Timestamp**: `2026-10-19T07:14:00Z`
- **Selected Concept**: `AIMech:LinearCouplingOfGradientAndMirrorDescentForFirstOrderOptimization` (*Linear Coupling of Gradient and Mirror Descent for First-Order Optimization*)
- **Record Path**: `data/curated/LinearCouplingOfGradientAndMirrorDescentForFirstOrderOptimization.yaml`
- **Primary Source**: Zeyuan Allen-Zhu, Lorenzo Orecchia — *Linear Coupling: An Ultimate Unification of Gradient and Mirror Descent* (`https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2017.3`).

## Identity & Boundary Resolution

Distinct from Katyusha Direct Negative-Momentum Acceleration for Stochastic Variance-Reduced Optimization (`AIMech:KatyushaDirectNegativeNegativeMomentumAccelerationForStochasticVarianceReducedOptimization` / `AIMech:KatyushaDirectNegativeMomentumAccelerationForStochasticVarianceReducedOptimization`), which introduces a three-point coupling with a SVRG reference snapshot tilde{x} (Katyusha momentum) specifically to stabilize variance-reduced stochastic gradients, and from Catalyst Universal Acceleration for First-Order Optimization (`AIMech:CatalystUniversalAccelerationForFirstOrderOptimization`), which is an outer-loop inexact proximal-point wrapper rather than a direct single-loop linear coupling of gradient descent and Bregman mirror descent steps.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 351 Linear Coupling AGM (Allen-Zhu & Orecchia 2014/2017): max_lemma43_viol=-4.76e-03, agm_err=0.000142 <= thm41_bound=0.021582 (vs gd_err=0.023792), kl_pinsker_gap=2.6440e-02
```
