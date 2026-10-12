"""Exact finite checks of NNDD definitions; not a historical implementation benchmark."""
from fractions import Fraction as F
import itertools
import json


def accepted(reference, query, k, threshold, r=1):
    """Sorted reference distances, self included; missing distances are infinite."""
    assert k >= 1 and threshold >= 0
    if len(reference) < k:
        return False
    ds = sorted(abs(query - p) for p in reference)[:k]
    if r == 'infinity':
        return max(ds) <= threshold
    assert isinstance(r, int) and r >= 1
    return sum(d ** r for d in ds) <= threshold ** r


def consistent(full, subset, k, threshold, r=1):
    assert set(subset) <= set(full)
    return all(accepted(full, p, k, threshold, r) ==
               accepted(subset, p, k, threshold, r) for p in full)


def greedy_k1(order, threshold):
    """CNNDD's k=1 specialization: every inserted point is self-accepted."""
    chosen = []
    for p in order:
        if not accepted(chosen, p, 1, threshold):
            chosen.append(p)
    return chosen


def main():
    d = [F(0), F(1)]
    s = [F(0)]
    assert consistent(d, s, 1, F(1))
    assert accepted(d, F(2), 1, F(1))
    assert not accepted(s, F(2), 1, F(1))
    # A future normal point at2 is lost; an abnormal point there is now rejected.
    assert all(accepted(d, p, 1, F(0)) for p in d)
    assert not accepted(d, F(1, 2), 1, F(0))

    full = [F(0), F(2)]
    assert all(not accepted(full, p, 2, F(1)) for p in full)
    assert consistent(full, [F(0)], 2, F(1))
    assert not accepted([F(0)], F(0), 2, F(1))
    # Original rejections can be preserved; consistency does not mean all accepted.
    # Section4 retains every full-reference rejected observation, so in this
    # case its output has2 points even though a one-point subset is consistent.

    a = greedy_k1([F(0), F(1), F(2)], F(1))
    b = greedy_k1([F(1), F(0), F(2)], F(1))
    assert a == [F(0), F(2)] and b == [F(1)]
    assert consistent([F(0), F(1), F(2)], a, 1, F(1))
    assert consistent([F(0), F(1), F(2)], b, 1, F(1))
    assert accepted(a, F(3), 1, F(1)) and not accepted(b, F(3), 1, F(1))

    ref = [F(3, 5), F(4, 5)]
    norm_decisions = [accepted(ref, F(0), 2, F(1), r) for r in [1, 2, 'infinity']]
    assert norm_decisions == [False, True, True]
    for subset_size in range(4):
        for subset in itertools.combinations([F(0), F(1), F(3)], subset_size):
            for query in [F(-1), F(0), F(1, 2), F(1), F(2), F(3), F(4)]:
                for k in [1, 2, 3]:
                    for r in [1, 2, 'infinity']:
                        if accepted(subset, query, k, F(2), r):
                            assert accepted([F(0), F(1), F(3)], query, k, F(2), r)
    # The printed arbitrary-k dominating-set reduction needs care: a complete
    # three-vertex graph has a dominating singleton, but k=2 infinity padding
    # makes every singleton reference reject every vertex. Its full-reference
    # distances0,1 meet threshold sqrt(5) at r=2. Compare squared values exactly.
    assert F(0) ** 2 + F(1) ** 2 <= F(5)
    assert all(not accepted([p], q, 2, F(3)) for p in [0, 1, 2] for q in [0, 1, 2])

    # The later PDD correspondence holds on D for r=infinity, not all queries.
    # For D={0,2}, k=2, theta=2, both prototype radii are2. Their accepted
    # balls have radius0. NNDD nevertheless accepts midpoint1 (both distances1).
    assert all(accepted([F(0), F(2)], p, 2, F(2), 'infinity') for p in [F(0), F(2)])
    assert accepted([F(0), F(2)], F(1), 2, F(2), 'infinity')
    assert not any(abs(F(1)-p)+F(2) <= F(2) for p in [F(0), F(2)])
    result = dict(
        consistent_subset_can_change_unseen_decision=True,
        consistency_can_preserve_original_rejections=True,
        insufficient_references_reject_even_self=True,
        greedy_k1_subsets=[[str(x) for x in a], [str(x) for x in b]],
        greedy_output_is_order_dependent_and_not_always_minimum=True,
        distance_vector=['3/5', '4/5'], threshold='1',
        l1_l2_linfinity_decisions=norm_decisions,
        checked_subset_acceptance_is_contained_in_full_acceptance=True,
        arbitrary_k_reduction_requires_more_than_dominating_singleton=True,
        later_pdd_training_equivalence_is_not_global_equivalence=True,
        scope='Exact finite definition checks and the k=1 specialization only; no historical code, fitted statistical model, timing or benchmark reproduction.'
    )
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
