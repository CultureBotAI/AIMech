# Discovery Report: Round 633 — Accordion (Critical-Regime Adaptive Gradient Communication and Batch-Size Scheduler)

- **Timestamp**: `2026-10-19T11:56:00Z`
- **Selected Concept**: `AIMech:AccordionCriticalRegimeAdaptiveGradientCommunication` (*Accordion (Critical-Regime Adaptive Gradient Communication and Batch-Size Scheduler)*)
- **Record Path**: `data/curated/AccordionCriticalRegimeAdaptiveGradientCommunication.yaml`
- **Primary Source**: Saurabh Agarwal, Hongyi Wang, Kangwook Lee, Shivaram Venkataraman, Dimitris Papailiopoulos — *Accordion: Adaptive Gradient Communication via Critical Learning Regime Identification* (`https://dblp.org/rec/journals/corr/abs-2010-16248`).

## Identity & Boundary Resolution

Distinct from static gradient compressors such as PowerSGD (AIMech:PowerSGDLowRankGradientCompression, Vogels et al. 2019), Top-K sparsification (AIMech:TopKGradientSparsification, Aji & Heafield 2017), and QSGD (AIMech:QSGDQuantizedStochasticGradientDescent, Alistarh et al. 2017), which use a fixed compression ratio throughout training. Distinct from AdaComp (AIMech:AdaCompAdaptiveResidualGradientCompression, Chen et al. 2018), which is a specific bin-level residual sparsifier/quantizer rather than a critical-regime controller that wraps arbitrary compressors (PowerSGD, Top-K) and batch-size schedules.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 633 Accordion verified: critical_windows=7/30, high_comp_windows=23/30, bs_comm_red=3.04x, lemma1_supp=4<=5, gamma=0.6000, cheb=1.56e-04
```
