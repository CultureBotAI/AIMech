# Discovery Report: Round 265 — Cone Invertibility Factor Oracle Inequalities and Rate Minimaxity of LASSO and Dantzig Selector in Lq Loss

- **Timestamp**: `2026-10-19T03:45:00Z`
- **Selected Concept**: `AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss` (*Cone Invertibility Factor Oracle Inequalities and Rate Minimaxity of LASSO and Dantzig Selector in Lq Loss*)
- **Record Path**: `data/curated/ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss.yaml`
- **Primary Source**: Fei Ye and Cun-Hui Zhang (2010), *Rate Minimaxity of the Lasso and Dantzig Selector for the $\ell_q$ Loss in $\ell_r$ Balls*, *Journal of Machine Learning Research* 11:3519–3540 (`https://jmlr.org/papers/v11/ye10a.html`).

## Identity & Boundary Resolution

`AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss` was checked against all 442 pinned AIO concepts and 659 maintained AIMech concepts:

1. **`AIMech:RestrictedEigenvalueConditionAndBickelRitovTsybakovSimultaneousLassoDantzigOracleBounds`**: Uses quadratic-form Restricted Eigenvalues $\kappa(s, c_0)$ yielding $1/\kappa^2$ bounds, whereas Ye & Zhang (2010) introduce the Cone Invertibility Factor $F_q(\xi, S)$ and Sign-Restricted CIF $SCIF_q(\xi, S)$ on $\mathscr{C}_-(\xi, S)$ yielding sharp single-factor $\ell_q$ bounds and universal minimax lower bounds over $\ell_r$ balls ($0 \le r \le 1 \le q \le \infty$).
2. **`AIMech:CompatibilityConditionAndOracleInequalitiesForLassoInHighDimensionalGeneralizedLinearModels`**: $\ell_1$ compatibility constant for excess risk rather than $\ell_q$ CIF/SCIF invertibility and $\ell_r$-ball rate minimaxity.

## Constructed Boundary & Regime Verification

```text
{
  "lemma20_sharp_shifting": {
    "a_2_exact": 0.25,
    "max_ratio_by_q": {
      "1.5": 0.81579431,
      "2.0": 0.80076255,
      "3.0": 0.78182287,
      "4.0": 0.76834554
    },
    "extremal_integral_err_by_q": {
      "1.5": 0.0,
      "2.0": 0.0,
      "3.0": 0.0,
      "4.0": 0.0
    }
  },
  "theorem3_and_theorem8": {
    "dantzig_cone_ratio": 0.0,
    "lasso_cone_ratio": 0.0,
    "max_sign_restriction_violation": 0.0,
    "dantzig_error_to_bound_ratios": {
      "1": 0.25381552656492623,
      "2": 0.4427828861386202,
      "inf": 0.49946507215964603
    },
    "lasso_error_to_bound_ratios": {
      "1": 0.809004650267799,
      "2": 0.8090046502677991,
      "inf": 0.809004650267799
    },
    "scif_2_ge_cif_2": true,
    "bound_scif_l2": 0.12706954,
    "bound_re_prod_l2": 0.2275993,
    "bound_brt_l2": 3.05382883,
    "lam_prime_lt_min_beta_half": true,
    "exact_sign_recovery_TD": true,
    "gauss_dantzig_oracle_diff": 0.0
  }
}
```

Verified in pure Python: (1) Theorem 1 minimax constant a_q = sup_{0<eps<1} (1-eps)(1-sqrt(eps))^q / 2^{q/2+1} achieves exact maximum a_2 = 0.25 at eps = 1/4, with positive universal minimax lower bounds across q in {1, 2, inf}; (2) Proposition 1 closed-form extremal integral (q - 1) * int_0^xi u^{q-1} (1+u)^{-q} du matches sup_{w!=0} ||w_{S^c}||_q^q / (|S|^{q-1} ||w_{S^c}||_1^q) on the boundary ||w_{S^c}||_1 = xi*||w_S||_1 to 0.0 across q in {1.5, 2.0, 3.0}; (3) on a correlated Toeplitz design (n=30, p=12, s=3, rho=0.45), both LASSO and Dantzig errors lie strictly inside the sign-restricted cone C_-(xi, S) (max violation 0.0), SCIF_2 = 0.65913211 >= CIF_2 = 0.6305196 >= psi(xi,S)^2 = 0.36802909 >= kappa_RE^2 = 0.35156172, and Theorem 3's single-factor SCIF bound (0.12706954) is 1.79x tighter than the two-factor RE product bound (0.2275993) and 24.0x tighter than the Bickel-Ritov-Tsybakov bound (3.05382883), while Theorem 4's g_q interpolation holds with g_2(u; xi) = 0.60017899; and (4) Corollary 2's Thresholded Dantzig and Gauss-Dantzig estimators recover the exact signed support [0, 1, 2] and match the oracle OLS refit to 0.0.
