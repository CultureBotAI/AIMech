#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 392:

ProxSkip and Scaffnew Probabilistic Proximal Skipping (Mishchenko et al., ICML
2022).
"""

import math
import random


def vec_add(a, b):
  return [x + y for x, y in zip(a, b)]


def vec_sub(a, b):
  return [x - y for x, y in zip(a, b)]


def vec_scale(s, a):
  return [s * x for x in a]


def dot(a, b):
  return sum(x * y for x, y in zip(a, b))


def norm_sq(a):
  return dot(a, a)


def prox_box(x, lo=-1.0, hi=1.0):
  return [max(lo, min(hi, v)) for v in x]


def verify_firm_nonexpansiveness():
  """Verify Lemma 3.3: ||P(x)-P(y)||^2 + ||Q(x)-Q(y)||^2 <= ||x-y||^2 for P=prox, Q=I-P."""
  rng = random.Random(39201)
  for _ in range(200):
    x = [rng.uniform(-4.0, 4.0) for _ in range(5)]
    y = [rng.uniform(-4.0, 4.0) for _ in range(5)]
    px = prox_box(x)
    py = prox_box(y)
    qx = vec_sub(x, px)
    qy = vec_sub(y, py)
    lhs = norm_sq(vec_sub(px, py)) + norm_sq(vec_sub(qx, qy))
    rhs = norm_sq(vec_sub(x, y))
    assert lhs <= rhs + 1e-12, f"Firm nonexpansiveness violated: {lhs} > {rhs}"


def verify_lyapunov_contraction():
  """Verify Theorem 3.6 exact expected one-step Lyapunov contraction on composite quadratic + box."""
  # f(x) = 0.5 * sum_i lambda_i (x_i - b_i)^2, psi(x) = indicator of [-1, 1]^d
  lambdas = [2.0, 4.0, 8.0, 16.0]
  b = [2.5, -2.0, 0.5, 1.8]
  L = max(lambdas)
  mu = min(lambdas)
  gamma = 1.0 / L
  p = 1.0 / math.sqrt(L / mu)
  zeta = min(gamma * mu, p * p)

  def grad_f(x):
    return [lam * (xi - bi) for lam, xi, bi in zip(lambdas, x, b)]

  # Unique composite optimum x_star = proj_{[-1,1]}(b) since f is separable
  x_star = prox_box(b)
  h_star = grad_f(x_star)
  # Check fixed-point identity: prox(x_star - (gamma/p) h_star) == x_star
  fp = prox_box(vec_sub(x_star, vec_scale(gamma / p, h_star)))
  assert norm_sq(vec_sub(fp, x_star)) < 1e-14

  rng = random.Random(39202)
  for _ in range(100):
    x_t = [rng.uniform(-3.0, 3.0) for _ in range(4)]
    h_t = [rng.uniform(-5.0, 5.0) for _ in range(4)]
    psi_t = norm_sq(vec_sub(x_t, x_star)) + (gamma * gamma / (p * p)) * norm_sq(
        vec_sub(h_t, h_star)
    )

    x_hat = vec_sub(x_t, vec_scale(gamma, vec_sub(grad_f(x_t), h_t)))
    # Branch theta=1 (prob p)
    x_next_1 = prox_box(vec_sub(x_hat, vec_scale(gamma / p, h_t)))
    h_next_1 = vec_add(h_t, vec_scale(p / gamma, vec_sub(x_next_1, x_hat)))
    psi_1 = norm_sq(vec_sub(x_next_1, x_star)) + (
        gamma * gamma / (p * p)
    ) * norm_sq(vec_sub(h_next_1, h_star))

    # Branch theta=0 (prob 1-p)
    x_next_0 = x_hat
    h_next_0 = h_t
    psi_0 = norm_sq(vec_sub(x_next_0, x_star)) + (
        gamma * gamma / (p * p)
    ) * norm_sq(vec_sub(h_next_0, h_star))

    expected_psi_next = p * psi_1 + (1.0 - p) * psi_0
    assert (
        expected_psi_next <= (1.0 - zeta) * psi_t + 1e-11
    ), f"Lyapunov contraction failed: {expected_psi_next} > {(1-zeta)*psi_t}"


def verify_scaffnew_vs_local_gd():
  """Verify Corollary 4.2: Scaffnew converges to exact consensus optimum under heterogeneity while Local GD drifts."""
  # n=4 clients, each with f_i(x) = 0.5 * a_i * (x - c_i)^2 in 1D
  a = [2.0, 4.0, 6.0, 12.0]
  c = [-4.0, 1.0, 5.0, -2.0]
  n = len(a)
  L = max(a)
  mu = min(a)
  kappa = L / mu
  gamma = 1.0 / L
  p = 1.0 / math.sqrt(kappa)

  # Global optimum x_star = sum(a_i c_i) / sum(a_i)
  x_star = sum(ai * ci for ai, ci in zip(a, c)) / sum(a)

  # Run Scaffnew
  rng = random.Random(39203)
  x_scaff = [0.0] * n
  h_scaff = [0.0] * n
  comm_rounds = 0
  T = 600
  for _ in range(T):
    x_hat = [
        x_scaff[i] - gamma * (a[i] * (x_scaff[i] - c[i]) - h_scaff[i])
        for i in range(n)
    ]
    if rng.random() < p:
      comm_rounds += 1
      avg_x = sum(x_hat) / n
      x_next = [avg_x] * n
    else:
      x_next = x_hat
    h_scaff = [
        h_scaff[i] + (p / gamma) * (x_next[i] - x_hat[i]) for i in range(n)
    ]
    x_scaff = x_next

  scaff_err = sum((xi - x_star) ** 2 for xi in x_scaff) / n
  # Verify h_i converged to grad f_i(x_star) = a_i(x_star - c_i)
  h_err = (
      sum((h_scaff[i] - a[i] * (x_star - c[i])) ** 2 for i in range(n)) / n
  )

  # Compare with unshifted Local GD with same expected communication frequency
  rng_lgd = random.Random(39203)
  x_lgd = [0.0] * n
  for _ in range(T):
    x_hat = [x_lgd[i] - gamma * (a[i] * (x_lgd[i] - c[i])) for i in range(n)]
    if rng_lgd.random() < p:
      avg_x = sum(x_hat) / n
      x_lgd = [avg_x] * n
    else:
      x_lgd = x_hat
  lgd_err = sum((xi - x_star) ** 2 for xi in x_lgd) / n

  assert (
      scaff_err < 1e-10
  ), f"Scaffnew failed to converge to exact optimum: {scaff_err}"
  assert h_err < 1e-9, f"Control variates failed to converge: {h_err}"
  assert (
      lgd_err > 1e-2
  ), f"Unshifted Local GD should exhibit client drift error: {lgd_err}"
  print(
      f"[PASS] Round 392 ProxSkip/Scaffnew verified: scaff_err={scaff_err:.3e},"
      f" h_err={h_err:.3e}, lgd_err={lgd_err:.3e}, comm_rounds={comm_rounds}/{T}"
  )


if __name__ == "__main__":
  verify_firm_nonexpansiveness()
  verify_lyapunov_contraction()
  verify_scaffnew_vs_local_gd()
