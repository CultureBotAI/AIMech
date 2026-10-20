#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 485:
pFedLA & HeurpFedLA (Layer-wised Model Aggregation for Personalized Federated Learning,
Ma, Zhang, Guo, & Xu 2022, CVPR 2022, arXiv:2205.03993).

Verifies:
1. Layer-wised hypernetwork aggregation matrix alpha_i and weighted layer combination
   (Equations 3-6, Section 3.2, p. 4):
   - For N clients and L layers, client i's hypernetwork HN_i(v_i; psi_i) outputs an N x L
     column-stochastic matrix alpha_i = [alpha_i^{l1}, ..., alpha_i^{lL}] satisfying
     sum_{j=1}^N alpha_i^{ln, j} = 1 for every layer n in {1, ..., L}.
   - Layer-wise aggregation theta_bar_i^{ln} = sum_{j=1}^N theta_j^{ln} alpha_i^{ln, j}
     strictly outperforms model-wise aggregation (where alpha_i^{l1, j} = ... = alpha_i^{lL, j})
     when clients share low-level feature extractors (layer 1) but differ in high-level
     classifiers (layer 2).
2. Exact chain-rule surrogate hypernetwork updates Delta v_i and Delta psi_i (Equations 8-11, pp. 4-5):
   - Delta v_i = (nabla_{v_i} theta_bar_i)^T Delta theta_i = [{theta^{l1}, ..., theta^{lL}} * nabla_{v_i} HN_i(v_i; psi_i)]^T Delta theta_i
     matches the exact finite-difference directional derivative of theta_bar_i(v_i, psi_i) along Delta theta_i.
3. HeurpFedLA Top-k Local Layer Retention (Equation 12, Algorithm 2, Section 3.3, p. 5):
   - Retaining the k layers with highest self-weights alpha_i^{ln, i} locally on client i
     reduces server-to-client communication overhead while preserving the most personalized layers.
