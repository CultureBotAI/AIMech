#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 721: Edge-Popup (Ramanujan et al., CVPR 2020)."""


def verify_edge_popup() -> None:
    # Verify Theorem 1 & Theorem B.1 (Ramanujan et al., CVPR 2020, Section 3.2 & Appendix B.1):
    # Fixed random weights w_{uv}, positive popup scores s_{uv}, top-k% selection h(s_{uv}) in {0, 1}.
    # Straight-through score update (Eq. 6): s_tilde_{uv} = s_{uv} - alpha * (dL / dI_v) * w_{uv} * Z_u.
    # Whenever a nonzero number of edges E_new replace E_old (|E_new| = |E_old| > 0),
    # the first-order Taylor change in loss sum_{e in E_new} (dL/dI_v) w_e Z_u - sum_{e in E_old} (dL/dI_v) w_e Z_u < 0.
    alpha = 0.1
    dL_dI_rho = -1.2
    Z = [1.0, 0.5, 0.8, 1.2]
    w_rho = [-0.5, 0.2, 0.9, 0.4]  # fixed random weights into node rho
    # Initial popup scores s_{u,rho}; top-50% (2 of 4 edges) initially selects u in {0, 3}
    s = [0.50, 0.40, 0.49, 0.70]

    def top_k_indices(scores: list[float], k_count: int) -> set[int]:
        return set(sorted(range(len(scores)), key=lambda u: scores[u], reverse=True)[:k_count])

    active_before = top_k_indices(s, 2)
    assert active_before == {0, 3}
    I_before = sum(w_rho[u] * Z[u] for u in active_before)

    # Straight-through score update (Eq. 6):
    s_tilde = [s[u] - alpha * dL_dI_rho * w_rho[u] * Z[u] for u in range(len(s))]
    active_after = top_k_indices(s_tilde, 2)
    # Edge 2 (w=0.9, Z=0.8 aligned with -dL/dI_rho > 0) pops up and replaces edge 0 (w=-0.5, Z=1.0)
    assert active_after == {2, 3}
    I_after = sum(w_rho[u] * Z[u] for u in active_after)

    # Verify inequality (Eq. 7-8 & 17-21):
    assert s[2] < s[0] and s_tilde[2] > s_tilde[0]
    first_order_delta_loss = dL_dI_rho * (I_after - I_before)
    assert first_order_delta_loss < 0.0
    print("Edge-Popup verification passed.")


if __name__ == "__main__":
    verify_edge_popup()
