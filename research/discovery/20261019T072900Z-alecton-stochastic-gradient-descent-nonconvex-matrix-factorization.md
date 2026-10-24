# Discovery Report: Round 366 — Alecton Riemannian-Rescaled Stochastic Gradient Descent for Non-Convex Low-Rank Matrix Problems

- **Timestamp**: `2026-10-19T07:29:00Z`
- **Selected Concept**: `AIMech:AlectonStochasticGradientDescentForNonconvexLowRankMatrixProblems` (*Alecton Riemannian-Rescaled Stochastic Gradient Descent for Non-Convex Low-Rank Matrix Problems*)
- **Record Path**: `data/curated/AlectonStochasticGradientDescentForNonconvexLowRankMatrixProblems.yaml`
- **Primary Source**: Christopher De Sa, Kunle Olukotun, Christopher Re — *Global Convergence of Stochastic Gradient Descent for Some Non-convex Matrix Problems* (`https://proceedings.mlr.press/v37/sa15.html`).

## Identity & Boundary Resolution

Distinct from AIMech:BurerMonteiroLowRankSemidefiniteProgrammingAndRiemannianStaircase (Round 336), which classifies deterministic second-order critical points of smooth semidefinite programs with linear constraints <A_i, Y Y^T> = b_i, and from AIMech:StreamingPCANearOptimalFiniteSampleOjaAlgorithm (Round 357), which analyzes rank-1 streaming covariance PCA with bounded-norm rank-1 samples x_t x_t^T via matrix product moments rather than proving global convergence for rank-p entrywise matrix completion, trace sensing, and subspace tracking under second-moment variance bounds (AVC) via Doob's optional stopping theorem on a determinant-ratio submartingale tau_k.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 366 Alecton SGD (De Sa, Olukotun, & Re 2015): colspace_diff=4.78e-16, lemma15_err=0.00e+00, z1_exact=0.4304<=0.5013, drift_margin=5.43e-04>=0, align_final=0.9907
```
