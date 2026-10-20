# Discovery Report: Round 556 — PowerGossip Low-Rank Communication Compression for Decentralized Deep Learning

- **Timestamp**: `2026-10-19T10:39:00Z`
- **Selected Concept**: `AIMech:PowerGossipLowRankCommunicationCompressionForDecentralizedDeepLearning` (*PowerGossip Low-Rank Communication Compression for Decentralized Deep Learning*)
- **Record Path**: `data/curated/PowerGossipLowRankCommunicationCompressionForDecentralizedDeepLearning.yaml`
- **Primary Source**: Thijs Vogels, Sai Praneeth Karimireddy, Martin Jaggi — *Practical Low-Rank Communication Compression in Decentralized Deep Learning* (`https://dblp.org/rec/conf/nips/VogelsKJ20`).

## Identity & Boundary Resolution

Introduced by Thijs Vogels, Sai Praneeth Karimireddy, and Martin Jaggi (NeurIPS 2020, Vol. 33, pp. 14171-14181; arXiv:2008.01425). Distinct from PowerSGD (Vogels, Karimireddy, & Jaggi, NeurIPS 2019), which performs centralized all-reduce low-rank approximation of error-compensated gradients rather than pairwise edge-wise model-difference compression; and distinct from Choco-SGD / Choco-Gossip (Koloskova et al., ICML 2019) and DeepSqueeze (Tang et al., 2019), which maintain full-model neighbor replicas or error buffers and require tuning an additional consensus stepsize gamma.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 556 PowerGossip verified: E[err1]=11.970204 <= (1-rho*delta)*err0=12.235657, err_power=0.118779 < err_rand=49.070122
```
