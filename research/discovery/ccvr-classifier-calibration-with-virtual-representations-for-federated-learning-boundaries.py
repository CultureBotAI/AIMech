"""Constructed boundary and numerical verification for Round 437:
CCVR: Classifier Calibration with Virtual Representations for Federated Learning
(Mi Luo, Fei Chen, Dapeng Hu, Yifan Zhang, Jian Liang, & Jiashi Feng 2021,
NeurIPS 2021, pp. 5972-5984, arXiv:2106.05001).
"""

from __future__ import annotations

import math
import random


def compute_mean(samples: list[list[float]], d: int) -> list[float]:
    n = len(samples)
    if n == 0:
        return [0.0] * d
    return [sum(s[i] for s in samples) / n for i in range(d)]


def compute_sample_cov(samples: list[list[float]], mean: list[float], d: int) -> list[list[float]]:
    n = len(samples)
    if n <= 1:
        return [[0.0] * d for _ in range(d)]
    cov = [[0.0] * d for _ in range(d)]
    for s in samples:
        diff = [s[i] - mean[i] for i in range(d)]
        for i in range(d):
            for j in range(d):
                cov[i][j] += diff[i] * diff[j]
    return [[cov[i][j] / (n - 1) for j in range(d)] for i in range(d)]


def main() -> None:
    rng = random.Random(437)
    d = 4
    K = 4
    # Highly non-IID client sample counts for class c across K=4 clients (including N_{c,k}=0 and N_{c,k}=1)
    client_counts = [12, 1, 0, 7]
    N_c = sum(client_counts)

    client_features: list[list[list[float]]] = []
    pooled_features: list[list[float]] = []
    for k, count in enumerate(client_counts):
        feats_k = []
        for _ in range(count):
            vec = [rng.gauss(0.8 * k - 1.0, 0.5 + 0.2 * i) for i in range(d)]
            feats_k.append(vec)
            pooled_features.append(vec)
        client_features.append(feats_k)

    # Centralized ground-truth mean and Bessel-corrected sample covariance on pooled features
    true_mu = compute_mean(pooled_features, d)
    true_cov = compute_sample_cov(pooled_features, true_mu, d)

    # CCVR Exact Federated GMM Aggregation (Section 4, Equations 2-3):
    # Each client uploads only (N_{c,k}, mu_{c,k}, Sigma_{c,k})
    client_stats = []
    for k in range(K):
        n_ck = len(client_features[k])
        mu_ck = compute_mean(client_features[k], d)
        cov_ck = compute_sample_cov(client_features[k], mu_ck, d)
        client_stats.append((n_ck, mu_ck, cov_ck))

    # Server reconstructs exact global mean mu_c (Eq. 2)
    ccvr_mu = [
        sum((n_ck / N_c) * mu_ck[i] for (n_ck, mu_ck, _) in client_stats)
        for i in range(d)
    ]

    # Server reconstructs exact global covariance Sigma_c (Eq. 3)
    ccvr_cov = [[0.0] * d for _ in range(d)]
    for n_ck, mu_ck, cov_ck in client_stats:
        if n_ck == 0:
            continue
        within_w = (n_ck - 1.0) / (N_c - 1.0)
        between_w = n_ck / (N_c - 1.0)
        delta = [mu_ck[i] - ccvr_mu[i] for i in range(d)]
        for i in range(d):
            for j in range(d):
                ccvr_cov[i][j] += within_w * cov_ck[i][j] + between_w * delta[i] * delta[j]

    mu_err = math.sqrt(sum((ccvr_mu[i] - true_mu[i]) ** 2 for i in range(d)))
    cov_err = math.sqrt(
        sum((ccvr_cov[i][j] - true_cov[i][j]) ** 2 for i in range(d) for j in range(d))
    )
    assert mu_err < 1e-14, f"CCVR mean mismatch: {mu_err}"
    assert cov_err < 1e-14, f"CCVR covariance mismatch: {cov_err}"

    # Verify communication efficiency: uploading (N_{c,k}, mu_{c,k}, Sigma_{c,k}) sends 1 + d + d(d+1)/2 scalars
    # regardless of N_{c,k}, and leaks zero raw feature vectors z_{c,k,j}.
    scalars_uploaded_per_class = 1 + d + d * (d + 1) // 2
    assert scalars_uploaded_per_class == 15

    print(
        f"[PASS] Round 437 CCVR (Luo et al. 2021): exact_mu_err={mu_err:.2e}, "
        f"exact_cov_err={cov_err:.2e}, scalars_per_class={scalars_uploaded_per_class}"
    )


if __name__ == "__main__":
    main()
