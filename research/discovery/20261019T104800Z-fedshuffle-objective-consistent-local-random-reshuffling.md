# Discovery Report: Round 565 — FedShuffle and FedShuffleMVR Objective-Consistent Local Random Reshuffling for Federated Learning

- **Timestamp**: `2026-10-19T10:48:00Z`
- **Selected Concept**: `AIMech:FedShuffleAndFedShuffleMvrObjectiveConsistentLocalRandomReshufflingForFederatedLearning` (*FedShuffle and FedShuffleMVR Objective-Consistent Local Random Reshuffling for Federated Learning*)
- **Record Path**: `data/curated/FedShuffleAndFedShuffleMvrObjectiveConsistentLocalRandomReshufflingForFederatedLearning.yaml`
- **Primary Source**: Samuel Horvath, Maziar Sanjabi, Lin Xiao, Peter Richtarik, Michael Rabbat — *FedShuffle: Recipes for Better Use of Local Work in Federated Learning* (`https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2204.13169`).

## Identity & Boundary Resolution

Distinct from FedAvg with Random Reshuffling (FedAvgRR, which uses unscaled local step sizes and biased Sum-One aggregation w_i / sum_{j in S^r} w_j and converges to a mismatched objective), FedNova (Wang et al., NeurIPS 2020; which rescales aggregation weights rather than local step sizes, forcing a smaller worst-case local step size and not analyzing random reshuffling), and FedRR / LocalRR (which assume full client participation and identical dataset sizes).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 565 FedShuffle verified: SO_weights=(0.1944,0.3556,0.4500) vs w=(0.1667,0.3333,0.5000), err_fs=0.0459 << err_fa=0.7363
```
