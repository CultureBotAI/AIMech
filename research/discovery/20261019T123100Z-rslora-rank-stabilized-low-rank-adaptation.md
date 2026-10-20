# Discovery Report: Round 668 — rsLoRA

- **Timestamp**: `2026-10-19T12:31:00Z`
- **Selected Concept**: `AIMech:RsLoRA` (*rsLoRA*)
- **Record Path**: `data/curated/RsLoRA.yaml`
- **Primary Source**: Damjan Kalajdzievski — *A Rank Stabilization Scaling Factor for Fine-Tuning with LoRA* (`https://dblp.org/search/publ/api?q=Rank+Stabilization+Scaling+Factor+LoRA+Kalajdzievski&format=xml`).

## Identity & Boundary Resolution

Distinct from AIMech:LowRankAdaptation (LoRA), which scales the adapter product B A by gamma_r = alpha / r and consequently suffers an O(1/r) collapse in effective update magnitude and gradient norms as r grows, and from AIMech:LoraPlusEfficientLowRankAdaptationWithAsymmetricLearningRates (LoRA+), which addresses the width-d asymmetry between A and B via unequal learning rates eta_B = lambda eta_A. rsLoRA (Damjan Kalajdzievski, arXiv:2312.03732) analyzes the infinite-rank limit r -> infinity of an adapter x_{out} = (W + gamma_r B A) x_{in} + b initialized with B_0 = 0 and A_{i,j} ~ N(0, sigma_A^2) independent of r. Theorem 3.2 proves that after n gradient steps, E_{A_0}[gamma_r B_n A_n] = -gamma_r^2 r sigma_A eta sum_{k=0}^{n-1} v_k x_k^T + O_r(gamma_r^3 r), so both the m-th forward activation moments and the backpropagated input gradients are Theta_r((gamma_r^2 r)^m), which is non-collapsing and stable (Theta_r(1)) if and only if gamma_r in Theta_r(1 / sqrt(r)).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 668 rsLoRA (Kalajdzievski 2023): lora_collapse_r4/r64=15.32x vs rslora_ratio=1.01x, loss_rslora_r8=0.2276<loss_lora_r8=2.1900
```
