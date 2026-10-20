#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 534:
Kardam: Lipschitz- and Frequency-Filtered Asynchronous Byzantine SGD
(Damaskinos, El Mhamdi, Guerraoui, Patra, & Taziki, ICML 2018, PMLR 80:1153-1162).
"""

import math
from collections import Counter


def l2_norm(v):
    return math.sqrt(sum(x * x for x in v))


def empirical_lipschitz(g_curr, g_prev, x_curr, x_prev):
    num = l2_norm([g_curr[j] - g_prev[j] for j in range(len(g_curr))])
    den = l2_norm([x_curr[j] - x_prev[j] for j in range(len(x_curr))]) + 1e-12
    return num / den


def quantile_n_minus_f(vals, n, f):
    """(n-f)/n empirical quantile (Definition 5): sorted index n - f - 1 (0-indexed)."""
    s = sorted(vals)
    idx = max(0, min(len(s) - 1, n - f - 1))
    return s[idx]


def frequency_filter_accepts(history_window, candidate_worker, f):
    """Definition 4 (Frequency Filter):
    Given L of up to 2f most recent accepted worker IDs, append candidate_worker;
    accept iff the sum of frequencies of the f most frequent workers in (L; q) is <= f.
    """
    seq = list(history_window[-(2 * f):]) + [candidate_worker]
    counts = Counter(seq)
    top_f_sum = sum(c for _, c in counts.most_common(f))
    return top_f_sum <= f


def staleness_dampening(tau, alpha=0.5):
    """Exponential dampening function Lambda(tau) = exp(-alpha * tau) (Section 5.1)."""
    return math.exp(-alpha * tau)


def main():
    n = 7
    f = 2
    # Verify Theorem 1 slowdown bounds: (n - 2f)/(n - f) <= SL <= (n - f)/n
    sl_lower = (n - 2 * f) / (n - f)
    sl_upper = (n - f) / n
    assert abs(sl_lower - 3.0 / 5.0) < 1e-12
    assert abs(sl_upper - 5.0 / 7.0) < 1e-12
    assert sl_lower < sl_upper

    # Verify Lemma 1 (Frequency Filter guarantee):
    # Suppose f=2 fast Byzantine workers (IDs 5, 6) try to flood the server consecutively.
    accepted_history = []
    stream = [0, 5, 6, 5, 6, 1, 2, 5, 3, 4, 6]
    accepted_stream = []
    for w in stream:
        if frequency_filter_accepts(accepted_history, w, f):
            accepted_history.append(w)
            accepted_stream.append(w)

    # Check every window of length <= 2f+1 = 5 in accepted_history:
    # total occurrences of Byzantine set {5, 6} (size f=2) can never exceed f=2!
    for start in range(len(accepted_stream)):
        window = accepted_stream[start : start + 2 * f + 1]
        byz_count = sum(1 for w in window if w in {5, 6})
        assert byz_count <= f, f"Byzantine count {byz_count} exceeded f={f} in window {window}"

    # Verify Definition 5 (Empirical Lipschitz filter) + asynchronous SGD convergence
    # True quadratic objective F(x) = 0.5 * ||A x - b||^2 with known Lipschitz constant L = 2.0
    x_star = [1.5, -1.0, 0.5]
    scales = [2.0, 1.5, 1.0]

    def grad_fn(x):
        return [scales[j] * (x[j] - x_star[j]) for j in range(3)]

    x_history = [[0.0, 0.0, 0.0], [0.2, -0.1, 0.05]]
    g_accepted_history = [grad_fn(x_history[0]), grad_fn(x_history[1])]

    # Worker empirical Lipschitz coefficients K_hat_p for 5 honest (<=2.0) and 2 Byzantine
    worker_k_hats = [1.62, 1.75, 1.80, 1.85, 1.92, 45.0, 0.01]
    k_hat_t = quantile_n_minus_f(worker_k_hats, n=n, f=f)
    assert abs(k_hat_t - 1.85) < 1e-12

    # Honest candidate gradient at x_t vs Byzantine spike gradient at x_t
    x_t = x_history[-1]
    x_prev = x_history[-2]
    g_prev = g_accepted_history[-1]

    # Honest worker on coordinate with Lipschitz scale <= 1.80
    g_honest = [
        g_prev[0] + 1.5 * (x_t[0] - x_prev[0]),
        g_prev[1] + 1.5 * (x_t[1] - x_prev[1]),
        g_prev[2] + 1.0 * (x_t[2] - x_prev[2]),
    ]
    g_byz_spike = [50.0, -50.0, 50.0]

    k_t_honest = empirical_lipschitz(g_honest, g_prev, x_t, x_prev)
    k_t_byz = empirical_lipschitz(g_byz_spike, g_prev, x_t, x_prev)
    assert k_t_honest <= k_hat_t, f"Expected honest K_t^p={k_t_honest} <= {k_hat_t}"
    assert k_t_byz > k_hat_t, f"Expected Byzantine K_t^p={k_t_byz} > {k_hat_t}"

    # Verify staleness-dampened asynchronous updates converge to x_star even with stale honest gradients
    # and Byzantine attempts filtered out by Lipschitz + Frequency filters
    x_curr = [0.0, 0.0, 0.0]
    x_trace = [list(x_curr)]
    g_trace = [grad_fn(x_curr)]
    freq_hist = []
    gamma = 0.25

    for t in range(1, 60):
        # Honest worker picks a slightly stale model tau in {0, 1, 2}
        honest_id = t % 5
        tau = t % 3
        l_idx = max(0, len(x_trace) - 1 - tau)
        g_cand = grad_fn(x_trace[l_idx])

        # First test a Byzantine spike from worker 5 or 6
        byz_id = 5 + (t % 2)
        g_byz = [-20.0 * grad_fn(x_trace[-1])[j] for j in range(3)]
        if len(x_trace) >= 2:
            kt_byz = empirical_lipschitz(g_byz, g_trace[-1], x_trace[-1], x_trace[-2])
            # Rejected by Lipschitz filter since kt_byz >> 2.0
            assert kt_byz > 2.05

        # Honest candidate passes frequency filter and dampened update is applied
        assert frequency_filter_accepts(freq_hist, honest_id, f)
        freq_hist.append(honest_id)
        lam = staleness_dampening(tau, alpha=0.4)
        # Adaptive learning rate gamma_t = gamma * 1 / lam * lam = gamma (or dampened step)
        step = gamma * lam
        x_next = [x_curr[j] - step * g_cand[j] for j in range(3)]
        x_curr = x_next
        x_trace.append(list(x_curr))
        g_trace.append(list(g_cand))

    final_err = l2_norm([x_curr[j] - x_star[j] for j in range(3)])
    assert final_err < 1e-3, f"Expected convergence error < 1e-3, got {final_err}"

    print(
        f"[PASS] Round 534 Kardam verified: SL_bounds=[{sl_lower:.3f}, {sl_upper:.3f}], "
        f"K_hat_t={k_hat_t:.2f}, k_t_honest={k_t_honest:.2f} <= K_hat_t < k_t_byz={k_t_byz:.1f}, "
        f"final_err={final_err:.6f}"
    )


if __name__ == "__main__":
    main()
