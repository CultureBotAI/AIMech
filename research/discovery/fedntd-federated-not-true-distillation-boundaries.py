#!/usr/bin/env python3
"""Constructed boundary verification for FedNTD (Lee et al., NeurIPS 2022, arXiv:2106.03097)."""

import math

def main():
    # 1. Verify Definition 1 & Proposition 1: Out-local distribution p_tilde and Gradient Diversity Lambda(beta)
    C = 5
    K = 4
    # Heterogeneous client class distributions whose average is uniform (sum_k p^k(c) = K/C = 0.8)
    p_clients = [
        [0.60, 0.20, 0.10, 0.05, 0.05],
        [0.05, 0.60, 0.20, 0.10, 0.05],
        [0.05, 0.05, 0.50, 0.25, 0.15],
        [0.10, 0.15, 0.00, 0.40, 0.35],
    ]
    # Make column sums exactly K/C = 0.80:
    p_clients = [
        [0.55, 0.20, 0.10, 0.10, 0.05],
        [0.10, 0.55, 0.20, 0.05, 0.10],
        [0.05, 0.00, 0.50, 0.25, 0.20],
        [0.10, 0.05, 0.00, 0.40, 0.45],
    ]
    for c in range(C):
        col_sum = sum(p_clients[k][c] for k in range(K))
        assert abs(col_sum - K / C) < 1e-12, f"Column {c} sum {col_sum} != {K/C}"

    p_tilde = [[(1.0 - p_clients[k][c]) / (C - 1) for c in range(C)] for k in range(K)]
    for k in range(K):
        assert abs(sum(p_tilde[k]) - 1.0) < 1e-12

    def lambda_empirical(beta):
        # Orthogonal unit class gradients g_c = e_c
        grads = [[p_clients[k][c] + beta * p_tilde[k][c] for c in range(C)] for k in range(K)]
        mean_norm_sq = sum(sum(g_c ** 2 for g_c in grads[k]) for k in range(K)) / K
        global_grad = [sum(grads[k][c] for k in range(K)) / K for c in range(C)]
        global_norm_sq = sum(g_c ** 2 for g_c in global_grad)
        return mean_norm_sq / global_norm_sq

    def lambda_analytic(beta):
        # Eq. (25) in Appendix P (normalized by 1/K^2 in denominator of Definition 2)
        var_sum = 0.0
        for k in range(K):
            mean_p = 1.0 / C
            var_k = sum((p_clients[k][c] - mean_p) ** 2 for c in range(C)) / C
            var_sum += var_k
        return (C ** 2 / K) * (((1.0 - beta / (C - 1)) / (1.0 + beta)) ** 2) * var_sum + 1.0

    betas = [0.0, 0.25, 0.5, 1.0, 1.5]  # C/2 - 1 = 1.5
    lam_vals = []
    for b in betas:
        le = lambda_empirical(b)
        la = lambda_analytic(b)
        assert abs(le - la) < 1e-12, f"Mismatch at beta={b}: {le} vs {la}"
        lam_vals.append(le)
    # Strictly decreasing on [0, C/2 - 1]
    for i in range(len(lam_vals) - 1):
        assert lam_vals[i + 1] < lam_vals[i], f"Lambda not decreasing: {lam_vals}"

    # 2. Verify Eq. (11): Not-true softmax & zero gradient wrt true-class logit z_y^l
    z_l = [2.4, -0.5, 1.1, 0.3, -1.2]
    z_g = [0.8, 0.2, 1.5, -0.4, 0.1]
    y = 0
    tau = 2.0

    def ntd_loss(z_student, z_teacher, true_y, temp):
        not_true = [c for c in range(C) if c != true_y]
        denom_s = sum(math.exp(z_student[c] / temp) for c in not_true)
        denom_t = sum(math.exp(z_teacher[c] / temp) for c in not_true)
        loss = 0.0
        for c in not_true:
            q_s = math.exp(z_student[c] / temp) / denom_s
            q_t = math.exp(z_teacher[c] / temp) / denom_t
            loss -= q_t * math.log(q_s / q_t)
        return loss

    eps = 1e-6
    z_l_pert = list(z_l)
    z_l_pert[y] += eps
    grad_true_logit = (ntd_loss(z_l_pert, z_g, y, tau) - ntd_loss(z_l, z_g, y, tau)) / eps
    assert abs(grad_true_logit) < 1e-15, f"True-class logit gradient must be 0, got {grad_true_logit}"

    # 3. Verify Proposition 2 (Eq. 14 & Appendix Q Eq. 41):
    # L_KL^{not-true} / (C - 1) == sum_{c=1}^C p_tilde_c E_{i notin S_c}[ -q_tau^{g,i}(c) log(q_tau^{l,i}(c)/q_tau^{g,i}(c)) ]
    samples = [
        (0, [2.1, 0.3, -0.4, 0.8, -1.0], [1.2, 0.5, 0.1, 0.4, -0.5]),
        (0, [1.8, -0.2, 0.5, 0.1, -0.7], [1.0, 0.2, 0.4, 0.3, -0.2]),
        (1, [-0.5, 2.5, 0.2, -0.3, 0.4], [0.1, 1.7, 0.3, -0.2, 0.2]),
        (2, [0.2, -0.1, 1.9, 0.6, -0.3], [0.3, 0.0, 1.4, 0.5, -0.1]),
        (3, [-0.4, 0.1, 0.3, 2.2, 0.0], [-0.1, 0.2, 0.2, 1.6, 0.1]),
        (4, [0.0, -0.3, -0.2, 0.4, 2.0], [0.1, -0.1, 0.0, 0.3, 1.5]),
    ]
    N_samp = len(samples)
    q_s_all, q_t_all = [], []
    for y_i, zs, zt in samples:
        ds = sum(math.exp(v / tau) for v in zs)
        dt = sum(math.exp(v / tau) for v in zt)
        q_s_all.append([math.exp(v / tau) / ds for v in zs])
        q_t_all.append([math.exp(v / tau) / dt for v in zt])

    l_kl_not_true_lhs = 0.0
    for i, (y_i, _, _) in enumerate(samples):
        for c in range(C):
            if c != y_i:
                l_kl_not_true_lhs += -q_t_all[i][c] * math.log(q_s_all[i][c] / q_t_all[i][c])
    l_kl_not_true_lhs /= (N_samp * (C - 1))

    l_kl_not_true_rhs = 0.0
    for c in range(C):
        not_sc = [i for i, (y_i, _, _) in enumerate(samples) if y_i != c]
        p_c_emp = (N_samp - len(not_sc)) / N_samp
        p_tilde_c_emp = (1.0 - p_c_emp) / (C - 1)
        mean_not_sc = sum(-q_t_all[i][c] * math.log(q_s_all[i][c] / q_t_all[i][c]) for i in not_sc) / len(not_sc)
        l_kl_not_true_rhs += p_tilde_c_emp * mean_not_sc

    assert abs(l_kl_not_true_lhs - l_kl_not_true_rhs) < 1e-14

    print(
        f"[PASS] Round 458 FedNTD verified: Lambda(0)={lam_vals[0]:.4f}->Lambda(1.5)={lam_vals[-1]:.4f}, "
        f"dL_NTD/dz_y={grad_true_logit:.1e}, Prop2_diff={abs(l_kl_not_true_lhs - l_kl_not_true_rhs):.2e}"
    )

if __name__ == "__main__":
    main()
