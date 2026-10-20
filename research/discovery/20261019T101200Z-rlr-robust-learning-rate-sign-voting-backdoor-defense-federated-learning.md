# Discovery Report: Round 529 — RLR Robust Learning Rate Sign-Voting Backdoor Defense for Federated Learning

- **Timestamp**: `2026-10-19T10:12:00Z`
- **Selected Concept**: `AIMech:RlrRobustLearningRateSignVotingBackdoorDefenseForFederatedLearning` (*RLR Robust Learning Rate Sign-Voting Backdoor Defense for Federated Learning*)
- **Record Path**: `data/curated/RlrRobustLearningRateSignVotingBackdoorDefenseForFederatedLearning.yaml`
- **Primary Source**: Mustafa Safa Ozdayi, Murat Kantarcioglu, Yulia R. Gel — *Defending against Backdoors in Federated Learning with Robust Learning Rate* (`https://dblp.org/rec/conf/aaai/OzdayiKG21`).

## Identity & Boundary Resolution

Introduced by Ozdayi, Kantarcioglu, and Gel (AAAI 2021, Vol. 35, No. 10, pp. 9268-9276, DOI:10.1609/aaai.v35i10.17118, arXiv:2007.03767). Distinct from SignSGD with majority vote (AIMech:SignSgdAndMajorityVoteCompressedNonconvexOptimization, Bernstein et al. 2018), which discards update magnitudes and updates by eta * sgn(sum_k sgn(Delta_t^k)), whereas RLR preserves the full-precision aggregated update magnitude (e.g., FedAvg or coordinate-wise median) and flips the sign of the server learning rate to -eta on any coordinate where the absolute sum of update signs falls below threshold theta. Also distinct from FoolsGold (AIMech:FoolsGoldCosineSimilaritySybilDefenseForFederatedLearning), which assigns scalar per-client learning rates alpha_k based on historical cosine similarity rather than per-dimension sign-voting learning rates.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 529 RLR (Ozdayi et al. 2021): diag(2*I_t-I)=[1.0, -1.0], main_dim_step=0.50, backdoor_dim_fedavg=+0.60 vs backdoor_dim_rlr=-0.60
```