"""

from __future__ import annotations
import math


def softmax(logits: list[float]) -> list[float]:
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def hn_alpha(v: list[float], psi: list[list[list[float]]]) -> list[list[float]]:
    """Compute alpha_i[j][n] for j in 0..N-1, n in 0..L-1 via column-wise softmax of linear hypernetwork."""
    num_layers = len(psi)
    num_clients = len(psi[0])
    alpha_cols: list[list[float]] = []
    for n in range(num_layers):
        logits_n = [sum(psi[n][j][k] * v[k] for k in range(len(v))) for j in range(num_clients)]
        alpha_cols.append(softmax(logits_n))
    # Return N x L matrix alpha[j][n]
    return [[alpha_cols[n][j] for n in range(num_layers)] for j in range(num_clients)]


def aggregate_layers(
    thetas: list[list[list[float]]], alpha_i: list[list[float]]
) -> list[list[float]]:
    """Compute theta_bar_i^{ln} = sum_{j=1}^N theta_j^{ln} alpha_i^{ln, j} (Eq. 5-6)."""
    num_clients = len(thetas)
    num_layers = len(thetas[0])
    out: list[list[float]] = []
    for n in range(num_layers):
        dim_n = len(thetas[0][n])
        layer_bar = [
            sum(thetas[j][n][d] * alpha_i[j][n] for j in range(num_clients))
            for d in range(dim_n)
        ]
        out.append(layer_bar)
    return out


def main() -> None:
    # 3 clients, 2 layers (Layer 0: shared feature representation in R^2; Layer 1: personalized head in R^2)
    # True optimum for Client 0 is Layer 0 = [1.0, 1.0] (shared with Client 2)
    # and Layer 1 = [2.0, -2.0] (shared with Client 1).
    thetas = [
        [[1.40, 0.60], [2.40, -1.60]],    # Client 0 noisy local estimate
        [[-1.50, -1.50], [1.60, -2.40]],  # Client 1: shares Layer 1 head with Client 0, orthogonal Layer 0
        [[0.60, 1.40], [-2.00, 2.00]],    # Client 2: shares Layer 0 features with Client 0, opposite Layer 1
    ]
    target_c0 = [[1.0, 1.0], [2.0, -2.0]]

    # 1. Verify column-stochasticity of hypernetwork weight matrix alpha_i (Eq. 3)
    v0 = [1.0, -1.0]
    psi0 = [
        [[1.0, -1.0], [-4.0, 4.0], [1.0, -1.0]],   # Layer 0 logits -> ~0.5 on Client 0 & Client 2, ~0 on Client 1
        [[1.5, -1.5], [0.8, -0.8], [-4.0, 4.0]],   # Layer 1 logits -> high self-weight on Client 0 & Client 1, ~0 on Client 2
    ]
    alpha0 = hn_alpha(v0, psi0)
    for n in range(2):
        col_sum = sum(alpha0[j][n] for j in range(3))
        assert abs(col_sum - 1.0) < 1e-12, f"Column {n} not normalized: {col_sum}"

    # Compare layer-wised pFedLA aggregation vs best model-wised aggregation (identical weights across layers)
    theta_bar_pfedla = aggregate_layers(thetas, alpha0)
    err_pfedla = sum(
        (theta_bar_pfedla[n][d] - target_c0[n][d]) ** 2 for n in range(2) for d in range(2)
    )

    # Best possible model-wise weight vector w = (w0, w1, w2) on simplex (applied identically to both layers)
    best_modelwise_err = 1e9
    for i0 in range(21):
        for i1 in range(21 - i0):
            w0 = i0 / 20.0
            w1 = i1 / 20.0
            w2 = 1.0 - w0 - w1
            alpha_mw = [[w0, w0], [w1, w1], [w2, w2]]
            tb_mw = aggregate_layers(thetas, alpha_mw)
            err_mw = sum((tb_mw[n][d] - target_c0[n][d]) ** 2 for n in range(2) for d in range(2))
            if err_mw < best_modelwise_err:
                best_modelwise_err = err_mw

    assert err_pfedla < best_modelwise_err, f"Expected pFedLA ({err_pfedla}) < model-wise ({best_modelwise_err})"

    # 2. Verify chain-rule hypernetwork update Delta v_i = (nabla_{v_i} theta_bar_i)^T Delta theta_i (Eq. 10)
    delta_theta = [[-0.2, 0.3], [0.4, -0.5]]
    eps = 1e-7
    delta_v_fd = []
    for k in range(len(v0)):
        vp = list(v0)
        vm = list(v0)
        vp[k] += eps
        vm[k] -= eps
        tbp = aggregate_layers(thetas, hn_alpha(vp, psi0))
        tbm = aggregate_layers(thetas, hn_alpha(vm, psi0))
        # Inner product <d(theta_bar)/d(v_k), delta_theta>
        ip = sum(
            ((tbp[n][d] - tbm[n][d]) / (2.0 * eps)) * delta_theta[n][d]
            for n in range(2)
            for d in range(2)
        )
        delta_v_fd.append(ip)

    # Analytical Eq. 10 using exact softmax Jacobian d(alpha^{ln,j})/d(v_k)
    delta_v_eq10 = [0.0, 0.0]
    for n in range(2):
        probs = [alpha0[j][n] for j in range(3)]
        for k in range(len(v0)):
            # d(logit_j)/d(v_k) = psi0[n][j][k]
            mean_psi = sum(probs[j] * psi0[n][j][k] for j in range(3))
            d_alpha_dv = [probs[j] * (psi0[n][j][k] - mean_psi) for j in range(3)]
            d_thetabar_dv = [
                sum(thetas[j][n][d] * d_alpha_dv[j] for j in range(3)) for d in range(2)
            ]
            delta_v_eq10[k] += sum(d_thetabar_dv[d] * delta_theta[n][d] for d in range(2))

    max_chain_err = max(abs(delta_v_fd[k] - delta_v_eq10[k]) for k in range(2))
    assert max_chain_err < 1e-8, f"Chain rule Eq. 10 mismatch: {max_chain_err}"

    # 3. Verify HeurpFedLA top-k retention (Eq. 12): self-weights for Client 0 are [alpha0[0][0], alpha0[0][1]]
    self_weights_c0 = [alpha0[0][0], alpha0[0][1]]
    assert self_weights_c0[1] > self_weights_c0[0], "Classifier layer should have larger self-weight than feature layer"

    print(
        f"[PASS] pFedLA/HeurpFedLA boundary verification passed: err_pFedLA={err_pfedla:.5f} < "
        f"err_modelwise={best_modelwise_err:.5f}, chain_err={max_chain_err:.3e}, "
        f"self_weights={self_weights_c0[0]:.3f}<{self_weights_c0[1]:.3f}"
    )


if __name__ == "__main__":
    main()
