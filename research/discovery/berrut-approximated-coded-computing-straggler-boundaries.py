"""Constructed boundary verification for Round 547: Berrut Approximated Coded Computing (Jahani-Nezhad & Maddah-Ali, IEEE TPAMI 2023)."""

from __future__ import annotations

import math


def berrut_eval(z: float, nodes: list[float], values: list[float]) -> float:
    # Equations (12), (18), (21): r_Berrut(z) = sum_{i=0}^n ((-1)^i / (z - x_i)) f_i / sum_{j=0}^n ((-1)^j / (z - x_j))
    for i, x_i in enumerate(nodes):
        if abs(z - x_i) < 1e-14:
            return values[i]
    num = 0.0
    den = 0.0
    for i, x_i in enumerate(nodes):
        w = (-1.0 if (i % 2 == 1) else 1.0) / (z - x_i)
        num += w * values[i]
        den += w
    return num / den


def lebesgue_constant_bound(N: int, s: int) -> float:
    # Theorem 7 (p. 7): Lambda_n <= ((s+1)(s+3)*pi^2 / 4 + 1) * (1 + pi^2 * (s+1) * ln(N - s))
    r_const = (s + 1) * (s + 3) * (math.pi ** 2) / 4.0
    return (r_const + 1.0) * (1.0 + (math.pi ** 2) * (s + 1) * math.log(N - s))


def run_bacc(inputs: list[float], N: int, straggler_indices: set[int], use_chebyshev: bool = True) -> list[float]:
    K = len(inputs)
    if use_chebyshev:
        # Step 1 (Eq. 19, p. 6): Chebyshev points of the first kind
        alphas = [math.cos((2 * j + 1) * math.pi / (2 * K)) for j in range(K)]
        # Step 2 (Eq. 20, p. 6): Chebyshev points of the second kind
        zs = [math.cos(i * math.pi / N) for i in range(N + 1)]
    else:
        alphas = [-1.0 + 2.0 * j / (K - 1) for j in range(K)]
        zs = [-1.0 + 2.0 * i / N for i in range(N + 1)]

    # Verify exact encoding property u(alpha_j) == X_j
    for j, a_j in enumerate(alphas):
        assert abs(berrut_eval(a_j, alphas, inputs) - inputs[j]) < 1e-12

    # Non-polynomial target function f(x) = x * sin(x) (Section V Case 2, p. 9)
    surviving_z = []
    surviving_y = []
    for i in range(N + 1):
        if i not in straggler_indices:
            x_hat = berrut_eval(zs[i], alphas, inputs)
            y_hat = x_hat * math.sin(x_hat)
            surviving_z.append(zs[i])
            surviving_y.append(y_hat)

    # Step 3 (Eq. 21, p. 7): Decode at alpha_j using Berrut's rational interpolant over surviving workers
    return [berrut_eval(a_j, surviving_z, surviving_y) for a_j in alphas]


def rel_error(approx: list[float], truth: list[float]) -> float:
    num = math.sqrt(sum((a - t) ** 2 for a, t in zip(approx, truth)))
    den = math.sqrt(sum(t * t for t in truth))
    return num / den


def main() -> None:
    K = 10
    N = 60
    inputs = [-2.5 + 0.5 * j for j in range(K)]
    truth = [x * math.sin(x) for x in inputs]

    # 1. Verify graceful degradation with straggler count s (Theorem 9, Remark 16, p. 8)
    stragglers_2 = {10, 35}
    stragglers_6 = {5, 10, 20, 35, 45, 55}
    stragglers_12 = {3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55}

    err_s2 = rel_error(run_bacc(inputs, N, stragglers_2, use_chebyshev=True), truth)
    err_s6 = rel_error(run_bacc(inputs, N, stragglers_6, use_chebyshev=True), truth)
    err_s12 = rel_error(run_bacc(inputs, N, stragglers_12, use_chebyshev=True), truth)

    assert err_s2 < err_s6 < err_s12 < 0.08, (
        f"Expected monotone accuracy with fewer stragglers: s2={err_s2}, s6={err_s6}, s12={err_s12}"
    )

    # 2. Verify Theorem 7 empirical Lebesgue constant vs theoretical logarithmic bound (p. 7)
    surviving_nodes = [math.cos(i * math.pi / N) for i in range(N + 1) if i not in stragglers_2]
    test_grid = [-0.999 + 0.002 * m for m in range(1000)]
    emp_lebesgue = 0.0
    for x in test_grid:
        if any(abs(x - z) < 1e-12 for z in surviving_nodes):
            continue
        weights = [((-1.0 if idx % 2 else 1.0) / (x - z)) for idx, z in enumerate(surviving_nodes)]
        den = abs(sum(weights))
        leb_x = sum(abs(w) for w in weights) / den
        if leb_x > emp_lebesgue:
            emp_lebesgue = leb_x

    theo_bound = lebesgue_constant_bound(N, len(stragglers_2))
    assert emp_lebesgue <= theo_bound

    print(
        f"[PASS] Round 547 BACC verified: "
        f"rel_err(s=2)={err_s2:.4f} < rel_err(s=6)={err_s6:.4f} < rel_err(s=12)={err_s12:.4f}, "
        f"emp_Lebesgue={emp_lebesgue:.2f} <= theo_bound={theo_bound:.1f}"
    )


if __name__ == "__main__":
    main()
