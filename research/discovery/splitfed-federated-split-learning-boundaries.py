#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 503: SplitFed / SFLv1 & SFLv2 (Thapa et al., AAAI 2022 / arXiv:2004.12088)."""

import math


def total_costs(
    K: int,
    p: float,
    q: float,
    W_size: float,
    beta: float,
    R: float,
    T: float,
    T_fedavg: float,
) -> dict[str, tuple[float, float]]:
    """Compute (total_communication, total_training_time) per global epoch (Table 2, p. 6)."""
    comm_fl = 2.0 * K * W_size
    time_fl = T + 2.0 * (W_size / R) + T_fedavg

    comm_sl = 2.0 * p * q + 2.0 * beta * K * W_size
    time_sl = T + 2.0 * (p * q / R) + 2.0 * beta * (W_size / R) * K

    comm_sflv1 = 2.0 * p * q + 2.0 * beta * K * W_size
    time_sflv1 = T + 2.0 * (p * q / (K * R)) + 2.0 * (beta * W_size / R) + T_fedavg

    comm_sflv2 = 2.0 * p * q + 2.0 * beta * K * W_size
    time_sflv2 = T + 2.0 * (p * q / (K * R)) + 2.0 * (beta * W_size / R) + 0.5 * T_fedavg

    return {
        "FL": (comm_fl, time_fl),
        "SL": (comm_sl, time_sl),
        "SFLV1": (comm_sflv1, time_sflv1),
        "SFLV2": (comm_sflv2, time_sflv2),
    }


def clip_gradient_l2(g: list[float], c_prime: float) -> list[float]:
    """Per-sample l2 norm clipping (Eq. 2, p. 5): g_bar = g / max(1, ||g||_2 / C')."""
    norm = math.sqrt(sum(x * x for x in g))
    scale = max(1.0, norm / c_prime)
    return [x / scale for x in g]


def main() -> None:
    # 1. Verify Table 2 cost identities and strict training-time ordering SFLV2 < SFLV1 < SL for K > 1 (Section 3.3, p. 6)
    costs = total_costs(K=20, p=10000.0, q=64.0, W_size=1.0e7, beta=0.1, R=1.0e7, T=2.0, T_fedavg=0.2)
    comm_fl, _ = costs["FL"]
    comm_sl, time_sl = costs["SL"]
    comm_sflv1, time_sflv1 = costs["SFLV1"]
    comm_sflv2, time_sflv2 = costs["SFLV2"]

    assert math.isclose(comm_sl, comm_sflv1, rel_tol=1e-12)
    assert math.isclose(comm_sflv1, comm_sflv2, rel_tol=1e-12)
    # When cut-layer activation traffic 2pq is small and client-side model fraction beta=0.1 << 1, SFL communication < FL communication
    assert comm_sflv1 < comm_fl
    # Training time ordering: SFLV2 < SFLV1 < SL
    assert time_sflv2 < time_sflv1 < time_sl

    # 2. Verify client-side per-sample gradient clipping (Eq. 2, p. 5)
    g_small = [0.3, 0.4]  # norm = 0.5 <= C' = 1.0 -> preserved
    g_large = [3.0, 4.0]  # norm = 5.0 > C' = 1.0 -> scaled to norm 1.0
    g_small_clipped = clip_gradient_l2(g_small, c_prime=1.0)
    g_large_clipped = clip_gradient_l2(g_large, c_prime=1.0)
    assert math.isclose(math.sqrt(sum(x * x for x in g_small_clipped)), 0.5, abs_tol=1e-12)
    assert math.isclose(math.sqrt(sum(x * x for x in g_large_clipped)), 1.0, abs_tol=1e-12)

    # 3. Verify equivalence of SFLV1 parallel split forward-backward + FedAvg with full-model FedAvg on 1-epoch linear split network
    # Full model y_hat = w_S * (w_C * x). On client k with sample (x_k, y_k) and loss 0.5*(w_S*w_C*x_k - y_k)^2:
    # Forward: smashed data A_k = w_C * x_k.
    # Server backward: dL/dw_S = (w_S * A_k - y_k) * A_k, smashed gradient dA_k = (w_S * A_k - y_k) * w_S.
    # Client backward: dL/dw_C = dA_k * x_k.
    w_C0, w_S0 = 1.2, -0.8
    eta = 0.05
    clients_data = [(1.0, 2.0), (2.0, -1.0), (-1.5, 0.5)]

    # SFLV1 update:
    grad_wS_list = []
    wC_updated_list = []
    for x_k, y_k in clients_data:
        a_k = w_C0 * x_k
        y_hat = w_S0 * a_k
        err = y_hat - y_k
        grad_wS_list.append(err * a_k)
        dA_k = err * w_S0
        grad_wC_k = dA_k * x_k
        wC_updated_list.append(w_C0 - eta * grad_wC_k)

    w_S_sflv1 = w_S0 - eta * (sum(grad_wS_list) / len(clients_data))
    w_C_sflv1 = sum(wC_updated_list) / len(clients_data)

    # Full-model 1-step FedAvg update:
    wC_fl = sum(
        w_C0 - eta * (((w_S0 * w_C0 * x_k) - y_k) * w_S0 * x_k) for x_k, y_k in clients_data
    ) / len(clients_data)
    wS_fl = sum(
        w_S0 - eta * (((w_S0 * w_C0 * x_k) - y_k) * (w_C0 * x_k)) for x_k, y_k in clients_data
    ) / len(clients_data)

    assert math.isclose(w_C_sflv1, wC_fl, abs_tol=1e-12)
    assert math.isclose(w_S_sflv1, wS_fl, abs_tol=1e-12)

    print(
        f"[PASS] Round 503 SplitFed (Thapa et al., AAAI 2022): "
        f"time_SFLV2={time_sflv2:.3f} < time_SFLV1={time_sflv1:.3f} < time_SL={time_sl:.3f}, "
        f"comm_SFL={comm_sflv1:.2e} < comm_FL={comm_fl:.2e}, "
        f"split-FedAvg exact match=(w_C={w_C_sflv1:.6f}, w_S={w_S_sflv1:.6f})"
    )


if __name__ == "__main__":
    main()
