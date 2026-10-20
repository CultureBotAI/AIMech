# Discovery Report: Round 612 — diffGrad

- **Timestamp**: `2026-10-19T11:35:00Z`
- **Selected Concept**: `AIMech:DiffGrad` (*diffGrad*)
- **Record Path**: `data/curated/DiffGrad.yaml`
- **Primary Source**: Shiv Ram Dubey, Soumendu Chakraborty, Swalpa Kumar Roy, Snehasis Mukherjee, Satish Kumar Singh, Bidyut Baran Chaudhuri — *diffGrad: An Optimization Method for Convolutional Neural Networks* (`https://dblp.org/rec/journals/tnn/DubeyCRMSC20.xml`).

## Identity & Boundary Resolution

Distinct from Adam and AMSGrad (which rely solely on exponential moving averages of past gradients m_t and squared gradients v_t without immediate short-term gradient-difference friction) and from AdaBelief (AIMech:AdaBelief, which replaces v_t in the denominator with the EMA of (g_t - m_t)^2). diffGrad retains Adam's bias-corrected moments m_hat_t and v_hat_t and multiplies the step size by the bounded logistic friction factor xi_t = 1 / (1 + exp(-|g_{t-1} - g_t|)) in [0.5, 1).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 612 diffGrad verified: F1_Adam=(x=0.2001, loss=0.0500), F1_diffGrad=(x=-0.3000, loss=6.87e-10), regret=4.7420<=thm1_rhs=4128.6455
```
