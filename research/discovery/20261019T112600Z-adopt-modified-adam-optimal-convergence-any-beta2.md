# Discovery Report: Round 603 — ADOPT (Adaptive Gradient Descent with Optimal Convergence)

- **Timestamp**: `2026-10-19T11:26:00Z`
- **Selected Concept**: `AIMech:AdoptModifiedAdamOptimalConvergenceAnyBeta2` (*ADOPT (Adaptive Gradient Descent with Optimal Convergence)*)
- **Record Path**: `data/curated/AdoptModifiedAdamOptimalConvergenceAnyBeta2.yaml`
- **Primary Source**: Shohei Taniguchi, Keno Harada, Gouki Minegishi, Yuta Oshima, Seong Cheol Jeong, Go Nagahara, Tomoshi Iiyama, Masahiro Suzuki, Yusuke Iwasawa, Yutaka Matsuo — *ADOPT: Modified Adam Can Converge with Any beta_2 with the Optimal Rate* (`https://dblp.org/rec/conf/nips/TaniguchiHMOJNI24`).

## Identity & Boundary Resolution

Distinct from Adam, AMSGrad (Reddi et al. 2018), AdaBelief (AIMech:AdaBeliefAdaptiveStepSizesByGradientBelief), and LaProp: whereas Adam updates m_t = beta_1 m_{t-1} + (1 - beta_1) g_t and divides m_t by sqrt(v_t) (creating statistical correlation between numerator g_t and denominator v_t that causes divergence on Reddi et al.'s counterexample when beta_2 is small), and whereas LaProp normalizes g_t by the contemporaneous sqrt(v_t) before momentum (failing the decorrelation requirement), ADOPT simultaneously lags the second moment by one step (v_{t-1}) and places coordinate-wise normalization inside the momentum recursion.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 603 ADOPT verified: adam=+1.0000, adopt=-1.0000, no_de=+1.0000, no_co=+0.7093, lemma_g7_err=2.61e-15, lemma_g8_err=2.02e-15, clip_ratio=5.0e+05
```
