# Discovery Report: Round 526 — FoolsGold Cosine-Similarity Sybil Defense for Federated Learning

- **Timestamp**: `2026-10-19T10:09:00Z`
- **Selected Concept**: `AIMech:FoolsGoldCosineSimilaritySybilDefenseForFederatedLearning` (*FoolsGold Cosine-Similarity Sybil Defense for Federated Learning*)
- **Record Path**: `data/curated/FoolsGoldCosineSimilaritySybilDefenseForFederatedLearning.yaml`
- **Primary Source**: Clement Fung, Chris J. M. Yoon, Ivan Beschastnikh — *Mitigating Sybils in Federated Learning Poisoning* (`https://www.usenix.org/conference/raid2020/presentation/fung`).

## Identity & Boundary Resolution

Distinct from FLTrust (which computes cosine similarity against a central server's root-dataset reference gradient g_0 rather than pairwise historical inter-client similarity with pardoning and logit inversion), and distinct from majority-bounded distance filters (Krum, Multi-Krum, Bulyan) that assume fewer than 50% malicious clients. Specifically denotes the FoolsGold algorithm of Fung, Yoon, & Beschastnikh (RAID 2020 / arXiv:1808.04866, Section 5, Algorithm 1, and Appendix A).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 526 FoolsGold (Fung et al. 2020): beta_m=0.6225, beta_g=0.3775, min_honest_alpha=0.7435 >> max_sybil_alpha=0.0000
```
