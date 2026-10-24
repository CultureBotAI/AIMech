# Discovery Report: Round 570 — ANITA Optimal Loopless Accelerated Variance-Reduced Gradient Method

- **Timestamp**: `2026-10-19T10:53:00Z`
- **Selected Concept**: `AIMech:AnitaOptimalLooplessAcceleratedVarianceReducedGradientMethod` (*ANITA Optimal Loopless Accelerated Variance-Reduced Gradient Method*)
- **Record Path**: `data/curated/AnitaOptimalLooplessAcceleratedVarianceReducedGradientMethod.yaml`
- **Primary Source**: Zhize Li — *ANITA: An Optimal Loopless Accelerated Variance-Reduced Gradient Method* (`https://api.openalex.org/works/W3137382134`).

## Identity & Boundary Resolution

Distinct from double-loop accelerated variance-reduced methods such as Katyusha (Allen-Zhu 2017) and Varag (Lan et al. 2019), and distinct from fixed-probability loopless Katyusha (L-Katyusha, Kovalev et al. 2020, which only handles strongly convex objectives mu > 0 with constant p_t = p): ANITA uses a single-loop structure with a dynamic three-stage snapshot probability schedule {p_t} in the general convex regime (mu = 0), achieving the first optimal O(n) stochastic gradient complexity matching the Woodworth-Srebro Omega(n) lower bound when n >= 1/epsilon^2.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 570 ANITA verified: theta_sc=0.4472, eta_sc=0.3980, phi_0=4.677e+00 -> phi_T=1.254e-16, f(w_T)=1.197e-16
```
