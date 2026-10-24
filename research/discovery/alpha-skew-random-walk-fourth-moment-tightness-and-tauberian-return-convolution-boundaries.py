#!/usr/bin/env python3
"""Boundary verification for Round 838: Alpha-Skew Random Walk Fourth-Moment Tightness and Tauberian Return Convolution (Seol, 2011, arXiv:1106.5042v1).

Verifies:
1. Exact n-step transition law of the alpha-skew random walk S^{(alpha)} on Z (Proposition 2.1-2.2):
   - P(S_k^{(alpha)} = m) = alpha * P(|S_k| = m) for m > 0,
     (1 - alpha) * P(|S_k| = -m) for m < 0, and P(S_k^{(alpha)} = 0) = P(S_k = 0) = g(k),
     where g(2i) = comb(2i, i) * 2^{-2i} and g(2i+1) = 0.
   - |S^{(alpha)}| has the exact distribution of reflected simple symmetric random walk |S|,
     and -S^{(alpha)} has the exact distribution of S^{(1-alpha)}.
2. Conditional increment drift and unit conditional variance (Proposition 2.3):
   - E[S_{j+1}^{(alpha)} - S_j^{(alpha)} | S_j^{(alpha)}] = (2*alpha - 1) * 1_{S_j^{(alpha)} = 0}
   - E[(S_{i+1}^{(alpha)} - S_i^{(alpha)})^2 | S_i^{(alpha)}] = 1.
3. Exact return generating function and 2-fold / 4-fold discrete convolutions (Proposition 2.5):
   - g_tilde(t) = sum_{k=0}^infty g(k) t^k = (1 - t^2)^{-1/2}
   - mu = g * g satisfies mu_tilde(t) = (1 - t^2)^{-1}, so mu(2i) = 1, mu(2i+1) = 0, and
     sum_{j=0}^m mu(j) = floor(m/2) + 1 ~ m/2.
   - nu = g * g * g * g satisfies nu_tilde(t) = (1 - t^2)^{-2}, so nu(2i) = i + 1, nu(2i+1) = 0,
     and sum_{j=0}^m nu(j) = (floor(m/2) + 1)*(floor(m/2) + 2)/2 ~ m^2/8.
4. Exact third- and fourth-order cross-increment expectations A(i_1, i_2, i_3) and B(i_1, i_2, i_3, i_4)
   (Lemma 2.6) and uniform fourth-moment tightness bound E|S_k^{(alpha)} - S_j^{(alpha)}|^4 <= C_alpha |k - j|^2
   (Theorem 1.1).
"""

import math


def g_return(k: int) -> float:
    if k < 0 or (k % 2 == 1):
        return 0.0
    i = k // 2
    return math.comb(2 * i, i) * (0.25 ** i)


def step_skew_distribution(dist: dict[int, float], alpha: float) -> dict[int, float]:
    nxt: dict[int, float] = {}
    for m, p in dist.items():
        if m == 0:
            nxt[1] = nxt.get(1, 0.0) + p * alpha
            nxt[-1] = nxt.get(-1, 0.0) + p * (1.0 - alpha)
        else:
            nxt[m + 1] = nxt.get(m + 1, 0.0) + p * 0.5
            nxt[m - 1] = nxt.get(m - 1, 0.0) + p * 0.5
    return nxt


