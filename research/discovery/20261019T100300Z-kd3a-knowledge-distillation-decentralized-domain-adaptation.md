# Discovery Report: Round 520 — KD3A (Knowledge Distillation Based Decentralized Domain Adaptation)

- **Timestamp**: `2026-10-19T10:03:00Z`
- **Selected Concept**: `AIMech:Kd3aKnowledgeDistillationBasedDecentralizedDomainAdaptation` (*KD3A (Knowledge Distillation Based Decentralized Domain Adaptation)*)
- **Record Path**: `data/curated/Kd3aKnowledgeDistillationBasedDecentralizedDomainAdaptation.yaml`
- **Primary Source**: Haozhe Feng, Zhaoyang You, Minghao Chen, Tianye Zhang, Minfeng Zhu, Fei Wu, Chao Wu, Wei Chen — *KD3A: Unsupervised Multi-Source Decentralized Domain Adaptation via Knowledge Distillation* (`https://dblp.org/rec/conf/icml/FengYCZZWWC21`).

## Identity & Boundary Resolution

Introduced by Hao-zhe Feng, Zhaoyang You, Minghao Chen, Tianye Zhang, Minfeng Zhu, Fei Wu, Chao Wu, and Wei Chen in 'KD3A: Unsupervised Multi-Source Decentralized Domain Adaptation via Knowledge Distillation' (ICML 2021, PMLR 139:3274-3283; arXiv:2011.09757). Distinct from FADA (Peng et al. ICLR 2020), which requires batch-level feature and gradient synchronization (100x higher communication cost) for adversarial domain alignment and K-means gap-statistics attention; and distinct from single-source hypothesis transfer SHOT (Liang et al. ICML 2020), which lacks multi-source Knowledge Vote, Consensus Focus marginal-contribution weighting, and BatchNorm MMD alignment.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 520 KD3A (Feng et al. 2021): fig1b_vote=(0.91,0.09,n=2), CF=[2.68, 2.65, 0.0], alpha_CF2=0.000, bn_mmd_opt=0.0622<0.1422
```
