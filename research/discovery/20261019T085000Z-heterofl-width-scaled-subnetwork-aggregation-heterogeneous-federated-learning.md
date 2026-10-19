# Discovery Report: Round 447 — HeteroFL (Computation and Communication Efficient Federated Learning for Heterogeneous Clients)

- **Timestamp**: `2026-10-19T08:50:00Z`
- **Selected Concept**: `AIMech:HeteroFlWidthScaledSubnetworkAggregationForHeterogeneousFederatedLearning` (*HeteroFL (Computation and Communication Efficient Federated Learning for Heterogeneous Clients)*)
- **Record Path**: `data/curated/HeteroFlWidthScaledSubnetworkAggregationForHeterogeneousFederatedLearning.yaml`
- **Primary Source**: Enmao Diao, Jie Ding, Vahid Tarokh — *HeteroFL: Computation and Communication Efficient Federated Learning for Heterogeneous Clients* (`https://openreview.net/forum?id=TNkPBBYFkXg`).

## Identity & Boundary Resolution

Distinct from FjORD (AIMech:FjordOrderedDropoutAndSelfDistillationForHeterogeneousFederatedLearning, Horvath et al. 2021), which randomly samples prefix widths p ~ D_P during local client SGD (Ordered Dropout) and applies self-distillation from each client's maximal submodel rather than training a single fixed submodel level p_i per client round with a 1/r^{p-1} activation Scaler and static Batch Normalization.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 447 HeteroFL (Diao et al. 2021): ratios=[1.0, 0.25, 0.0625], err_heterofl=6.6727e-03 << err_naive_zeropad=6.4915e-01
/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/scratch/aimech-work/research/discovery/heterofl-width-scaled-subnetwork-aggregation-heterogeneous-federated-learning-boundaries.py:15: SyntaxWarning: invalid escape sequence '\ '
  Aggregating each disjoint parameter partition W_g^{p-1} \ W_g^p using only the m - m^{(p)}
```
