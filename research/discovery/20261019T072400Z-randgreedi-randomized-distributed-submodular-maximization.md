# Discovery Report: Round 361 — RandGreeDi and NMRandGreeDi Randomized Distributed Submodular Maximization under Hereditary Constraints

- **Timestamp**: `2026-10-19T07:24:00Z`
- **Selected Concept**: `AIMech:RandGreeDiRandomizedDistributedSubmodularMaximization` (*RandGreeDi and NMRandGreeDi Randomized Distributed Submodular Maximization under Hereditary Constraints*)
- **Record Path**: `data/curated/RandGreeDiRandomizedDistributedSubmodularMaximization.yaml`
- **Primary Source**: Rafael da Ponte Barbosa, Alina Ene, Huy L. Nguyen, Justin Ward — *The Power of Randomization: Distributed Submodular Maximization on Massive Datasets* (`https://proceedings.mlr.press/v37/barbosa15.html`).

## Identity & Boundary Resolution

Distinct from AIMech:GreeDiTwoStageDistributedSubmodularMaximization (Round 359), which analyzes arbitrary deterministic partitions (yielding worst-case 1/Theta(min(sqrt(k), m)) approximation) and metric-space Lipschitz/density conditions rather than proving worst-case constant-factor alpha*beta/(alpha+beta) and alpha*beta/(alpha+2*beta) approximations for all hereditary constraints and non-monotone objectives via the Lovasz extension decomposition f^-(1_OPT - p) + f^-(p) >= f(OPT). Also distinct from AIMech:AmortizedFilteringForLogarithmicAdaptivitySubmodularMaximization (Round 360), which targets O(log n) adaptive query rounds in the centralized parallel oracle model.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 361 RandGreeDi (Barbosa et al. 2015): homog_err=4.44e-16, det_ratio_l3=0.5833, det_ratio_l5=0.3667, randgreedi_ratio_l3=1.0000, lovasz_sum=36.0000>=36.0
```
