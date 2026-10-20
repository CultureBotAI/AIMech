# Discovery Report: Round 627 — ZeRO-Offload

- **Timestamp**: `2026-10-19T11:50:00Z`
- **Selected Concept**: `AIMech:ZeROOffloadHeterogeneousLargeModelTraining` (*ZeRO-Offload*)
- **Record Path**: `data/curated/ZeROOffloadHeterogeneousLargeModelTraining.yaml`
- **Primary Source**: Jie Ren, Samyam Rajbhandari, Reza Yazdani Aminabadi, Olatunji Ruwase, Shuangyan Yang, Minjia Zhang, Dong Li, Yuxiong He — *ZeRO-Offload: Democratizing Billion-Scale Model Training* (`https://dblp.org/rec/conf/usenix/0015RARYZ0H21`).

## Identity & Boundary Resolution

Distinct from GPU-only model-state sharding (ZeRO-1/2/3, which require aggregate GPU memory to hold all model states), from layer-to-layer weight swapping (L2L, which keeps optimizer compute on GPU, incurs 28M CPU-GPU communication per step, and cannot scale across multiple GPUs), and from ZeRO-Infinity (which builds on ZeRO-3 to partition parameters and offload to NVMe plus CPU with memory-centric tiling).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 627 ZeRO-Offload verified: min_comm_vol=4.0M, max_mem_reduction=8.0x, valid_4M_cuts=3, zero2_cpu_speedup_16gpu=16.0x, dpu_throughput_gain=1.45x, dpu_final_loss=1.14e-10
```
