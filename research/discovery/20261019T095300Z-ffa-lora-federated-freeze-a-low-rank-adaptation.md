# Discovery Report: Round 510 — FFA-LoRA: Federated Freeze-A Low-Rank Adaptation

- **Timestamp**: `2026-10-19T09:53:00Z`
- **Selected Concept**: `AIMech:FfaLoraFederatedFreezeALowRankAdaptation` (*FFA-LoRA: Federated Freeze-A Low-Rank Adaptation*)
- **Record Path**: `data/curated/FfaLoraFederatedFreezeALowRankAdaptation.yaml`
- **Primary Source**: Youbang Sun, Zitao Li, Yaliang Li, Bolin Ding — *Improving LoRA in Privacy-preserving Federated Learning* (`https://dblp.org/rec/conf/iclr/SunLLD24`).

## Identity & Boundary Resolution

Distinct from vanilla federated LoRA / FedIT (Zhang et al., 2023; Kuang et al., 2023), which jointly trains both low-rank matrices A and B on each client and averages them separately on the server—incurring the bilinear aggregation error (1/2)(B_1 + B_2)(1/2)(A_1 + A_2) != (1/2)(B_1 A_1 + B_2 A_2) (Eq. 3) and quadratic DP-SGD noise amplification xi_B xi_A. Distinct from FLoRA (AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation; Wang et al., NeurIPS 2024), which trains both A_k and B_k on clients and eliminates cross-term aggregation noise by stacking A_k vertically and B_k horizontally on the server rather than freezing A_0 globally across clients. Also encompasses the authors' ultra-low-budget QVP Adapter extension W = W_0 + Q_0 V P_0 with frozen Q_0 in R^{d x r}, P_0 in R^{r x k} and trainable zero-initialized V in R^{r x r} (Appendix A.4, p. 16).

## Constructed Boundary & Regime Verification

```text
FFA-LoRA boundary verification passed: {'lora_agg_err': 1.651494, 'ffa_agg_err': 1.6184142622847344e-16, 'thm1_convergence_errs': [0.171516, 0.006861, 6.9e-05, 1e-06]}
```
