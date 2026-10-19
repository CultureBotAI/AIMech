# Discovery Report: Round 256 — Tensor Spectral Decomposition of Centered 3-Star Graph Moments for Dirichlet Mixed-Membership Community Models

- **Timestamp**: `2026-10-19T01:42:00Z`
- **Selected Concept**: `AIMech:TensorSpectralDecompositionForDirichletMixedMembershipCommunityModels` (*Tensor Spectral Decomposition of Centered 3-Star Graph Moments for Dirichlet Mixed-Membership Community Models*)
- **Record Path**: `data/curated/TensorSpectralDecompositionForDirichletMixedMembershipCommunityModels.yaml`
- **Primary Source**: Animashree Anandkumar, Rong Ge, Daniel Hsu, and Sham M. Kakade (2014), *A Tensor Approach to Learning Mixed Membership Community Models*, *Journal of Machine Learning Research* 15(66):2239-2312 (`arXiv:1302.2684v4`).

## Identity & Boundary Resolution

`AIMech:TensorSpectralDecompositionForDirichletMixedMembershipCommunityModels` was checked against all 442 pinned AIO concepts and 650 maintained AIMech concepts:

1. **`AIMech:OrthogonalTensorPowerMethodForLatentVariableModels`**: Analyzes exchangeable single-object multi-view latent variable models, whereas Anandkumar, Ge, Hsu, & Kakade (2014) formulate 5-way vertex-partitioned $\alpha_0$-centered 3-star subgraph count tensors for dyadic networks where edges couple pairs of Dirichlet memberships.
2. **`AIMech:MixedMembershipStochasticBlockmodel`**: Defines the generative Dirichlet MMSB and nested variational EM inference without tensor spectral moment centering or polynomial-time $\ell_1$/$\ell_\infty$ recovery guarantees.

## Constructed Boundary & Regime Verification

```text
Anandkumar et al. (2014) tensor MMSB verified: E[psi psi^T] err=2.98e-16, 3-star centering err=1.67e-16, tensor power eig err=8.88e-16 (lambdas=[2.2361, 1.7321, 1.4639]), E[Q' Pi^T] err=2.60e-16.
```

Verified in pure Python: (1) for alpha = (0.3, 0.5, 0.7) (alpha_0 = 1.5), the whitened membership vector psi_u (Eq. 18) satisfies ||E[psi_u psi_u^T] - I_3||_F = 2.98e-16 and the centered 3-star tensor formula (Eq. 15, normalized by the factor 2 from Proposition C.2 Eq. 96) cancels all off-diagonal Dirichlet cross-terms to 1.67e-16; (2) multi-partition SVD whitening W_A, alignment R_{A,B}, R_{A,C} (Lemma 3.1, Eq. 21), and deflated tensor power iteration (Procedure 2) recover the exact eigenvalues lambda_i = alpha_hat_i^{-1/2} = (2.2361, 1.7321, 1.4639) to 8.88e-16; and (3) the linear pseudo-inverse matrix Q' (Section 3.3, Appendix B.3) satisfies ||E_Pi[Q' Pi^T] - I_3||_F = 2.60e-16.
