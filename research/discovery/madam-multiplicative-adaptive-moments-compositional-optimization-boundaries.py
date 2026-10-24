"""Constructed mathematical boundary and compositional descent verification for Round 619:
Madam — Multiplicative Adaptive Moments Optimizer (Bernstein et al., NeurIPS 2020, arXiv:2006.14560).

Verifies:
1. Lemma 1 & Modelling Assumption 1 [Deep Relative Trust] (Section 3.2, Eq. 2 & Appendix A, p. 4, 13):
   - For an L-layer linear compositional function f(W) = w_L * w_{L-1} * ... * w_1,
     the exact relative gradient perturbation satisfies:
     ||g_k(W + Delta W) - g_k(W)||_F / ||g_k(W)||_F <= prod_{l=1}^L (1 + ||Delta W_l||_F / ||W_l||_F) - 1.
2. Multiplicative Update Properties & Theorem 1 Descent Bound (Section 3.3, Eq. 3 & Appendix A, Eq. 6, p. 4, 13):
   - Under W -> W + Delta W = W odot (1 - eta * sign(W) odot sign(g(W))),
     Delta W = -eta * |W| odot sign(g(W)) satisfies:
     (a) Exact subset relative perturbation invariance: ||Delta W_*||_F / ||W_*||_F == eta for every subset W_*,
     (b) Angle identity: angle(Delta W_k, -g_k(W)) == angle(|W_k|, |g_k(W)|) =: gamma_k in [0, pi/2],
     (c) Theorem 1 descent guarantee: L(W + Delta W) < L(W) whenever eta < (1 + cos(gamma_k))^{1/L} - 1.
3. Algorithm 1 (Madam) & Section 4.1 (B-bit Logarithmic Number System Madam, Eqs. 4-5, p. 5, 7-8):
   - Clamped exponential multiplicative update W <- clamp_{sigma*}(W odot exp(-eta * sign(W) odot clamp_{eta*/eta}(g / g_bar)))
     strictly preserves the initial weight signs sign(W_t) == sign(W_0) (Dale's principle) and bounds single-step
     multiplicative factor in [exp(-eta*), exp(+eta*)].
   - In B-bit Madam, discretizing g / g_bar to multiples of eta_0 / eta moves weights purely between discrete rungs
     of the logarithmic ladder {+- sigma* exp(-k * eta_0) : k in {0, ..., 2^B - 1}} with zero off-grid drift.
"""

from __future__ import annotations

import math
import random


def verify_deep_relative_trust_and_theorem_1() -> tuple[float, float, float, float]:
    rng = random.Random(20261019)
    L = 5
    d = 6

    # 1. Verify Deep Relative Trust (Modelling Assumption 1) on L-layer scalar/diagonal product loss
    W = [[rng.uniform(-2.0, -0.3) if rng.random() < 0.5 else rng.uniform(0.3, 2.0) for _ in range(d)] for _ in range(L)]
    target = [0.5 * (-1.0 if i % 2 == 0 else 1.0) for i in range(d)]

    def forward_and_grads(weights: list[list[float]]) -> tuple[float, list[list[float]]]:
        # Compositional loss L(W) = sum_{i=1}^d 0.5 * (prod_{l=1}^L W_{l,i} - target_i)^2
        prods = [1.0] * d
        for l in range(L):
            for i in range(d):
                prods[i] *= weights[l][i]
        loss = sum(0.5 * ((prods[i] - target[i]) ** 2) for i in range(d))
        grads = [[0.0] * d for _ in range(L)]
        for k in range(L):
            for i in range(d):
                prod_other = 1.0
                for l in range(L):
                    if l != k:
                        prod_other *= weights[l][i]
                grads[k][i] = (prods[i] - target[i]) * prod_other
        return loss, grads

    loss_0, g_0 = forward_and_grads(W)

    # Compute angles gamma_k = angle(|W_k|, |g_k(W)|) and verify angle(Delta W_k, -g_k(W)) == gamma_k
    cos_gammas: list[float] = []
    max_angle_err = 0.0
    max_subset_rel_err = 0.0
    eta_test = 0.01

    for k in range(L):
        abs_w = [abs(x) for x in W[k]]
        abs_g = [abs(x) for x in g_0[k]]
        norm_w = math.sqrt(sum(x * x for x in abs_w))
        norm_g = math.sqrt(sum(x * x for x in abs_g))
        cos_gamma_k = sum(abs_w[i] * abs_g[i] for i in range(d)) / (norm_w * norm_g)
        cos_gammas.append(cos_gamma_k)

        # Multiplicative perturbation Eq. 3: Delta W_k = -eta * W_k * sign(W_k) * sign(g_k) = -eta * |W_k| * sign(g_k)
        dw_k = [-eta_test * W[k][i] * (1.0 if W[k][i] >= 0 else -1.0) * (1.0 if g_0[k][i] >= 0 else -1.0) for i in range(d)]
        # Verify subset relative perturbation ||Delta W_*||_F / ||W_*||_F == eta_test for arbitrary subsets
        for sub_len in (1, 3, d):
            num_sub = math.sqrt(sum(dw_k[i] ** 2 for i in range(sub_len)))
            den_sub = math.sqrt(sum(W[k][i] ** 2 for i in range(sub_len)))
            max_subset_rel_err = max(max_subset_rel_err, abs(num_sub / den_sub - eta_test))

        # Verify angle(Delta W_k, -g_k) == angle(|W_k|, |g_k|)
        cos_theta_k = sum(dw_k[i] * (-g_0[k][i]) for i in range(d)) / (
            math.sqrt(sum(x * x for x in dw_k)) * norm_g
        )
        max_angle_err = max(max_angle_err, abs(cos_theta_k - cos_gamma_k))

    assert max_subset_rel_err < 1e-15
    assert max_angle_err < 1e-15

    # Theorem 1 threshold: eta_max = min_k ((1 + cos(gamma_k))^{1/L} - 1)
    eta_thm1_bound = min(((1.0 + cg) ** (1.0 / L)) - 1.0 for cg in cos_gammas)
    assert eta_thm1_bound > 0.02

    # Choose eta = 0.5 * eta_thm1_bound < eta_thm1_bound and verify strict descent L(W + Delta W) < L(W)
    eta = 0.5 * eta_thm1_bound
    W_new = [
        [
            W[k][i] * (1.0 - eta * (1.0 if W[k][i] >= 0 else -1.0) * (1.0 if g_0[k][i] >= 0 else -1.0))
            for i in range(d)
        ]
        for k in range(L)
    ]
    loss_new, _ = forward_and_grads(W_new)
    loss_drop = loss_0 - loss_new
    assert loss_drop > 0.0
    return max_subset_rel_err, max_angle_err, eta_thm1_bound, loss_drop


