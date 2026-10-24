"""Constructed boundary verification for Round 546: BRIDGE (Fang, Yang, & Bajwa, IEEE TSIPN 2022)."""

from __future__ import annotations

import math


def dist2(a: list[float], b: list[float]) -> float:
    return math.sqrt(sum((a[k] - b[k]) ** 2 for k in range(len(a))))


def screen_bridge_t(self_w: list[float], neighbor_ws: list[list[float]], b: int) -> list[float]:
    # Equations (7)-(10), p. 7: filter b largest and b smallest in each coordinate of N_j,
    # then average remaining |N_j| - 2b values together with self_w (denominator |N_j| - 2b + 1).
    d = len(self_w)
    m = len(neighbor_ws)
    assert m >= 2 * b + 1
    out = []
    for k in range(d):
        coord_vals = sorted(w[k] for w in neighbor_ws)
        surviving = coord_vals[b : m - b]
        out.append((sum(surviving) + self_w[k]) / (m - 2 * b + 1))
    return out


def screen_bridge_m(self_w: list[float], neighbor_ws: list[list[float]]) -> list[float]:
    # Equation (11), p. 7: coordinate-wise median of N_j U {j}
    d = len(self_w)
    all_ws = neighbor_ws + [self_w]
    m = len(all_ws)
    out = []
    for k in range(d):
        s = sorted(w[k] for w in all_ws)
        if m % 2 == 1:
            out.append(s[m // 2])
        else:
            out.append(0.5 * (s[m // 2 - 1] + s[m // 2]))
    return out


def screen_bridge_k(self_w: list[float], neighbor_ws: list[list[float]], b: int) -> list[float]:
    # Equation (12), p. 7: decentralized Krum over i in N_j with distances to |N_j| - b - 2 closest in N_j U {j}
    m = len(neighbor_ws)
    assert m >= b + 3
    all_ws = neighbor_ws + [self_w]
    best_score = float("inf")
    best_idx = 0
    keep = m - b - 2
    for i, w_i in enumerate(neighbor_ws):
        dists = sorted(
            dist2(w_h, w_i) for h, w_h in enumerate(all_ws) if h != i
        )
        score = sum(dists[:keep])
        if score < best_score:
            best_score = score
            best_idx = i
    return neighbor_ws[best_idx][:]


def main() -> None:
    # Part 1: Verify exact nonfaulty convex-combination representation Y(t) for BRIDGE-T (Eq. 14-15, p. 8)
    # Suppose node j has 4 regular neighbors with scalar values [1.0, 2.0, 4.0, 5.0], self value 3.0,
    # and b = 1 Byzantine neighbor sending 3.5 (which survives inside [2.0, 4.0]).
    # Filtered set C_j^k has [2.0, 3.5, 4.0], N_underline has [1.0], N_overline has [5.0].
    # Since 3.5 = 0.25 * 1.0 + 0.75 * 4.0 (or between min trimmed 1.0 and max trimmed 5.0: 3.5 = (3/8)*1.0 + (5/8)*5.0),
    # the screened output (2.0 + 3.5 + 4.0 + 3.0) / 4 = 3.125 is a strict convex combination of regular values!
    y_val = screen_bridge_t([3.0], [[1.0], [2.0], [4.0], [5.0], [3.5]], b=1)[0]
    assert abs(y_val - 3.125) < 1e-12
    assert 1.0 <= y_val <= 5.0

    # Part 2: Decentralized strongly convex optimization in d = 4 dimensions across r = 6 regular nodes
    # and b = 1 Byzantine node (M = 7 total, fully connected so |N_j| = 6 >= 2b + 1 = 3 and >= b + 3 = 4).
    d = 4
    r = 6
    b = 1
    w_star = [1.5, -1.0, 0.5, -0.5]
    # Local empirical risks f_j(w) = 0.5 * ||w - (w_star + noise_j)||^2 under i.i.d. finite samples (Theorem 2, p. 10)
    biases = [
        [0.02, -0.01, 0.01, -0.02],
        [-0.02, 0.01, -0.01, 0.02],
        [0.01, 0.02, -0.02, 0.01],
        [-0.01, -0.02, 0.02, -0.01],
        [0.015, -0.015, 0.005, -0.005],
        [-0.015, 0.015, -0.005, 0.005],
    ]

    w_dgd = [[0.0] * d for _ in range(r)]
    w_bt = [[0.0] * d for _ in range(r)]
    w_bm = [[0.0] * d for _ in range(r)]
    w_bk = [[0.0] * d for _ in range(r)]

    byz_msg = [50.0, -50.0, 50.0, -50.0]

    for t in range(150):
        rho = 0.25 / (1.0 + 0.05 * t)

        # DGD update (Eq. 6, p. 6)
        next_dgd = []
        for j in range(r):
            nbrs = [w_dgd[i] for i in range(r) if i != j] + [byz_msg]
            avg = [(w_dgd[j][k] + sum(nb[k] for nb in nbrs)) / (r + b) for k in range(d)]
            grad = [w_dgd[j][k] - (w_star[k] + biases[j][k]) for k in range(d)]
            next_dgd.append([avg[k] - rho * grad[k] for k in range(d)])
        w_dgd = next_dgd

        # BRIDGE-T update (Algorithm 1 + Eq. 10)
        next_bt = []
        for j in range(r):
            nbrs = [w_bt[i] for i in range(r) if i != j] + [byz_msg]
            y_j = screen_bridge_t(w_bt[j], nbrs, b=b)
            grad = [w_bt[j][k] - (w_star[k] + biases[j][k]) for k in range(d)]
            next_bt.append([y_j[k] - rho * grad[k] for k in range(d)])
        w_bt = next_bt

        # BRIDGE-M update (Algorithm 1 + Eq. 11)
        next_bm = []
        for j in range(r):
            nbrs = [w_bm[i] for i in range(r) if i != j] + [byz_msg]
            y_j = screen_bridge_m(w_bm[j], nbrs)
            grad = [w_bm[j][k] - (w_star[k] + biases[j][k]) for k in range(d)]
            next_bm.append([y_j[k] - rho * grad[k] for k in range(d)])
        w_bm = next_bm

        # BRIDGE-K update (Algorithm 1 + Eq. 12)
        next_bk = []
        for j in range(r):
            nbrs = [w_bk[i] for i in range(r) if i != j] + [byz_msg]
            y_j = screen_bridge_k(w_bk[j], nbrs, b=b)
            grad = [w_bk[j][k] - (w_star[k] + biases[j][k]) for k in range(d)]
            next_bk.append([y_j[k] - rho * grad[k] for k in range(d)])
        w_bk = next_bk

    err_dgd = max(dist2(w_dgd[j], w_star) for j in range(r))
    err_bt = max(dist2(w_bt[j], w_star) for j in range(r))
    err_bm = max(dist2(w_bm[j], w_star) for j in range(r))
    err_bk = max(dist2(w_bk[j], w_star) for j in range(r))
    consensus_bt = max(dist2(w_bt[j], w_bt[0]) for j in range(r))

    assert err_bt < 0.02, f"BRIDGE-T failed to converge: {err_bt}"
    assert err_bm < 0.03, f"BRIDGE-M failed to converge: {err_bm}"
    assert err_bk < 0.08, f"BRIDGE-K failed to converge: {err_bk}"
    assert consensus_bt < 0.01, f"BRIDGE-T failed to reach consensus: {consensus_bt}"
    assert err_dgd > 5.0, f"Expected DGD to fail under Byzantine attack: {err_dgd}"

    print(
        f"[PASS] Round 546 BRIDGE verified: "
        f"err_BRIDGE_T={err_bt:.4f}, err_BRIDGE_M={err_bm:.4f}, err_BRIDGE_K={err_bk:.4f} << err_DGD={err_dgd:.2f}"
    )


if __name__ == "__main__":
    main()
