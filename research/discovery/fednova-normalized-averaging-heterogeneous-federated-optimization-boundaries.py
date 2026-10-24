#!/usr/bin/env python3
"""Boundary verification for Round 386: FedNova Normalized Averaging for Heterogeneous Federated Optimization
(Wang, Liu, Liang, Joshi, & Poor 2020, NeurIPS 2020, pp. 7611-7623, arXiv:2007.07481).

Verifies:
1. Lemma 4 / Theorem 2 closed-form objective inconsistency for quadratic local objectives
   F_i(x) = 0.5 * H_i * x^2 - e_i * x with heterogeneous local steps tau_i:
   true optimum x* = (sum_i p_i H_i)^{-1} (sum_i p_i e_i),
   FedAvg limit as eta -> 0: x_inf^{FedAvg} = (sum_i p_i tau_i H_i)^{-1} (sum_i p_i tau_i e_i) != x*,
   and non-vanishing gradient norm ||nabla F(x_inf^{FedAvg})||^2 > 0 scaling with chi^2_{p||w},
   whereas FedNova limit as eta -> 0 is exact x_inf^{FedNova} = x*!
2. Local solver weighting vectors a_i in R^{tau_i} and L1 norms ||a_i||_1 (Section 4.1-4.3):
   - Vanilla SGD: a_i = [1, 1, ..., 1]^T, ||a_i||_1 = tau_i
   - Proximal SGD (FedProx with alpha = eta * mu): a_i = [(1-alpha)^{tau_i-1}, ..., 1]^T,
     ||a_i||_1 = (1 - (1-alpha)^{tau_i}) / alpha
   - Momentum SGD (factor rho): a_i = [1 - rho^{tau_i}, ..., 1 - rho]^T / (1 - rho),
     ||a_i||_1 = (tau_i - rho * (1 - rho^{tau_i}) / (1 - rho)) / (1 - rho)
3. FedNova normalized averaging (Section 5, Theorem 3):
   d_i^{(t)} = G_i^{(t)} a_i / ||a_i||_1 and x^{(t+1,0)} = x^{(t,0)} - tau_eff * sum_i p_i eta d_i^{(t)}
   eliminates objective inconsistency (chi^2_{p||w} = 0) and converges to x* across all three
   local solver types (Vanilla, Proximal, Momentum) under heterogeneous tau_i.
"""

from __future__ import annotations


def run_local_solver(
    x0: float,
    h_i: float,
    e_i: float,
    eta: float,
    tau_i: int,
    solver: str,
    alpha: float = 0.1,
    rho: float = 0.8,
) -> tuple[float, list[float], list[float]]:
    x = x0
    grads: list[float] = []
    u = 0.0
    for _ in range(tau_i):
        g = h_i * x - e_i
        grads.append(g)
        if solver == "sgd":
            x = x - eta * g
        elif solver == "prox":
            x = x - eta * (g + (alpha / eta) * (x - x0))
        elif solver == "momentum":
            u = rho * u + g
            x = x - eta * u
        else:
            raise ValueError(solver)
    if solver == "sgd":
        a_i = [1.0] * tau_i
    elif solver == "prox":
        a_i = [(1.0 - alpha) ** (tau_i - 1 - k) for k in range(tau_i)]
    elif solver == "momentum":
        a_i = [(1.0 - (rho ** (tau_i - k))) / (1.0 - rho) for k in range(tau_i)]
    else:
        raise ValueError(solver)
    return x, grads, a_i


