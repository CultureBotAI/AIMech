# Discovery Report: Round 688 — NOLA

- **Timestamp**: `2026-10-19T12:51:00Z`
- **Selected Concept**: `AIMech:NOLA` (*NOLA*)
- **Record Path**: `data/curated/NOLA.yaml`
- **Primary Source**: Soroush Abbasi Koohpayegani, K. L. Navaneet, Parsa Nooralinejad, Soheil Kolouri, Hamed Pirsiavash — *NOLA: Compressing LoRA using Linear Combination of Random Basis* (`https://dblp.org/search/publ/api?q=2310.02556&format=xml`).

## Identity & Boundary Resolution

Distinct from standard LoRA (AIMech:LoRA, whose parameter count r(m + n) is lower-bounded by m + n at rank r = 1 and tied to layer dimensions), from VeRA (AIMech:VeraVectorBasedRandomMatrixAdaptation, which scales a single random matrix pair via diagonal vectors d in R^m and b in R^r whose parameter count still depends on layer dimension m and rank r), and from PRANC (which forms a direct linear combination of full m x n random matrices requiring O(k d^2) compute and spanning only a k-dimensional linear subspace rather than NOLA's O(k d r) compute and bilinear cross-basis subspace). Formulated by Koohpayegani, Navaneet, Nooralinejad, Kolouri, and Pirsiavash (ICLR 2024, arXiv:2310.02556).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 688 NOLA (Koohpayegani et al., ICLR 2024): params=12<rank1_LoRA=32, rank(dW)=4, subspace_rank(NOLA)=36>>subspace_rank(PRANC)=12, speedup=42.0x
```
