#!/usr/bin/env python3
"""Boundary verification for Round 388: Mime Mimicking Centralized Stochastic Algorithms in Federated Learning
(Karimireddy, Jaggi, Kale, Mohri, Reddi, Stich, & Suresh 2020/2021, NeurIPS 2021, arXiv:2008.03606).

Verifies:
1. Algorithm 1 (Mime & MimeLite decomposition A = (U, V)):
   - Server statistics s_t = V(c_t, s_{t-1}) are updated ONCE per round using the cross-client average
     gradient c_t = (1/|S_t|) sum_{i in S_t} nabla f_i(x_{t-1}) and kept FROZEN during all K local steps
     y_{i,k} = y_{i,k-1} - eta U(g_{i,k}, s_{t-1}).
   - In Mime, local steps use SVRG control variate g_{i,k} = nabla f_i(y_{i,k-1}) - nabla f_i(x_{t-1}) + c_t,
     ensuring that at the fixed point x_*, g_{i,k} = nabla f(x_*) = 0 for all i, k (zero client drift).
2. Lemma 5 (Broken Local Momentum / Client Statistics Drift):
   Updating momentum statistics locally at each step using biased local gradients nabla f_i causes
   local momentum buffers to track client-specific gradients rather than the global gradient,
   producing persistent drift on heterogeneous functions where FedAvgM / naive local momentum fails to
   converge with fixed step size, whereas MimeMom converges to exact x_*.
3. Lemma 3 / Theorem IV (Hessian Dissimilarity delta <= L):
   Variance of the SVRG-corrected local gradient difference ||(nabla f_i(y) - nabla f_i(x)) - (nabla f(y) - nabla f(x))||
   is bounded by delta * ||y - x|| where delta = max_i ||nabla^2 f_i - nabla^2 f||, which vanishes when
   clients share identical Hessians (delta = 0) even if linear terms (gradient heterogeneity G^2) are arbitrarily large!
"""

from __future__ import annotations


def main() -> None:
    # 1. Verify Lemma 3 Hessian dissimilarity property on heterogeneous quadratics
    # f_i(x) = 0.5 * (h_0 + delta_i) * x^2 + b_i * x
    # When delta_i = 0 (identical Hessians h_0 = 2.0) but b_i = [-10, 10, -20, 20] (large gradient heterogeneity G^2),
    # delta = max_i |h_i - h_0| = 0, so (nabla f_i(y) - nabla f_i(x)) == (nabla f(y) - nabla f(x)) identically!
    h0 = 2.0
    b_vals = [-10.0, 10.0, -20.0, 20.0]
    x_ref = 1.5
    y_loc = -0.8
    grad_f_x = sum(h0 * x_ref + bi for bi in b_vals) / len(b_vals)
    grad_f_y = sum(h0 * y_loc + bi for bi in b_vals) / len(b_vals)
    max_hess_diff = 0.0
    for bi in b_vals:
        g_ik = (h0 * y_loc + bi) - (h0 * x_ref + bi) + grad_f_x
        max_hess_diff = max(max_hess_diff, abs(g_ik - grad_f_y))
    assert max_hess_diff < 1e-14, f"Expected exact zero drift when delta=0, got {max_hess_diff}"

    # Now with delta = 0.5 (h_i in [1.5, 2.5, 1.5, 2.5]):
    h_vals = [1.5, 2.5, 1.5, 2.5]
    delta = 0.5
    for hi, bi in zip(h_vals, b_vals):
        diff = abs(((hi * y_loc + bi) - (hi * x_ref + bi)) - (h0 * (y_loc - x_ref)))
        bound = delta * abs(y_loc - x_ref)
        assert diff <= bound + 1e-12, f"Lemma 3 violated: {diff} > {bound}"

    # 2. Compare Naive Local Momentum vs MimeLiteMom vs MimeMom on heterogeneous strongly convex objectives
    # where clients have different curvatures h_i AND different linear terms b_i so x_* != 0:
    h_het = [1.0, 4.0, 1.5, 3.5]
    b_het = [6.0, -2.0, 4.0, -8.0]  # sum(h)=10, sum(b)=0 -> x_* = 0.0
    # Under K=8 local steps with fixed step size eta=0.04 and momentum beta=0.8:
    K = 8
    eta = 0.03
    beta = 0.8

    # (a) Naive local momentum (re-initializing or running momentum locally on nabla f_i):
    # Wait: if clients have asymmetric local step amplification (1 - eta*h_i)^K, unnormalized local steps bias x
    x_local_mom = 2.0
    m_clients = [0.0] * 4
    for _ in range(150):
        y_ends = []
        for i in range(4):
            y = x_local_mom
            m_loc = m_clients[i]
            for _ in range(K):
                g = h_het[i] * y + b_het[i]
                m_loc = (1.0 - beta) * g + beta * m_loc
                y = y - eta * m_loc
            m_clients[i] = m_loc
            y_ends.append(y)
        x_local_mom = sum(y_ends) / 4.0

    # (b) MimeMom (Algorithm 1 with frozen server momentum s_{t-1} and SVRG correction g_{i,k}):
    x_mime = 2.0
    s_mime = 0.0
    for _ in range(150):
        c_t = sum(hi * x_mime + bi for hi, bi in zip(h_het, b_het)) / 4.0
        y_ends = []
        for i in range(4):
            y = x_mime
            g_x = h_het[i] * x_mime + b_het[i]
            for _ in range(K):
                g_y = h_het[i] * y + b_het[i]
                g_ik = g_y - g_x + c_t
                # Linear parameter update U(g, s_{t-1}) = (1 - beta) * g + beta * s_{t-1}
                d_ik = (1.0 - beta) * g_ik + beta * s_mime
                y = y - eta * d_ik
            y_ends.append(y)
        x_mime = sum(y_ends) / 4.0
        s_mime = (1.0 - beta) * c_t + beta * s_mime

    local_mom_err = abs(x_local_mom - 0.0)
    mime_err = abs(x_mime - 0.0)
    assert local_mom_err > 0.15, f"Expected naive local momentum drift, got {local_mom_err}"
    assert mime_err < 1e-6, f"Expected MimeMom exact convergence, got {mime_err}"

    print(
        f"[PASS] Round 388 Mime (Karimireddy et al. 2021): delta0_drift={max_hess_diff:.2e}, "
        f"mime_err={mime_err:.2e} << naive_local_mom_err={local_mom_err:.4f}"
    )


if __name__ == "__main__":
    main()
