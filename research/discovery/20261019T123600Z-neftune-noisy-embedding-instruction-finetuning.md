# Discovery Report: Round 673 — NEFTune

- **Timestamp**: `2026-10-19T12:36:00Z`
- **Selected Concept**: `AIMech:NEFTune` (*NEFTune*)
- **Record Path**: `data/curated/NEFTune.yaml`
- **Primary Source**: Neel Jain, Ping-yeh Chiang, Yuxin Wen, John Kirchenbauer, Hong-Min Chu, Gowthami Somepalli, Brian R. Bartoldson, Bhavya Kailkhura, Avi Schwarzschild, Aniruddha Saha, Micah Goldblum, Jonas Geiping, Tom Goldstein — *NEFTune: Noisy Embeddings Improve Instruction Finetuning* (`https://dblp.org/search/publ/api?q=NEFTune+Noisy+Embeddings+Improve+Instruction+Finetuning&format=xml`).

## Identity & Boundary Resolution

Distinct from adversarial embedding perturbation methods such as FreeLB (which require inner-loop gradient ascent steps to compute worst-case adversarial perturbations) and from parameter-space noise injection or dropout. NEFTune (Noisy Embedding Instruction Fine Tuning; Neel Jain, Ping-yeh Chiang, Yuxin Wen, John Kirchenbauer, Hong-Min Chu, Gowthami Somepalli, Brian R. Bartoldson, Bhavya Kailkhura, Avi Schwarzschild, Aniruddha Saha, Micah Goldblum, Jonas Geiping, & Tom Goldstein, ICLR 2024, arXiv:2310.05914) samples a single zero-overhead random vector epsilon ~ Uniform(-1, 1)^{B x L x d} per forward pass and computes X'_emb = X_emb + (alpha / sqrt(L d)) epsilon (Algorithm 1). Because E[epsilon_{t,j}^2] = 1/3, the perturbation has expected Euclidean norm alpha / sqrt(3) independent of sequence length L and embedding dimension d, reducing overfitting to the exact phrasing and length formatting of small instruction datasets without degrading factual knowledge or token-level nearest-neighbor semantics.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 673 NEFTune (Jain et al., ICLR 2024): rms_norm=2.8868~alpha/sqrt(3)=2.8868, hessian_reg_gap=0.0150, token_flips=0/64
```
