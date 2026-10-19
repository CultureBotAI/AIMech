# Discovery Report: Round 255 — Atomic Norm Convex Geometry and Tangent Cone Gaussian Width for Linear Inverse Problems

- **Timestamp**: `2026-10-19T01:32:00Z`
- **Selected Concept**: `AIMech:AtomicNormConvexGeometryAndTangentConeGaussianWidthForLinearInverseProblems` (*Atomic Norm Convex Geometry and Tangent Cone Gaussian Width for Linear Inverse Problems*)
- **Record Path**: `data/curated/AtomicNormConvexGeometryAndTangentConeGaussianWidthForLinearInverseProblems.yaml`
- **Primary Source**: Venkat Chandrasekaran, Benjamin Recht, Pablo A. Parrilo, and Alan S. Willsky (2012), *The Convex Geometry of Linear Inverse Problems*, *Foundations of Computational Mathematics* 12(6):805-849 (`arXiv:1012.0621v3`, `DOI:10.1007/s10208-012-9135-7`).

## Identity & Boundary Resolution

`AIMech:AtomicNormConvexGeometryAndTangentConeGaussianWidthForLinearInverseProblems` was checked against all 442 pinned AIO concepts and 649 maintained AIMech concepts:

1. **`AIMech:RestrictedIsometryPropertyForCompressedSensing`**: Analyzes uniform restricted isometries over $s$-sparse coordinate subspaces for $\ell_1$ minimization, whereas Chandrasekaran et al. (2012) establish the general atomic-norm gauge $\|x\|_{\mathcal{A}}$, tangent/normal cone polarity $T_{\mathcal{A}}(x^\star) = N_{\mathcal{A}}(x^\star)^*$, and polar normal-cone distance bound $w(T_{\mathcal{A}}(x^\star) \cap \mathbb{S}^{p-1}) \le \mathbb{E}_g[\operatorname{dist}(g, N_{\mathcal{A}}(x^\star))]$ across arbitrary compact atomic sets.
2. **`AIMech:NuclearNormConvexRelaxationForMatrixCompletion`**: Specializes to nuclear-norm entry sampling under coherence conditions, whereas Chandrasekaran et al. (2012) unify sparse vectors, low-rank matrices, sign vectors, orthogonal matrices, permutation matrices, and semidefinite theta-body relaxations $\mathrm{TH}_k(I)$ of real algebraic varieties.

## Constructed Boundary & Regime Verification

```text
Chandrasekaran et al. (2012) atomic norm & Gaussian width verified: l1 w^2(p=100,s=5)=20.39 (MC=20.38, bound=36.21); linf k-face sum=40.0==40; O(12) w^2=105.0; Moreau residual<1e-10.
```

Verified analytically and via Monte Carlo: (1) on the l_inf k-face cone T_A(x*) = (-R_+)^{p-k} x R^k and its polar N_A(x*) = R_+^{p-k} x {0}^k, Moreau orthogonal decomposition g = Pi_N(g) + Pi_T(g) holds to < 1e-12 with E[dist(g, N)^2] = (p+k)/2, E[dist(g, T)^2] = (p-k)/2, and exact sum p = 40.0 (Lemma 3.7, Corollary 3.8, Proposition 3.12); (2) for s=5 sparse vectors in R^{100}, the exact normal-cone variational integral inf_t E[dist(g, N)^2] = 20.39 matches Monte Carlo (20.38) and lies strictly below the closed-form Proposition 3.10 bound 2*s*log(p/s) + (5/4)*s = 36.21; (3) for orthogonal matrices O(m) at X* = I_m, dim(so(m)) + (1/2)dim(Sym_m) = (3m^2 - m)/4 = 105.0 at m=12 (Proposition 3.13); and (4) Moreau proximal/dual-ball decomposition x = Pi_A(x; mu) + Lambda_A(x; mu) and <x - Pi_A(x; mu), Pi_A(x; mu)> = mu ||Pi_A(x; mu)||_A hold to < 1e-10 for both A_{l1} and A_{linf} (Section 5, Eqs. 18-29).
