# Discovery Report: Round 666 — LoRA-FA

- **Timestamp**: `2026-10-19T12:29:00Z`
- **Selected Concept**: `AIMech:LoRAFA` (*LoRA-FA*)
- **Record Path**: `data/curated/LoRAFA.yaml`
- **Primary Source**: Longteng Zhang, Lin Zhang, Shaohuai Shi, Xiaowen Chu, Bo Li — *LoRA-FA: Memory-Efficient Low-Rank Adaptation for Large Language Models Fine-Tuning* (`https://dblp.org/search/publ/api?q=LoRA-FA+Longteng+Zhang&format=xml`).

## Identity & Boundary Resolution

Distinct from AIMech:LowRankAdaptation (LoRA), which updates both A in R^{d_{in} x r} and B in R^{r x d_{out}} and must retain the full input activation tensor X in R^{b x s x d_{in}} in GPU memory to compute dL/dA = (alpha/r) X^T (dL/dY) B^T during backpropagation, and from AIMech:LoraPlusEfficientLowRankAdaptationWithAsymmetricLearningRates (LoRA+), which still updates both A and B with asymmetric learning rates. LoRA-FA (Longteng Zhang, Lin Zhang, Shaohuai Shi, Xiaowen Chu, and Bo Li, arXiv:2308.03303) proves that stacked linear low-rank updates collapse to single-layer linear regression within the column space of A_0 (Theorem 3.1) and derives the closed-form gradient correction g^B = (r/alpha)^2 (A^T A)^{-1} g^B_{LoRA-FA} (Theorem 4.1) that minimizes the Frobenius norm discrepancy ||(alpha/r) A g^B - g||_F^2 against the full-fine-tuning gradient g while guaranteeing dL <= 0. Because A is frozen, only the r-dimensional intermediate activation X A in R^{b x s x r} (2bsr bytes instead of 2bsd + 2bsr bytes) is stored for backpropagation, and K = (A^T A)^{-1} in R^{r x r} is precomputed once at initialization.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 666 LoRA-FA (Zhang et al. 2023): E_res=21.0, err_opt=72.4186<err_raw=56250.7211, dL=-0.2297<0, act_savings=18.0GB
```
