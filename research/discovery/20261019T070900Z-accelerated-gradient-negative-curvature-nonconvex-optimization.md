# Discovery Report: Round 347 — Accelerated Gradient and Negative-Curvature Exploitation for Non-Convex Optimization

- **Timestamp**: `2026-10-19T07:09:00Z`
- **Selected Concept**: `AIMech:AcceleratedGradientAndNegativeCurvatureExploitationForNonConvexOptimization` (*Accelerated Gradient and Negative-Curvature Exploitation for Non-Convex Optimization*)
- **Record Path**: `data/curated/AcceleratedGradientAndNegativeCurvatureExploitationForNonConvexOptimization.yaml`
- **Primary Source**: Yair Carmon, John C. Duchi, Oliver Hinder, Aaron Sidford — *Accelerated Methods for NonConvex Optimization* (`https://doi.org/10.1137/17M1114296`).

## Identity & Boundary Resolution

Distinct from Perturbed Gradient Descent (`AIMech:PerturbedGradientDescentForEscapingSaddlePointsInHessianLipschitzOptimization`), which adds uniform ball noise to standard gradient descent and requires O_tilde(Delta_f L_1 epsilon^{-2}) gradient evaluations, and from Catalyst Universal Acceleration (`AIMech:CatalystUniversalAccelerationForFirstOrderOptimization`), which accelerates convex composite objectives rather than alternating Lanczos negative-curvature descent with radially penalized almost-convex proximal AGD. Specifically captures the gamma-almost convexity definition (Definition 4), the `Almost-convex-AGD` proximal sequence (Lemma 3.1), `Negative-curvature-descent` (Lemma 3.2), the radial hinge-squared regularizer rho_alpha(x) = L_1 [||x|| - alpha/L_2]_+^2 (Lemma 4.1), the O_tilde(epsilon^{-7/4}) complexity bound (Theorem 4.3), and the two-phase `Accelerated-strict-saddle-method` (Algorithm 2, Theorem 5.1).

## Constructed Boundary & Regime Verification

```text
[PASS] Carmon et al. accelerated non-convex boundaries verified: NCD_drop=0.029590>=cubic_bound=0.027042>=0.003704, eps^-7/4=1.0e+07<eps^-2=1.0e+08, strict_saddle_eps=8.3333e-03
```
