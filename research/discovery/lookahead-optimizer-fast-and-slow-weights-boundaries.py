"""Constructed mathematical boundary and dynamical verification for Round 614:
Lookahead Optimizer (Zhang, Lucas, Hinton, & Ba, NeurIPS 2019, arXiv:1907.08610).

Verifies:
1. Algorithm 1 & Eqs. 1-2 (Section 2, p. 2):
   - Outer slow-weight interpolation phi_t = phi_{t-1} + alpha * (theta_{t,k} - phi_{t-1})
     equals the exact exponential moving average (EMA) of the final inner-loop fast weights:
     phi_t = alpha * sum_{j=1}^t (1 - alpha)^{t-j} theta_{j,k} + (1 - alpha)^t phi_0.
2. Proposition 1 & Eq. 13 (Optimal slow-weights step size on quadratic loss, Section 2.1, p. 3 & Appendix B.2, p. 16):
   - For L(x) = 0.5 * x^T A x - b^T x with minimizer theta* = A^{-1} b,
     alpha* = ((theta_{t,0} - theta*)^T A (theta_{t,0} - theta_{t,k})) / ((theta_{t,0} - theta_{t,k})^T A (theta_{t,0} - theta_{t,k}))
     strictly minimizes L(theta_{t,0} + alpha * (theta_{t,k} - theta_{t,0})) with zero derivative at alpha*.
3. Lemma 1 & Proposition 2 (Noisy quadratic model steady-state variance fixed point, Section 3.1, Eqs. 6-7, p. 4 & Appendix A, Eqs. 8-11, p. 13-14):
   - Unrolled slow-weight expectation E[phi_{t+1}] = [(1 - alpha)I + alpha(I - gamma*A)^k] E[phi_t]
     and variance recursion V[phi_{t+1}] = [(1 - alpha)I + alpha(I - gamma*A)^k]^2 V[phi_t] + alpha^2 * sum_{i=0}^{k-1} (I - gamma*A)^{2i} gamma^2 A^2 Sigma
     converge to V*_LA = [alpha^2 (I - (I - gamma*A)^{2k}) / (alpha^2 (I - (I - gamma*A)^{2k}) + 2*alpha*(1 - alpha)*(I - (I - gamma*A)^k))] V*_SGD < V*_SGD.
4. Deterministic quadratic linear dynamical system with Classical Momentum (Section 3.2 & Appendix B.1, p. 5, 14-16):
   - Exact equivalence between step-by-step inner Classical Momentum + outer Lookahead interpolation
     and the stacked state-transition operator M = L * B^{k-1} * T.
"""

from __future__ import annotations

import math
import random


