# Discovery Report: Round 619 — Madam

- **Timestamp**: `2026-10-19T11:42:00Z`
- **Selected Concept**: `AIMech:Madam` (*Madam*)
- **Record Path**: `data/curated/Madam.yaml`
- **Primary Source**: Jeremy Bernstein, Jiawei Zhao, Markus Meister, Ming-Yu Liu, Anima Anandkumar, Yisong Yue — *Learning compositional functions via multiplicative weight updates* (`https://dblp.org/search/publ/api?q=Learning+compositional+functions+via+multiplicative+weight+updates&format=json`).

## Identity & Boundary Resolution

Distinct from additive adaptive optimizers such as Adam and RMSprop (which add -eta g / g_bar to W and can flip weight signs and violate relative perturbation bounds on small weights) and from layer-wise relative optimizers such as LARS, LAMB, and Fromage (which require global layer-wise Frobenius norm reductions). Madam guarantees ||Delta W_*||_F / ||W_*||_F = eta locally for every subset of weights W_* without layer-level synchronization.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 619 Madam verified: subset_rel_err=1.73e-18, angle_err=1.11e-16, thm1_eta_bound=0.0785, loss_drop=5.8476e+01>0, sign_flips=0, ladder_quant_err=1.25e-12, loss_ratio=9.5913e-05<<1
```
