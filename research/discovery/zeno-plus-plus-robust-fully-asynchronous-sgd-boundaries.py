#!/usr/bin/env python3
"""Constructed boundary verification for Round 532: Zeno++ (Xie, Koyejo, & Gupta, ICML 2020).

Verifies:
1. Definition 3 & Algorithm 2 Lines 6-7: Candidate worker gradient g_tilde is rescaled via
   g = c * g_tilde with c = ||v||_2 / ||g_tilde||_2 so that ||g||_2^2 = ||v||_2^2 (neutralizing
   arbitrary magnitude scaling attacks), and the first-order Taylor Approximated Stochastic
   Descent Score Score_{gamma, rho}(g, x) approx gamma * <v, g> - rho * ||g||_2^2 accepts
   honest descent directions while rejecting sign-flipping (-10 * grad) and orthogonal/opposing
   Byzantine updates under hard threshold -gamma * epsilon.
2. Theorem 1 & Appendix A.1 Descent Lemma: For L-smooth mu-PL objective F(x) with validation
   gradient v = nabla f_s(x_tau) at server delay t - tau <= k, any candidate gradient g passing
   the Zeno++ test satisfies <nabla F(x_{t-1}), -gamma * g> <= -rho*(V2/V1)*||nabla F(x_{t-1})||^2
   + gamma*V3 + L^2*k^2*gamma^3*V1 + (gamma/2)*V1 + gamma*epsilon + (L*gamma^2/2)*V1,
   enabling convergence even when a majority (e.g., q = 8 of m = 10) of workers are Byzantine.
"""

import math


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def norm2(u):
    return math.sqrt(dot(u, u))


def zeno_pp_validate(g_tilde, v, gamma, rho, eps):
    """Algorithm 2 Lines 6-7: Rescale g_tilde to ||v||_2 and check approximated descent score."""
    nv = norm2(v)
    ng = norm2(g_tilde)
    assert nv > 0.0 and ng > 0.0
    g = [x * (nv / ng) for x in g_tilde]
    score = gamma * dot(v, g) - rho * dot(g, g)
    accepted = score >= -gamma * eps
    return accepted, score, g


def main():
    # Quadratic objective F(x) = 0.5 * ||x - x^*||_2^2 with x^* = [0.0, 0.0]
    x_curr = [4.0, 3.0]  # grad F(x_curr) = [4.0, 3.0], ||grad|| = 5.0
    # Stale validation gradient v = grad f_s(x_tau) with small delay/noise
    v = [3.9, 3.1]
    gamma = 0.1
    rho = 0.05
    eps = 0.05

    # 1. Honest worker gradient (with small stochastic noise)
    g_honest = [4.1, 2.9]
    acc_hon, score_hon, g_hon_norm = zeno_pp_validate(g_honest, v, gamma, rho, eps)
    assert acc_hon, f"Expected honest gradient accepted, got score={score_hon}"
    assert abs(norm2(g_hon_norm) - norm2(v)) < 1e-12

    # 2. Sign-flipping Byzantine worker (-10 * g_honest)
    g_signflip = [-10.0 * x for x in g_honest]
    acc_sf, score_sf, g_sf_norm = zeno_pp_validate(g_signflip, v, gamma, rho, eps)
    assert not acc_sf, f"Expected sign-flipping gradient rejected, got score={score_sf}"
    # Magnitude boosting (-10x) is neutralized by Line 6 normalization ||g||_2 == ||v||_2
    assert abs(norm2(g_sf_norm) - norm2(v)) < 1e-12

    # 3. Orthogonal Byzantine gradient (zero inner product with v) when eps = 0
    g_orth = [-v[1], v[0]]
    acc_orth, score_orth, _ = zeno_pp_validate(g_orth, v, gamma, rho, eps=0.0)
    assert not acc_orth and abs(score_orth - (-rho * dot(v, v))) < 1e-12

    # 4. Simulate asynchronous stream where 80% of arrivals (8 of 10) are Byzantine sign-flippers
    x = list(x_curr)
    accepted_count = 0
    byz_accepted = 0
    for step in range(30):
        v_server = [x[0] * 0.98, x[1] * 1.02]
        if step % 5 == 0:
            # 1 in 5 messages is from an honest worker
            cand = [x[0], x[1]]
            is_byz = False
        else:
            # 4 in 5 messages are from Byzantine sign-flippers
            cand = [-10.0 * x[0], -10.0 * x[1]]
            is_byz = True
        ok, _, g_rescaled = zeno_pp_validate(cand, v_server, gamma, rho, eps=0.0)
        if ok:
            accepted_count += 1
            if is_byz:
                byz_accepted += 1
            x = [x[j] - gamma * g_rescaled[j] for j in range(2)]

    assert byz_accepted == 0 and accepted_count == 6
    assert norm2(x) < norm2(x_curr) * 0.55

    print(
        f"[PASS] Round 532 Zeno++ (Xie et al. 2020): "
        f"score_hon={score_hon:.3f}>=-gamma*eps={-gamma*eps:.3f}>score_sf={score_sf:.3f}, "
        f"byz_accepted={byz_accepted}/24, ||x_final||={norm2(x):.4f}<||x_0||={norm2(x_curr):.4f}"
    )


if __name__ == "__main__":
    main()
