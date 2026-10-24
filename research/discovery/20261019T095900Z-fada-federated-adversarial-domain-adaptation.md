# Discovery Report: Round 516 — FADA (Federated Adversarial Domain Adaptation)

- **Timestamp**: `2026-10-19T09:59:00Z`
- **Selected Concept**: `AIMech:FadaFederatedAdversarialDomainAdaptation` (*FADA (Federated Adversarial Domain Adaptation)*)
- **Record Path**: `data/curated/FadaFederatedAdversarialDomainAdaptation.yaml`
- **Primary Source**: Xingchao Peng, Zijun Huang, Yizhe Zhu, Kate Saenko — *Federated Adversarial Domain Adaptation* (`https://dblp.org/rec/conf/iclr/PengHZS20`).

## Identity & Boundary Resolution

Introduced by Xingchao Peng, Zijun Huang, Yizhe Zhu, and Kate Saenko in 'Federated Adversarial Domain Adaptation' (ICLR 2020; arXiv:1911.02054). Distinct from centralized multi-source domain adaptation methods (DCTN, Xu et al. CVPR 2018; M3SDA, Peng et al. ICCV 2019; MDAN, Zhao et al. NeurIPS 2018), which require direct co-location of source and target domain examples on a single machine; and distinct from FedBN (Li et al. ICLR 2021), which handles feature shift across labeled federated clients via local batch normalization rather than adapting multiple labeled source clients to an unlabeled target client via dynamic attention and MINE feature disentanglement.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 516 FADA (Peng et al. 2020): d_H_mix=0.378<=weighted=0.378, dyn_w0=0.981>>dyn_w2=0.0007, MINE_corr=0.310>>MINE_indep=-0.364
```
