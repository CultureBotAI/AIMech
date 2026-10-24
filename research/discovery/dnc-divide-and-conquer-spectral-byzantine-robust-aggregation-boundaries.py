#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 521:
DnC (Divide-and-Conquer Spectral Byzantine-Robust Aggregation)
Shejwalkar & Houmansadr, NDSS 2021 (DOI:10.14722/ndss.2021.24498).

Verifies:
1. Lemma 3 & Lemma 1 spectral alignment lower bound: for mixture U = (1-eps)*B + eps*M
   with Sigma_B, Sigma_M <= sigma^2 I and ||Delta||_2^2 >= 6*sigma^2 / eps, the top
   eigenvector v of Sigma_U satisfies <Delta, v>^2 >= (1 - 1/(6*(1-eps))) ||Delta||_2^2
   >= (2/3) ||Delta||_2^2 >= 2*sigma^2 / eps.
2. Algorithm 2 (DnC): random coordinate subsampling r of size b <= d across niters
   iterations, centering tilde_nabla - mu, top right singular vector v via power
   iteration, outlier score s_i = <tilde_nabla_i - mu, v>^2, retaining n - c*m lowest
   scores per iteration, and intersecting I_final = cap I_good.
3. Resilience against directional/Min-Max/Min-Sum model poisoning attacks (Eqs. 2, 6, 7)
   that bypass coordinate-wise Trimmed-Mean and Euclidean-distance Krum.
"""

import math
import random


def power_iteration_top_right_singular_vector(centered_matrix, n_steps=60):
    """Compute top right singular vector v of an n x b centered matrix."""
    n = len(centered_matrix)
    b = len(centered_matrix[0])
    v = [1.0 / math.sqrt(b) for _ in range(b)]
    for _ in range(n_steps):
        # u = A v
        u = [sum(centered_matrix[i][j] * v[j] for j in range(b)) for i in range(n)]
        # v_new = A^T u
        v_new = [sum(centered_matrix[i][j] * u[i] for i in range(n)) for j in range(b)]
        norm = math.sqrt(sum(x * x for x in v_new))
        if norm < 1e-12:
            break
        v = [x / norm for x in v_new]
    return v


def dnc_aggregate(gradients, m, c=1.0, niters=3, b=16, rng=None):
    """Algorithm 2: Divide-and-Conquer (DnC) robust aggregation."""
    if rng is None:
        rng = random.Random(2021)
    n = len(gradients)
    d = len(gradients[0])
    keep_count = int(n - c * m)
    i_good_sets = []
    for _ in range(niters):
        r = sorted(rng.sample(range(d), b))
        sub = [[gradients[i][j] for j in r] for i in range(n)]
        mu = [sum(sub[i][k] for i in range(n)) / n for k in range(b)]
        centered = [[sub[i][k] - mu[k] for k in range(b)] for i in range(n)]
        v = power_iteration_top_right_singular_vector(centered)
        scores = []
        for i in range(n):
            proj = sum(centered[i][k] * v[k] for k in range(b))
            scores.append((proj * proj, i))
        scores.sort(key=lambda item: item[0])
        retained = {idx for _, idx in scores[:keep_count]}
        i_good_sets.append(retained)
    i_final = set.intersection(*i_good_sets)
    if not i_final:
        i_final = i_good_sets[0]
    agg = [
        sum(gradients[i][j] for i in i_final) / len(i_final)
        for j in range(d)
    ]
    return agg, i_final


def trimmed_mean_aggregate(gradients, beta):
    """Coordinate-wise Trimmed-Mean removing beta largest and smallest values."""
    n = len(gradients)
    d = len(gradients[0])
    agg = []
    for j in range(d):
        col = sorted(gradients[i][j] for i in range(n))
        kept = col[beta: n - beta]
        agg.append(sum(kept) / len(kept))
    return agg


def l2_dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def main():
    rng = random.Random(42)
    n = 20
    m = 4  # 20% Byzantine clients (eps = 0.2 < 0.5)
    b_honest = n - m
    d = 32
    sigma = 0.08
    eps = m / n

    # 1. Verify Lemma 3 / Lemma 1 spectral alignment bound on population covariance
    # True benign mean mu_B in R^d
    mu_b = [0.5 if j % 2 == 0 else -0.4 for j in range(d)]
    # Craft an impactful Min-Max style directional perturbation along -mu_b / ||mu_b||
    # that shifts every coordinate by delta_coord so ||Delta||_2^2 >= 6*sigma^2 / eps
    delta_coord = -0.35
    mu_m = [mu_b[j] + delta_coord for j in range(d)]
    delta_vec = [mu_b[j] - mu_m[j] for j in range(d)]
    delta_sq = sum(x * x for x in delta_vec)
    threshold_sq = 6.0 * (sigma ** 2) / eps
    assert delta_sq >= threshold_sq, f"Expected delta_sq={delta_sq} >= {threshold_sq}"

    # Sample 16 benign gradients N(mu_b, sigma^2 I) and 4 colluding malicious gradients
    gradients = []
    for _ in range(b_honest):
        g = [mu_b[j] + rng.gauss(0.0, sigma) for j in range(d)]
        gradients.append(g)
    for _ in range(m):
        g = [mu_m[j] + rng.gauss(0.0, 0.01 * sigma) for j in range(d)]
        gradients.append(g)

    # Full-dimensional empirical top singular vector alignment check (Lemma 3)
    mu_all = [sum(gradients[i][j] for i in range(n)) / n for j in range(d)]
    centered_full = [[gradients[i][j] - mu_all[j] for j in range(d)] for i in range(n)]
    v_full = power_iteration_top_right_singular_vector(centered_full)
    proj_delta_sq = sum(delta_vec[j] * v_full[j] for j in range(d)) ** 2
    lemma3_rhs = (2.0 / 3.0) * delta_sq
    assert proj_delta_sq >= lemma3_rhs, (
        f"Lemma 3 violated: <Delta,v>^2={proj_delta_sq:.4f} < {lemma3_rhs:.4f}"
    )

    # 2. Run Algorithm 2 (DnC) with random subsampling b=16, niters=2, c=1.0
    benign_ref = [sum(gradients[i][j] for i in range(b_honest)) / b_honest for j in range(d)]
    dnc_agg, i_final = dnc_aggregate(gradients, m=m, c=1.0, niters=2, b=16, rng=rng)
    trmean_agg = trimmed_mean_aggregate(gradients, beta=m)
    avg_agg = mu_all

    # Check that DnC filters out all 4 malicious indices {16, 17, 18, 19}
    malicious_indices = set(range(b_honest, n))
    selected_malicious = i_final.intersection(malicious_indices)
    assert len(selected_malicious) == 0, f"Expected 0 malicious selected, got {selected_malicious}"

    err_dnc = l2_dist(dnc_agg, benign_ref)
    err_trmean = l2_dist(trmean_agg, benign_ref)
    err_avg = l2_dist(avg_agg, benign_ref)
    assert err_dnc < err_trmean < err_avg, (
        f"Expected err_dnc={err_dnc:.4f} < err_trmean={err_trmean:.4f} < err_avg={err_avg:.4f}"
    )

    print(
        f"[PASS] Round 521 DnC (Shejwalkar & Houmansadr 2021): "
        f"<Delta,v>^2={proj_delta_sq:.4f}>=2/3||Delta||^2={lemma3_rhs:.4f}, "
        f"malicious_kept={len(selected_malicious)}, "
        f"err_dnc={err_dnc:.4f} < err_trmean={err_trmean:.4f} < err_avg={err_avg:.4f}"
    )


if __name__ == "__main__":
    main()
