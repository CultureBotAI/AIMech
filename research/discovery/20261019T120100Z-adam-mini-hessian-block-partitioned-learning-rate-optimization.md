# Discovery Report: Round 638 — Adam-mini (Hessian-Block-Partitioned Learning Rate Optimization)

- **Timestamp**: `2026-10-19T12:01:00Z`
- **Selected Concept**: `AIMech:AdamMiniHessianBlockPartitionedLearningRateOptimization` (*Adam-mini (Hessian-Block-Partitioned Learning Rate Optimization)*)
- **Record Path**: `data/curated/AdamMiniHessianBlockPartitionedLearningRateOptimization.yaml`
- **Primary Source**: Yushun Zhang, Congliang Chen, Ziniu Li, Tian Ding, Chenwei Wu, Diederik P. Kingma, Yinyu Ye, Zhi-Quan Luo, Ruoyu Sun — *Adam-mini: Use Fewer Learning Rates To Gain More* (`https://dblp.org/rec/conf/iclr/ZhangCLD0K0L025`).

## Identity & Boundary Resolution

Distinct from NovoGrad (AIMech:NovoGrad), which partitions parameters coarsely by entire PyTorch layers (causing training instability on billion-parameter Transformers) and normalizes the current gradient before accumulating first-order momentum; Adam-mini partitions Transformer parameters by smallest dense Hessian sub-blocks (heads for Query/Key, output neurons for Value/Attn.Proj/MLP, and tokens for Embedding/Output) and retains standard AdamW first-order momentum m_b while averaging g_b (.) g_b per block. Distinct from LAMB (AIMech:LambLayerwiseAdaptiveLargeBatchOptimization), which retains full coordinate-wise v in R^d alongside layerwise trust-ratio scaling and saves zero memory.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 638 Adam-mini verified: dense_tau=0.505, r_adam=1.18>r_mini=1.00, v_removed=99.9827%, state_saving=49.99%, block_lr_ratio=2.360
```
