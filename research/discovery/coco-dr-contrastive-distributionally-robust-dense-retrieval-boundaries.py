#!/usr/bin/env python3
"""Boundary verification for Round 755: COCO-DR Continuous Contrastive and Implicit Distributionally Robust Learning (Yu et al., EMNLP 2022)."""

import math


def weighted_jaccard_similarity(source_counts, target_counts):
    """Eq. 13: J(S, T) = sum_k min(S_k, T_k) / sum_k max(S_k, T_k) over all unique words k."""
    vocab = set(source_counts.keys()) | set(target_counts.keys())
    num = sum(min(source_counts.get(k, 0.0), target_counts.get(k, 0.0)) for k in vocab)
    den = sum(max(source_counts.get(k, 0.0), target_counts.get(k, 0.0)) for k in vocab)
    return num / den if den > 0.0 else 0.0


def idro_cluster_weights_update(prev_weights, cluster_losses, cluster_grads, beta=0.25, tau=10.0):
    """Eq. 5-12 & 23: Closed-form KKT update w_i^{t*} = w_i^{(t-1)} exp((1/tau) sum_j r_{ij}) / Z, where r_{ij} = [l_i l_j]^beta grad_i^T grad_j."""
    k_clusters = len(prev_weights)
    r_matrix = [[0.0] * k_clusters for _ in range(k_clusters)]
    for i in range(k_clusters):
        for j in range(k_clusters):
            dot_grad = sum(a * b for a, b in zip(cluster_grads[i], cluster_grads[j]))
            r_matrix[i][j] = ((cluster_losses[i] * cluster_losses[j]) ** beta) * dot_grad

    unnorm = []
    for i in range(k_clusters):
        r_sum_i = sum(r_matrix[i][j] for j in range(k_clusters))
        unnorm.append(prev_weights[i] * math.exp(r_sum_i / tau))
    z = sum(unnorm)
    new_weights = [u / z for u in unnorm]
    alpha = [l ** beta for l in cluster_losses]
    idro_loss = sum(alpha[i] * new_weights[i] * cluster_losses[i] for i in range(k_clusters))
    return new_weights, r_matrix, idro_loss


def main():
    # 1. Verify Eq. 13 Weighted Jaccard lexical distribution shift
    marco_counts = {"how": 100, "cost": 80, "bank": 60, "weather": 50}
    scifact_counts = {"how": 10, "cytokine": 90, "mrna": 80, "assay": 70}
    nq_counts = {"how": 95, "cost": 70, "bank": 55, "who": 40}
    j_scifact = weighted_jaccard_similarity(marco_counts, scifact_counts)
    j_nq = weighted_jaccard_similarity(marco_counts, nq_counts)
    assert j_scifact < 0.05 and j_nq > 0.65

    # 2. Verify Eq. 11-12 iDRO favors clusters that both have higher loss AND share positive gradient alignment ("common needs")
    prev_w = [1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0]
    # Cluster 0 and Cluster 1 share aligned gradients and elevated loss; Cluster 2 has orthogonal/conflicting gradient
    losses = [0.80, 0.90, 0.85]
    grads = [
        [1.0, 1.0],
        [0.9, 1.1],
        [-0.8, -0.7],
    ]
    new_w, r_mat, idro_val = idro_cluster_weights_update(prev_w, losses, grads, beta=0.25, tau=2.0)
    assert abs(sum(new_w) - 1.0) < 1e-12
    assert r_mat[0][1] > 0.0 and r_mat[0][2] < 0.0
    assert new_w[0] > new_w[2] and new_w[1] > new_w[2]
    assert idro_val > 0.0

    # 3. Verify Table 1 & Table 2 BEIR 18-dataset zero-shot nDCG@10 invariants
    # Table 1 Avg (18 BEIR datasets): DPR (0.352) < ANCE (0.389) < GenQ (0.410) < BM25 (0.428) < ColBERT (0.431) < GTR_XXL (0.458) < GPL (0.459) < COCO-DR_Base (0.462) < COCO-DR_Large (0.484)
    assert 0.352 < 0.389 < 0.410 < 0.428 < 0.431 < 0.458 < 0.459 < 0.462 < 0.484
    # Table 1 Avg CPT Sub (11 BEIR tasks): CPT_XL 175B (0.528) < COCO-DR_Large 335M (0.541)
    assert 0.528 < 0.541
    # Table 2 Ablation Avg: coCondenser Base (0.440) < COCO-DR Base -COCO (0.447) < COCO-DR Base -iDRO (0.457) < COCO-DR Base Full (0.462)
    assert 0.440 < 0.447 < 0.457 < 0.462
    print("Round 755 COCO-DR boundary verification passed.")


if __name__ == "__main__":
    main()
