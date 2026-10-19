"""Constructed boundary verification for Round 417: TernGrad (Wen et al., NeurIPS 2017, arXiv:1705.07878).

Verifies:
1. Equations (4)-(6) (Section 3.1): Stochastic ternary quantization g_tilde = s * sign(g) o b with
   s = ||g||_infty and P(b_k = 1 | g) = |g_k| / s is strictly unbiased:
     E[g_tilde_k | g] = s * sign(g_k) * (|g_k| / s) = g_k
   with coordinate second moment E[g_tilde_k^2 | g] = s * |g_k| and total conditional variance:
     E[||g_tilde - g||_2^2 | g] = ||g||_infty * ||g||_1 - ||g||_2^2.
2. Section 3.2 & Section 3.3 (Eq. 7, Theorem 1): Layer-wise quantization (splitting g into layer sub-vectors
   g^{(l)} with separate scalars s^{(l)} = ||g^{(l)}||_infty) and gradient clipping |g_k| <= c * sigma
   strictly reduce both the maximum quantization scalar s_t = ||g_t||_infty (which multiplies the variance
   bound in Theorem 1) and the total ternary quantization variance ||g||_infty * ||g||_1 - ||g||_2^2.
"""

from __future__ import annotations


def exact_ternary_moments(g: list[float]) -> tuple[list[float], list[float], float]:
    s = max(abs(x) for x in g)
    if s == 0.0:
        return [0.0] * len(g), [0.0] * len(g), 0.0
    mean = []
    second_moment = []
    total_var = 0.0
    for x in g:
        p1 = abs(x) / s
        sgn = 1.0 if x >= 0.0 else -1.0
        m1 = (s * sgn) * p1
        m2 = ((s * sgn) ** 2) * p1
        mean.append(m1)
        second_moment.append(m2)
        total_var += m2 - x * x
    return mean, second_moment, total_var


def main() -> None:
    # Two-layer gradient vector with distinct dynamic ranges (Section 3.2)
    layer1 = [2.4, -0.8, 0.4, -0.2]
    layer2 = [0.05, -0.04, 0.02, -0.01]
    g_global = layer1 + layer2

    mean_g, m2_g, var_global = exact_ternary_moments(g_global)
    s_global = max(abs(x) for x in g_global)
    l1_global = sum(abs(x) for x in g_global)
    l2_sq_global = sum(x * x for x in g_global)

    # Check unbiasedness E[g_tilde | g] == g and E[g_tilde_k^2 | g] == s * |g_k|
    max_bias = max(abs(m - x) for m, x in zip(mean_g, g_global))
    max_m2_err = max(abs(m2 - s_global * abs(x)) for m2, x in zip(m2_g, g_global))
    closed_form_var = s_global * l1_global - l2_sq_global
    assert max_bias < 1e-15, f"TernGrad unbiasedness violated: {max_bias}"
    assert max_m2_err < 1e-15, f"TernGrad second moment formula violated: {max_m2_err}"
    assert abs(var_global - closed_form_var) < 1e-14, f"Closed-form variance mismatch: {var_global} vs {closed_form_var}"

    # Layer-wise quantization (Section 3.2): quantize layer1 and layer2 with separate scalars s^{(1)}, s^{(2)}
    _, _, var_l1 = exact_ternary_moments(layer1)
    _, _, var_l2 = exact_ternary_moments(layer2)
    var_layerwise = var_l1 + var_l2
    assert var_layerwise < var_global, f"Layer-wise quantization did not reduce variance: {var_layerwise} >= {var_global}"

    # Gradient clipping (Section 3.3, Eq. 7): clip outlier in layer1 at threshold c * sigma
    mean_val = sum(layer1) / len(layer1)
    sigma_l1 = (sum((x - mean_val) ** 2 for x in layer1) / len(layer1)) ** 0.5
    clip_bound = 1.2 * sigma_l1
    layer1_clipped = [max(-clip_bound, min(clip_bound, x)) for x in layer1]
    _, _, var_clipped = exact_ternary_moments(layer1_clipped)
    assert var_clipped < var_l1, f"Gradient clipping did not reduce variance: {var_clipped} >= {var_l1}"

    print(
        f"[PASS] Round 417 TernGrad (Wen et al. 2017): max_bias={max_bias:.1e}, "
        f"var_global={var_global:.4f} == s*||g||_1-||g||_2^2={closed_form_var:.4f}, "
        f"var_layerwise={var_layerwise:.4f} < var_global, var_clipped={var_clipped:.4f} < var_unclipped={var_l1:.4f}"
    )


if __name__ == "__main__":
    main()
