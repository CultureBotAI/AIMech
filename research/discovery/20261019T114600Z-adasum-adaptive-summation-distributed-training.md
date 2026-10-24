# Discovery Report: Round 623 — AdaSum Adaptive Summation for Distributed Training

- **Timestamp**: `2026-10-19T11:46:00Z`
- **Selected Concept**: `AIMech:AdaSumAdaptiveSummationForDistributedTraining` (*AdaSum Adaptive Summation for Distributed Training*)
- **Record Path**: `data/curated/AdaSumAdaptiveSummationForDistributedTraining.yaml`
- **Primary Source**: Saeed Maleki, Madan Musuvathi, Todd Mytkowicz, Olli Saarikivi, Tianju Xu, Vadim Eksarevskiy, Jaliya Ekanayake, Emad Barsoum — *Scaling Distributed Training with Adaptive Summation* (`https://dblp.org/rec/conf/mlsys/MalekiMMSXEEB21`).

## Identity & Boundary Resolution

Distinct from standard synchronous AllReduce summation/averaging, from delay-compensated asynchronous SGD (DC-ASGD, which uses only diagonal g_i odot g_i and requires a tuned hyperparameter), and from per-layer norm trust-ratio optimizers (LARS, LAMB): AdaSum operates across workers via a two-phase recursive vector-halving collective (ADASUMRVH) after local optimizer steps, reducing to the exact sum g_1 + g_2 when g_1 and g_2 are orthogonal and to the exact average (g_1 + g_2)/2 when g_1 = g_2.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 623 AdaSum verified: seq_emul_err=2.22e-16, orth_err=0.00e+00, par_err=0.00e+00, orth_range=[0.1250, 1.0000], lemmaA2_min_cos=0.942809>0.942, eq11_err=2.66e-15, norm_ratio=1.0647 in [1,2], hessian_err_ratio=0.6667<1
```
