# Discovery Report: Round 615 — SWATS

- **Timestamp**: `2026-10-19T11:38:00Z`
- **Selected Concept**: `AIMech:SWATS` (*SWATS*)
- **Record Path**: `data/curated/SWATS.yaml`
- **Primary Source**: Nitish Shirish Keskar, Richard Socher — *Improving Generalization Performance by Switching from Adam to SGD* (`https://dblp.org/rec/journals/corr/abs-1712-07628.xml`).

## Identity & Boundary Resolution

Distinct from AdaBound/AMSBound (AIMech:AdaBoundAndAMSBound, which smoothly pinches coordinate-wise step sizes via scheduled upper and lower bounds parameterized by gamma) and from Padam (AIMech:Padam, which maintains a constant partial-adaptivity power p in (0, 1/2] throughout training). SWATS executes a discrete phase switch from Adam to uniform-step-size SGD(M) where both the switchover iteration and the post-switch SGD learning rate Lambda are inferred automatically from the projection of -gamma_k g_k onto p_k.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 615 SWATS verified: proj_err=1.78e-15, rayleigh_err=8.88e-16, orth_norm_gap=1.7611e-01>0, switch_step=2, Lambda_sgd=0.0504, sgd_min_norm_err=1.57e-16, adam_excess_norm=0.1030>0
```
