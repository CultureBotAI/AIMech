#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 396:

Per-FedAvg Model-Agnostic Meta-Learning for Personalized FL (Fallah et al.,
NeurIPS 2020).
"""

import math
import random


def verify_maml_gradient_and_hf_approximation():
  """Verify Eq. (4) exact meta-gradient vs Section 5 Hessian-free (HF) finite-difference approximation."""
  # Non-quadratic smooth function f_i(w) = 0.5 * a * (w - c)^2 + 0.25 * b * (w - c)^4
  a, b, c = 2.0, 0.5, 1.2
  alpha = 0.1
  delta = 1e-6

  def grad_f(w):
    return a * (w - c) + b * ((w - c) ** 3)

  def hess_f(w):
    return a + 3.0 * b * ((w - c) ** 2)

  for w in [-1.5, 0.0, 0.8, 2.5]:
    w_adapt = w - alpha * grad_f(w)
    g_adapt = grad_f(w_adapt)
    exact_meta_grad = (1.0 - alpha * hess_f(w)) * g_adapt
    # Hessian-free finite difference approximation: d_i = (grad f(w + delta * g_adapt) - grad f(w - delta * g_adapt)) / (2 * delta)
    d_hf = (grad_f(w + delta * g_adapt) - grad_f(w - delta * g_adapt)) / (
        2.0 * delta
    )
    hf_meta_grad = g_adapt - alpha * d_hf
    assert abs(exact_meta_grad - hf_meta_grad) < 1e-9


def verify_lemma43_compositional_bias():
  """Verify Lemma 4.3: inner stochastic gradient noise induces non-vanishing bias O(alpha * L * sigma_G / sqrt(D))

  for nonlinear grad f_i unless batch size D grows.
  """
  # f(w) = 0.25 * (w - 1)^4, grad f(w) = (w - 1)^3, which is nonlinear in inner noise!
  alpha = 0.2
  w = 2.0
  true_g = (w - 1.0) ** 3
  true_hess = 3.0 * ((w - 1.0) ** 2)
  true_meta_grad = (1.0 - alpha * true_hess) * ((w - alpha * true_g - 1.0) ** 3)

  rng = random.Random(39601)
  sigma = 0.8

  def estimate_bias(D, trials=4000):
    acc = 0.0
    for _ in range(trials):
      noise1 = rng.gauss(0.0, sigma / math.sqrt(D))
      noise2 = rng.gauss(0.0, sigma / math.sqrt(D))
      noise3 = rng.gauss(0.0, sigma / math.sqrt(D))
      g1 = true_g + noise1
      w_tilde = w - alpha * g1
      g2 = (w_tilde - 1.0) ** 3 + noise2
      h3 = true_hess + noise3
      acc += (1.0 - alpha * h3) * g2
    return abs((acc / trials) - true_meta_grad)

  bias_d1 = estimate_bias(1)
  bias_d64 = estimate_bias(64)
  assert (
      bias_d1 > 4.0 * bias_d64
  ), f"Compositional bias should shrink with inner batch size D: D=1 bias={bias_d1}, D=64 bias={bias_d64}"


def verify_per_fedavg_vs_fedavg_on_heterogeneous_curvatures():
  """Verify Section 3: Per-FedAvg finds an initialization w* that minimizes post-adaptation loss

  sum_i f_i(w - alpha grad f_i(w)), beating standard FedAvg initialization when curvatures differ.
  """
  # Two clients: client 1 has high curvature a1=8.0 at c1=2.0; client 2 has low curvature a2=1.0 at c2=-2.0
  a = [8.0, 1.0]
  c = [2.0, -2.0]
  alpha = 0.1  # One step of GD with alpha=0.1 shrinks client 1 error by (1 - 0.8) = 0.2, client 2 by (1 - 0.1) = 0.9!
  # Standard FedAvg minimizes 0.5*a1*(w-c1)^2 + 0.5*a2*(w-c2)^2 -> weights client 1 heavily (a1=8 vs a2=1)
  w_fedavg = (a[0] * c[0] + a[1] * c[1]) / (a[0] + a[1])

  # Per-FedAvg minimizes F(w) = 0.5 * sum_i a_i * (1 - alpha * a_i)^2 * (w - c_i)^2
  # Notice client 1's effective meta-curvature is a1*(1 - alpha*a1)^2 = 8 * (0.2)^2 = 0.32,
  # while client 2's effective meta-curvature is a2*(1 - alpha*a2)^2 = 1 * (0.9)^2 = 0.81!
  # Thus Per-FedAvg places w* closer to client 2 (the harder-to-adapt client) because client 1 adapts rapidly in 1 step!
  w = 0.0
  beta = 0.05
  for _ in range(300):
    meta_grads = []
    for i in range(2):
      w_adapt = w - alpha * (a[i] * (w - c[i]))
      g_adapt = a[i] * (w_adapt - c[i])
      meta_g = (1.0 - alpha * a[i]) * g_adapt
      meta_grads.append(meta_g)
    w = w - beta * (sum(meta_grads) / 2.0)

  def post_adapt_loss(w_init):
    total = 0.0
    for i in range(2):
      w_i = w_init - alpha * a[i] * (w_init - c[i])
      total += 0.5 * a[i] * ((w_i - c[i]) ** 2)
    return total / 2.0

  loss_per_fedavg = post_adapt_loss(w)
  loss_fedavg = post_adapt_loss(w_fedavg)
  assert (
      loss_per_fedavg < 0.40 * loss_fedavg
  ), f"Per-FedAvg post-adaptation loss must beat FedAvg: {loss_per_fedavg} vs {loss_fedavg}"
  print(
      "[PASS] Round 396 Per-FedAvg verified:"
      f" w_per_fedavg={w:.4f} (closer to slow-adapting client -2.0) vs"
      f" w_fedavg={w_fedavg:.4f};"
      f" post_adapt_loss={loss_per_fedavg:.4f} < {loss_fedavg:.4f}"
  )


if __name__ == "__main__":
  verify_maml_gradient_and_hf_approximation()
  verify_lemma43_compositional_bias()
  verify_per_fedavg_vs_fedavg_on_heterogeneous_curvatures()
