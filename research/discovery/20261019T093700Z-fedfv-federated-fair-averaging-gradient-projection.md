# Discovery Report: Round 494 — FedFV (Federated Fair Averaging via Loss-Ordered Internal and Historical External Gradient Projection)

- **Timestamp**: `2026-10-19T09:37:00Z`
- **Selected Concept**: `AIMech:FedFvFederatedFairAveragingViaLossOrderedAndHistoricalGradientProjection` (*FedFV (Federated Fair Averaging via Loss-Ordered Internal and Historical External Gradient Projection)*)
- **Record Path**: `data/curated/FedFvFederatedFairAveragingViaLossOrderedAndHistoricalGradientProjection.yaml`
- **Primary Source**: Zheng Wang, Xiaoliang Fan, Jianzhong Qi, Chenglu Wen, Cheng Wang, Rongshan Yu — *Federated Learning with Fair Averaging* (`https://www.ijcai.org/proceedings/2021/223`).

## Identity & Boundary Resolution

Distinct from FedMGDA+ (AIMech:FedMgdaPlusMultiObjectiveParetoStationaryFederatedOptimization, Hu et al. 2022), which normalizes local pseudo-gradients to unit L2 norm and solves a box-constrained simplex quadratic program min_{lambda in Delta_m, ||lambda - p||_inf <= eps} ||sum_i lambda_i g_i||^2 without normal-plane gradient projection or historical external-conflict buffers; and distinct from q-FFL (AIMech:QFairFederatedLearningAlphaFairResourceAllocation, Li et al. 2020), which reweights client losses by (1/(q+1)) F_k^{q+1}(w) using a Lipschitz upper-bound step size without detecting negative cosine similarities g_i . g_j < 0 or projecting conflicting gradients onto normal hyperplanes.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 494 FedFV (Wang et al. 2021): conflict_avg_g3=-0.6667 -> conflict_fv_g3=0.1400, Thm2_f=0.9835>0.3434>0.0, Thm3_id_err=0.00e+00, pareto_norm=0.00e+00
```
