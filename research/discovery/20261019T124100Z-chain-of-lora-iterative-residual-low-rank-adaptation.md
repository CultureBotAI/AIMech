# Discovery Report: Round 678 — Chain of LoRA

- **Timestamp**: `2026-10-19T12:41:00Z`
- **Selected Concept**: `AIMech:ChainOfLoRA` (*Chain of LoRA*)
- **Record Path**: `data/curated/ChainOfLoRA.yaml`
- **Primary Source**: Wenhan Xia, Chengwei Qin, Elad Hazan — *Chain of LoRA: Efficient Fine-tuning of Language Models via Residual Learning* (`https://dblp.org/rec/conf/icml/XiaQH24.xml`).

## Identity & Boundary Resolution

Distinct from standard LoRA (AIMech:LoRA, which optimizes a single pair of low-rank matrices B and A whose update rank is bounded above by a single rank r), from AdaLoRA (AIMech:AdaLoRA, which dynamically prunes singular values within a single SVD-parameterized adapter during training rather than chaining and merging successive residual low-rank updates), and from rsLoRA (AIMech:RsLoRA, which modifies the scaling factor alpha / sqrt(r) of a single high-rank LoRA module rather than constructing a high-rank update via a sequential chain of low-rank residual steps). Formulated by Xia, Qin, and Hazan (ICML 2024, PMLR 235:54088-54099, arXiv:2401.04151).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 678 Chain of LoRA (Xia et al., ICML 2024): err_M1=5.0140->M2=1.7000->M3=1.08e-15, stepdown_err=1.7000<lora_r3=3.0232 (flops 11<15)
```
