#!/usr/bin/env python3
"""Constructed boundary verification for CEDR (MacAvaney et al., SIGIR 2019, arXiv:1904.07094).

Verifies:
1. Multi-layer contextualized similarity tensor S_{Q,D}[l, q, d] = cos(context_{Q,D}(q, l), context_{Q,D}(d, l))
   in R^{L x |Q| x |D|} (Section 2.2, Eq. 1).
2. Sense disambiguation for identical surface tokens: when q and d share the same surface word
   (e.g., "curb" = restrain vs. "curb" = street edge, Figure 1), static embeddings give cos = 1.0
   for both relevant and non-relevant occurrences, whereas contextualized layer representations yield
   distinct similarity scores (< 1.0) that separate the relevant sense from the off-topic sense.
3. Joint CEDR-KNRM integration (Section 2.3): multi-layer RBF kernel pooling log-counts concatenated
   with BERT's [CLS] classification vector outperform non-CEDR multi-layer kernel pooling alone.
"""

from __future__ import annotations

import math


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def norm(a: list[float]) -> float:
    return math.sqrt(dot(a, a))


def cosine_sim(a: list[float], b: list[float]) -> float:
    return dot(a, b) / (norm(a) * norm(b))


def build_contextualized_similarity_tensor(
    q_layer_embs: list[list[list[float]]],
    d_layer_embs: list[list[list[float]]],
) -> list[list[list[float]]]:
    """Implements Eq. (1): S_{Q,D}[l, i, j] = cos(context(q_i, l), context(d_j, l))."""
    assert len(q_layer_embs) == len(d_layer_embs)
    tensor: list[list[list[float]]] = []
    for q_embs_l, d_embs_l in zip(q_layer_embs, d_layer_embs):
        mat_l = [[cosine_sim(q_vec, d_vec) for d_vec in d_embs_l] for q_vec in q_embs_l]
        tensor.append(mat_l)
    return tensor


def knrm_multi_layer_features(
    sim_tensor: list[list[list[float]]],
    mus: list[float],
    sigmas: list[float],
) -> list[float]:
    """Computes KNRM soft-TF log-kernel-pooled features across each layer l in 1..L (Sections 2.2-2.3)."""
    features: list[float] = []
    for mat_l in sim_tensor:
        for mu, sigma in zip(mus, sigmas):
            q_sum = 0.0
            for q_row in mat_l:
                kernel_sum = sum(math.exp(-((s - mu) ** 2) / (2.0 * (sigma ** 2))) for s in q_row)
                q_sum += math.log(max(kernel_sum, 1e-12))
            features.append(q_sum)
    return features


def cedr_knrm_score(
    sim_tensor: list[list[list[float]]],
    cls_vec: list[float],
    mus: list[float],
    sigmas: list[float],
    w_kernels: list[float],
    w_cls: list[float],
) -> tuple[float, float]:
    """Returns (non_cedr_score, cedr_joint_score) by concatenating [CLS] with multi-layer kernel signals."""
    k_feats = knrm_multi_layer_features(sim_tensor, mus, sigmas)
    non_cedr = dot(w_kernels, k_feats)
    cedr_joint = dot(w_kernels + w_cls, k_feats + cls_vec)
    return non_cedr, cedr_joint


def main() -> None:
    # Query Q = ["curb", "population", "growth"] (Robust04 query 435, Figure 1)
    # Static GloVe gives identical vector for "curb" regardless of sense -> cos("curb", "curb") == 1.0!
    glove_curb = [1.0, 0.0, 0.0]
    assert abs(cosine_sim(glove_curb, glove_curb) - 1.0) < 1e-12

    # L = 2 contextualized layers:
    # Query embeddings across L = 2 layers (sense 1: restrain population growth)
    q_layers = [
        [[0.90, 0.35, 0.10], [0.20, 0.90, 0.25], [0.25, 0.85, 0.30]],  # Layer 1
        [[0.92, 0.38, 0.05], [0.15, 0.94, 0.20], [0.20, 0.88, 0.28]],  # Layer 2
    ]
    # Relevant document D+ ("attempts to curb population growth"):
    d_pos_layers = [
        [[0.85, 0.42, 0.15], [0.22, 0.88, 0.28], [0.28, 0.82, 0.32]],
        [[0.88, 0.44, 0.08], [0.18, 0.91, 0.22], [0.22, 0.86, 0.30]],
    ]
    cls_pos = [0.85, 0.75]

    # Non-relevant document D- ("citywide street curb construction"):
    # Notice "curb" here has the street-edge sense, shifting its contextualized vector away from q's "curb"!
    d_neg_layers = [
        [[0.20, -0.30, 0.92], [0.10, 0.15, 0.95], [0.05, 0.20, 0.90]],
        [[0.15, -0.35, 0.94], [0.08, 0.12, 0.96], [0.04, 0.18, 0.92]],
    ]
    cls_neg = [-0.60, -0.50]

    s_pos = build_contextualized_similarity_tensor(q_layers, d_pos_layers)
    s_neg = build_contextualized_similarity_tensor(q_layers, d_neg_layers)

    # Verify Eq. (1) sense disambiguation: even for identical word "curb" (index 0, 0),
    # similarity is < 1.0 and is much higher in relevant context than street-construction context:
    sim_curb_pos_l2 = s_pos[1][0][0]
    sim_curb_neg_l2 = s_neg[1][0][0]
    assert sim_curb_neg_l2 < sim_curb_pos_l2 < 1.0

    # Verify CEDR-KNRM joint scoring (Section 2.3):
    mus = [1.0, 0.7]
    sigmas = [0.1, 0.2]
    w_kernels = [0.25, 0.20, 0.30, 0.25]  # 2 layers x 2 kernels
    w_cls = [0.60, 0.50]

    non_cedr_pos, cedr_pos = cedr_knrm_score(s_pos, cls_pos, mus, sigmas, w_kernels, w_cls)
    non_cedr_neg, cedr_neg = cedr_knrm_score(s_neg, cls_neg, mus, sigmas, w_kernels, w_cls)

    assert non_cedr_pos > non_cedr_neg
    assert (cedr_pos - cedr_neg) > (non_cedr_pos - non_cedr_neg)

    print(
        f"[PASS] CEDR boundaries verified: sim_curb_pos={sim_curb_pos_l2:.4f} > sim_curb_neg={sim_curb_neg_l2:.4f}, "
        f"cedr_margin={cedr_pos - cedr_neg:.4f} > non_cedr_margin={non_cedr_pos - non_cedr_neg:.4f}"
    )


if __name__ == "__main__":
    main()
