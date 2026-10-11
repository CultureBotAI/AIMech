"""Original finite arithmetic for CTAugment source conventions; no model or author code."""
from fractions import Fraction as F
import json


def calculate():
    probabilities = [F(1, 5), F(4, 5)] + [F(0)] * 8
    target = [F(1)] + [F(0)] * 9
    distance = sum(abs(q - y) for q, y in zip(probabilities, target))
    paper_score = 1 - distance / (2 * len(probabilities))
    implementation_score = 1 - distance / 2
    assert paper_score == F(23, 25)
    assert implementation_score == probabilities[0] == F(1, 5)
    # For any valid L-class distribution, the printed score is at least 1 - 1/L.
    # Initial weight 1 and convex EMA updates preserve this lower bound.
    lower_bound = 1 - F(1, len(probabilities))
    threshold = F(4, 5)
    assert lower_bound > threshold
    # The pinned implementation thresholds smoothed, max-normalized node weights,
    # then samples intervals weighted by the sum of their endpoints.
    weights = [F(1, 2), F(1), F(1, 2)]
    smoothed = [w + F(1, 100) for w in weights]
    relative = [w / max(smoothed) for w in smoothed]
    retained = [w if w >= threshold else F(0) for w in relative]
    intervals = [retained[i] + retained[i + 1] for i in range(2)]
    interval_probabilities = [w / sum(intervals) for w in intervals]
    assert retained == [0, 1, 0]
    assert interval_probabilities == [F(1, 2), F(1, 2)]
    return {
        'scope': 'Curator arithmetic only; not training, a performance test, or author-issued errata.',
        'ten_class_feedback': {'true_class_probability': str(probabilities[0]),
                              'l1_distance': str(distance),
                              'printed_paper_score': str(paper_score),
                              'pinned_code_score': str(implementation_score),
                              'paper_score_lower_bound': str(lower_bound),
                              'raw_paper_cutoff': str(threshold)},
        'interval_sampling': {'original_node_weights': list(map(str, weights)),
                              'retained_relative_weights': list(map(str, retained)),
                              'interval_probabilities': list(map(str, interval_probabilities)),
                              'interpretation': 'Both adjacent intervals remain selectable even though the outer node weights were zeroed.'}}


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
