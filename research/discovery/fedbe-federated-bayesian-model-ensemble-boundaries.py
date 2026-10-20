#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 475:
FedBE (Making Bayesian Model Ensemble Applicable to Federated Learning,
Chen & Chao 2021, ICLR 2021, arXiv:2009.01974).

Verifies:
1. Diagonal Gaussian posterior fitting over client models {w_i} (Equation 5):
   mu = sum_i (|D_i| / |D|) w_i (which equals the FedAvg weight average w_bar),
   Sigma_diag = diag(sum_i (|D_i| / |D|) (w_i - mu)^2),
   and Dirichlet simplex convex-combination posterior (Equations 6-7):
   w^{(m)} = sum_i (gamma_i^{(m)} |D_i| / sum_{i'} gamma_{i'}^{(m)} |D_{i'}|) w_i,
   gamma^{(m)} ~ Dir(alpha).
2. Second-order Taylor expansion of Bayesian model ensemble vs FedAvg (Equations 8-9):
   (1/M) sum_{m=1}^M p(y | x; w^{(m)}) - p(y | x; w_bar)
   = <nabla_w p(y | x; w_bar), (1/M) sum_m Omega^{(m)}> + O(Omega^2),
   demonstrating non-zero curvature gain O(Omega^2) on nonlinear predictive models
   even when E[Omega^{(m)}] = 0.
3. Server-side ensemble knowledge distillation with Stochastic Weight Averaging (SWA)
   (Algorithm 1): pseudo-labeling unlabeled server data U = {x_j}_{j=1}^J via
   p_hat_j = (1/M') sum_{m'=1}^{M'} p(y | x_j; w^{(m')}) over
   {w_bar} U {w_i} U {w^{(m)}} and averaging cyclical-step student iterates.
"""

from __future__ import annotations
import math
import random


def sigmoid(z: float) -> float:
    return 1.0 / (1.0 + math.exp(-z))


def predict_prob(x: list[float], w: list[float]) -> float:
    # Nonlinear 2-unit neural predictor: p(y=1 | x; w) = sigmoid(w[2]*tanh(w[0]*x[0] + w[1]*x[1]))
    h = math.tanh(w[0] * x[0] + w[1] * x[1])
    return sigmoid(w[2] * h)


def fit_gaussian_posterior(
    client_weights: list[list[float]], client_sizes: list[int]
) -> tuple[list[float], list[float]]:
    total_d = sum(client_sizes)
    dim = len(client_weights[0])
    mu = [
        sum((client_sizes[i] / total_d) * client_weights[i][d] for i in range(len(client_weights)))
        for d in range(dim)
    ]
    var_diag = [
        sum(
            (client_sizes[i] / total_d) * ((client_weights[i][d] - mu[d]) ** 2)
            for i in range(len(client_weights))
        )
        for d in range(dim)
    ]
    return mu, var_diag


def main() -> None:
    rng = random.Random(475)
    client_weights = [
        [1.4, -0.2, 1.8],
        [-0.3, 1.5, 1.6],
        [0.8, 0.9, 2.0],
    ]
    client_sizes = [100, 100, 100]

    # 1. Verify Eq (5) Gaussian mean equals FedAvg w_bar and variance is strictly positive under client drift
    w_bar, var_diag = fit_gaussian_posterior(client_weights, client_sizes)
    assert all(v > 0.01 for v in var_diag), f"Expected positive diagonal variance across non-IID clients: {var_diag}"

    # Sample M=20 global models from N(mu, Sigma_diag) plus symmetric antithetic pairs so mean(Omega^{(m)}) == 0
    sampled_models: list[list[float]] = []
    for _ in range(10):
        z = [rng.gauss(0.0, 1.0) for _ in range(3)]
        w_plus = [w_bar[d] + math.sqrt(var_diag[d]) * z[d] for d in range(3)]
        w_minus = [w_bar[d] - math.sqrt(var_diag[d]) * z[d] for d in range(3)]
        sampled_models.append(w_plus)
        sampled_models.append(w_minus)

    # Verify mean perturbation (1/M) sum_m (w^{(m)} - w_bar) == 0, yet ensemble prediction != FedAvg prediction (Eq 9)
    mean_omega = [
        sum(w[d] - w_bar[d] for w in sampled_models) / len(sampled_models)
        for d in range(3)
    ]
    assert max(abs(mo) for mo in mean_omega) < 1e-15

    x_test = [1.2, -1.0]
    p_fedavg = predict_prob(x_test, w_bar)
    p_gauss_ens = sum(predict_prob(x_test, w) for w in sampled_models) / len(sampled_models)
    assert abs(p_gauss_ens - p_fedavg) > 1e-3, "O(Omega^2) curvature term in Eq (9) must separate ensemble from FedAvg"

    # 2. Verify Dirichlet simplex sampling (Eq 7) produces convex combinations of client models
    for _ in range(10):
        gammas = [rng.gammavariate(0.5, 1.0) for _ in range(3)]
        denom = sum(g * sz for g, sz in zip(gammas, client_sizes))
        coeffs = [(g * sz) / denom for g, sz in zip(gammas, client_sizes)]
        assert abs(sum(coeffs) - 1.0) < 1e-15 and all(c >= 0.0 for c in coeffs)

    # 3. Verify Algorithm 1 SWA knowledge distillation matches ensemble pseudo-labels on unlabeled server set U
    unlabeled_U = [[1.0, -0.5], [-0.6, 1.1], [0.7, 0.8], [-0.9, -0.7]]
    all_ensemble_models = [w_bar] + client_weights + sampled_models
    pseudo_targets = [
        sum(predict_prob(xj, wm) for wm in all_ensemble_models) / len(all_ensemble_models)
        for xj in unlabeled_U
    ]

    def kd_kl_loss(w_student: list[float]) -> float:
        loss = 0.0
        for xj, p_hat in zip(unlabeled_U, pseudo_targets):
            q = min(max(predict_prob(xj, w_student), 1e-12), 1.0 - 1e-12)
            loss += -(p_hat * math.log(q) + (1.0 - p_hat) * math.log(1.0 - q))
        return loss / len(unlabeled_U)

    loss_init = kd_kl_loss(w_bar)
    # Run cyclical SWA updates initialized at w_bar
    w_curr = w_bar[:]
    swa_collected: list[list[float]] = []
    eps = 1e-6
    for step in range(1, 61):
        # Cyclical step size between 0.15 and 0.04
        eta_swa = 0.04 + 0.11 * ((step % 10) / 9.0)
        grad = [0.0, 0.0, 0.0]
        base_l = kd_kl_loss(w_curr)
        for d in range(3):
            w_pert = w_curr[:]
            w_pert[d] += eps
            grad[d] = (kd_kl_loss(w_pert) - base_l) / eps
        w_curr = [w_curr[d] - eta_swa * grad[d] for d in range(3)]
        if step >= 20 and step % 10 == 0:
            swa_collected.append(w_curr[:])

    w_swa = [
        sum(ws[d] for ws in swa_collected) / len(swa_collected)
        for d in range(3)
    ]
    loss_swa = kd_kl_loss(w_swa)
    assert loss_swa < loss_init, f"SWA distillation must reduce cross-entropy to ensemble targets: {loss_swa} vs {loss_init}"

    print(
        f"[PASS] FedBE boundary verification passed: |p_ens-p_fedavg|={abs(p_gauss_ens - p_fedavg):.4e}, "
        f"KD_loss_init={loss_init:.5f} -> KD_loss_SWA={loss_swa:.5f}"
    )


if __name__ == "__main__":
    main()
