# Discovery Report: Round 472 — pFedGP (Personalized Federated Learning with Gaussian Processes and Shared Deep Kernel Trees)

- **Timestamp**: `2026-10-19T09:15:00Z`
- **Selected Concept**: `AIMech:PFedGpPersonalizedFederatedLearningWithGaussianProcessesAndSharedDeepKernelTrees` (*pFedGP (Personalized Federated Learning with Gaussian Processes and Shared Deep Kernel Trees)*)
- **Record Path**: `data/curated/PFedGpPersonalizedFederatedLearningWithGaussianProcessesAndSharedDeepKernelTrees.yaml`
- **Primary Source**: Idan Achituve, Aviv Shamsian, Aviv Navon, Gal Chechik, Ethan Fetaya — *Personalized Federated Learning with Gaussian Processes* (`https://proceedings.neurips.cc/paper/2021/hash/44f683a84163b3523afe57c2e008bc8c-Abstract.html`).

## Identity & Boundary Resolution

Distinct from pFedBayes (AIMech:PFedBayesPersonalizedFederatedLearningViaVariationalBayesianInference, Zhang et al. 2022), which places factorized Gaussian variational posteriors over neural network weights rather than non-parametric Gaussian Processes with Pólya-Gamma augmentation over a shared deep kernel; and distinct from FedPA (AIMech:FedPaFederatedPosteriorAveragingViaLocalMcmcAndShrinkageCovariance, Al-Shedivat et al. 2021), which aggregates approximate client parameter posteriors into a single global parameter vector.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 472 pFedGP verified: mu_full=0.561960==mu_fitc=0.561960, var_full=0.722118==var_fitc=0.722118, KL_cond=0.2673>0
```
