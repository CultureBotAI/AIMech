# Discovery Report: Round 618 — WNGrad

- **Timestamp**: `2026-10-19T11:41:00Z`
- **Selected Concept**: `AIMech:WNGrad` (*WNGrad*)
- **Record Path**: `data/curated/WNGrad.yaml`
- **Primary Source**: Xiaoxia Wu, Rachel Ward, Leon Bottou — *WNGrad: Learn the Learning Rate in Gradient Descent* (`https://dblp.org/rec/journals/corr/abs-1803-02865.xml`).

## Identity & Boundary Resolution

Motivated by the Pythagorean norm growth ||v_{k+1}||_2^2 = ||v_k||_2^2 + (eta^2 / ||v_k||_2^2) ||P_{v_k^perp} nabla f||_2^2 of Weight Normalization on the unit sphere (Equation 4), WNGrad satisfies b_{k+1}^2 = b_k^2 + 2 ||g_k||_2^2 + ||g_k||_2^4 / b_k^2, avoiding square-root operations while remaining invariant to rescaling f -> lambda f when b_1 = C ||nabla f(x_1)||_2 (Remark 2.2). Also includes momentum extensions WNGrad-Momentum and WN-Adam (Algorithm 4).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 618 WNGrad verified: eq4_err=8.88e-16, sq_id_err=7.11e-15, scale_inv_err=2.78e-16, lemma26_rat=0.2188<=1, lemma25_rat=0.6240<=1, lemma33_rat=1.0000>=1, thm31_rat=8.5248e-07<=1
```
