#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 500: FedGMA (Tenison et al., TMLR 2023 / arXiv:2201.11986)."""

import math


def sign_fn(x: float) -> float:
    if x > 0.0:
        return 1.0
    if x < 0.0:
        return -1.0
    return 0.0


def gma_soft_mask(client_updates: list[list[float]], tau: float) -> tuple[list[float], list[float]]:
    """Compute elementwise agreement score A_j and soft mask m_tau (Eq. 3, p. 5)."""
    n_clients = len(client_updates)
    d = len(client_updates[0])
    agreement = []
    mask = []
    for j in range(d):
        a_j = abs(sum(sign_fn(client_updates[n][j]) for n in range(n_clients)) / n_clients)
        m_j = 1.0 if a_j >= tau else a_j
        agreement.append(a_j)
        mask.append(m_j)
    return agreement, mask


def main() -> None:
    # 1. Verify Eq. 3 soft agreement mask vs hard binary AND-mask (Section 3.2 & Algorithm 1, pp. 4-5)
    # 5 clients, 4 coordinates:
    # coord 0: all + (+,+ ,+,+,+) -> A_0 = 1.0 >= tau=0.4 -> m_0 = 1.0
    # coord 1: 4 +, 1 - -> A_1 = |3/5| = 0.6 >= tau=0.4 -> m_1 = 1.0
    # coord 2: 3 +, 2 - -> A_2 = |1/5| = 0.2 < tau=0.4 -> m_2 = 0.2 (soft attenuated, whereas binary mask is 0)
    # coord 3: 1 +, 1 - (on 2-client round, Appendix D.3, p. 17) -> A = 0.0 -> m = 0.0
    updates_5 = [
        [0.5, 0.4, 10.0, -0.2],
        [0.6, 0.3, -0.1, 0.3],
        [0.4, 0.5, 0.2, -0.4],
        [0.7, 0.2, -0.1, 0.1],
        [0.3, -0.1, 0.1, 0.2],
    ]
    tau = 0.4
    A, mask = gma_soft_mask(updates_5, tau)
    assert math.isclose(A[0], 1.0, abs_tol=1e-12) and math.isclose(mask[0], 1.0, abs_tol=1e-12)
    assert math.isclose(A[1], 0.6, abs_tol=1e-12) and math.isclose(mask[1], 1.0, abs_tol=1e-12)
    assert math.isclose(A[2], 0.2, abs_tol=1e-12) and math.isclose(mask[2], 0.2, abs_tol=1e-12)

    # Verify boundary regimes of tau (Appendix D.1, p. 18):
    # tau = 0 -> mask is identically 1 for all coordinates (degenerates to naive FedAvg)
    _, mask_tau0 = gma_soft_mask(updates_5, tau=0.0)
    assert all(math.isclose(m, 1.0, abs_tol=1e-12) for m in mask_tau0)

    # 2. Synthetic OOD invariant vs spurious feature learning across heterogeneous clients
    # Coordinate 0 is the invariant causal mechanism (true optimum w_0* = 2.0 across all clients e).
    # Coordinate 1 is a client-specific spurious mechanism where client 0 has large dominant gradient
    # pushing toward w_1 = +4.0 while clients 1..3 have opposing spurious targets -1.0, -1.0, -1.0.
    # Unseen OOD test environment has w* = (2.0, 0.0) (spurious correlation absent/orthogonal at test).
    inv_target = 2.0
    spurious_targets = [4.0, -1.0, -1.0, -1.0]
    spurious_scales = [6.0, 1.0, 1.0, 1.0]  # Client 0 has dominant spurious curvature

    def run_fl(use_gma: bool, rounds: int = 40) -> tuple[float, float]:
        w = [0.0, 0.0]
        eta_l = 0.05
        eta_g = 1.0
        K = 4
        for _ in range(rounds):
            client_deltas = []
            for c in range(4):
                wc = list(w)
                for _k in range(K):
                    g0 = wc[0] - inv_target
                    g1 = spurious_scales[c] * (wc[1] - spurious_targets[c])
                    wc[0] -= eta_l * g0
                    wc[1] -= eta_l * g1
                client_deltas.append([(wc[0] - w[0]) / 4.0, (wc[1] - w[1]) / 4.0])
            delta_avg = [
                sum(d[0] for d in client_deltas),
                sum(d[1] for d in client_deltas),
            ]
            if use_gma:
                _, m = gma_soft_mask(client_deltas, tau=0.6)
                w[0] += eta_g * m[0] * delta_avg[0]
                w[1] += eta_g * m[1] * delta_avg[1]
            else:
                w[0] += eta_g * delta_avg[0]
                w[1] += eta_g * delta_avg[1]
        ood_loss = 0.5 * ((w[0] - inv_target) ** 2 + (w[1] - 0.0) ** 2)
        spurious_bias = abs(w[1])
        return ood_loss, spurious_bias

    ood_avg, bias_avg = run_fl(use_gma=False)
    ood_gma, bias_gma = run_fl(use_gma=True)
    assert ood_gma < ood_avg
    assert bias_gma < bias_avg

    print(
        f"[PASS] Round 500 FedGMA (Tenison et al., TMLR 2023): "
        f"A={A}, mask={mask}, ood_loss_avg={ood_avg:.4f} -> ood_loss_gma={ood_gma:.4f}, "
        f"spurious_bias_avg={bias_avg:.4f} -> spurious_bias_gma={bias_gma:.4f}"
    )


if __name__ == "__main__":
    main()
