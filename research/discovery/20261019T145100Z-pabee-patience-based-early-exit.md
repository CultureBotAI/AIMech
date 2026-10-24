# Discovery Report: Round 808 — PABEE: Patience-Based Early Exit for Pretrained Language Models

- **Timestamp**: `2026-10-19T14:51:00Z`
- **Selected Concept**: `AIMech:PABEEPatienceBasedEarlyExitForBERT` (*PABEE: Patience-Based Early Exit for Pretrained Language Models*)
- **Record Path**: `data/curated/PABEEPatienceBasedEarlyExitForBERT.yaml`
- **Primary Source**: Wangchunshu Zhou, Canwen Xu, Tao Ge, Julian McAuley, Ke Xu, Furu Wei — *BERT Loses Patience: Fast and Robust Inference with Early Exit* (`https://arxiv.org/bibtex/2006.04152`).

## Identity & Boundary Resolution

Introduced by Wangchunshu Zhou, Canwen Xu, Tao Ge, Julian McAuley, Ke Xu, and Furu Wei (NeurIPS 2020, arXiv:2006.04152). Distinct from single-layer confidence or entropy early-exit mechanisms such as BranchyNet, Shallow-Deep Networks, DeeBERT, and FastBERT (Round 807): instead of trusting a single low layer's potentially over-confident softmax score, PABEE requires t consecutive inter-layer agreements (t + 1 agreeing layers in a row), which supports both classification and continuous regression (e.g., STS-B), mitigates deep-layer overthinking, and creates an implicit multi-layer ensemble defense against adversarial attacks.

## Constructed Boundary & Regime Verification

```text
{"concept": "PABEEPatienceBasedEarlyExitForBERT", "fig1_exit_layer": 4, "fig1_pred": "Neg", "reg_exit_layer": 5, "weighted_loss": 0.833333, "p_stop_exact": 0.740636, "p_stop_lower_bound_eq7": 0.328, "p_misc_exact": 0.00178, "p_misc_upper_bound_eq8": 0.002112, "overall_error_rate_pabee": 0.027717, "baseline_error_rate_p": 0.1, "status": "ok"}
```
