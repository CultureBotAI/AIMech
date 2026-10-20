# Discovery Report: Round 684 — Flora Gradient Compression

- **Timestamp**: `2026-10-19T12:47:00Z`
- **Selected Concept**: `AIMech:FloraGradientCompression` (*Flora Gradient Compression*)
- **Record Path**: `data/curated/FloraGradientCompression.yaml`
- **Primary Source**: Yongchang Hao, Yanshuai Cao, Lili Mou — *Flora: Low-Rank Adapters Are Secretly Gradient Compressors* (`https://dblp.org/rec/conf/icml/HaoCM24.xml`).

## Identity & Boundary Resolution

Distinct from standard LoRA (AIMech:LoRA, which maintains two explicit adapter matrices B and A whose total weight change is confined to a fixed rank-r subspace), from federated FLoRA (AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation, which stacks heterogeneous-rank client LoRA adapters on a federated server), from GaLore (AIMech:GaLoreGradientLowRankProjection, which computes costly singular value decompositions of gradients and stores explicit projection matrices rather than regenerating Gaussian random projections on the fly from scalar random seeds and transferring momentum via M_{t,W} A_{t,W} (A'_W)^T), and from ReLoRA (AIMech:ReLoRA, which requires an initial full-rank warm-start phase and periodic LoRA merge-and-reinit restarts). Formulated by Hao, Cao, and Mou (ICML 2024, PMLR 235:17554-17571, arXiv:2402.03293).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 684 Flora (Hao et al., ICML 2024): thm21_err=(2.28e-16,1.27e-17), rank_fixed=2->rank_flora=8, err_fixed=8.2564->err_flora=0.7873
```