def main() -> None:
    p = [0.25, 0.25, 0.25, 0.25]
    H = [2.0, 4.0, 1.5, 3.5]
    e = [1.0, -3.0, 4.0, -2.0]
    taus = [2, 10, 1, 15]

    h_bar = sum(pi * hi for pi, hi in zip(p, H))
    e_bar = sum(pi * ei for pi, ei in zip(p, e))
    x_star = e_bar / h_bar

    # 1. Verify Lemma 4 / Theorem 2 FedAvg surrogate limit vs true optimum
    w_fedavg = [pi * ti for pi, ti in zip(p, taus)]
    w_sum = sum(w_fedavg)
    w_fedavg = [wi / w_sum for wi in w_fedavg]
    chi2_pw = sum(((pi - wi) ** 2) / wi for pi, wi in zip(p, w_fedavg))
    assert chi2_pw > 0.3, f"Expected substantial chi^2 mismatch, got {chi2_pw}"

    x_fedavg_limit = sum(wi * ei for wi, ei in zip(w_fedavg, e)) / sum(
        wi * hi for wi, hi in zip(w_fedavg, H)
    )
    grad_at_fedavg_limit = abs(h_bar * x_fedavg_limit - e_bar)
    assert grad_at_fedavg_limit > 0.4, f"Expected non-vanishing gradient, got {grad_at_fedavg_limit}"

    # 2. Verify exact algebraic identity x^{(t,0)} - x_i^{(t,tau_i)} == eta * sum_k a_{i,k} g_{i,k}
    # and closed-form ||a_i||_1 formulas for all 3 solvers
    eta0 = 0.005
    alpha = 0.08
    rho = 0.75
    for solver in ("sgd", "prox", "momentum"):
        for i in range(4):
            x_end, grads, a_i = run_local_solver(
                1.25, H[i], e[i], eta0, taus[i], solver, alpha=alpha, rho=rho
            )
            lhs = 1.25 - x_end
            rhs = eta0 * sum(ak * gk for ak, gk in zip(a_i, grads))
            assert abs(lhs - rhs) < 1e-12, f"Solver {solver} identity mismatch: {lhs} vs {rhs}"
            l1 = sum(abs(ak) for ak in a_i)
            if solver == "sgd":
                l1_formula = float(taus[i])
            elif solver == "prox":
                l1_formula = (1.0 - ((1.0 - alpha) ** taus[i])) / alpha
            else:
                l1_formula = (
                    taus[i] - rho * (1.0 - (rho ** taus[i])) / (1.0 - rho)
                ) / (1.0 - rho)
            assert abs(l1 - l1_formula) < 1e-12, f"L1 formula mismatch for {solver}: {l1} vs {l1_formula}"

    # 3. Compare FedAvg vs FedNova with diminishing step size eta_t (Lemma 4 limit eta -> 0)
    x_fa = 1.0
    for t in range(1, 800):
        eta_t = 0.004 / (1.0 + 0.015 * t)
        deltas = []
        l1s = []
        for i in range(4):
            x_end, grads, a_i = run_local_solver(x_fa, H[i], e[i], eta_t, taus[i], "sgd")
            deltas.append(x_end - x_fa)
            l1s.append(sum(a_i))
        tau_eff = sum(pi * l1 for pi, l1 in zip(p, l1s))
        d_list = [-(x_end_delta) / (eta_t * l1) for x_end_delta, l1 in zip(deltas, l1s)]
        x_fa = x_fa - tau_eff * eta_t * sum(wi * di for wi, di in zip(w_fedavg, d_list))

    fednova_errs = {}
    for solver in ("sgd", "prox", "momentum"):
        x_fn = 1.0
        for t in range(1, 800):
            eta_t = 0.004 / (1.0 + 0.015 * t)
            alpha_t = 2.0 * eta_t
            d_list = []
            l1s = []
            for i in range(4):
                x_end, grads, a_i = run_local_solver(
                    x_fn, H[i], e[i], eta_t, taus[i], solver, alpha=alpha_t, rho=rho
                )
                l1 = sum(a_i)
                l1s.append(l1)
                d_i = sum(ak * gk for ak, gk in zip(a_i, grads)) / l1
                d_list.append(d_i)
            tau_eff = sum(pi * l1 for pi, l1 in zip(p, l1s))
            x_fn = x_fn - tau_eff * eta_t * sum(pi * di for pi, di in zip(p, d_list))
        fednova_errs[solver] = abs(x_fn - x_star)
        assert fednova_errs[solver] < 1e-2, f"FedNova ({solver}) failed to converge to x*: err={fednova_errs[solver]}"

    fa_err = abs(x_fa - x_star)
    fa_limit_diff = abs(x_fa - x_fedavg_limit)
    assert fa_err > 0.15, f"FedAvg should exhibit objective inconsistency bias, got {fa_err}"
    assert fa_limit_diff < 5e-3, f"FedAvg should approach surrogate optimum x_inf^{{FedAvg}}, diff={fa_limit_diff}"

    print(
        f"[PASS] Round 386 FedNova (Wang et al. 2020): chi2_pw={chi2_pw:.4f}, "
        f"fa_err={fa_err:.4f} (surrogate_diff={fa_limit_diff:.4e}), "
        f"fednova_errs(sgd={fednova_errs['sgd']:.2e}, prox={fednova_errs['prox']:.2e}, mom={fednova_errs['momentum']:.2e})"
    )


if __name__ == "__main__":
    main()
