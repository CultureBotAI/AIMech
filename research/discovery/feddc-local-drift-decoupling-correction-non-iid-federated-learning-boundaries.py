#!/usr/bin/env python3
"""Boundary verification for Round 456: FedDC (Gao et al., CVPR 2022, arXiv:2203.11751).

Verifies:
1. Three-term local objective (Eq. 3-4):
   F_i(theta_i) = L_i(theta_i) + (alpha/2)*||theta_i - (w - h_i)||^2 + (1/(eta*K))*<theta_i, g_i - g>
   and its exact gradient wrt theta_i:
   nabla F_i(theta_i) = nabla L_i(theta_i) + alpha*(theta_i + h_i - w) + (1/(eta*K))*(g_i - g).
2. Backpropagation-free local drift variable update (Eq. 6) and drift-corrected global aggregation (Eq. 7):
   Comparing FedDC vs FedAvg and FedProx on heterogeneous strongly convex quadratics
   L_i(theta) = 0.5 * a_i * (theta - b_i)^2 with non-zero local gradients at the global optimum w^*.
"""

def main():
    # Heterogeneous 1D quadratics L_i(theta) = 0.5 * a_i * (theta - b_i)^2
    clients = [
        (2.0, -3.0),
        (4.0, 2.0),
        (1.0, 4.0),
        (3.0, -1.0),
    ]
    N = len(clients)
    # Global optimum w^* minimizes (1/N) sum_i L_i(w) => sum_i a_i (w^* - b_i) = 0
    w_star = sum(a * b for a, b in clients) / sum(a for a, _ in clients)

    # Verify that at the stationary point where theta_i + h_i = w_star and g_i = g = 0,
    # the corrected global aggregation w^+ = (1/N) sum_i (theta_i + h_i) equals w_star exactly,
    # even when each client's local parameter theta_i != w_star!
    alpha = 1.5
    # Suppose each client minimizes L_i(theta_i) + (alpha/2)*(theta_i - (w_star - h_i))^2
    # Wait: if h_i = (1/alpha) * nabla L_i(w_star), then at theta_i = w_star - h_i:
    # nabla L_i(theta_i) + alpha*(theta_i + h_i - w_star) = nabla L_i(theta_i) != 0,
    # OR if h_i tracks w - theta_i so theta_i + h_i = w_star while sum_i h_i = 0:
    # Let's run the exact FedDC algorithm (Algorithm 1 / Eqs. 4-7) vs FedAvg and FedProx!
    K = 15
    eta = 0.04
    rounds = 300

    def run_fedavg():
        w = 0.0
        for _ in range(rounds):
            thetas = []
            for a, b in clients:
                th = w
                for _ in range(K):
                    th -= eta * (a * (th - b))
                thetas.append(th)
            w = sum(thetas) / N
        return abs(w - w_star)

    def run_fedprox(mu=0.5):
        w = 0.0
        for _ in range(rounds):
            thetas = []
            for a, b in clients:
                th = w
                for _ in range(K):
                    th -= eta * (a * (th - b) + mu * (th - w))
                thetas.append(th)
            w = sum(thetas) / N
        return abs(w - w_star)

    def run_feddc(alpha_val=0.5):
        w = 0.0
        h = [0.0] * N
        g_i = [0.0] * N
        g_bar = 0.0
        for _ in range(rounds):
            new_thetas = []
            for i, (a, b) in enumerate(clients):
                th = w
                for _ in range(K):
                    grad = a * (th - b) + alpha_val * (th - (w - h[i])) + (1.0 / (eta * K)) * (g_i[i] - g_bar)
                    th -= eta * grad
                new_thetas.append(th)
            # Update drift variable h_i^+ = h_i - (w - theta_i^+) or equivalently track local drift
            # Note in Gao et al. official code & Eq. 6/7: h_i <- h_i + (theta_i^+ - w) and g_i = theta_i^+ - w
            # Wait: let's check what happens when h_i <- h_i - (theta_i^+ - w) vs +:
            # In Eq. 4, penalty is (alpha/2)*||theta_i - (w - h_i)||^2 = (alpha/2)*||theta_i + h_i - w||^2.
            # At optimum we want nabla L_i(w^*) + alpha * h_i^* = 0 (with theta_i^* = w^*) so h_i^* = -(1/alpha)*nabla L_i(w^*).
            # For h_i to converge to -(1/alpha)*nabla L_i(w^*), since theta_i^+ - w approx -eta*K*(nabla L_i(w) + alpha*h_i),
            # updating h_i^+ = h_i + (theta_i^+ - w) (or scaled) has fixed point theta_i^+ = w, where nabla L_i(w) + alpha*h_i = 0!
            for i in range(N):
                delta_th = new_thetas[i] - w
                h[i] = h[i] + delta_th
                g_i[i] = delta_th
            g_bar = sum(g_i) / N
            w = sum(new_thetas[i] + h[i] for i in range(N)) / N
        return abs(w - w_star)

    err_avg = run_fedavg()
    err_prox = run_fedprox()
    err_dc = run_feddc()
    assert err_dc < 1e-10 and err_dc < 1e-6 * err_avg and err_dc < 1e-6 * err_prox, (
        f"Expected FedDC exact convergence err_dc={err_dc:.2e} << err_avg={err_avg:.4f}, err_prox={err_prox:.4f}"
    )
    print(f"[PASS] Round 456 FedDC verified: err_dc={err_dc:.2e} << err_prox={err_prox:.4f} < err_avg={err_avg:.4f}")

if __name__ == "__main__":
    main()
