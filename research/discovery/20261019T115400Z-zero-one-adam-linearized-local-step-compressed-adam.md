# Discovery Report: Round 631 — 0/1 Adam (Linearized Adaptive-Freezing and Local-Step Compressed Adam)

- **Timestamp**: `2026-10-19T11:54:00Z`
- **Selected Concept**: `AIMech:ZeroOneAdamLinearizedLocalStepCompressedAdam` (*0/1 Adam (Linearized Adaptive-Freezing and Local-Step Compressed Adam)*)
- **Record Path**: `data/curated/ZeroOneAdamLinearizedLocalStepCompressedAdam.yaml`
- **Primary Source**: Yucheng Lu, Conglong Li, Minjia Zhang, Christopher De Sa, Yuxiong He — *Maximizing Communication Efficiency for Large-scale Training via 0/1 Adam* (`https://dblp.org/rec/conf/iclr/LuLZSH23`).

## Identity & Boundary Resolution

Distinct from 1-bit Adam (AIMech:OneBitAdamErrorCompensatedPreconditionedMomentum, Tang et al. 2021), which is a special case of Algorithm 4 with T_v = {0, ..., T_0 - 1} and T_u = {0, ..., T - 1} (requiring a long continuous full-precision warmup stage that can take >50% of wall-clock training time and disallowing local steps). Distinct from Qsparse-local-SGD (Basu et al. 2019) and Local SGD (Stich 2018), which apply local steps to linear SGD without adaptive second-moment preconditioning or linear momentum state reconstruction from compressed trajectory buffers.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 631 0/1 Adam verified: tv_count=148, max_m_bound=2301, sync_err=2.22e-16, lemma4_ratio=0.1469<=1, vol_red=0.8716
```
