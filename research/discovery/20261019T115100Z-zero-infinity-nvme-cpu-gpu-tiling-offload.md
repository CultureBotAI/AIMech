# Discovery Report: Round 628 — ZeRO-Infinity

- **Timestamp**: `2026-10-19T11:51:00Z`
- **Selected Concept**: `AIMech:ZeROInfinityHeterogeneousExtremeScaleTraining` (*ZeRO-Infinity*)
- **Record Path**: `data/curated/ZeROInfinityHeterogeneousExtremeScaleTraining.yaml`
- **Primary Source**: Samyam Rajbhandari, Olatunji Ruwase, Jeff Rasley, Shaden Smith, Yuxiong He — *ZeRO-Infinity: Breaking the GPU Memory Wall for Extreme Scale Deep Learning* (`https://dblp.org/rec/conf/sc/RajbhandariRRSH21`).

## Identity & Boundary Resolution

Distinct from ZeRO-Offload (which builds on ZeRO-2, replicates FP16 parameters on every GPU, uses single-owner broadcast limiting offload bandwidth to one PCIe link, and cannot offload to NVMe), from GPU-only ZeRO-3, and from 3D Parallelism (which requires manual tensor-slicing model parallelism and pipeline-stage refactoring and is bounded by aggregate GPU HBM capacity).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 628 ZeRO-Infinity verified: mswm_1T=9.7656GiB, ait_err=0.00e+00, eff_70GBs=0.9704, eff_4x_match_err=0.00e+00, tiling_err=4.44e-16, tiling_mem_reduction=4.0x, node_cpu_bw=48.0GB/s, nvme_64node_gain=133.3x
```
