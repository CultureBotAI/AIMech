# Discovery Report: Round 662 — RoSA

- **Timestamp**: `2026-10-19T12:25:00Z`
- **Selected Concept**: `AIMech:RoSA` (*RoSA*)
- **Record Path**: `data/curated/RoSA.yaml`
- **Primary Source**: Mahdi Nikdan, Soroush Tabesh, Elvir Crncevic, Dan Alistarh — *RoSA: Accurate Parameter-Efficient Fine-Tuning via Robust Adaptation* (`https://dblp.org/rec/conf/icml/NikdanTCA24.xml`).

## Identity & Boundary Resolution

Distinct from AIMech:LowRankAdaptation (LoRA), which constrains weight updates solely to a low-rank product BA and struggles to capture high-rank outlier residuals that emerge during complex generative reasoning tasks, and from pure sparse fine-tuning methods that optimize only a sparse coordinate subset without a global low-rank subspace component. RoSA (Mahdi Nikdan, Soroush Tabesh, Elvir Crncevic, and Dan Alistarh, ICML 2024, PMLR v235, arXiv:2401.04679) models the full-fine-tuning update matrix via a robust PCA decomposition W = W_0 + Delta_W^L + Delta_W^S, where Delta_W^L = B A in R^{m x n} has rank r << min(m, n) and Delta_W^S in R^{m x n} has density d = ||Delta_W^S||_0 / (m n) << 1 on a fixed support mask M. To avoid materializing full dense m x n weight gradient matrices during backpropagation, RoSA accumulates the low-rank branch for a short warm-up window while extracting top-k gradient coordinates layer-by-layer to construct M, and then uses a custom sparse-dense matrix multiplication (SpMM) backward kernel to compute gradients only at the active indices of M.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 662 RoSA (Nikdan et al. 2024): err_rosa=2.95e-06 << err_lora=10.5702 & err_spa=1.2970 (params_rosa=70<96), sddmm_err=0.00e+00
```
