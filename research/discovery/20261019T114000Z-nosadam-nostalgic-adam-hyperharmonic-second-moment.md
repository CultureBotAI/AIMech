# Discovery Report: Round 617 — Nostalgic Adam

- **Timestamp**: `2026-10-19T11:40:00Z`
- **Selected Concept**: `AIMech:NosAdam` (*Nostalgic Adam*)
- **Record Path**: `data/curated/NosAdam.yaml`
- **Primary Source**: Haiwen Huang, Chang Wang, Bin Dong — *Nostalgic Adam: Weighting more of the past gradients when designing the adaptive learning rate* (`https://dblp.org/rec/conf/ijcai/HuangWD19.xml`).

## Identity & Boundary Resolution

Distinct from Adam (which uses constant beta_2 in (0, 1) giving exponentially increasing weights (1 - beta_2) beta_2^{t-k} to recent gradients and violating Gamma_t >= 0), from AMSGrad (which forces monotonicity via a hard running maximum v_hat_t = max(v_hat_{t-1}, v_t) that permanently stalls step sizes after an outlier gradient spike), and from AdaShift (AIMech:AdaShift, which shifts gradients by n steps). NosAdam generalizes AdaGrad (recovered at gamma = 0 up to 1/t averaging) and extends to p-norm moment scaling in p-NosAdam (Theorem A.1).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 617 NosAdam verified: unrolled_err=2.66e-15, min_gamma_diff=9.86e+01>=0, lemma_a5_rat=0.9988<=1, regret_ratio=0.0002<=1, x_adam=1.00>0, x_nosadam=-1.00<0, spike_v_ratio=0.0276<<1
```
