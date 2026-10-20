# Discovery Report: Round 572 — L-SVRG and L-Katyusha (Loopless Variance-Reduced Gradient Methods)

- **Timestamp**: `2026-10-19T10:55:00Z`
- **Selected Concept**: `AIMech:LSvrgAndLKatyushaLooplessVarianceReducedGradientMethods` (*L-SVRG and L-Katyusha (Loopless Variance-Reduced Gradient Methods)*)
- **Record Path**: `data/curated/LSvrgAndLKatyushaLooplessVarianceReducedGradientMethods.yaml`
- **Primary Source**: Dmitry Kovalev, Samuel Horvath, Peter Richtarik — *Don't Jump Through Hoops and Remove Those Loops: SVRG and Katyusha are Better Without the Outer Loop* (`https://dblp.org/search/publ/api?q=Remove+Those+Loops+Kovalev+Horvath&format=json`).

## Identity & Boundary Resolution

Distinct from standard double-loop SVRG (Johnson and Zhang, 2013) and Katyusha (Allen-Zhu, 2017; AIMech:KatyushaDirectNegativeMomentumAccelerationForStochasticVarianceReducedOptimization), which require a fixed deterministic inner-loop length m (where standard SVRG theory requires m = Theta(L/mu) depending on the unknown strong convexity parameter mu). Also distinct from ANITA (Li, 2021; Round 570), which uses a decaying step-size schedule to attain O(n + sqrt(nL/epsilon)) on general convex problems, and from ProxSkip-L-SVRG (Malinovsky et al., 2022; Round 571), which embeds L-SVRG inside probabilistic proximal/communication skipping.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 572 L-SVRG & L-Katyusha verified: E[Phi_1]=13.5165<=rhs=13.8490, err_lsvrg=8.921e-09, err_lkat=2.041e-28, psi_ratio=1.656e-29
```