def verify_ema_and_proposition_1() -> tuple[float, float, float]:
    rng = random.Random(20261019)
    d = 4
    # Positive definite diagonal A and vector b
    A = [1.5, 4.0, 10.0, 25.0]
    b = [0.6, -1.6, 5.0, -7.5]
    theta_star = [b[i] / A[i] for i in range(d)]

    def loss_quad(x: list[float]) -> float:
        return sum(0.5 * A[i] * (x[i] ** 2) - b[i] * x[i] for i in range(d))

    phi_0 = [rng.uniform(-2.0, 2.0) for _ in range(d)]
    phi = list(phi_0)
    alpha = 0.5
    k = 5
    gamma = 0.04

    theta_final_history: list[list[float]] = []
    max_ema_err = 0.0
    max_prop1_grad_err = 0.0
    min_prop1_gain = float("inf")

    for t in range(1, 21):
        theta = list(phi)
        theta_t0 = list(phi)
        for _ in range(k):
            grad = [A[j] * theta[j] - b[j] + rng.gauss(0.0, 0.05) for j in range(d)]
            theta = [theta[j] - gamma * grad[j] for j in range(d)]
        theta_tk = list(theta)
        theta_final_history.append(theta_tk)

        # Verify Proposition 1 optimal step size alpha* between theta_{t,0} and theta_{t,k}
        diff = [theta_t0[j] - theta_tk[j] for j in range(d)]
        num = sum((theta_t0[j] - theta_star[j]) * A[j] * diff[j] for j in range(d))
        den = sum(diff[j] * A[j] * diff[j] for j in range(d))
        alpha_star = num / den

        phi_opt = [theta_t0[j] + alpha_star * (theta_tk[j] - theta_t0[j]) for j in range(d)]
        # Derivative d/d_alpha L(theta_t0 + alpha*(theta_tk - theta_t0)) at alpha_star
        grad_alpha_star = sum(
            (theta_tk[j] - theta_t0[j]) * (A[j] * phi_opt[j] - b[j]) for j in range(d)
        )
        max_prop1_grad_err = max(max_prop1_grad_err, abs(grad_alpha_star))

        loss_opt = loss_quad(phi_opt)
        for delta in (-0.25, -0.05, 0.05, 0.25):
            a_alt = alpha_star + delta
            phi_alt = [theta_t0[j] + a_alt * (theta_tk[j] - theta_t0[j]) for j in range(d)]
            min_prop1_gain = min(min_prop1_gain, loss_quad(phi_alt) - loss_opt)

        # Standard Lookahead update Eq. 1
        phi = [phi[j] + alpha * (theta_tk[j] - phi[j]) for j in range(d)]

        # Unrolled EMA Eq. 2
        phi_ema = [((1.0 - alpha) ** t) * phi_0[j] for j in range(d)]
        for s_idx in range(1, t + 1):
            w = alpha * ((1.0 - alpha) ** (t - s_idx))
            for j in range(d):
                phi_ema[j] += w * theta_final_history[s_idx - 1][j]

        err = max(abs(phi[j] - phi_ema[j]) for j in range(d))
        max_ema_err = max(max_ema_err, err)

    assert max_ema_err < 1e-14
    assert max_prop1_grad_err < 1e-13
    assert min_prop1_gain > 0.0
    return max_ema_err, max_prop1_grad_err, min_prop1_gain


def verify_noisy_quadratic_proposition_2() -> tuple[float, float]:
    # Proposition 2 & Lemma 1 (Section 3.1, Eqs. 6-7 & Appendix A, Eqs. 10-11)
    A_diag = [0.5, 2.0, 8.0, 20.0]
    Sigma_diag = [2.0, 1.0, 0.5, 0.25]
    L_max = max(A_diag)
    gamma = 0.06  # strictly < 2 / L_max = 0.1
    assert 0.0 < gamma < 2.0 / L_max
    alpha = 0.5
    k = 5

    max_fp_err = 0.0
    max_ratio = 0.0

    for a, sig2 in zip(A_diag, Sigma_diag):
        # SGD variance fixed point Eq. 6 (using Sigma = sig2 as in Eq. 9 & proof on p. 13)
        v_sgd_star = (gamma * gamma * a * a * sig2) / (1.0 - ((1.0 - gamma * a) ** 2))

        # Lookahead variance recursion Lemma 1 (Eq. 11)
        contraction = (1.0 - alpha) + alpha * ((1.0 - gamma * a) ** k)
        noise_sum = sum(((1.0 - gamma * a) ** (2 * i)) * (gamma * gamma * a * a * sig2) for i in range(k))
        v_la = 1.7  # arbitrary initial variance
        for _ in range(400):
            v_la = (contraction * contraction) * v_la + (alpha * alpha) * noise_sum

        # Proposition 2 closed-form Eq. 7
        one_minus_2k = 1.0 - ((1.0 - gamma * a) ** (2 * k))
        one_minus_k = 1.0 - ((1.0 - gamma * a) ** k)
        prefactor = (alpha * alpha * one_minus_2k) / (
            alpha * alpha * one_minus_2k + 2.0 * alpha * (1.0 - alpha) * one_minus_k
        )
        v_la_star = prefactor * v_sgd_star

        max_fp_err = max(max_fp_err, abs(v_la - v_la_star))
        max_ratio = max(max_ratio, v_la_star / v_sgd_star)
        assert v_la_star < v_sgd_star

    assert max_fp_err < 1e-14
    assert max_ratio < 1.0
    return max_fp_err, max_ratio


