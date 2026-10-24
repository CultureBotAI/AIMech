# Discovery Report: Round 736 — Prototypical Calibration for Few-Shot Language Models

- **Timestamp**: `2026-10-19T13:39:00Z`
- **Selected Concept**: `AIMech:PrototypicalCalibrationForFewShotLanguageModels` (*Prototypical Calibration for Few-Shot Language Models*)
- **Record Path**: `data/curated/PrototypicalCalibrationForFewShotLanguageModels.yaml`
- **Primary Source**: Zhixiong Han, Yaru Hao, Li Dong, Yutao Sun, Furu Wei — *Prototypical Calibration for Few-shot Learning of Language Models* (`https://dblp.org/search/publ/api?q=Prototypical+Calibration+for+Few-shot+Learning+of+Language+Models+Han&h=5&format=xml`).

## Identity & Boundary Resolution

Distinct from Contextual Calibration (AIMech:CalibrateBeforeUseContextualCalibration) and Domain-Conditional PMI (AIMech:PMIDCDomainConditionalPointwiseMutualInformation), which apply diagonal scaling or subtract a single content-free/domain-premise baseline probability rather than estimating full class-conditional Gaussian covariances and means over the output distribution of an unlabeled estimate set. Also distinct from Prototypical Networks in metric meta-learning, which compute Euclidean distances to labeled support-set averages in a learned encoder representation space rather than fitting an unsupervised GMM with bipartite matching over frozen language-model log-probability outputs.

## Constructed Boundary & Regime Verification

```text
PROCA verification passed: naive_acc=0.50 -> proca_acc=1.00, best_CLA=-3.8650, perm=(2, 0, 1)
```
