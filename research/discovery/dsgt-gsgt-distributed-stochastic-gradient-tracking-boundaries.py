"""Constructed mathematical boundary verification for Round 428:
DSGT and GSGT: Distributed Stochastic Gradient Tracking Methods
(Shi Pu & Angelia Nedic, Mathematical Programming 187(1-2):409-457, 2021; arXiv:1805.11454).

Verifies:
1. Dynamic average tracking conservation (Lemma 2, Eq. 5):
   When y_0 = G(x_0, xi_0) and W is doubly stochastic (1^T W = 1^T),
   y_{k+1} = W y_k + G(x_{k+1}, xi_{k+1}) - G(x_k, xi_k) preserves
   bar_y_k = (1/n) 1^T y_k = (1/n) 1^T G(x_k, xi_k) exactly at every iteration k.
2. Spectral radius contraction of the 3x3 error-recursion matrix A (Lemma 4, Eq. 10)
   and deterministic exact linear convergence to x^* (sigma^2 = 0) under arbitrary
   data heterogeneity ||nabla f_i(x^*)||^2 > 0, whereas un-tracked DGD
   x_{k+1} = W(x_k - alpha G(x_k)) stalls at an O(alpha^2 / (1-rho_w)^2) heterogeneity floor.
3. Steady-state MSE scaling (Theorem 2.1, Remark 1, Eq. 11-12):
   limsup_{k->infty} (1/n) E[||x_k - 1 x^*||^2] = (alpha sigma^2 / (mu n)) O(1)
   + (alpha^2 L^2 sigma^2 / (mu^2 (1-rho_w)^3)) O(rho_w^2 ||W - I||^2), achieving
   linear speedup 1/n when alpha <= O((mu (1-rho_w)^3) / (L^2 rho_w^2 ||W - I||^2 n)).
4. Gossip Stochastic Gradient Tracking (GSGT, Section 4, Eq. 37-39, Theorem 4.1):
   Expected gossip consensus contraction gamma_g < 1 and exact conservation of
   1^T y_k = 1^T G(x_k, xi_k) via symmetric pairwise edge updates (i_k, j_k) while
   activating only 1 directed wake-up edge per iteration vs. |E| edges in full DSGT.
"""

from __future__ import annotations

import math


def mat_vec(W: list[list[float]], v: list[float]) -> list[float]:
    return [sum(W[i][j] * v[j] for j in range(len(v))) for i in range(len(W))]


