# Discovery Report: Round 663 — FourierFT

- **Timestamp**: `2026-10-19T12:26:00Z`
- **Selected Concept**: `AIMech:FourierFT` (*FourierFT*)
- **Record Path**: `data/curated/FourierFT.yaml`
- **Primary Source**: Ziqi Gao, Qichao Wang, Aochuan Chen, Zijing Liu, Bingzhe Wu, Liang Chen, Jia Li — *Parameter-Efficient Fine-Tuning with Discrete Fourier Transform* (`https://dblp.org/rec/conf/icml/GaoWC0WCL24.xml`).

## Identity & Boundary Resolution

Distinct from AIMech:LowRankAdaptation (LoRA) and AIMech:VeRA, which parameterize weight updates directly in the spatial domain via low-rank matrix products and therefore require at least O(d_1 + d_2) parameters or high rank to represent complex spatial patterns. FourierFT (Ziqi Gao, Qichao Wang, Aochuan Chen, Zijing Liu, Bingzhe Wu, Liang Chen, and Jia Li, ICML 2024, PMLR v235, arXiv:2405.03003) represents the weight update Delta_W in R^{d_1 x d_2} in the orthogonal 2D Fourier basis. A fixed entry index table E in {0, ..., d_1-1} x {0, ..., d_2-1} of length n << d_1 d_2 is sampled once (uniformly or with a central-frequency radial Gaussian bias), a trainable coefficient vector c in R^n is scattered into a sparse spectral matrix S = ToMatrix(c) in R^{d_1 x d_2} at locations E, and the spatial weight update is reconstructed via the 2D inverse discrete Fourier transform Delta_W = alpha * Re(F^{-1}(ToMatrix(c))). Because every spectral coefficient modulates a global 2D complex sinusoid across all d_1 x d_2 spatial entries, FourierFT decouples parameter count n from layer dimensions (d_1, d_2) and can generate full-rank spatial updates when the sampled frequencies span rows and columns.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 663 FourierFT (Gao et al. 2024): params_fourier=8<params_lora_r1=16, rank_fourier=6>rank_lora=1, max_grad_err=2.36e-07
```
