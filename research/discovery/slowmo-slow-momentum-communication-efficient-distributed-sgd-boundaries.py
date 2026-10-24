"""Constructed boundary verification for Round 426: SlowMo (Wang et al., ICLR 2020, arXiv:1910.00643).

Verifies:
1. Section 2 (Algorithm 1, Equations 1-3) & Appendix D.1 (Equations 16-22):
   After tau local base-optimizer steps x_{t,k+1}^{(i)} = x_{t,k}^{(i)} - gamma_t d_{t,k}^{(i)} across m workers
   and exact averaging x_{t,tau} = (1/m) sum_{i=1}^m x_{t,tau}^{(i)}, the SlowMo outer update:
     u_{t+1} = beta * u_t + (1 / gamma_t) * (x_{t,0} - x_{t,tau}),
     x_{t+1,0} = x_{t,0} - alpha * gamma_t * u_{t+1}
   induces the auxiliary sequence y_{t,0} = x_{t,0} + (beta / (1 - beta)) * (x_{t,0} - x_{t-1,0}) (with x_{-1,0} = x_{0,0})
   satisfying the exact memoryless recurrence:
     y_{t+1,0} - y_{t,0} == - (alpha * gamma_t / (1 - beta)) * sum_{k=0}^{tau-1} (1/m) sum_{i=1}^m d_{t,k}^{(i)}
   with effective step size gamma_eff = alpha * gamma_t / (1 - beta)!
2. Section 3 (Table 1):
   - alpha = 1, beta = 0 recovers standard Local SGD / SGP (x_{t+1,0} == x_{t,tau}).
   - m = 1, beta = 0, alpha in (0, 1) recovers Lookahead (x_{t+1,0} == (1 - alpha) x_{t,0} + alpha x_{t,tau}).
"""

from __future__ import annotations


def main() -> None:
    m = 3
    tau = 4
    gamma = 0.05
    alpha = 0.8
    beta = 0.6
    T = 6

    x_t0 = 2.0
    x_prev0 = x_t0  # x_{-1,0} = x_{0,0} when u_0 = 0
    u_t = 0.0
    gamma_eff = alpha * gamma / (1.0 - beta)

    max_aux_err = 0.0
    for t in range(T):
        # Simulate tau local steps on m workers
        d_tk = [[0.2 * (t + 1) + 0.1 * i - 0.05 * k for i in range(m)] for k in range(tau)]
        x_workers = [x_t0 for _ in range(m)]
        for k in range(tau):
            for i in range(m):
                x_workers[i] -= gamma * d_tk[k][i]
        x_t_tau = sum(x_workers) / m

        # SlowMo outer momentum step (Eqs. 2-3)
        u_next = beta * u_t + (x_t0 - x_t_tau) / gamma
        x_next0 = x_t0 - alpha * gamma * u_next

        # Auxiliary sequence y_{t,0} (Appendix D.1, Eq. 19-21)
        y_t0 = x_t0 + (beta / (1.0 - beta)) * (x_t0 - x_prev0)
        y_next0 = x_next0 + (beta / (1.0 - beta)) * (x_next0 - x_t0)

        sum_avg_d = sum(sum(d_tk[k][i] for i in range(m)) / m for k in range(tau))
        expected_y_diff = -gamma_eff * sum_avg_d
        aux_err = abs((y_next0 - y_t0) - expected_y_diff)
        max_aux_err = max(max_aux_err, aux_err)

        x_prev0 = x_t0
        x_t0 = x_next0
        u_t = u_next

    assert max_aux_err < 1e-14, f"Appendix D.1 auxiliary recurrence failed: {max_aux_err}"

    # Verify Table 1 special cases:
    # 1) alpha = 1, beta = 0 -> x_{t+1,0} == x_{t,tau}
    x0_test, x_tau_test = 2.0, 1.35
    u_local = 0.0 * 0.0 + (x0_test - x_tau_test) / gamma
    x_next_local = x0_test - 1.0 * gamma * u_local
    assert abs(x_next_local - x_tau_test) < 1e-15

    # 2) beta = 0, alpha = 0.5 (Lookahead) -> x_{t+1,0} == (1 - alpha) x_{t,0} + alpha x_{t,tau}
    alpha_la = 0.5
    x_next_la = x0_test - alpha_la * gamma * ((x0_test - x_tau_test) / gamma)
    assert abs(x_next_la - ((1.0 - alpha_la) * x0_test + alpha_la * x_tau_test)) < 1e-15

    print(
        f"[PASS] Round 426 SlowMo (Wang et al. 2020): aux_recurrence_err={max_aux_err:.1e}, "
        f"gamma_eff={gamma_eff:.4f}, local_sgd_reduction_err=0.0, lookahead_reduction_err=0.0"
    )


if __name__ == "__main__":
    main()