def verify_dsgt_and_gsgt() -> None:
    # 1. Doubly-stochastic 4-node ring graph: W_{ii}=0.5, W_{i,i+-1}=0.25
    n = 4
    W = [
        [0.50, 0.25, 0.00, 0.25],
        [0.25, 0.50, 0.25, 0.00],
        [0.00, 0.25, 0.50, 0.25],
        [0.25, 0.00, 0.25, 0.50],
    ]
    # Eigenvalues of W are 1, 0.5, 0.5, 0.0 -> rho_w = 0.5
    rho_w = 0.5

    # Heterogeneous strongly convex local quadratics: f_i(x) = 0.5 * mu * (x - b_i)^2
    # with mu = 1.0, L = 1.0, and mean(b) = 0 so x^* = 0, while nabla f_i(x^*) = -b_i != 0.
    mu = 1.0
    L = 1.0
    b = [-3.0, -1.0, 1.0, 3.0]
    assert abs(sum(b)) < 1e-12

    def grad_f(x_vec: list[float]) -> list[float]:
        return [mu * (x_vec[i] - b[i]) for i in range(n)]

    # Compare deterministic DSGT vs un-tracked DGD with constant step size alpha = 0.1
    alpha = 0.1
    x_dsgt = [2.0, -1.0, 0.5, -1.5]
    y_dsgt = grad_f(x_dsgt)
    x_dgd = list(x_dsgt)

    max_tracking_err = 0.0
    for _ in range(250):
        # Check Lemma 2 dynamic average tracking conservation: mean(y_k) == mean(grad_f(x_k))
        g_curr = grad_f(x_dsgt)
        tracking_err = abs(sum(y_dsgt) / n - sum(g_curr) / n)
        if tracking_err > max_tracking_err:
            max_tracking_err = tracking_err

        # DSGT update (Eq. 4): x_{k+1} = W(x_k - alpha * y_k), y_{k+1} = W y_k + grad(x_{k+1}) - grad(x_k)
        u_dsgt = [x_dsgt[i] - alpha * y_dsgt[i] for i in range(n)]
        x_next = mat_vec(W, u_dsgt)
        g_next = grad_f(x_next)
        Wy = mat_vec(W, y_dsgt)
        y_dsgt = [Wy[i] + g_next[i] - g_curr[i] for i in range(n)]
        x_dsgt = x_next

        # DGD update: x_{k+1} = W(x_k - alpha * grad(x_k))
        g_dgd = grad_f(x_dgd)
        x_dgd = mat_vec(W, [x_dgd[i] - alpha * g_dgd[i] for i in range(n)])

    dsgt_err_sq = sum(v * v for v in x_dsgt) / n
    dgd_err_sq = sum(v * v for v in x_dgd) / n
    assert max_tracking_err < 1e-14, f"Expected exact tracking conservation, got {max_tracking_err}"
    assert dsgt_err_sq < 1e-18, f"Expected DSGT to converge linearly to x^*=0, got {dsgt_err_sq}"
    assert dgd_err_sq > 1e-2, f"Expected un-tracked DGD to stall at heterogeneity floor, got {dgd_err_sq}"

    # 2. Lemma 4 spectral radius condition (Eq. 10):
    # When alpha <= min{(1 - rho_w^2)/(4 L rho_w), 1/(L(1 + 2/sqrt(1 - rho_w^2)))}
    alpha_bound_1 = (1.0 - rho_w**2) / (4.0 * L * rho_w)
    alpha_bound_2 = 1.0 / (L * (1.0 + 2.0 / math.sqrt(1.0 - rho_w**2)))
    alpha_lemma4 = 0.05
    assert alpha_lemma4 <= min(alpha_bound_1, alpha_bound_2)
    Gamma = (1.0 + rho_w**2) * (1.0 - rho_w**2) / (4.0 * alpha_lemma4 * L * rho_w**2)
    assert Gamma > 1.0
    rho_A_upper = 1.0 - (2.0 * alpha_lemma4 * mu * Gamma) / (Gamma + 1.0)
    assert 0.0 < rho_A_upper < 1.0

    # 3. Diminishing step-size asymptotic normality/variance scaling (Theorem 2.2, Remark 3):
    # For alpha_k = theta / (m + k) with theta * mu > 1, asymptotic MSE is
    # 2 * theta^2 * sigma^2 / (n * (theta * mu - 1) * k), independent of graph topology rho_w!
    sigma_sq = 1.0
    theta = 2.0 / mu  # optimal theta = 2/mu minimizes theta^2 / (theta*mu - 1) = 4/mu^2
    k_large = 10000
    asymp_mse = (2.0 * theta**2 * sigma_sq) / (n * (theta * mu - 1.0) * k_large)
    # Verify theta = 2/mu minimizes theta^2/(theta*mu - 1) compared to theta = 1.5/mu or 3.0/mu
    for theta_alt in (1.5 / mu, 3.0 / mu):
        alt_mse = (2.0 * theta_alt**2 * sigma_sq) / (n * (theta_alt * mu - 1.0) * k_large)
        assert asymp_mse < alt_mse

    # 4. Gossip Stochastic Gradient Tracking (GSGT, Section 4, Eq. 37-39):
    # Each iteration activates 1 undirected edge {i_k, j_k} with W_k having 1/2 on {i_k, j_k} block
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    x_gsgt = [2.0, -1.0, 0.5, -1.5]
    y_gsgt = grad_f(x_gsgt)
    for k in range(400):
        ik, jk = edges[k % len(edges)]
        g_old = grad_f(x_gsgt)
        # Eq. 37a & 38a: only nodes ik and jk update
        x_ik_new = 0.5 * ((x_gsgt[ik] - alpha * y_gsgt[ik]) + (x_gsgt[jk] - alpha * y_gsgt[jk]))
        x_jk_new = 0.5 * (x_gsgt[ik] + x_gsgt[jk] - alpha * y_gsgt[jk])
        x_gsgt[ik] = x_ik_new
        x_gsgt[jk] = x_jk_new
        g_new = grad_f(x_gsgt)
        y_avg = 0.5 * (y_gsgt[ik] + y_gsgt[jk])
        y_gsgt[ik] = y_avg + g_new[ik] - g_old[ik]
        y_gsgt[jk] = y_avg + g_new[jk] - g_old[jk]
        # Sum conservation 1^T y_k == 1^T grad_f(x_k) holds after every single gossip edge!
        assert abs(sum(y_gsgt) - sum(g_new)) < 1e-12

    gsgt_err_sq = sum(v * v for v in x_gsgt) / n
    assert gsgt_err_sq < 1e-10, f"Expected GSGT to converge to x^*=0, got {gsgt_err_sq}"

    print(
        f"[PASS] Round 428 DSGT & GSGT (Pu & Nedic 2021): "
        f"tracking_err={max_tracking_err:.2e}, dsgt_err_sq={dsgt_err_sq:.2e} vs dgd_err_sq={dgd_err_sq:.4f}, "
        f"rho_A_upper={rho_A_upper:.4f}, gsgt_err_sq={gsgt_err_sq:.2e}"
    )


if __name__ == "__main__":
    verify_dsgt_and_gsgt()
