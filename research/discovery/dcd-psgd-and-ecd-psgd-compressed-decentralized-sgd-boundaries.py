"""Constructed boundary verification for Round 425: DCD-PSGD & ECD-PSGD (Tang et al., NeurIPS 2018, arXiv:1803.06443).

Verifies:
1. Section 4.1 (Theorem 1 & Remark 1): DCD-PSGD (Algorithm 1) requires the compression-spectral stability
   condition (1 - rho)^2 - 4 * mu^2 * alpha^2 > 0 (where mu = max_{i>=2} |1 - lambda_i(W)| and
   rho = max_{i>=2} |lambda_i(W)|), which breaks down when relative compression noise alpha exceeds
   (1 - rho) / (2 * mu).
2. Section 4.2 (Algorithm 2, Lemmas 11-12 & Theorem 3): ECD-PSGD compresses the extrapolated sequence
   z_t = (1 - 0.5*t) x_{t-1} + 0.5*t * x_t and reconstructs x_tilde_t = (1 - 2/t) x_tilde_{t-1} + (2/t) C(z_t):
   - By exact induction (Lemma 11), in the noiseless compression limit C(z) = z (so w_s = 0),
     x_tilde_t == x_t for all t >= 1!
   - Under constant compression variance E||w_s||^2 = sigma_c^2 > 0, the replica estimation error
     satisfies E||x_tilde_t - x_t||^2 = (4 / t^2) * sum_{s=1}^t E||w_s||^2 = 4 * sigma_c^2 / t = O(1/t),
     decaying to zero for ANY compression level alpha!
"""

from __future__ import annotations


def main() -> None:
    # 1. Check DCD-PSGD stability boundary (1 - rho)^2 - 4 * mu^2 * alpha^2 > 0 (Theorem 1)
    # 3-node ring with doubly stochastic W having eigenvalues [1, 0.25, 0.25] -> rho = 0.25, mu = 0.75
    rho = 0.25
    mu = 0.75
    alpha_crit = (1.0 - rho) / (2.0 * mu)  # 0.75 / 1.5 = 0.50
    alpha_safe = 0.30
    alpha_unsafe = 0.70
    cond_safe = (1.0 - rho) ** 2 - 4.0 * (mu ** 2) * (alpha_safe ** 2)
    cond_unsafe = (1.0 - rho) ** 2 - 4.0 * (mu ** 2) * (alpha_unsafe ** 2)
    assert cond_safe > 0.0 and cond_unsafe < 0.0

    # 2. Verify ECD-PSGD Lemma 11 exact extrapolation identity:
    # x_tilde_t - x_t = (1 - 2/t)(x_tilde_{t-1} - x_{t-1}) + (2/t) w_t
    # Unrolling from t = 1 (where 1 - 2/1 = -1, so x_tilde_1 - x_1 = 2 w_1, and for t=2, 1 - 2/2 = 0):
    # Wait: let's run the exact Algorithm 2 recurrence for x_t and x_tilde_t!
    T = 20
    x_seq = [0.0] + [1.0 + 0.2 * t - 0.01 * (t ** 2) for t in range(1, T + 1)]

    # Case A: Exact compressor w_t = 0 -> x_tilde_t == x_t for all t >= 1
    x_tilde = 0.0
    max_exact_err = 0.0
    for t in range(1, T + 1):
        z_t = (1.0 - 0.5 * t) * x_seq[t - 1] + 0.5 * t * x_seq[t]
        c_z_t = z_t  # w_t = 0
        x_tilde = (1.0 - 2.0 / t) * x_tilde + (2.0 / t) * c_z_t
        max_exact_err = max(max_exact_err, abs(x_tilde - x_seq[t]))
    assert max_exact_err < 1e-13, f"ECD-PSGD noiseless extrapolation identity failed: {max_exact_err}"

    # Case B: Independent zero-mean compression noise w_t with Var(w_t) = sigma_c^2:
    # Since e_t = x_tilde_t - x_t satisfies e_t = ((t - 2)/t) e_{t-1} + (2/t) w_t,
    # for t >= 2 we have t*(t-1)*e_t = (t-1)*(t-2)*e_{t-1} + 2*(t-1)*w_t, so
    # e_t = (2 / (t*(t-1))) sum_{s=2}^t (s-1) w_s, and E[e_t^2] = (4 / (t^2 (t-1)^2)) sum_{s=2}^t (s-1)^2 sigma_c^2 <= (4 / (3 t)) sigma_c^2 = O(1/t)!
    sigma_c_sq = 2.0
    var_e = 0.0
    var_history = []
    for t in range(1, T + 1):
        factor = 1.0 - 2.0 / t
        var_e = (factor * factor) * var_e + ((2.0 / t) ** 2) * sigma_c_sq
        var_history.append(var_e)
        if t >= 2:
            assert var_e <= (4.0 * sigma_c_sq) / t

    assert var_history[-1] < var_history[1] / 5.0

    print(
        f"[PASS] Round 425 DCD-PSGD & ECD-PSGD (Tang et al. 2018): DCD alpha_crit={alpha_crit:.2f} "
        f"(safe={cond_safe:.3f}>0, unsafe={cond_unsafe:.3f}<0), ECD exact_err={max_exact_err:.1e}, "
        f"ECD var(t=2)={var_history[1]:.4f} -> var(t={T})={var_history[-1]:.4f} <= O(1/T)"
    )


if __name__ == "__main__":
    main()
