#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 395:

pFedMe Personalized Federated Learning with Moreau Envelopes (T. Dinh et al.,
NeurIPS 2020).
"""


def verify_moreau_envelope_properties():
  """Verify Proposition 1: For f_i(theta) = 0.5 * a_i * (theta - c_i)^2,

  prox_{f_i/lambda}(w) = (a_i c_i + lambda w) / (a_i + lambda),
  F_i(w) = 0.5 * (a_i * lambda / (a_i + lambda)) * (w - c_i)^2,
  and grad F_i(w) = lambda * (w - prox_{f_i/lambda}(w)) with strong convexity mu_F = lambda * mu / (lambda + mu).
  """
  a_i = 4.0
  c_i = -2.5
  lam = 6.0
  for w in [-3.0, 0.0, 1.5, 4.0]:
    theta_hat = (a_i * c_i + lam * w) / (a_i + lam)
    assert abs(a_i * (theta_hat - c_i) + lam * (theta_hat - w)) < 1e-12
    F_val = 0.5 * a_i * (theta_hat - c_i) ** 2 + 0.5 * lam * (theta_hat - w) ** 2
    mu_F = (a_i * lam) / (a_i + lam)
    F_exact = 0.5 * mu_F * (w - c_i) ** 2
    assert abs(F_val - F_exact) < 1e-12
    grad_F_from_prox = lam * (w - theta_hat)
    grad_F_exact = mu_F * (w - c_i)
    assert abs(grad_F_from_prox - grad_F_exact) < 1e-12


def run_pfedme_algorithm():
  """Verify Algorithm 1 (pFedMe) with K-step inner approximate proximal solver vs global FedAvg."""
  a = [2.0, 4.0, 3.0, 5.0]
  c = [-4.0, -1.0, 2.0, 5.0]
  N = len(a)
  lam = 4.0
  beta = 1.0
  R = 3
  K = 25
  gamma_inner = 1.0 / (max(a) + lam)

  mu_Fs = [(a[i] * lam) / (a[i] + lam) for i in range(N)]
  w_star = sum(mu_Fs[i] * c[i] for i in range(N)) / sum(mu_Fs)
  theta_stars = [(a[i] * c[i] + lam * w_star) / (a[i] + lam) for i in range(N)]

  w = 0.0
  theta_tilde = [0.0] * N
  for t in range(600):
    eta = 0.08 / (1.0 + 0.05 * t)
    w_locals = []
    for i in range(N):
      w_ir = w
      for _ in range(R):
        th = w_ir
        for _ in range(K):
          g_h = a[i] * (th - c[i]) + lam * (th - w_ir)
          th = th - gamma_inner * g_h
        theta_tilde[i] = th
        w_ir = w_ir - eta * lam * (w_ir - theta_tilde[i])
      w_locals.append(w_ir)
    w = (1.0 - beta) * w + beta * (sum(w_locals) / N)

  # Final personalized evaluation at converged w
  for i in range(N):
    th = w
    for _ in range(K):
      g_h = a[i] * (th - c[i]) + lam * (th - w)
      th = th - gamma_inner * g_h
    theta_tilde[i] = th

  w_err = abs(w - w_star)
  theta_err = max(abs(theta_tilde[i] - theta_stars[i]) for i in range(N))

  pers_loss = sum(0.5 * a[i] * (theta_tilde[i] - c[i]) ** 2 for i in range(N)) / N
  global_loss = sum(0.5 * a[i] * (w - c[i]) ** 2 for i in range(N)) / N

  assert w_err < 5e-3, f"pFedMe global model w failed to converge to Moreau optimum: {w_err}"
  assert theta_err < 5e-3, f"pFedMe personalized models failed to converge to proximal optima: {theta_err}"
  assert pers_loss < 0.35 * global_loss, f"Personalized models must achieve much lower local loss than global model: {pers_loss} vs {global_loss}"
  print(
      "[PASS] Round 395 pFedMe verified:"
      f" w_err={w_err:.3e}, theta_err={theta_err:.3e},"
      f" pers_loss={pers_loss:.4f} < global_loss={global_loss:.4f}"
  )


if __name__ == "__main__":
  verify_moreau_envelope_properties()
  run_pfedme_algorithm()
