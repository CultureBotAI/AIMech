# Discovery Report: Round 640 — LISA (Layerwise Importance Sampled AdamW)

- **Timestamp**: `2026-10-19T12:03:00Z`
- **Selected Concept**: `AIMech:LISALayerwiseImportanceSampledAdamW` (*LISA (Layerwise Importance Sampled AdamW)*)
- **Record Path**: `data/curated/LISALayerwiseImportanceSampledAdamW.yaml`
- **Primary Source**: Rui Pan, Xiang Liu, Shizhe Diao, Renjie Pi, Jipeng Zhang, Chi Han, Tong Zhang — *LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning* (`https://dblp.org/rec/conf/nips/PanLDPZH024`).

## Identity & Boundary Resolution

Distinct from BAdam (AIMech:BAdamBlockCoordinateAdamFullParameterOptimization), which partitions all model layers into D blocks of equal status and updates one block per K-step epoch via cyclic or random-reshuffling block coordinate descent; LISA is grounded in the empirical skewness of layerwise weight norms w^{(ell)} = (1/T) sum_{t=1}^T ||theta_t^{(ell)}||_2 in LoRA (where embedding and LM head norms exceed intermediate layers by 10^2x), assigning importance-sampling probabilities {1.0, gamma/N_L, ..., gamma/N_L, 1.0} so E and H remain continuously active while gamma intermediate layers are sampled every K steps. Distinct from LoRA (AIMech:LoraLowRankAdaptation), which freezes base weights and constrains updates to rank-r adapter matrices across all layers.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 640 LISA verified: exp_active=2.0, prob_err=0.0078, lr_ratio=0.0625, active_param_frac=9.90%, avg_regret=8.3380e-02, final_gap=1.2058e-02
```
