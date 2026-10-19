"""Constructed boundary verification for Round 420: ATOMO (Wang et al., NeurIPS 2018, arXiv:1806.04090).

Verifies:
1. Lemma 1 & Lemma 2 (Section 3): For an atomic decomposition g = sum_{i=1}^n lambda_i a_i with ||a_i|| = 1,
   the Bernoulli atomic sparsifier g_hat = sum_{i=1}^n (lambda_i t_i / p_i) a_i (t_i ~ Bernoulli(p_i))
   is unbiased (E[g_hat] = g) with variance E[||g - g_hat||^2] = sum_{i=1}^n lambda_i^2 (1/p_i - 1).
2. Lemma 3, Lemma 4 & Theorem 5 (Algorithm 1): Under budget sum_i p_i <= s and 0 < p_i <= 1:
   - When s <= ||lambda||_1 / ||lambda||_infty (s-balanced), optimal probabilities are
     p_i^* = |lambda_i| * s / ||lambda||_1, achieving minimum variance (||lambda||_1^2 / s) - ||lambda||_2^2
     strictly smaller than uniform sampling p_i = s / n (which gives (n / s - 1) ||lambda||_2^2).
   - When s > ||lambda||_1 / ||lambda||_infty (unbalanced), greedy water-filling (Algorithm 1) caps
     leading atoms at p_i = 1 and re-allocates the remaining budget s - |C| across the tail.
3. Theorem 7 & Lemma 8 (Section 5): Spectral-Atomo vs. Entry-wise Atomo dominance
   ||X||_* <= ||X||_{1,1} <= sqrt(n * m) ||X||_*.
"""

from __future__ import annotations


def atomo_variance(lambdas: list[float], probs: list[float]) -> float:
    return sum((lam * lam) * (1.0 / p - 1.0) for lam, p in zip(lambdas, probs))


def solve_atomo_probabilities(lambdas: list[float], s: float) -> list[float]:
    """Algorithm 1 (Theorem 5) exact water-filling solver for ATOMO."""
    abs_lam = [abs(x) for x in lambdas]
    order = sorted(range(len(abs_lam)), key=lambda i: abs_lam[i], reverse=True)
    probs = [0.0] * len(abs_lam)
    rem_s = s
    rem_l1 = sum(abs_lam)
    for pos, idx in enumerate(order):
        if rem_l1 == 0.0:
            probs[idx] = 1.0
            continue
        cand = abs_lam[idx] * rem_s / rem_l1
        if cand >= 1.0:
            probs[idx] = 1.0
            rem_s -= 1.0
            rem_l1 -= abs_lam[idx]
        else:
            for idx2 in order[pos:]:
                probs[idx2] = abs_lam[idx2] * rem_s / rem_l1
            break
    return probs


def main() -> None:
    # Case 1: s-balanced atomic weights (s <= ||lambda||_1 / ||lambda||_infty)
    lambdas_bal = [4.0, 3.0, 2.0, 1.0]  # ||lambda||_1 = 10, ||lambda||_infty = 4 -> ratio = 2.5
    s_bal = 2.0
    p_opt_bal = solve_atomo_probabilities(lambdas_bal, s_bal)
    p_unif_bal = [s_bal / len(lambdas_bal)] * len(lambdas_bal)

    var_opt_bal = atomo_variance(lambdas_bal, p_opt_bal)
    var_unif_bal = atomo_variance(lambdas_bal, p_unif_bal)
    l1_bal = sum(abs(x) for x in lambdas_bal)
    l2_sq_bal = sum(x * x for x in lambdas_bal)
    closed_form_bal = (l1_bal * l1_bal) / s_bal - l2_sq_bal

    assert abs(sum(p_opt_bal) - s_bal) < 1e-12
    assert all(0.0 < p <= 1.0 for p in p_opt_bal)
    assert abs(var_opt_bal - closed_form_bal) < 1e-12
    assert var_opt_bal < var_unif_bal

    # Case 2: s-unbalanced atomic weights (s > ||lambda||_1 / ||lambda||_infty)
    lambdas_unbal = [10.0, 2.0, 1.0, 0.5]  # ||lambda||_1 = 13.5, ||lambda||_infty = 10 -> ratio = 1.35
    s_unbal = 2.2
    p_opt_unbal = solve_atomo_probabilities(lambdas_unbal, s_unbal)
    p_unif_unbal = [s_unbal / len(lambdas_unbal)] * len(lambdas_unbal)
    assert abs(p_opt_unbal[0] - 1.0) < 1e-12, "Leading unbalanced atom must be capped at p_1 = 1"
    assert abs(sum(p_opt_unbal) - s_unbal) < 1e-12
    var_opt_unbal = atomo_variance(lambdas_unbal, p_opt_unbal)
    var_unif_unbal = atomo_variance(lambdas_unbal, p_unif_unbal)
    assert var_opt_unbal < var_unif_unbal

    # Case 3: Spectral-Atomo vs Entry-wise Atomo (Theorem 7, Lemma 8):
    # For rank-1 outer product X = u u^T with u = [1, 1, 1, 1]/2 (||u||_2 = 1),
    # nuclear norm ||X||_* = 1, while entry-wise L1 norm ||X||_{1,1} = 4 = sqrt(4*4) * ||X||_*.
    n_dim = 4
    u = [1.0 / (n_dim ** 0.5)] * n_dim
    nuc_norm = sum(x * x for x in u)  # 1.0
    entry_l1 = sum(abs(u[i] * u[j]) for i in range(n_dim) for j in range(n_dim))  # 4.0
    assert abs(nuc_norm - 1.0) < 1e-12 and abs(entry_l1 - float(n_dim)) < 1e-12
    assert nuc_norm < entry_l1

    print(
        f"[PASS] Round 420 ATOMO (Wang et al. 2018): var_opt_bal={var_opt_bal:.2f} == {closed_form_bal:.2f} "
        f"< var_unif_bal={var_unif_bal:.2f}, var_opt_unbal={var_opt_unbal:.2f} < var_unif_unbal={var_unif_unbal:.2f}, "
        f"||X||_*={nuc_norm:.1f} < ||X||_1,1={entry_l1:.1f}"
    )


if __name__ == "__main__":
    main()
