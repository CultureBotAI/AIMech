# Discovery Report: Round 585 — Schedule-Free Optimization (Schedule-Free SGD and Schedule-Free AdamW)

- **Timestamp**: `2026-10-19T11:08:00Z`
- **Selected Concept**: `AIMech:ScheduleFreeOptimizationViaIterateAveragingAndMomentumInterpolation` (*Schedule-Free Optimization (Schedule-Free SGD and Schedule-Free AdamW)*)
- **Record Path**: `data/curated/ScheduleFreeOptimizationViaIterateAveragingAndMomentumInterpolation.yaml`
- **Primary Source**: Aaron Defazio, Xingyu Alice Yang, Harsh Mehta, Konstantin Mishchenko, Ahmed Khaled, Ashok Cutkosky — *The Road Less Scheduled* (`https://dblp.org/search/publ/api?q=The+Road+Less+Scheduled+Defazio&format=json`).

## Identity & Boundary Resolution

Distinct from Polyak-Ruppert averaging (beta = 0, which evaluates gradients purely at the fast base sequence y_t = z_t and suffers from instability and poor deep learning performance) and from Primal averaging (beta = 1, which evaluates gradients purely at the slow running average y_t = x_t and converges too slowly in early stages). By setting beta in (0, 1) (typically beta in [0.9, 0.98]), Schedule-Free interpolation immediately injects (1 - beta) Delta_t into y_{t+1} while gradually incorporating the remainder via x_{t+1}, achieving worst-case optimal O(DG/sqrt{T}) non-smooth convex convergence for every beta in [0, 1].

## Constructed Boundary & Regime Verification

```text
[PASS] Round 585 Schedule-Free verified: bregman_diff=6.66e-16, ld_yT_xT_diff=0.00e+00, err_sf=2.4800e-05<err_pa=9.7315e-02
```
