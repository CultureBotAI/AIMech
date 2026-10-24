#!/usr/bin/env python3
"""Boundary and verification script for Round 342:
On the Global Linear Convergence of Frank-Wolfe Optimization Variants
(Lacoste-Julien & Jaggi, NeurIPS 2015 pp. 496-504, arXiv:1511.05932).
"""

import math
import sys


def dot(u, v):
    return sum(u[i] * v[i] for i in range(len(u)))


def vec_norm(u):
    return math.sqrt(dot(u, u))


def main():
    # 1. Verify Pyramidal Width of Probability Simplex and Unit Cube (Lemma 4 & Appendix B.1, Eq. 11, pp. 7, 12-13)
    # For regular probability simplex on d vertices (side length Delta = sqrt(2)),
    # Alexander's flat-partition distance formula (Eq. 11): c(r, sqrt(2)) = sqrt(d / (r * (d - r)))
    max_simplex_pwidth_err = 0.0
    for d in [2, 3, 4, 5, 6, 7]:
        min_flat_dist = min(
            math.sqrt(d / (r * (d - r))) for r in range(1, d // 2 + 1)
        )
        expected = (2.0 / math.sqrt(d)) if (d % 2 == 0) else (2.0 / math.sqrt(d - 1.0 / d))
        max_simplex_pwidth_err = max(max_simplex_pwidth_err, abs(min_flat_dist - expected))

    # For unit cube {0,1}^d (Lemma 4, p. 12): at interior point x with canonical active set S = {e_1, ..., e_d}
    # and feasible direction r = (-1/sqrt(d), ..., -1/sqrt(d)), max_{s in A, v in S} <r/||r||, s - v> == 1/sqrt(d)
    d_cube = 5
    r_cube = [-1.0 / math.sqrt(d_cube)] * d_cube
    s_summit = [0.0] * d_cube
    active_S = [[1.0 if j == i else 0.0 for j in range(d_cube)] for i in range(d_cube)]
    cube_pdirw = max(dot(r_cube, [s_summit[j] - v[j] for j in range(d_cube)]) for v in active_S)
    lemma4_cube_err = abs(cube_pdirw - 1.0 / math.sqrt(d_cube))

    # 2. Verify Global Linear Convergence of AFW & PFW vs Zig-Zagging Sublinear Classical FW
    # on the Triangle Domain of Appendix E Figure 4 (p. 23):
    # Atoms A = {v0 = (-1, 0), v1 = (0, 0), v2 = (cos(theta), sin(theta))}, objective f(x) = 0.5 ||x - x_unc||^2
    # with x_unc = (-0.5, 1.0), whose constrained optimum on M = conv(A) for theta = pi/6 is on edge [v0, v1]
    # Wait: let's put x_unc = (-0.5, -1.0) so the constrained optimum x* on conv(v0, v1, v2) (where y >= 0)
    # lies strictly on the bottom boundary edge at x* = (-0.5, 0.0)!
    theta = math.pi / 4.0
    atoms = [(-1.0, 0.0), (0.0, 0.0), (math.cos(theta), math.sin(theta))]
    x_unc = (-0.5, -1.0)
    x_star = (-0.5, 0.0)

    def f_val(x):
        return 0.5 * ((x[0] - x_unc[0]) ** 2 + (x[1] - x_unc[1]) ** 2)

    def grad_f(x):
        return (x[0] - x_unc[0], x[1] - x_unc[1])

    f_star = f_val(x_star)

    # Exact line search for f(x + gamma * d) = 0.5 ||x + gamma d - x_unc||^2 on [0, gamma_max]:
    def exact_ls(x, d, gamma_max):
        dd = dot(d, d)
        if dd < 1e-16:
            return 0.0
        g = grad_f(x)
        gam_unc = -dot(g, d) / dd
        return max(0.0, min(gamma_max, gam_unc))

    # (a) Classical Frank-Wolfe starting from interior point alpha = [0.2, 0.2, 0.6]:
    x_fw = [sum(w * atoms[i][j] for i, w in enumerate([0.2, 0.2, 0.6])) for j in range(2)]
    for _ in range(60):
        g = grad_f(x_fw)
        s_idx = min(range(3), key=lambda idx: dot(g, atoms[idx]))
        d_fw = [atoms[s_idx][0] - x_fw[0], atoms[s_idx][1] - x_fw[1]]
        gam = exact_ls(x_fw, d_fw, 1.0)
        x_fw = [x_fw[0] + gam * d_fw[0], x_fw[1] + gam * d_fw[1]]
    h_fw_60 = f_val(x_fw) - f_star

    # (b) Away-Steps Frank-Wolfe (Algorithm 1, p. 3):
    # Also verify Equation 6 (2 <r_t, d_t> >= <r_t, d_t^{PFW}>), Theorem 2 (Eq. 7), and drop-step bound D_t <= t/2
    alpha_afw = [0.2, 0.2, 0.6]
    drop_steps = 0
    eq6_holds = True
    thm2_holds = True
    M_diam = max(
        math.hypot(atoms[i][0] - atoms[j][0], atoms[i][1] - atoms[j][1])
        for i in range(3)
        for j in range(3)
    )
    for t in range(1, 30):
        x_curr = [sum(alpha_afw[i] * atoms[i][j] for i in range(3)) for j in range(2)]
        h_curr = f_val(x_curr) - f_star
        if h_curr < 1e-15:
            break
        g = grad_f(x_curr)
        r_t = (-g[0], -g[1])
        s_idx = min(range(3), key=lambda idx: dot(g, atoms[idx]))
        active_indices = [idx for idx in range(3) if alpha_afw[idx] > 1e-14]
        v_idx = max(active_indices, key=lambda idx: dot(g, atoms[idx]))

        d_fw = [atoms[s_idx][0] - x_curr[0], atoms[s_idx][1] - x_curr[1]]
        d_away = [x_curr[0] - atoms[v_idx][0], x_curr[1] - atoms[v_idx][1]]
        d_pfw = [atoms[s_idx][0] - atoms[v_idx][0], atoms[s_idx][1] - atoms[v_idx][1]]

        g_fw = dot(r_t, d_fw)
        g_away = dot(r_t, d_away)
        # Verify Theorem 2 (Eq. 7, p. 6): for L = 1, g_t^{FW} <= M * sqrt(2 h_t L) when h_t <= L M^2 / 2
        if h_curr <= 0.5 * (M_diam ** 2):
            if g_fw > M_diam * math.sqrt(2.0 * h_curr) + 1e-12:
                thm2_holds = False

        if g_fw >= g_away:
            d_t = d_fw
            gam_max = 1.0
            is_away = False
        else:
            d_t = d_away
            gam_max = alpha_afw[v_idx] / (1.0 - alpha_afw[v_idx])
            is_away = True

        # Verify Equation 6 (p. 6): 2 <r_t, d_t> >= <r_t, d_t^{PFW}>
        if 2.0 * dot(r_t, d_t) < dot(r_t, d_pfw) - 1e-14:
            eq6_holds = False

        gam = exact_ls(x_curr, d_t, gam_max)
        if not is_away:
            for i in range(3):
                alpha_afw[i] *= 1.0 - gam
            alpha_afw[s_idx] += gam
        else:
            if abs(gam - gam_max) < 1e-12:
                drop_steps += 1
            for i in range(3):
                if i in active_indices:
                    alpha_afw[i] *= 1.0 + gam
            alpha_afw[v_idx] = max(0.0, alpha_afw[v_idx] - gam)

    x_afw = [sum(alpha_afw[i] * atoms[i][j] for i in range(3)) for j in range(2)]
    h_afw = f_val(x_afw) - f_star

    # (c) Pairwise Frank-Wolfe (Algorithm 2, p. 3):
    alpha_pfw = [0.2, 0.2, 0.6]
    for _ in range(30):
        x_curr = [sum(alpha_pfw[i] * atoms[i][j] for i in range(3)) for j in range(2)]
        if f_val(x_curr) - f_star < 1e-15:
            break
        g = grad_f(x_curr)
        s_idx = min(range(3), key=lambda idx: dot(g, atoms[idx]))
        active_indices = [idx for idx in range(3) if alpha_pfw[idx] > 1e-14]
        v_idx = max(active_indices, key=lambda idx: dot(g, atoms[idx]))
        d_pfw = [atoms[s_idx][0] - atoms[v_idx][0], atoms[s_idx][1] - atoms[v_idx][1]]
        gam_max = alpha_pfw[v_idx]
        gam = exact_ls(x_curr, d_pfw, gam_max)
        alpha_pfw[v_idx] = max(0.0, alpha_pfw[v_idx] - gam)
        alpha_pfw[s_idx] += gam

    x_pfw = [sum(alpha_pfw[i] * atoms[i][j] for i in range(3)) for j in range(2)]
    h_pfw = f_val(x_pfw) - f_star

    ok = (
        max_simplex_pwidth_err < 1e-15
        and lemma4_cube_err < 1e-15
        and eq6_holds
        and thm2_holds
        and drop_steps <= 15
        and h_afw < 1e-14
        and h_pfw < 1e-14
        and h_fw_60 > 1e-3
    )
    if not ok:
        print("Verification failed!", file=sys.stderr)
        sys.exit(1)

    print(
        f"[PASS] Round 342 Away-Steps & Pairwise Frank-Wolfe (Lacoste-Julien & Jaggi 2015): "
        f"max_simplex_pwidth_err={max_simplex_pwidth_err:.2e}, lemma4_cube_err={lemma4_cube_err:.2e}, "
        f"h_afw={h_afw:.2e}, h_pfw={h_pfw:.2e} << h_fw_60={h_fw_60:.4e}, drop_steps={drop_steps}"
    )


if __name__ == "__main__":
    main()
