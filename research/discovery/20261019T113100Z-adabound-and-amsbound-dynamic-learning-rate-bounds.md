# Discovery Report: Round 608 — AdaBound and AMSBound Dynamic Learning-Rate Bounds Optimization

- **Timestamp**: `2026-10-19T11:31:00Z`
- **Selected Concept**: `AIMech:AdaBoundAndAmsBoundDynamicLearningRateBoundsOptimization` (*AdaBound and AMSBound Dynamic Learning-Rate Bounds Optimization*)
- **Record Path**: `data/curated/AdaBoundAndAmsBoundDynamicLearningRateBoundsOptimization.yaml`
- **Primary Source**: Liangchen Luo, Yuanhao Xiong, Yan Liu, Xu Sun — *Adaptive Gradient Methods with Dynamic Bound of Learning Rate* (`https://dblp.org/rec/conf/iclr/LuoXLS19`).

## Identity & Boundary Resolution

Distinct from Adam (Kingma & Ba, 2015), which sets eta_l(t) = 0 and eta_u(t) = infinity and can fail to converge on convex problems due to either huge or tiny learning rates (Theorems 1-3); distinct from AMSGrad (Reddi et al., 2018), which enforces non-increasing step sizes via v_hat_t = max(v_hat_{t-1}, v_t) to curb large learning rates but does not bound tiny learning rates from below; distinct from SWATS (Keskar & Socher, 2017), which performs a discrete hard switch from Adam to SGD at a thresholded step rather than a continuous dynamic-bound transformation; and distinct from Padam (Chen et al., 2020), which scales the second-moment denominator exponent to v_hat_t^p with p in (0, 1/2] rather than clipping step sizes to time-varying bounds [eta_l(t), eta_u(t)].

## Constructed Boundary & Regime Verification

```text
[PASS] Round 608 AdaBound/AMSBound verified: R_adam/T=100.00>=100, R_adabound/T=0.10, R_amsbound/T=0.10, min_v_gap=9.0285e-02>=0, lemma2_rat=0.0553<=1, lemma3_rat=0.0000<=1, thm4_rat=0.0000<=1
```