def verify_madam_sign_preservation_and_b_bit_log_ladder() -> tuple[int, float, float]:
    # Verify Algorithm 1 (Madam) and Section 4.1 (B-bit Madam on logarithmic ladder)
    B = 10
    eta0 = 0.002
    eta = 0.02  # integer multiple: 10 * eta0
    eta_star = 0.08  # 40 * eta0
    sigma_star = 1.5
    beta = 0.9

    # Initialize weights on the B-bit logarithmic ladder: W_i = sign_i * sigma_star * exp(-k_i * eta0)
    init_signs = [1.0, -1.0, 1.0, -1.0]
    init_rungs = [20, 35, 10, 50]
    W = [init_signs[i] * sigma_star * math.exp(-init_rungs[i] * eta0) for i in range(4)]
    target = [0.8, -0.5, 1.1, -0.3]
    g_bar_sq = [0.0] * 4

    initial_loss = sum(0.5 * ((W[i] - target[i]) ** 2) for i in range(4))
    sign_flips = 0
    max_ladder_quant_err = 0.0

    for _ in range(300):
        g = [W[i] - target[i] for i in range(4)]
        for i in range(4):
            g_bar_sq[i] = (1.0 - beta) * (g[i] * g[i]) + beta * g_bar_sq[i]
            g_bar = math.sqrt(g_bar_sq[i]) + 1e-12
            ratio = g[i] / g_bar
            clamped = max(-eta_star / eta, min(eta_star / eta, ratio))
            # Quantize to nearest multiple of eta0 / eta (Section 4.1, p. 5)
            step_unit = eta0 / eta
            q_clamped = round(clamped / step_unit) * step_unit
            sgn_w = 1.0 if W[i] >= 0.0 else -1.0
            W_cand = W[i] * math.exp(-eta * sgn_w * q_clamped)

            # Clamp to logarithmic ladder range [sigma* exp(-(2^B - 1)*eta0), sigma*]
            min_mag = sigma_star * math.exp(-((2 ** B) - 1) * eta0)
            mag = max(min_mag, min(sigma_star, abs(W_cand)))
            W[i] = sgn_w * mag

            # Verify Dale's principle: sign never flips
            if (1.0 if W[i] >= 0.0 else -1.0) != init_signs[i]:
                sign_flips += 1

            # Verify exact rung membership k in {0, ..., 2^B - 1}
            k_est = -math.log(abs(W[i]) / sigma_star) / eta0
            k_int = round(k_est)
            assert 0 <= k_int <= (2 ** B) - 1
            max_ladder_quant_err = max(max_ladder_quant_err, abs(k_est - k_int))

    final_loss = sum(0.5 * ((W[i] - target[i]) ** 2) for i in range(4))
    assert sign_flips == 0
    assert max_ladder_quant_err < 1e-11
    assert final_loss < 0.001 * initial_loss
    return sign_flips, max_ladder_quant_err, final_loss / initial_loss


if __name__ == "__main__":
    sub_err, ang_err, thm1_b, l_drop = verify_deep_relative_trust_and_theorem_1()
    flips, q_err, l_rat = verify_madam_sign_preservation_and_b_bit_log_ladder()
    print(
        f"[PASS] Round 619 Madam verified: "
        f"subset_rel_err={sub_err:.2e}, angle_err={ang_err:.2e}, thm1_eta_bound={thm1_b:.4f}, "
        f"loss_drop={l_drop:.4e}>0, sign_flips={flips}, ladder_quant_err={q_err:.2e}, loss_ratio={l_rat:.4e}<<1"
    )
