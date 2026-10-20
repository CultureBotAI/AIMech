# Discovery Report: Round 537 — Lagrange Coded Computing for Straggler-Resilient, Byzantine-Secure, and T-Private Distributed Polynomial Evaluation

- **Timestamp**: `2026-10-19T10:20:00Z`
- **Selected Concept**: `AIMech:LagrangeCodedComputingForResilientSecureAndPrivateDistributedLearning` (*Lagrange Coded Computing for Straggler-Resilient, Byzantine-Secure, and T-Private Distributed Polynomial Evaluation*)
- **Record Path**: `data/curated/LagrangeCodedComputingForResilientSecureAndPrivateDistributedLearning.yaml`
- **Primary Source**: Qian Yu, Songze Li, Netanel Raviv, Seyed Mohammadreza Mousavi Kalan, Mahdi Soltanolkotabi, A. Salman Avestimehr — *Lagrange Coded Computing: Optimal Design for Resiliency, Security, and Privacy* (`https://dblp.org/rec/conf/aistats/YuLRKSA19.xml`).

## Identity & Boundary Resolution

Distinct from Gradient Coding for Straggler-Resilient Distributed Optimization (AIMech:GradientCodingForStragglerResilientDistributedOptimization, which linearly encodes partial gradients computed on uncoded replicated data blocks without data privacy or general polynomial universality) and from DRACO (AIMech:DracoByzantineResilientDistributedTrainingViaRedundantGradients, which treats gradient evaluation as a black-box function requiring a 2A + 1 multiplicative redundancy factor rather than a 2A additive worker overhead). Lagrange Coded Computing / LCC (Yu et al., AISTATS 2019, PMLR 89:1215-1225 / arXiv:1806.00939, Section III-IV, Theorems 1-2, Equation 2, pp. 4-6) fixes K + T distinct interpolation nodes beta_1, ..., beta_{K+T} in F_q and constructs the degree-(K+T-1) Lagrange polynomial u(z) = sum_{j=1}^K X_j prod_{k != j} (z - beta_k)/(beta_j - beta_k) + sum_{j=K+1}^{K+T} Z_j prod_{k != j} (z - beta_k)/(beta_j - beta_k), assigning worker i the single coded share tilde{X}_i = u(alpha_i). Each worker computes tilde{Y}_i = f(tilde{X}_i) = f(u(alpha_i)), an evaluation of a composed polynomial of degree at most (K + T - 1) deg(f), enabling the master to recover {f(X_j) = f(u(beta_j))}_{j=1}^K from any N - S responding workers with up to A Byzantine errors whenever N >= (K + T - 1) deg(f) + S + 2A + 1.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 537 LCC verified: N_min=8, T=1 uniform-privacy=17/17, decoded=[2, 16]==[2, 16], R_LCC=7 << R_GC=31
```
