#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 394:

q-Fair Federated Learning (q-FFL) and q-FedAvg (Li et al., ICLR 2020).
"""

import math


def verify_lemma3_local_smoothness():
  """Verify Lemma 3: Hessian of f_q(w) = f(w)^{q+1}/(q+1) is q f(w)^{q-1} grad f grad f^T + f(w)^q nabla^2 f(w),

  and its spectral norm is upper-bounded by L_q(w) = L f(w)^q + q f(w)^{q-1} ||grad f(w)||^2.
  """
  # f(w) = 0.5 * (a1 (w1 - c1)^2 + a2 (w2 - c2)^2) + f0 with L = max(a1, a2)
  a1, a2 = 3.0, 7.0
  c1, c2 = 1.0, -2.0
  f0 = 0.5
  L = max(a1, a2)
  w1, w2 = 2.5, 0.5
  f_val = 0.5 * (a1 * (w1 - c1) ** 2 + a2 * (w2 - c2) ** 2) + f0
  g1, g2 = a1 * (w1 - c1), a2 * (w2 - c2)
  grad_norm_sq = g1 * g1 + g2 * g2

  for q in [0.0, 0.5, 1.0, 2.0, 5.0]:
    # Exact 2x2 Hessian of f(w)^{q+1}/(q+1)
    h11 = q * (f_val ** (q - 1.0)) * g1 * g1 + (f_val**q) * a1
    h12 = q * (f_val ** (q - 1.0)) * g1 * g2
    h22 = q * (f_val ** (q - 1.0)) * g2 * g2 + (f_val**q) * a2
    # Largest eigenvalue of symmetric 2x2 matrix [[h11, h12], [h12, h22]]
    tr = h11 + h22
    det = h11 * h22 - h12 * h12
    lambda_max = 0.5 * (tr + math.sqrt(max(0.0, tr * tr - 4.0 * det)))
    L_q = L * (f_val**q) + q * (f_val ** (q - 1.0)) * grad_norm_sq
    assert (
        lambda_max <= L_q + 1e-10
    ), f"Lemma 3 upper bound violated for q={q}: {lambda_max} > {L_q}"


def run_q_fedavg(q, T=300, local_steps=4):
  """Run Algorithm 2 (q-FedAvg) on heterogeneous devices with distinct loss floors and targets."""
  # 5 devices in 2D with different targets and base difficulties
  targets = [
      (0.0, 0.0),
      (0.2, -0.1),
      (-0.1, 0.2),
      (1.5, 1.5),
      (-1.2, 1.8),
  ]
  floors = [0.2, 0.25, 0.3, 1.2, 1.5]
  curv = 2.0
  L = curv
  eta = 0.1
  m = len(targets)

  def device_loss(k, w):
    tx, ty = targets[k]
    return 0.5 * curv * ((w[0] - tx) ** 2 + (w[1] - ty) ** 2) + floors[k]

  def device_grad(k, w):
    tx, ty = targets[k]
    return [curv * (w[0] - tx), curv * (w[1] - ty)]

  w = [0.0, 0.0]
  for _ in range(T):
    sum_delta = [0.0, 0.0]
    sum_h = 0.0
    for k in range(m):
      Fk = device_loss(k, w)
      w_loc = list(w)
      for _ in range(local_steps):
        g = device_grad(k, w_loc)
        w_loc = [w_loc[0] - eta * g[0], w_loc[1] - eta * g[1]]
      # Algorithm 2 step: Delta_k^t = L (w^t - w_loc)
      delta_kt = [L * (w[0] - w_loc[0]), L * (w[1] - w_loc[1])]
      norm_delta_sq = delta_kt[0] ** 2 + delta_kt[1] ** 2
      fk_q = Fk**q
      fk_qm1 = Fk ** (q - 1.0) if q > 0 else 0.0
      delta_k = [fk_q * delta_kt[0], fk_q * delta_kt[1]]
      h_k = q * fk_qm1 * norm_delta_sq + L * fk_q
      sum_delta[0] += delta_k[0] / m
      sum_delta[1] += delta_k[1] / m
      sum_h += h_k / m
    w = [w[0] - sum_delta[0] / sum_h, w[1] - sum_delta[1] / sum_h]

  losses = [device_loss(k, w) for k in range(m)]
  mean_loss = sum(losses) / m
  var_loss = sum((l - mean_loss) ** 2 for l in losses) / m
  max_loss = max(losses)
  return losses, var_loss, max_loss


def main():
  verify_lemma3_local_smoothness()
  _, var_q0, max_q0 = run_q_fedavg(0.0)
  _, var_q1, max_q1 = run_q_fedavg(1.0)
  _, var_q5, max_q5 = run_q_fedavg(5.0)

  assert (
      var_q0 > var_q1 > var_q5
  ), f"Variance across devices must decrease monotonically with q: {var_q0}, {var_q1}, {var_q5}"
  assert (
      max_q0 > max_q1 > max_q5
  ), f"Worst-device loss must decrease monotonically with q: {max_q0}, {max_q1}, {max_q5}"
  print(
      "[PASS] Round 394 q-FFL verified:"
      f" var(q=0)={var_q0:.4f} > var(q=1)={var_q1:.4f} > var(q=5)={var_q5:.4f};"
      f" max(q=0)={max_q0:.4f} > max(q=5)={max_q5:.4f}"
  )


if __name__ == "__main__":
  main()
