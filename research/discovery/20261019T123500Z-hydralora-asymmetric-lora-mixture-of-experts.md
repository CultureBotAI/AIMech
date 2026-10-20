# Discovery Report: Round 672 — HydraLoRA

- **Timestamp**: `2026-10-19T12:35:00Z`
- **Selected Concept**: `AIMech:HydraLoRA` (*HydraLoRA*)
- **Record Path**: `data/curated/HydraLoRA.yaml`
- **Primary Source**: Chunlin Tian, Zhan Shi, Zhijiang Guo, Li Li, Cheng-Zhong Xu — *HydraLoRA: An Asymmetric LoRA Architecture for Efficient Fine-Tuning* (`https://dblp.org/search/publ/api?q=HydraLoRA+Asymmetric+LoRA+Architecture&format=xml`).

## Identity & Boundary Resolution

Distinct from AIMech:LowRankAdaptation (monolithic single-pair B A), AIMech:MELoRA (block-diagonal concatenation of independent mini-adapters (A_i, B_i) along partitioned input/output dimensions without dynamic gating), and symmetric LoRA-MoE / LoraHub architectures that maintain N separate (A_i, B_i) pairs. HydraLoRA (Chunlin Tian, Zhan Shi, Zhijiang Guo, Li Li, & Cheng-Zhong Xu, NeurIPS 2024, arXiv:2404.19245) is motivated by the empirical observation (Section 2.3, Figure 3) that when multiple LoRA heads are trained on distinct sub-domains, their down-projection matrices A converge to overlapping representations capturing shared corpus knowledge while their up-projection matrices B diverge to capture sub-domain specificities. HydraLoRA shares one central matrix A in R^{r x k} across all samples and deploys N expert matrices B_i in R^{d x r} (where N can be chosen automatically via TF-IDF + k-means elbow clustering on heterogeneous corpora) weighted by router scores omega_i = softmax(W_g^T x)_i (Equations 2-4).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 672 HydraLoRA (Tian et al., NeurIPS 2024): param_saving=0.375, merge_err=6.78e-16, loss_hydra=0.0514<<loss_monolithic=32.1526
```