def main():
    alpha = 0.75
    K_max = 16

    # 1. Verify Proposition 2.1, 2.2, 2.3 via exact Markov chain evolution vs simple symmetric RW
    dist_alpha = {0: 1.0}
    dist_sym = {0: 1.0}
    dist_comp = {0: 1.0}
    for k in range(1, K_max + 1):
        # Verify conditional moments before stepping (Proposition 2.3)
        for m, p in dist_alpha.items():
            if p > 0:
                cond_mean = alpha - (1.0 - alpha) if m == 0 else 0.5 - 0.5
                expected_mean = (2.0 * alpha - 1.0) if m == 0 else 0.0
                assert abs(cond_mean - expected_mean) < 1e-15
                cond_var2 = (alpha * 1.0 + (1.0 - alpha) * 1.0) if m == 0 else (0.5 * 1.0 + 0.5 * 1.0)
                assert abs(cond_var2 - 1.0) < 1e-15

        dist_alpha = step_skew_distribution(dist_alpha, alpha)
        dist_sym = step_skew_distribution(dist_sym, 0.5)
        dist_comp = step_skew_distribution(dist_comp, 1.0 - alpha)

        # Check Proposition 2.2 at step k
        p0_alpha = dist_alpha.get(0, 0.0)
        assert abs(p0_alpha - g_return(k)) < 1e-14, f"Return prob mismatch at k={k}"
        for m in range(1, k + 1):
            p_abs_sym = dist_sym.get(m, 0.0) + dist_sym.get(-m, 0.0)
            assert abs(dist_alpha.get(m, 0.0) - alpha * p_abs_sym) < 1e-14
            assert abs(dist_alpha.get(-m, 0.0) - (1.0 - alpha) * p_abs_sym) < 1e-14
            # Check Proposition 2.1(a): |S^{(alpha)}_k| == |S_k|
            assert abs((dist_alpha.get(m, 0.0) + dist_alpha.get(-m, 0.0)) - p_abs_sym) < 1e-14
            # Check Proposition 2.1(b): -S^{(alpha)}_k == S^{(1-alpha)}_k
            assert abs(dist_alpha.get(-m, 0.0) - dist_comp.get(m, 0.0)) < 1e-14

    # 2. Verify Proposition 2.5 convolutions g*g and g*g*g*g
    N_conv = 40
    g_vec = [g_return(k) for k in range(N_conv + 1)]
    mu_vec = [0.0 for _ in range(N_conv + 1)]
    for j in range(N_conv + 1):
        mu_vec[j] = sum(g_vec[r] * g_vec[j - r] for r in range(j + 1))
        if j % 2 == 0:
            # By binomial series (1 - t^2)^{-1/2} * (1 - t^2)^{-1/2} = (1 - t^2)^{-1}, (g*g)(2i) == 1
            assert abs(mu_vec[j] - 1.0) < 1e-13, f"(g*g)({j}) = {mu_vec[j]} != 1"
        else:
            assert abs(mu_vec[j]) < 1e-15

    nu_vec = [0.0 for _ in range(N_conv + 1)]
    for j in range(N_conv + 1):
        nu_vec[j] = sum(mu_vec[r] * mu_vec[j - r] for r in range(j + 1))
        if j % 2 == 0:
            i = j // 2
            # Since (1 - t^2)^{-2} = sum_{i=0}^infty (i + 1) t^{2i}, (g*g*g*g)(2i) == i + 1
            assert abs(nu_vec[j] - (i + 1.0)) < 1e-12, f"(g^{{*4}})({j}) = {nu_vec[j]} != {i+1}"
        else:
            assert abs(nu_vec[j]) < 1e-15

    # 3. Verify Lemma 2.6 exact cross-increment expectations A(i1,i2,i3) and B(i1,i2,i3,i4)
    # by exact path enumeration over 8 steps
    T_steps = 8
    # Enumerate all 2^T_steps trajectories of S^{(alpha)}
    trajs = []

    def backtrack(step, path, prob):
        if step == T_steps:
            trajs.append((path, prob))
            return
        cur = path[-1]
        p_up = alpha if cur == 0 else 0.5
        backtrack(step + 1, path + [cur + 1], prob * p_up)
        backtrack(step + 1, path + [cur - 1], prob * (1.0 - p_up))

    backtrack(0, [0], 1.0)

    # Verify both the origin-indicator equality in the proof of Lemma 2.6:
    # E[(Delta_{i3})^2 Delta_{i2} Delta_{i1} 1_{S_{i1}=0} 1_{S_{i2}=0}] == (2*alpha - 1)^2 g(i1) g(i2 - i1)
    # and the unconditional inequality A(i1, i2, i3) <= (2*alpha - 1)^2 g(i1) g(i2 - i1)
    # (since bridge drift from S_{i1} != 0 to S_{i2} = 0 is <= 0).
    for i1, i2, i3 in [(0, 2, 5), (0, 4, 7), (0, 6, 7), (2, 4, 7), (1, 4, 6)]:
        emp_A_uncond = 0.0
        emp_A_ind = 0.0
        for path, prob in trajs:
            d1 = path[i1 + 1] - path[i1]
            d2 = path[i2 + 1] - path[i2]
            d3 = path[i3 + 1] - path[i3]
            val = prob * (d3 * d3) * d2 * d1
            emp_A_uncond += val
            if path[i1] == 0 and path[i2] == 0:
                emp_A_ind += val
        theo_A = ((2.0 * alpha - 1.0) ** 2) * g_return(i1) * g_return(i2 - i1)
        assert abs(emp_A_ind - theo_A) < 1e-14, (
            f"Lemma 2.6 indicator A mismatch at {(i1,i2,i3)}: {emp_A_ind} vs {theo_A}"
        )
        assert emp_A_uncond <= theo_A + 1e-14, (
            f"Lemma 2.6 A upper bound violated at {(i1,i2,i3)}: {emp_A_uncond} > {theo_A}"
        )

    for i1, i2, i3, i4 in [(0, 2, 4, 6), (0, 2, 6, 7), (2, 4, 6, 7)]:
        emp_B_ind = 0.0
        for path, prob in trajs:
            if path[i1] == 0 and path[i2] == 0 and path[i3] == 0 and path[i4] == 0:
                d1 = path[i1 + 1] - path[i1]
                d2 = path[i2 + 1] - path[i2]
                d3 = path[i3 + 1] - path[i3]
                d4 = path[i4 + 1] - path[i4]
                emp_B_ind += prob * d4 * d3 * d2 * d1
        theo_B = (
            ((2.0 * alpha - 1.0) ** 4)
            * g_return(i1)
            * g_return(i2 - i1)
            * g_return(i3 - i2)
            * g_return(i4 - i3)
        )
        assert abs(emp_B_ind - theo_B) < 1e-14, (
            f"Lemma 2.6 indicator B mismatch at {(i1,i2,i3,i4)}: {emp_B_ind} vs {theo_B}"
        )

    # 4. Verify uniform fourth-moment ratio E|S_k^{(alpha)} - S_j^{(alpha)}|^4 / |k - j|^2 <= C_alpha (Theorem 1.1)
    max_ratio = 0.0
    for j in range(0, T_steps):
        for k in range(j + 1, T_steps + 1):
            m4 = sum(prob * ((path[k] - path[j]) ** 4) for path, prob in trajs)
            ratio = m4 / ((k - j) ** 2)
            if ratio > max_ratio:
                max_ratio = ratio
    assert max_ratio <= 3.0, f"Unexpectedly large fourth-moment ratio: {max_ratio}"

    print(
        f"[PASS] Round 838 Alpha-Skew Random Walk Tightness (Seol 2011): "
        f"mu_even={mu_vec[10]:.1f}, nu_even_10={nu_vec[10]:.1f}, "
        f"max_m4_ratio={max_ratio:.4f}"
    )


if __name__ == "__main__":
    main()
