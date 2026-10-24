# Discovery Report: Round 616 — AdaShift

- **Timestamp**: `2026-10-19T11:39:00Z`
- **Selected Concept**: `AIMech:AdaShift` (*AdaShift*)
- **Record Path**: `data/curated/AdaShift.yaml`
- **Primary Source**: Zhiming Zhou, Qingru Zhang, Guansong Lu, Hongwei Wang, Weinan Zhang, Yong Yu — *AdaShift: Decorrelation and Convergence of Adaptive Learning Rate Methods* (`https://dblp.org/rec/conf/iclr/ZhouZLWZY19.xml`).

## Identity & Boundary Resolution

Distinct from Adam and AMSGrad (which compute v_t using the contemporaneous squared gradient g_t^2, inducing positive correlation between v_t and |g_t| that biases the net update factor k(g_t) against large informative gradients). By separating the temporal support of m_t ({g_t, ..., g_{t-n+1}}) from the temporal support of v_t ({g_{t-n}, g_{t-n-1}, ...}), AdaShift makes v_t statistically independent of m_t under mini-batch independence and guarantees an unbiased expected net update factor E[k(g_t)] across all gradient magnitudes.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 616 AdaShift verified: lemma2_m_err=4.44e-16, lemma2_v_err=1.07e-14, lemma3_k_gap=1.5904e-02>0, adam_k_ratio=0.1302<1, shift_k_gap=0.0445<<1, theta_adam=478.65>0, theta_adashift=-63.25<0
```
