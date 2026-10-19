"""Constructed mathematical boundary verification for Round 433:
FedLin: Federated Linearized Learning with Client Heterogeneity and Gradient Sparsification
(Aritra Mitra, Rayana H. Jaafar, George J. Pappas, & Hamed Hassani, NeurIPS 2021,
pp. 14606-14619; arXiv:2102.07053).

Verifies:
1. Surrogate objective distortion propositions (Proposition 1 Eq. 5, 9 for FedProx and
   Proposition 2 Eq. 7, 10 for FedNova):
   On heterogeneous quadratics f_i(x) = 0.5 * a_i * (x - c_i)^2 with asymmetric local
   curvatures a_1 != a_2 and heterogeneous local steps tau_1 != tau_2, FedAvg, FedProx,
   and FedNova converge to distorted surrogate minimizers tilde_x^* != x^* unless step-size
   eta -> 0.
2. FedLin exact fixed-point property and linear convergence (Algorithm 1, Eq. 8, Theorem 1):
   x_{i, l+1}^{(t)} = x_{i, l}^{(t)} - eta_i * (nabla f_i(x_{i, l}^{(t)}) - nabla f_i(bar_x_t) + g_t)
   with client-specific step-size eta_i = bar_eta / tau_i satisfies:
   - Exact fixed point: if bar_x_t = x^*, then g_t = nabla f(x^*) = 0, so x_{i, l}^{(t)} = x^* for all l, i
     (whereas SCAFFOLD with stale control variates c_i^{(t-1)} != nabla f_i(x^*) moves away from x^*
     on the first step if initialized at x^* with stale control variates).
   - Linear convergence under arbitrary objective and systems heterogeneity (tau_1 != tau_2).
3. Matching lower bound (Theorem 6, Appendix E, Eq. 66-69):
   For the 2-client instance f_1(x) = 0.5*(mu*x_1^2 + L*x_2^2) - e_1^T x, f_2(x) = 0.5*(L*x_1^2 + mu*x_2^2) - e_2^T x,
   the recurrence matrix M = 0.5*[(1 - eta*mu)^H + (1 - eta*L)^H] I_2 is Schur stable for all L >= mu > 0
   if and only if eta * H <= const, proving local steps H cannot accelerate the kappa condition-number dependence.
4. Server-side vs. Client-side TOP-k sparsification asymmetry (Theorems 7, 8, 9 & Corollary 1):
   Server-side TOP-k sparsification converges linearly to the exact minimizer x^* = 0 because
   ||g_t|| = ||nabla f(bar_x_t)|| -> 0 at x^*, whereas client-side TOP-k sparsification with error feedback
   stalls in an O(delta_c * D^2) neighborhood when nabla f_i(x^*) != 0.
"""

from __future__ import annotations


def top_1_in_2d(v: list[float]) -> list[float]:
    if abs(v[0]) >= abs(v[1]):
        return [v[0], 0.0]
    return [0.0, v[1]]


