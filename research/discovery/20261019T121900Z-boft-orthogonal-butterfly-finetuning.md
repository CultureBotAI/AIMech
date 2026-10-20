# Discovery Report: Round 656 — Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization (BOFT)

- **Timestamp**: `2026-10-19T12:19:00Z`
- **Selected Concept**: `AIMech:BoftOrthogonalButterflyFinetuning` (*Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization (BOFT)*)
- **Record Path**: `data/curated/BoftOrthogonalButterflyFinetuning.yaml`
- **Primary Source**: Weiyang Liu, Zeju Qiu, Yao Feng, Yuliang Xiu, Yuxuan Xue, Longhui Yu, Haiwen Feng, Zhen Liu, Juyeon Heo, Songyou Peng, Yandong Wen, Michael J. Black, Adrian Weller, Bernhard Schölkopf — *Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization* (`https://dblp.org/rec/conf/iclr/LiuQFXXYF0HPWBW24.html`).

## Identity & Boundary Resolution

Distinct from additive low-rank adapters such as LoRA (Hu et al., 2022) and DoRA (Liu et al., 2024), which add a low-rank update W_0 + B A that alters pairwise neuron angles (hyperspherical energy) rather than multiplying W^0 by an exact orthogonal matrix R^T R = I_d. Also distinct from single-stage block-diagonal Orthogonal Finetuning (OFT, Qiu et al., 2023), which corresponds to the degenerate m = 1 special case of BOFT and cannot mix coordinates across distinct b-dimensional blocks.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 656 BOFT boundary and mathematical verification succeeded.
```
