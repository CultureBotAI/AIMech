# Discovery Report: Round 728 — Calibrate Before Use Contextual Calibration

- **Timestamp**: `2026-10-19T13:31:00Z`
- **Selected Concept**: `AIMech:CalibrateBeforeUseContextualCalibration` (*Calibrate Before Use Contextual Calibration*)
- **Record Path**: `data/curated/CalibrateBeforeUseContextualCalibration.yaml`
- **Primary Source**: Tony Z. Zhao, Eric Wallace, Shi Feng, Dan Klein, Sameer Singh — *Calibrate Before Use: Improving Few-Shot Performance of Language Models* (`https://dblp.org/search/publ/api?q=Calibrate+Before+Use+Improving+Few-Shot+Performance+of+Language+Models+Zhao&format=xml`).

## Identity & Boundary Resolution

Distinct from statistical confidence calibration such as Temperature Scaling (Guo et al., ICML 2017, AIMech:TemperatureScaling), which requires a labeled validation set to align predicted confidence with empirical accuracy, and from Domain Conditional Pointwise Mutual Information (PMI_DC, Holtzman et al., EMNLP 2021, AIMech:PMIDCDomainConditionalPointwiseMutualInformation), which divides each open-ended hypothesis continuation by its unconditional probability under a short domain premise string rather than fitting a closed-set uniform affine transformation on content-free test inputs inside a few-shot prompt.

## Constructed Boundary & Regime Verification

```text
Contextual Calibration verification passed.
```
