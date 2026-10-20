# Discovery Report: Round 670 — S-LoRA

- **Timestamp**: `2026-10-19T12:33:00Z`
- **Selected Concept**: `AIMech:SLoRA` (*S-LoRA*)
- **Record Path**: `data/curated/SLoRA.yaml`
- **Primary Source**: Ying Sheng, Shiyi Cao, Dacheng Li, Coleman Hooper, Nicholas Lee, Shuo Yang, Christopher Chou, Banghua Zhu, Lianmin Zheng, Kurt Keutzer, Joseph E. Gonzalez, Ion Stoica — *S-LoRA: Serving Thousands of Concurrent LoRA Adapters* (`https://dblp.org/search/publ/api?q=S-LoRA+Serving+Thousands+Concurrent+LoRA+Adapters&format=xml`).

## Identity & Boundary Resolution

Distinct from AIMech:LowRankAdaptation (LoRA), which merges a single adapter W' = W + A B into the base weights and incurs prohibitive weight duplication or serial swapping latency when serving many concurrent adapters, and from AIMech:PagedAttention, which pages only KV cache tensors for a single static weight set. S-LoRA (Ying Sheng, Shiyi Cao, Dacheng Li, Coleman Hooper, Nicholas Lee, Shuo Yang, Christopher Chou, Banghua Zhu, Lianmin Zheng, Kurt Keutzer, Joseph E. Gonzalez, and Ion Stoica, MLSys 2024, arXiv:2311.03285) stores thousands of LoRA adapters in host RAM and dynamically prefetches active adapters into GPU memory. Because a per-layer KV cache tensor has shape (S, H) and a LoRA weight matrix has shape (R, H) sharing the hidden dimension H, S-LoRA allocates both from a unified memory pool partitioned into pages of H elements (where sequence length S uses S pages and rank R uses R pages). Custom Triton/CUDA kernels—Multi-size Batched Gather Matrix-Matrix Multiplication (MBGMM) for prefill and Multi-size Batched Gather Matrix-Vector Multiplication (MBGMV) for decode—compute x A B directly over non-contiguous pages across heterogeneous ranks R without padding, while S-LoRA Tensor Parallelism restricts added multi-GPU communication to 5(N-1)Br/N elements.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 670 S-LoRA (Sheng et al., MLSys 2024): mbgmv_err=4.44e-16, tp_comm_ratio=0.00977<0.01, opt_reward=2.7300>fcfs=2.2500&lcfs=2.6500
```
