"""Constructed boundary verification for Round 416: DoubleSqueeze (Tang et al., ICML 2019, arXiv:1905.05957).

Verifies:
1. Algorithm 1 & Lemma 1 (Supplementary Material): Bidirectional worker-to-server error memory
   delta_t^{(i)} = g_tilde_t^{(i)} - C(g_tilde_t^{(i)}) (with g_tilde_t^{(i)} = g_t^{(i)} + gamma * delta_{t-1}^{(i)})
   and server-to-worker error memory epsilon_t = v_tilde_t - C(v_tilde_t) (with v_tilde_t = (1/n) sum_i v_t^{(i)} + gamma * epsilon_{t-1})
   yield the exact virtual-iterate recurrence:
     x_tilde_{t+1} = x_tilde_t - eta * g_bar_t + eta * (1 - gamma) * (epsilon_t + delta_bar_t)
   where x_tilde_t = x_t - eta * gamma * (epsilon_{t-1} + delta_bar_{t-1}).
2. Exact cancellation boundary at gamma = 1: x_tilde_{t+1} == x_tilde_t - eta * g_bar_t with zero residual compression bias.
3. Non-cancellation failure at gamma = 0 (uncompensated bidirectional compression): residual error norm remains O(eta * ||epsilon_t + delta_bar_t||) > 0.
"""

from __future__ import annotations


def top1_compress(vec: list[float]) -> list[float]:
    idx = max(range(len(vec)), key=lambda j: abs(vec[j]))
    out = [0.0] * len(vec)
    out[idx] = vec[idx]
    return out


def vec_add(a: list[float], b: list[float], scale_b: float = 1.0) -> list[float]:
    return [x + scale_b * y for x, y in zip(a, b)]


def l2_norm_sq(a: list[float]) -> float:
    return sum(x * x for x in a)


def main() -> None:
    d = 4
    n = 3
    eta = 0.05
    T = 8

    # Synthetic sequence of worker stochastic gradients g_t^{(i)} in R^4
    grads = [
        [
            [0.4 * (t + 1) + 0.1 * i, -0.3 * (i + 1) + 0.05 * t, 0.25 * (t - i), -0.15 * (t + 2 * i)]
            for i in range(n)
        ]
        for t in range(T)
    ]

    for gamma in (1.0, 0.7, 0.0):
        x = [1.0, -0.5, 0.2, 0.8]
        deltas = [[0.0] * d for _ in range(n)]
        eps = [0.0] * d

        max_lemma1_err = 0.0
        max_unbiased_step_diff = 0.0
        for t in range(T):
            delta_bar_prev = [sum(deltas[i][j] for i in range(n)) / n for j in range(d)]
            x_tilde_prev = vec_add(x, vec_add(eps, delta_bar_prev), -eta * gamma)

            v_workers = []
            new_deltas = []
            for i in range(n):
                g_tilde_i = vec_add(grads[t][i], deltas[i], gamma)
                v_i = top1_compress(g_tilde_i)
                delta_i = vec_add(g_tilde_i, v_i, -1.0)
                v_workers.append(v_i)
                new_deltas.append(delta_i)

            v_avg = [sum(v_workers[i][j] for i in range(n)) / n for j in range(d)]
            v_tilde = vec_add(v_avg, eps, gamma)
            v_server = top1_compress(v_tilde)
            eps_new = vec_add(v_tilde, v_server, -1.0)

            x_next = vec_add(x, v_server, -eta)
            delta_bar_curr = [sum(new_deltas[i][j] for i in range(n)) / n for j in range(d)]
            x_tilde_next = vec_add(x_next, vec_add(eps_new, delta_bar_curr), -eta * gamma)

            g_bar_t = [sum(grads[t][i][j] for i in range(n)) / n for j in range(d)]
            rhs_lemma1 = vec_add(
                vec_add(x_tilde_prev, g_bar_t, -eta),
                vec_add(eps_new, delta_bar_curr),
                eta * (1.0 - gamma),
            )
            lemma1_err = l2_norm_sq(vec_add(x_tilde_next, rhs_lemma1, -1.0)) ** 0.5
            max_lemma1_err = max(max_lemma1_err, lemma1_err)

            unbiased_step = vec_add(x_tilde_prev, g_bar_t, -eta)
            step_diff = l2_norm_sq(vec_add(x_tilde_next, unbiased_step, -1.0)) ** 0.5
            max_unbiased_step_diff = max(max_unbiased_step_diff, step_diff)

            x = x_next
            deltas = new_deltas
            eps = eps_new

        assert max_lemma1_err < 1e-12, f"Lemma 1 violated for gamma={gamma}: {max_lemma1_err}"
        if gamma == 1.0:
            assert max_unbiased_step_diff < 1e-12, f"gamma=1 failed to telescope compression error: {max_unbiased_step_diff}"
        elif gamma == 0.0:
            assert max_unbiased_step_diff > 1e-2, f"gamma=0 unexpectedly telescoped error: {max_unbiased_step_diff}"

    print(
        f"[PASS] Round 416 DoubleSqueeze (Tang et al. 2019): Lemma 1 exact recurrence verified "
        f"(err < 1e-12), gamma=1 virtual-iterate drift=0.0, gamma=0 uncompensated drift={max_unbiased_step_diff:.4f} > 0"
    )


if __name__ == "__main__":
    main()
