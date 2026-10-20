# Discovery Report: Round 730 — Domain Conditional Pointwise Mutual Information (PMI_DC) Scoring

- **Timestamp**: `2026-10-19T13:33:00Z`
- **Selected Concept**: `AIMech:PMIDCDomainConditionalPointwiseMutualInformation` (*Domain Conditional Pointwise Mutual Information (PMI_DC) Scoring*)
- **Record Path**: `data/curated/PMIDCDomainConditionalPointwiseMutualInformation.yaml`
- **Primary Source**: Ari Holtzman, Peter West, Vered Shwartz, Yejin Choi, Luke Zettlemoyer — *Surface Form Competition: Why the Highest Probability Answer Isn't Always Right* (`https://dblp.org/search/publ/api?q=Surface+Form+Competition+Why+the+Highest+Probability+Answer+Holtzman&format=xml`).

## Identity & Boundary Resolution

Distinct from standard direct probability arg max_i P(y_i | x) and length-normalized average log-likelihood AVG = (1/l_i) sum_j log P(y_i^j | x, y_i^{<j}), which do not factor out surface-form rarity, and from Contextual Calibration (Zhao et al., ICML 2021, AIMech:CalibrateBeforeUseContextualCalibration), which fits an affine matrix over a fixed closed label set using multiple content-free inputs rather than computing the symmetric log-probability difference log P(y_i | x) - log P(y_i | x_domain) for arbitrary open-set per-question answer options.

## Constructed Boundary & Regime Verification

```text
Domain Conditional PMI verification passed.
```
