"""Constructed boundary verification for Round 545: ClippedGossip / Self-Centered Clipping (He, Karimireddy, & Jaggi, 2022)."""

from __future__ import annotations

import math


def clip(vec: list[float], tau: float) -> list[float]:
    norm = math.sqrt(sum(v * v for v in vec))
    if norm <= 1e-12 or norm <= tau:
        return vec[:]
    scale = tau / norm
    return [v * scale for v in vec]


def consensus_variance(states: list[float]) -> float:
    mean = sum(states) / len(states)
    return sum((x - mean) ** 2 for x in states) / len(states)


def trimmed_mean_1d(vals: list[float], b: int) -> float:
    s = sorted(vals)
    kept = s[b : len(s) - b] if len(s) > 2 * b else s
    return sum(kept) / len(kept)


def main() -> None:
    # Part 1: Verify Proposition IV(i) (p. 17): under dissensus attack with eps_i = 1,
    # plain gossip makes zero progress (x_i^{t+1} == x_i^t).
    # Regular node i has x_i = 10.0, regular neighbors k in {1, 2} with x_1 = 20.0, x_2 = 26.0,
    # weights W_i0 = 0.4, W_i1 = 0.25, W_i2 = 0.25, and Byzantine neighbor j=3 with weight W_i3 = 0.10.
    x_i = 10.0
    reg_neighbors = [(0.25, 20.0), (0.25, 26.0)]
    w_byz = 0.10
    w_self = 1.0 - sum(w for w, _ in reg_neighbors) - w_byz
    eps_i = 1.0
    # Dissensus attack (Definition A, Eq. 6, p. 9):
    reg_diff_sum = sum(w * (x_k - x_i) for w, x_k in reg_neighbors)
    x_byz = x_i - eps_i * (reg_diff_sum / w_byz)
    x_i_next_gossip = (
        w_self * x_i
        + sum(w * x_k for w, x_k in reg_neighbors)
        + w_byz * x_byz
    )
    assert abs(x_i_next_gossip - x_i) < 1e-12, f"Expected no progress, got {x_i_next_gossip}"

    # Part 2: Dumbbell topology consensus under dissensus attack (Section 4.1 Theorem I, Fig. 1, 9, p. 4-5, 19)
    # 6 regular nodes: Clique A = {0, 1, 2} initialized at 0.0, Clique B = {3, 4, 5} initialized at 200.0.
    # Bridge edge connects node 2 and node 3. Nodes 2 and 3 each also have 1 Byzantine neighbor with weight delta = 0.08.
    adj_reg = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2, 4, 5],
        4: [3, 5],
        5: [3, 4],
    }
    delta = {0: 0.0, 1: 0.0, 2: 0.08, 3: 0.08, 4: 0.0, 5: 0.0}
    W_reg: dict[tuple[int, int], float] = {}
    for i in range(6):
        deg = len(adj_reg[i])
        w_edge = (1.0 - delta[i]) / (deg + 1)
        W_reg[(i, i)] = w_edge
        for j in adj_reg[i]:
            W_reg[(i, j)] = w_edge

    init_x = [0.0, 0.0, 0.0, 200.0, 200.0, 200.0]
    init_var = consensus_variance(init_x)
    assert abs(init_var - 10000.0) < 1e-9

    x_cg = init_x[:]
    x_tm = init_x[:]

    for _ in range(120):
        # ClippedGossip step (Section 4.1, p. 4 & Eq. 24, p. 28)
        next_cg = []
        for i in range(6):
            # Theoretical clipping radius tau_i (Eq. 24)
            if delta[i] > 0.0:
                reg_sq = sum(
                    W_reg[(i, j)] * ((x_cg[i] - x_cg[j]) ** 2) for j in adj_reg[i]
                )
                tau_i = math.sqrt(reg_sq / delta[i])
                # Dissensus attacker with eps = 1.5
                reg_drift = sum(W_reg[(i, j)] * (x_cg[j] - x_cg[i]) for j in adj_reg[i])
                x_b = x_cg[i] - 1.5 * (reg_drift / delta[i])
                clipped_b = x_cg[i] + clip([x_b - x_cg[i]], tau_i)[0]
            else:
                tau_i = 1e9
                clipped_b = x_cg[i]

            acc = W_reg[(i, i)] * x_cg[i] + delta[i] * clipped_b
            for j in adj_reg[i]:
                clipped_j = x_cg[i] + clip([x_cg[j] - x_cg[i]], tau_i)[0]
                acc += W_reg[(i, j)] * clipped_j
            next_cg.append(acc)
        x_cg = next_cg

        # Coordinate-wise Trimmed Mean (TM, b=1) on dumbbell topology (Section 6.1, p. 8)
        next_tm = []
        for i in range(6):
            vals = [x_tm[i]] + [x_tm[j] for j in adj_reg[i]]
            if delta[i] > 0.0:
                reg_drift = sum(W_reg[(i, j)] * (x_tm[j] - x_tm[i]) for j in adj_reg[i])
                vals.append(x_tm[i] - 1.5 * (reg_drift / delta[i]))
            next_tm.append(trimmed_mean_1d(vals, b=1))
        x_tm = next_tm

    var_cg = consensus_variance(x_cg)
    var_tm = consensus_variance(x_tm)

    assert var_cg < 50.0, f"Expected ClippedGossip consensus error < 50, got {var_cg}"
    assert var_tm > 9000.0, f"Expected TM to fail on dumbbell cut, got {var_tm}"

    print(
        f"[PASS] Round 545 ClippedGossip verified: "
        f"dissensus_gossip_progress=0.0, var_ClippedGossip={var_cg:.2f} << var_TM={var_tm:.2f} (init={init_var:.1f})"
    )


if __name__ == "__main__":
    main()
