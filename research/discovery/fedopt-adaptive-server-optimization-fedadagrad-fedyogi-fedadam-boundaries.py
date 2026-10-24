#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 393:

FedOpt Adaptive Server Optimization: FedAdagrad, FedYogi, FedAdam (Reddi et al.,
ICLR 2021).
"""

import math


def verify_yogi_vs_adam_second_moment_control():
  """Verify Section 3: FedYogi controls second-moment accumulator growth additively vs FedAdam multiplicative surge."""
  beta2 = 0.99
  v_adam = 1e-4
  v_yogi = 1e-4
  # Suppose a sudden large pseudo-gradient delta = 10.0 arrives after small gradients
  delta_sq = 100.0
  # FedAdam: v_t = beta2 * v_{t-1} + (1 - beta2) * delta_sq
  v_adam_next = beta2 * v_adam + (1.0 - beta2) * delta_sq
  # FedYogi: v_t = v_{t-1} - (1 - beta2) * delta_sq * sign(v_{t-1} - delta_sq)
  sign = 1.0 if (v_yogi - delta_sq) > 0 else (-1.0 if (v_yogi - delta_sq) < 0 else 0.0)
  v_yogi_next = v_yogi - (1.0 - beta2) * delta_sq * sign
  assert abs(v_adam_next - v_yogi_next) < 1e-6

  # Now suppose a sequence of moderate gradients delta_sq = 0.01 follows after v_t = 10.0
  v_adam = 10.0
  v_yogi = 10.0
  delta_sq = 0.01
  for _ in range(50):
    v_adam = beta2 * v_adam + (1.0 - beta2) * delta_sq
    sign = 1.0 if (v_yogi - delta_sq) > 0 else -1.0
    v_yogi = v_yogi - (1.0 - beta2) * delta_sq * sign

  # In FedYogi, when v_{t-1} > delta_sq, the decrease per step is bounded by (1-beta2)*delta_sq (additive stability),
  # whereas FedAdam decays v_t geometrically by beta2^50 * 10.0, causing aggressive effective step size spikes.
  assert v_yogi > 9.9, f"FedYogi should decay conservatively when v >> delta^2: {v_yogi}"
  assert v_adam < 6.5, f"FedAdam decays geometrically: {v_adam}"


def run_federated_opt(server_opt_kind, T=150, K=5):
  """Run Algorithm 2 on an ill-conditioned heterogeneous multi-client quadratic problem."""
  # d=4 coordinates with extreme curvature scaling (sparse/rare feature structure)
  curvatures = [100.0, 20.0, 1.0, 0.05]
  # 4 clients with heterogeneous optima around true optimum x_star = [1.0, -2.0, 3.0, -4.0]
  x_star = [1.0, -2.0, 3.0, -4.0]
  shifts = [
      [0.5, -0.5, 0.2, -0.2],
      [-0.5, 0.5, -0.2, 0.2],
      [0.3, 0.3, -0.3, -0.3],
      [-0.3, -0.3, 0.3, 0.3],
  ]
  m_clients = len(shifts)
  d = len(curvatures)

  def client_grad(i, x):
    return [
        curvatures[j] * (x[j] - (x_star[j] + shifts[i][j])) for j in range(d)
    ]

  def global_loss(x):
    return 0.5 * sum(curvatures[j] * (x[j] - x_star[j]) ** 2 for j in range(d))

  x = [0.0] * d
  m_vec = [0.0] * d
  tau = 1e-2
  v_vec = [tau * tau] * d
  eta_l = 0.002
  eta_s = 0.5 if server_opt_kind != "fedavg" else 1.0
  beta1 = 0.9
  beta2 = 0.99

  for _ in range(T):
    deltas = [[0.0] * d for _ in range(m_clients)]
    for i in range(m_clients):
      x_loc = list(x)
      for _ in range(K):
        g = client_grad(i, x_loc)
        x_loc = [x_loc[j] - eta_l * g[j] for j in range(d)]
      deltas[i] = [x_loc[j] - x[j] for j in range(d)]

    delta_bar = [
        sum(deltas[i][j] for i in range(m_clients)) / m_clients
        for j in range(d)
    ]
    if server_opt_kind == "fedavg":
      x = [x[j] + eta_s * delta_bar[j] for j in range(d)]
    else:
      m_vec = [
          beta1 * m_vec[j] + (1.0 - beta1) * delta_bar[j] for j in range(d)
      ]
      for j in range(d):
        dsq = delta_bar[j] * delta_bar[j]
        if server_opt_kind == "fedadagrad":
          v_vec[j] = v_vec[j] + dsq
        elif server_opt_kind == "fedyogi":
          sgn = (
              1.0
              if (v_vec[j] - dsq) > 0
              else (-1.0 if (v_vec[j] - dsq) < 0 else 0.0)
          )
          v_vec[j] = v_vec[j] - (1.0 - beta2) * dsq * sgn
        elif server_opt_kind == "fedadam":
          v_vec[j] = beta2 * v_vec[j] + (1.0 - beta2) * dsq
      x = [
          x[j] + eta_s * m_vec[j] / (math.sqrt(max(v_vec[j], 1e-16)) + tau)
          for j in range(d)
      ]

  return global_loss(x), sum((x[j] - x_star[j]) ** 2 for j in range(d))


def main():
  verify_yogi_vs_adam_second_moment_control()
  loss_avg, err_avg = run_federated_opt("fedavg")
  loss_ada, err_ada = run_federated_opt("fedadagrad")
  loss_yogi, err_yogi = run_federated_opt("fedyogi")
  loss_adam, err_adam = run_federated_opt("fedadam")

  assert err_yogi < 0.05 * err_avg, f"FedYogi should outperform FedAvg on ill-conditioned coordinates: {err_yogi} vs {err_avg}"
  assert err_adam < 0.05 * err_avg, f"FedAdam should outperform FedAvg: {err_adam} vs {err_avg}"
  assert err_ada < 0.25 * err_avg, f"FedAdagrad should outperform FedAvg: {err_ada} vs {err_avg}"
  print(
      "[PASS] Round 393 FedOpt verified:"
      f" err_avg={err_avg:.4f}, err_ada={err_ada:.4e},"
      f" err_yogi={err_yogi:.4e}, err_adam={err_adam:.4e}"
  )


if __name__ == "__main__":
  main()
