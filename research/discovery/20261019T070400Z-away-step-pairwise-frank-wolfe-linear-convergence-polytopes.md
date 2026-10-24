# Discovery Report: Round 342 — Away-Step and Pairwise Frank-Wolfe Linear Convergence on Polytopes

- **Timestamp**: `2026-10-19T07:04:00Z`
- **Selected Concept**: `AIMech:AwayStepAndPairwiseFrankWolfeLinearConvergenceOnPolytopes` (*Away-Step and Pairwise Frank-Wolfe Linear Convergence on Polytopes*)
- **Record Path**: `data/curated/AwayStepAndPairwiseFrankWolfeLinearConvergenceOnPolytopes.yaml`
- **Primary Source**: Simon Lacoste-Julien, Martin Jaggi — *On the Global Linear Convergence of Frank-Wolfe Optimization Variants* (`https://papers.nips.cc/paper/2015/hash/c058f544c737782deacefa532d9add4c-Abstract.html`).

## Identity & Boundary Resolution

Distinct from standard Frank-Wolfe / Conditional Gradient, which moves only toward vertices s_t in A and stagnates at O(1/t) when the optimum lies on a facet, and from projected gradient methods such as Catalyst or Soft-Impute, which require Euclidean or Bregman projections onto M at every step rather than linear minimization oracle (LMO) calls. Specifically captures the active-set Away-Steps (Algorithm 1) and Pairwise (Algorithm 2) conditional gradient updates, the drop-step amortisation bound, the Pyramidal Width PWidth(A) and Geometric Strong Convexity mu_f^G = mu * delta^2 (Theorem 6), and the exact simplex/cube pyramidal widths (Section 3.1 and Lemma 4).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 342 Away-Steps & Pairwise Frank-Wolfe (Lacoste-Julien & Jaggi 2015): max_simplex_pwidth_err=2.22e-16, lemma4_cube_err=0.00e+00, h_afw=0.00e+00, h_pfw=0.00e+00 << h_fw_60=1.9397e-03, drop_steps=1
```
