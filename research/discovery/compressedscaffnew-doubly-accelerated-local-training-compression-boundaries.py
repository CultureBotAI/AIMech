#!/usr/bin/env python3
"""Constructed boundary verification for Round 576: CompressedScaffnew (Condat, Agarsky, Richtarik, 2022/2026)."""

from __future__ import annotations

import random


def make_template_mask(d: int, n: int, s: int) -> list[list[int]]:
    """Construct the d x n binary template pattern with exactly s ones per row (Figure 1, Section 2)."""
    mask = [[0] * n for _ in range(d)]
    if d >= n / s:
        for k in range(d):
            for offset in range(s):
                col = (s * k + offset) % n
                mask[k][col] = 1
    else:
        for col in range(d * s):
            row = col % d
            mask[row][col] = 1
    return mask


def sample_mask(
    template: list[list[int]], rng: random.Random
) -> list[list[int]]:
    """Randomly permute columns of the template mask so each row has s ones."""
    d = len(template)
    n = len(template[0])
    perm = list(range(n))
    rng.shuffle(perm)
    return [[template[k][perm[i]] for i in range(n)] for k in range(d)]


def main() -> None:
    rng = random.Random(576)
    n, d, s = 8, 6, 2
    mu = 0.5
    L = 4.0
    # Construct n heterogeneous quadratic functions f_i(x) = 0.5 x^T A_i x - b_i^T x
    a_diags = []
    b_vecs = []
    for i in range(n):
        diag = [
            mu + (L - mu) * ((k + i) % d) / (d - 1)
            for k in range(d)
        ]
        a_diags.append(diag)
        b_vecs.append([rng.gauss(0.0, 2.0) for _ in range(d)])

    avg_diag = [sum(a_diags[i][k] for i in range(n)) / n for k in range(d)]
    avg_b = [sum(b_vecs[i][k] for i in range(n)) / n for k in range(d)]
    x_star = [avg_b[k] / avg_diag[k] for k in range(d)]

    def grad_i(i: int, x: list[float]) -> list[float]:
        return [a_diags[i][k] * x[k] - b_vecs[i][k] for k in range(d)]

    h_star = [grad_i(i, x_star) for i in range(n)]

    # Verify template mask properties (Figure 1): every row sums to s, column sums in {floor(sd/n), ceil(sd/n)}
    template = make_template_mask(d, n, s)
    for k in range(d):
        assert sum(template[k]) == s
    col_sums = [sum(template[k][i] for k in range(d)) for i in range(n)]
    assert min(col_sums) >= (s * d) // n and max(col_sums) <= (s * d + n - 1) // n

    # Theorem 1 parameters
    gamma = 2.0 / (L + mu)
    eta = (n * (s - 1)) / (s * (n - 1))
    assert 0.5 < eta <= 1.0
    p = 0.4
    rho = max(
        (1.0 - gamma * mu) ** 2,
        (gamma * L - 1.0) ** 2,
        1.0 - (p * p * eta * (s - 1)) / (n - 1),
    )
    assert 0.0 < rho < 1.0

    # Run CompressedScaffnew (Algorithm 1)
    x_clients = [[0.0] * d for _ in range(n)]
    h_clients = [[0.0] * d for _ in range(n)]

    def lyapunov(
        xs: list[list[float]], hs: list[list[float]]
    ) -> float:
        term_x = sum(
            sum((xs[i][k] - x_star[k]) ** 2 for k in range(d))
            for i in range(n)
        ) / gamma
        term_h = (
            (gamma / (p * p * eta))
            * ((n - 1) / (s - 1))
            * sum(
                sum((hs[i][k] - h_star[i][k]) ** 2 for k in range(d))
                for i in range(n)
            )
        )
        return term_x + term_h

    psi_0 = lyapunov(x_clients, h_clients)
    steps = 2500
    for _ in range(steps):
        x_hat = [
            [
                x_clients[i][k] - gamma * grad_i(i, x_clients[i])[k] + gamma * h_clients[i][k]
                for k in range(d)
            ]
            for i in range(n)
        ]
        if rng.random() < p:
            qt = sample_mask(template, rng)
            # Server aggregates compressed vectors: x_bar^t = (1/s) sum_{j=1}^n C_j^t(x_hat_j^t)
            x_bar = [
                sum(qt[k][j] * x_hat[j][k] for j in range(n)) / s
                for k in range(d)
            ]
            for i in range(n):
                x_clients[i] = list(x_bar)
                for k in range(d):
                    if qt[k][i] == 1:
                        h_clients[i][k] += (p * eta / gamma) * (
                            x_bar[k] - x_hat[i][k]
                        )
            # Verify control variates always sum to zero across clients for every coordinate
            for k in range(d):
                assert abs(sum(h_clients[i][k] for i in range(n))) < 1e-11
        else:
            x_clients = x_hat

    psi_T = lyapunov(x_clients, h_clients)
    assert psi_T < 1e-16 * psi_0 and psi_T <= (rho**steps) * psi_0, (
        f"CompressedScaffnew failed to contract Psi^t: {psi_0} -> {psi_T}"
    )

    print(
        f"[PASS] Round 576 CompressedScaffnew verified: eta={eta:.4f}, rho={rho:.4f}, "
        f"psi_0={psi_0:.3e} -> psi_T={psi_T:.3e}"
    )


if __name__ == "__main__":
    main()
