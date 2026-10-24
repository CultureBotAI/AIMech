# Discovery Report: Round 428 — DSGT and GSGT (Distributed and Gossip Stochastic Gradient Tracking)

- **Timestamp**: `2026-10-19T08:31:00Z`
- **Selected Concept**: `AIMech:DsgtAndGsgtDistributedStochasticGradientTracking` (*DSGT and GSGT (Distributed and Gossip Stochastic Gradient Tracking)*)
- **Record Path**: `data/curated/DsgtAndGsgtDistributedStochasticGradientTracking.yaml`
- **Primary Source**: Shi Pu, Angelia Nedic — *Distributed Stochastic Gradient Tracking Methods* (`https://doi.org/10.1007/s10107-020-01487-0`).

## Identity & Boundary Resolution

Distinct from deterministic DIGing and Push-DIGing (AIMech:DigingAndPushDigingDistributedInexactGradientTrackingOverTimeVaryingGraphs, Nedic, Olshevsky, & Shi 2017), which analyze exact gradients over time-varying B-connected graphs via small-gain theorems, and from D2 (AIMech:D2VarianceReducedDecentralizedTrainingOverHeterogeneousData, Tang et al. 2018), which uses a single-variable two-step recursion X_{t+1} = (2 X_t - X_{t-1} - gamma G_t + gamma G_{t-1}) W requiring lambda_n(W) > -1/3 rather than explicit dynamic average consensus tracking y_{k+1} = W y_k + G_{k+1} - G_k and randomized pairwise gossip GSGT.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 428 DSGT & GSGT (Pu & Nedic 2021): tracking_err=3.89e-16, dsgt_err_sq=1.73e-35 vs dgd_err_sq=0.0331, rho_A_upper=0.9051, gsgt_err_sq=4.35e-17
```