def verify_dynamical_system_matrix_equivalence() -> float:
    # Appendix B.1 (p. 14-16): stacked fast-weight state vector [theta_{t,0}, theta_{t-1,k}, ..., theta_{t-1,1}]^T
    # evolves via M = L * B^{k-1} * T for 1D quadratic f(x) = 0.5 * a * x^2 with Classical Momentum (reset/interpolated state).
    a = 3.0
    eta = 0.08
    beta = 0.85
    alpha = 0.5
    k = 4
    dim = k + 1  # state is [theta_{t,0}, theta_{t-1,k}, theta_{t-1,k-1}, ..., theta_{t-1,1}]

    def mat_mul(X: list[list[float]], Y: list[list[float]]) -> list[list[float]]:
        return [
            [sum(X[i][m] * Y[m][j] for m in range(dim)) for j in range(dim)]
            for i in range(dim)
        ]

    def mat_vec(X: list[list[float]], v: list[float]) -> list[float]:
        return [sum(X[i][j] * v[j] for j in range(dim)) for i in range(dim)]

    # Build L, B, T of size (k+1) x (k+1) as in Appendix B.1 (p. 15-16)
    L_mat = [[0.0] * dim for _ in range(dim)]
    L_mat[0][0] = alpha
    L_mat[0][dim - 1] = 1.0 - alpha
    for r in range(1, dim):
        L_mat[r][r - 1] = 1.0

    B_mat = [[0.0] * dim for _ in range(dim)]
    B_mat[0][0] = (1.0 + beta) - eta * a
    B_mat[0][1] = -beta
    for r in range(1, dim):
        B_mat[r][r - 1] = 1.0

    T_mat = [[0.0] * dim for _ in range(dim)]
    T_mat[0][0] = 1.0 - eta * a
    T_mat[0][1] = beta
    T_mat[0][2] = -beta
    for r in range(1, dim):
        T_mat[r][r - 1] = 1.0

    M = T_mat
    for _ in range(k - 1):
        M = mat_mul(B_mat, M)
    M = mat_mul(L_mat, M)

    # Simulate direct inner-loop recurrence matching T followed by (k-1) steps of B and outer interpolation L
    state = [2.0, 1.8, 1.5, 1.2, 1.0]
    max_dyn_err = 0.0
    for _ in range(15):
        state_mat = mat_vec(M, state)
        # Direct step-by-step application of T, B^{k-1}, L
        # Step 1 (T): theta_{t-1,1} = (1 - eta*a)*theta_{t-1,0} + beta*(theta_{t-2,k} - theta_{t-2,k-1})
        th_prev_0 = state[0]
        v_init = state[1] - state[2]
        th_curr = th_prev_0 - eta * a * th_prev_0 + beta * v_init
        seq = [th_prev_0, th_curr]  # [theta_{t-1,0}, theta_{t-1,1}, ...]
        for i_step in range(2, k + 1):
            th_next = (1.0 + beta - eta * a) * seq[-1] - beta * seq[-2]
            seq.append(th_next)
        # Outer update L: theta_{t,0} = alpha * theta_{t-1,k} + (1 - alpha) * theta_{t-1,0}
        th_t0 = alpha * seq[k] + (1.0 - alpha) * seq[0]
        direct_state = [th_t0] + [seq[j] for j in range(k, 0, -1)]
        err = max(abs(state_mat[j] - direct_state[j]) for j in range(dim))
        max_dyn_err = max(max_dyn_err, err)
        state = state_mat

    assert max_dyn_err < 1e-14
    return max_dyn_err


if __name__ == "__main__":
    ema_err, p1_err, p1_gain = verify_ema_and_proposition_1()
    fp_err, var_rat = verify_noisy_quadratic_proposition_2()
    dyn_err = verify_dynamical_system_matrix_equivalence()
    print(
        f"[PASS] Round 614 Lookahead verified: "
        f"ema_err={ema_err:.2e}, prop1_grad_err={p1_err:.2e}, prop1_gain={p1_gain:.4e}>0, "
        f"prop2_fp_err={fp_err:.2e}, var_ratio={var_rat:.4f}<1, dyn_err={dyn_err:.2e}"
    )
