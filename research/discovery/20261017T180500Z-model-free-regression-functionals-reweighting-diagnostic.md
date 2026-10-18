# Discovery Report: Model-Free Regression Functionals, Regressor-Reweighting Well-Specification Diagnostic, and M-of-N XY-Bootstrap Sandwich Limit (Round 215)

- **Report ID**: `20261017T180500Z-model-free-regression-functionals-reweighting-diagnostic`
- **Created At**: `2026-10-17T18:05:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:ModelFreeRegressionFunctionalsReweightingDiagnosticAndXYBootstrapLimit` (`data/curated/ModelFreeRegressionFunctionalsReweightingDiagnosticAndXYBootstrapLimit.yaml`)
- **Verification Script**: `research/discovery/model-free-regression-functionals-reweighting-diagnostic-boundaries.py` (SHA-256: `0adc88a7e5c209379bd0b63c7d05a36952e06a517418c0dc28357ba247a24852`)

## Summary of Primary Sources Inspected

1. **Buja, Brown, Kuchibhotla, Berk, George, & Zhao (2019)**, *Models as Approximations II: A Model-Free Theory of Parametric Regression*, *Statistical Science*, 34(4):545–565 (`DOI:10.1214/18-STS694`, `arXiv:1612.03257v2`).
   - Read all 36 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/0c3c9245eb4a0ce8.pdf`, `936127` bytes, SHA-256 `72a14bd879fea7af300f738eac9ee12150971e696fe7a54091308e8a10fd7309`), Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3143/content.md`, `3917` bytes, SHA-256 `ee7d6d0599045cf704dfc2cda4f820eab301cebbd13e4b3248070627648dad9b`), and arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3142/content.md`, `6983` bytes, SHA-256 `c949deb1ad28bbdd850cb940ddf6db17d1202c48149c6dcd48db708f6eef93dd`).

## Constructed Boundary & Regime Verification

```text
All model-free regression functionals & reweighting diagnostic boundary checks passed.
```

Executed pure-Python verification in research/discovery/model-free-regression-functionals-reweighting-diagnostic-boundaries.py (SHA-256 0adc88a7e5c209379bd0b63c7d05a36952e06a517418c0dc28357ba247a24852): verified (1) Basu-Harris-Hjort-Jones density power divergence S_alpha Fisher consistency at true Gaussian (mu_0, sigma_0) and redescending location score psi_alpha(y) -> 0 for extreme outliers; (2) Lemma 4.1 & Proposition 4.1 exact invariance of reweighted OLS slope across interior deciles xi_(1)..xi_(9) under well-specification (tilt d = 0) vs. monotonic slope drift and large positive tilt d > 0.8 under quadratic misspecification; (3) Propositions 6.4-6.6 & Corollary 7.1 exact L^2(P) orthogonality between Noise IF = IF(Y, X) - IF(X) and Approximation IF = IF(X), Pythagorean variance split Var(IF) = E[Var(IF|X)] + Var(IF(X)), and vanishing of Noise EO in the deterministic noiseless limit; and (4) Proposition 8.1 & Corollary 8.1 convergence of scaled M-of-N XY-bootstrap variance M * Var*(theta^*_M - theta_hat_N) to the empirical sandwich covariance AV[P_hat_N; theta(.)].
