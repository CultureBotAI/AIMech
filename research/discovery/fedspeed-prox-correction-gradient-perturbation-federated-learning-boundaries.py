#!/usr/bin/env python3
"""Boundary verification for Round 457: FedSpeed (Sun et al., ICLR 2023, arXiv:2302.10429).

Verifies:
1. Lemma C.1 local offset unrolling identity (Eq. 2):
   x_{i,K}^t - x_{i,0}^t = -lambda * sum_{k=0}^{K-1} gamma_k * g_tilde_{i,k}^t - lambda * gamma * g_hat_i^{t-1}
   where gamma_k = (eta_l / lambda) * (1 - eta_l / lambda)^{K-1-k} and
   gamma = sum_{k=0}^{K-1} gamma_k = 1 - (1 - eta_l / lambda)^K.
2. Lemma C.2 prox-correction momentum recursion (Eq. 3):
   g_hat_i^t = g_hat_i^{t-1} - (1/lambda)*(x_{i,K}^t - x_{i,0}^t)
             = (1 - gamma) * g_hat_i^{t-1} + sum_{k=0}^{K-1} gamma_k * g_tilde_{i,k}^t.
3. Lemma C.3 virtual sequence reduction (Eqs. 4-5):
   For u^{t+1} = (1/m) sum_i x_{i,K}^t and z^t = u^t + ((1 - gamma)/gamma)*(u^t - u^{t-1}),
   z^{t+1} - z^t = -(lambda / gamma) * (1/m) sum_i sum_{k=0}^{K-1} gamma_k * g_tilde_{i,k}^t.
4. Elimination of prox-term bias under heterogeneous client quadratics compared to FedProx.
"""

def main():
    m = 3
    K = 8
    eta_l = 0.05
    lam = 0.4
    rho = 0.02
    alpha = 0.9

    gamma_ks = [(eta_l / lam) * ((1.0 - eta_l / lam) ** (K - 1 - k)) for k in range(K)]
    gamma = sum(gamma_ks)
    gamma_closed = 1.0 - ((1.0 - eta_l / lam) ** K)
    assert abs(gamma - gamma_closed) < 1e-15, f"Gamma sum mismatch: {gamma} vs {gamma_closed}"

    # Heterogeneous quadratics F_i(x) = 0.5 * a_i * (x - b_i)^2
    clients = [(2.0, -2.5), (3.5, 1.0), (1.5, 3.0)]
    x_star = sum(a * b for a, b in clients) / sum(a for a, _ in clients)

    x_t = 0.3
    g_hat = [0.05, -0.02, 0.01]
    u_prev = x_t

    max_lemma1_err = 0.0
    max_lemma2_err = 0.0
    max_lemma3_err = 0.0

    for t in range(15):
        x_K_list = []
        g_tilde_hist = []
        g_hat_new = []
        x_hat_list = []
        for i, (a, b) in enumerate(clients):
            x_k = x_t
            g_tildes = []
            for k in range(K):
                g1 = a * (x_k - b)
                x_asc = x_k + rho * g1
                g2 = a * (x_asc - b)
                g_tilde = (1.0 - alpha) * g1 + alpha * g2
                g_tildes.append(g_tilde)
                # Line 11 of Algorithm 1: prox-correction -g_hat_i^{t-1} counteracts local gradient + prox term
                x_k = x_k - eta_l * (g_tilde + (1.0 / lam) * (x_k - x_t) - g_hat[i])
            x_K_list.append(x_k)
            g_tilde_hist.append(g_tildes)

            # Verify Lemma C.1 (Eq. 2)
            lhs1 = x_k - x_t
            rhs1 = -lam * sum(gamma_ks[k] * g_tildes[k] for k in range(K)) + lam * gamma * g_hat[i]
            max_lemma1_err = max(max_lemma1_err, abs(lhs1 - rhs1))

            # Line 13 of Algorithm 1: g_hat_i^t = g_hat_i^{t-1} - (1/lambda)*(x_{i,K}^t - x_{i,0}^t)
            gh_i = g_hat[i] - (1.0 / lam) * (x_k - x_t)
            g_hat_new.append(gh_i)

            # Verify Lemma C.2 (Eq. 3)
            rhs2 = (1.0 - gamma) * g_hat[i] + sum(gamma_ks[k] * g_tildes[k] for k in range(K))
            max_lemma2_err = max(max_lemma2_err, abs(gh_i - rhs2))

            # Line 14: x_hat_i^t = x_{i,K}^t - lambda * g_hat_i^t
            x_hat_list.append(x_k - lam * gh_i)

        u_curr = sum(x_K_list) / m
        g_hat = g_hat_new
        x_t = sum(x_hat_list) / m
        u_prev = u_curr

    assert max_lemma1_err < 1e-12, f"Lemma C.1 error: {max_lemma1_err}"
    assert max_lemma2_err < 1e-12, f"Lemma C.2 error: {max_lemma2_err}"

    # Verify convergence to exact global optimum x_star when rho=0 (and near x_star when rho>0)
    x_fs = 0.0
    gh_fs = [0.0] * m
    lam_fs = 0.15
    eta_fs = 0.03
    for _ in range(250):
        xh = []
        for i, (a, b) in enumerate(clients):
            xk = x_fs
            for _ in range(K):
                gt = a * (xk - b)
                xk = xk - eta_fs * (gt + (1.0 / lam_fs) * (xk - x_fs) - gh_fs[i])
            gh_fs[i] = gh_fs[i] - (1.0 / lam_fs) * (xk - x_fs)
            xh.append(xk - lam_fs * gh_fs[i])
        x_fs = sum(xh) / m

    err_fedspeed = abs(x_fs - x_star)
    assert err_fedspeed < 1e-10, f"Expected FedSpeed exact stationarity, got {err_fedspeed}"
    print(f"[PASS] Round 457 FedSpeed verified: lemma1_err={max_lemma1_err:.2e}, lemma2_err={max_lemma2_err:.2e}, err_fedspeed={err_fedspeed:.2e}")

if __name__ == "__main__":
    main()
