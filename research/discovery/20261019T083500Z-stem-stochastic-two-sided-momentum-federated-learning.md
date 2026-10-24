# Discovery Report: Round 432 — STEM (Stochastic Two-Sided Momentum for Federated Learning)

- **Timestamp**: `2026-10-19T08:35:00Z`
- **Selected Concept**: `AIMech:StemStochasticTwoSidedMomentumForFederatedLearning` (*STEM (Stochastic Two-Sided Momentum for Federated Learning)*)
- **Record Path**: `data/curated/StemStochasticTwoSidedMomentumForFederatedLearning.yaml`
- **Primary Source**: Prashant Khanduri, Pranay Sharma, Haibo Yang, Mingyi Hong, Jia Liu, Ketan Rajawat, Pramod K. Varshney — *STEM: A Stochastic Two-Sided Momentum Algorithm Achieving Near-Optimal Sample and Communication Complexities for Federated Learning* (`https://proceedings.neurips.cc/paper/2021/hash/301ad0e3bd5cb1627a2044908a42fdc2-Abstract.html`).

## Identity & Boundary Resolution

Distinct from single-node STORM (AIMech:StormStochasticRecursiveMomentumForNonconvexOptimization, Cutkosky & Orabona 2019), which operates on a single machine without periodic multi-step local updates or inter-client heterogeneity, from SlowMo (AIMech:SlowMoSlowMomentumForCommunicationEfficientDistributedSgd, Wang et al. 2020), which applies klassical Polyak momentum only at the outer server synchronization step with O(epsilon^{-2}) sample complexity, and from MIME (AIMech:MimeMimickingCentralizedStochasticAlgorithmsInFederatedLearning, Karimireddy et al. 2021), which holds server statistics fixed during local steps.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 432 STEM (Khanduri et al. 2021): comm_STEM=10000.0 << comm_FedAvg=1000000.0, sample_STEM=62500.0 << sample_FedAvg=6250000.0, stem_err=6.51e-15
```
