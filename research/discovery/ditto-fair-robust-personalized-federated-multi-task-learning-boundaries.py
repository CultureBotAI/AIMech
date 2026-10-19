#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 397:

Ditto: Fair and Robust Federated Learning Through Personalization (Li et al.,
ICML 2021).
"""

import random


def verify_theorem8_closed_form_lambda():
  """Verify Theorem 8: exact Bayes-optimal and maximally fair regularization parameter

  lambda* = (sigma^2 * K) / (tau^2 * K + (tau_a^2 - tau^2) * K_a + sigma^2 / n)
  and its comparative statics wrt heterogeneity tau^2, sample size n, and adversarial corruption (K_a, tau_a^2).
  """
  sigma_sq = 1.0
  K = 20
  n = 10

  def lam_star(tau_sq, K_a, tau_a_sq):
    return (sigma_sq * K) / (
        tau_sq * K + (tau_a_sq - tau_sq) * K_a + sigma_sq / n
    )

  # 1. Homogeneous clean case (tau^2 = 0, K_a = 0) -> lambda* = K * n = 200 (heavy pooling toward global average)
  assert abs(lam_star(0.0, 0, 0.0) - K * n) < 1e-12
  # 2. Increasing heterogeneity tau^2 strictly decreases lambda*
  assert lam_star(0.1, 0, 0.1) > lam_star(1.0, 0, 1.0) > lam_star(10.0, 0, 10.0)
  # 3. Increasing adversarial devices K_a or corruption variance tau_a^2 strictly decreases lambda*
  assert lam_star(0.5, 0, 5.0) > lam_star(0.5, 4, 5.0) > lam_star(0.5, 10, 5.0)
  assert lam_star(0.5, 4, 2.0) > lam_star(0.5, 4, 20.0)


def verify_ditto_empirical_fairness_and_robustness():
  """Verify Section 3.3 empirical generalization risk and variance across benign devices under Byzantine corruption."""
  rng = random.Random(39701)
  K = 16
  K_a = 4
  K_b = K - K_a
  n = 8
  sigma_sq = 1.0
  tau_sq = 0.4
  tau_a_sq = 25.0  # Strong Byzantine corruption on K_a devices

  lam_opt = (sigma_sq * K) / (
      tau_sq * K + (tau_a_sq - tau_sq) * K_a + sigma_sq / n
  )

  # Simulate 2000 Monte Carlo realizations of hierarchical Gaussian point estimation (Theorem 8 setting)
  trials = 2000
  mse_local_sum = 0.0
  mse_global_sum = 0.0
  mse_ditto_sum = 0.0
  var_global_sum = 0.0
  var_ditto_sum = 0.0

  for _ in range(trials):
    theta = rng.gauss(0.0, 2.0)
    true_v = []
    hat_v = []
    for k in range(K):
      var_v = tau_sq if k < K_b else tau_a_sq
      vk = theta + rng.gauss(0.0, var_v**0.5)
      true_v.append(vk)
      # Empirical mean of n local samples x_{k,i} = v_k + z_{k,i}
      samples = [vk + rng.gauss(0.0, sigma_sq**0.5) for _ in range(n)]
      hat_v.append(sum(samples) / n)

    w_star = sum(hat_v) / K
    # Ditto closed-form solution of min_{v_k} 0.5*(v_k - hat_v_k)^2/(sigma^2/n) + 0.5*lambda*(v_k - w_star)^2
    # Wait: in Theorem 8, local empirical loss is (1/2)*(v_k - hat_v_k)^2 and penalty is (lambda/2)*(v_k - w_star)^2,
    # so v_k(lambda) = (hat_v_k + lambda * w_star) / (1 + lambda), where alpha = 1 / (1 + lambda).
    v_ditto = [(hat_v[k] + lam_opt * w_star) / (1.0 + lam_opt) for k in range(K_b)]

    errs_local = [(hat_v[k] - true_v[k]) ** 2 for k in range(K_b)]
    errs_global = [(w_star - true_v[k]) ** 2 for k in range(K_b)]
    errs_ditto = [(v_ditto[k] - true_v[k]) ** 2 for k in range(K_b)]

    m_loc = sum(errs_local) / K_b
    m_glob = sum(errs_global) / K_b
    m_dit = sum(errs_ditto) / K_b

    mse_local_sum += m_loc
    mse_global_sum += m_glob
    mse_ditto_sum += m_dit

    var_global_sum += sum((e - m_glob) ** 2 for e in errs_global) / K_b
    var_ditto_sum += sum((e - m_dit) ** 2 for e in errs_ditto) / K_b

  mse_local = mse_local_sum / trials
  mse_global = mse_global_sum / trials
  mse_ditto = mse_ditto_sum / trials
  var_global = var_global_sum / trials
  var_ditto = var_ditto_sum / trials

  assert mse_ditto < mse_local, f"Ditto must beat pure local training: {mse_ditto} vs {mse_local}"
  assert mse_ditto < mse_global, f"Ditto must beat corrupted global model: {mse_ditto} vs {mse_global}"
  assert var_ditto < var_global, f"Ditto must achieve lower benign test-error variance (higher fairness) than global model: {var_ditto} vs {var_global}"
  print(
      "[PASS] Round 397 Ditto verified:"
      f" lambda*={lam_opt:.4f}, mse_ditto={mse_ditto:.4f} <"
      f" min(local={mse_local:.4f}, global={mse_global:.4f});"
      f" var_ditto={var_ditto:.4f} < var_global={var_global:.4f}"
  )


if __name__ == "__main__":
  verify_theorem8_closed_form_lambda()
  verify_ditto_empirical_fairness_and_robustness()