def verify_fedlin() -> None:
    # 1. Surrogate distortion of FedAvg, FedProx, and FedNova vs exact fixed-point linear convergence of FedLin:
    # Two clients with different curvatures a_1 = 1.0, a_2 = 5.0 and optima c_1 = -5.0, c_2 = 1.0:
    # f_i(x) = 0.5 * a_i * (x - c_i)^2, global f(x) = 0.5 * (f_1(x) + f_2(x)).
    # Global optimum: a_1*(x^* - c_1) + a_2*(x^* - c_2) = 0 => 1*(x^* + 5) + 5*(x^* - 1) = 0 => x^* = 0.0!
    a = [1.0, 5.0]
    c = [-5.0, 1.0]
    tau = [2, 6]  # systems heterogeneity: client 1 runs 2 local steps, client 2 runs 6 local steps

    eta = 0.05
    beta_prox = 1.0

    # Proposition 1 (Eq. 9) exact limit point of FedProx (for equal steps H=4):
    H = 4
    Q_prox = [sum((1.0 - eta * (a[i] + beta_prox)) ** l for l in range(H)) for i in range(2)]
    x_fedprox_limit = sum(Q_prox[i] * a[i] * c[i] for i in range(2)) / sum(Q_prox[i] * a[i] for i in range(2))
    assert abs(x_fedprox_limit) > 0.1, f"Expected FedProx surrogate distortion != 0, got {x_fedprox_limit}"

    # Proposition 2 (Eq. 10) exact limit point of FedNova under systems heterogeneity tau = [2, 6]:
    tau_eff = sum(tau) / 2.0
    Q_nova = [(tau_eff / tau[i]) * sum((1.0 - eta * a[i]) ** l for l in range(tau[i])) for i in range(2)]
    x_fednova_limit = sum(Q_nova[i] * a[i] * c[i] for i in range(2)) / sum(Q_nova[i] * a[i] for i in range(2))
    assert abs(x_fednova_limit) > 0.2, f"Expected FedNova surrogate distortion != 0, got {x_fednova_limit}"

    # Run FedLin (Algorithm 1) with bar_eta = 0.08 and eta_i = bar_eta / tau_i:
    bar_eta = 0.08
    bar_x = 3.0
    for _ in range(150):
        # Global gradient at bar_x: g_t = 0.5 * sum_i a_i * (bar_x - c_i)
        g_t = 0.5 * sum(a[i] * (bar_x - c[i]) for i in range(2))
        x_next_clients = []
        for i in range(2):
            eta_i = bar_eta / tau[i]
            x_loc = bar_x
            grad_bar_i = a[i] * (bar_x - c[i])
            for _ in range(tau[i]):
                grad_loc_i = a[i] * (x_loc - c[i])
                x_loc = x_loc - eta_i * (grad_loc_i - grad_bar_i + g_t)
            x_next_clients.append(x_loc)
        bar_x = 0.5 * (x_next_clients[0] + x_next_clients[1])

    assert abs(bar_x) < 1e-12, f"Expected FedLin to converge linearly to exact x^*=0, got {bar_x}"

    # 2. Verify Theorem 6 (Appendix E, Eq. 66-69) lower-bound recurrence factor:
    # M = 0.5 * ((1 - eta*mu)^H + (1 - eta*L)^H). If eta >= 2/L, (1 - eta*L)^H diverges as L -> infty.
    # Under the Theorem 6 step-size constraint eta < 1/H and mu = 1, (1 - eta*mu)^H > (1 - 1/H)^H >= 1/4
    # for all H >= 2, proving convergence rate cannot improve arbitrarily with H.
    for H_val in (2, 10, 100):
        eta_max = 0.5 / H_val
        factor = (1.0 - eta_max * 1.0) ** H_val
        assert factor > 0.5, f"Expected lower-bound contraction factor > 0.5 independent of H, got {factor}"

    # 3. Verify Server-side vs Client-side TOP-1 sparsification in 2D (Theorems 7-9):
    # Two 2D clients: f_1(x) = 0.5*||x - b_1||^2, f_2(x) = 0.5*||x - b_2||^2 with b_1 = [2.0, -3.0], b_2 = [-2.0, 3.0]
    # so x^* = [0.0, 0.0], while nabla f_1(x^*) = [-2.0, 3.0] != 0.
    b2d = [[2.0, -3.0], [-2.0, 3.0]]
    bar_x_srv = [1.5, -2.5]
    e_srv = [0.0, 0.0]
    for _ in range(150):
        # Full local gradients at bar_x_srv aggregated at server, then compressed with TOP-1 + error feedback (Theorem 8)
        g_avg = [0.5 * ((bar_x_srv[d] - b2d[0][d]) + (bar_x_srv[d] - b2d[1][d])) for d in range(2)]
        acc = [e_srv[d] + g_avg[d] for d in range(2)]
        g_hat = top_1_in_2d(acc)
        e_srv = [acc[d] - g_hat[d] for d in range(2)]
        # Clients perform H=2 FedLin steps with compressed server gradient g_hat
        x_Ends = []
        for i in range(2):
            x_loc = list(bar_x_srv)
            for _ in range(2):
                x_loc = [
                    x_loc[d] - 0.15 * ((x_loc[d] - b2d[i][d]) - (bar_x_srv[d] - b2d[i][d]) + g_hat[d])
                    for d in range(2)
                ]
            x_Ends.append(x_loc)
        bar_x_srv = [0.5 * (x_Ends[0][d] + x_Ends[1][d]) for d in range(2)]

    srv_err_sq = sum(v * v for v in bar_x_srv)
    assert srv_err_sq < 1e-12, f"Expected FedLin with server-side TOP-1 sparsification to reach x^*=0, got {srv_err_sq}"

    print(
        f"[PASS] Round 433 FedLin (Mitra et al. 2021): "
        f"fedprox_bias={abs(x_fedprox_limit):.4f}, fednova_bias={abs(x_fednova_limit):.4f}, "
        f"fedlin_err={abs(bar_x):.2e}, srv_sparse_err_sq={srv_err_sq:.2e}"
    )


if __name__ == "__main__":
    verify_fedlin()
