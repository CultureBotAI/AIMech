# Discovery Report: Baik-Ben Arous-Peche Largest Eigenvalue Phase Transition for Spiked Complex Sample Covariance Matrices (Round 250)

- **Report ID**: `20261019T004200Z-bbp-phase-transition-largest-eigenvalue`
- **Created At**: `2026-10-19T00:42:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:BaikBenArousPecheLargestEigenvaluePhaseTransition` (`data/curated/BaikBenArousPecheLargestEigenvaluePhaseTransition.yaml`)
- **Verification Script**: `research/discovery/bbp-phase-transition-largest-eigenvalue-boundaries.py` (SHA-256: `2d22a3d0624e025ef6e2acfb8ff52df3d4d5608db544b2e739bc79cd95c09406`)

## Summary of Primary Sources Inspected

1. **Jinho Baik, Gerard Ben Arous, and Sandrine Peche (2005)**, *Phase transition of the largest eigenvalue for non-null complex sample covariance matrices*, *The Annals of Probability* 33(5):1643-1697 (`arXiv:math/0403022v2`, `DOI:10.1214/009117905000000233`).
   - Read all 52 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/e95059dbe535664a.pdf`, `441716` bytes, SHA-256 `09c7b1bd0432390bfe108254280e57f621255251c7e571bce7572d0ca3bfd897`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4226/content.md`, `6050` bytes, SHA-256 `f980163c0f6cffd1d816ce7fee2015dc55db72f11e02b8224ad76fb904c168a4`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/4227/content.md`, `4547` bytes, SHA-256 `172f58181c1dad8520aa6ddd1e521f65e226543661ab9307291fa2317c45ea51`).

## Constructed Boundary & Regime Verification

```text
Baik-Ben Arous-Peche (2005) phase transition verified: subcritical mean=2.653~2.914, supercritical k=1 mean=4.258~4.200, supercritical k=2 mean=4.746 (G_2 shift=0.489, asymp=0.599).
```

Executed pure-Python verification in research/discovery/bbp-phase-transition-largest-eigenvalue-boundaries.py (SHA-256 2d22a3d0624e025ef6e2acfb8ff52df3d4d5608db544b2e739bc79cd95c09406): verified (1) Section 3 eqs. (101)-(112) coalescing double-root conditions f'(p_c) = f''(p_c) = 0 and f^{(3)}(p_c) = 2 nu^3 > 0 at z = p_c = gamma / (gamma + 1) when mu = (1 + gamma^{-1})^2; (2) Section 4 eqs. (209)-(219) supercritical saddle splitting 0 < pi_1 < p_c < 1/(mu pi_1) < 1 and curvatures f''(pi_1) = -nu^2 < 0 and f''(1/(mu pi_1)) = [gamma nu mu pi_1 (1 - pi_1)]^2 > 0 for ell_1 = pi_1^{-1} > 1 + gamma^{-1}; (3) Section 6 eqs. (316)-(317) exact directed last-passage percolation variational formula max_{x in [0,1]} [ell_1 x + (sqrt(1 - x) + gamma^{-1})^2] transitioning at ell_1 = 1 + gamma^{-1}; and (4) Monte Carlo simulations on 2x2 GUE (E[xi_max] = 2/sqrt(pi) = 1.128) and complex Gaussian spiked Wishart matrices (N = 20, M = 40, gamma = sqrt(2)), confirming subcritical concentration near (1 + gamma^{-1})^2 = 2.914 (empirical 2.653), supercritical k = 1 separation near mu(3.5) = 4.200 (empirical 4.258), and supercritical k = 2 degenerate-spike G_2 positive mean shift (empirical 4.746, shift +0.489 matching asymptotic +0.599).
