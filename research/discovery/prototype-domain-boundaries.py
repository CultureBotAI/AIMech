"""Exact source-boundary traces for PDD/CPDD; not historical code or a benchmark."""
from fractions import Fraction as F
import json


def prototypes(data, k, theta):
    assert 1 <= k <= len(data)
    radii = [sorted(abs(x-y) for y in data)[k-1] for x in data]
    return {i: r for i, r in enumerate(radii) if r <= theta}


def neighborhoods(data, ps, theta, rho=F(1)):
    return {i: {j for j, y in enumerate(data) if abs(data[i]-y)+r <= rho*theta}
            for i, r in ps.items()}


def prediction(data, ps, selected, query, theta):
    return any(abs(data[i]-query)+ps[i] <= theta for i in selected)


def main():
    data = [F(0), F(2)]
    ps = prototypes(data, 2, F(2))
    assert ps == {0: F(2), 1: F(2)}
    assert all(prediction(data, ps, ps, q, F(2)) for q in data)
    assert not prediction(data, ps, ps, F(1), F(2))
    assert max(abs(F(1)-x) for x in data) <= F(2)  # NNDD infinity accepts.
    cover = neighborhoods(data, ps, F(2))
    assert cover == {0: {0}, 1: {1}}
    covered = set(ps)
    assert len(covered) <= len(ps)  # The printed Figure1 guard still holds.
    assert max(len(v-covered) for v in cover.values()) == 0
    shrunk = neighborhoods(data, ps, F(2), F(3, 4))
    assert all(not v for v in shrunk.values())  # Full eligible coverage infeasible.

    # A positive coverage goal with eta<1 can stop before all prototypes are
    # covered; such a result is not automatically a consistent subset.
    assert F(1) >= F(1, 2)*len(ps)
    assert not prediction(data, ps, [0], data[1], F(2))

    # Trace a single Figure3 iteration with its whole candidate sample T=D.
    # This isolates Theorem5.1's proposed Dprime-exhaustion stopping change.
    data = [F(0), F(1, 10), F(10), F(101, 10)]
    theta = F(1, 5)
    ps = prototypes(data, 1, theta)
    cover = neighborhoods(data, ps, theta)
    current_sample = set(range(len(data)))
    candidate_pool = set(ps)
    covered = set()
    chosen = min(candidate_pool, key=lambda i: (-len(cover[i]-covered), ps[i], i))
    gain = len(cover[chosen]-covered)
    assert gain == 2 > 0
    selected = {chosen}
    covered |= cover[chosen]
    assert chosen in current_sample  # The printed inner loop ends here.
    remaining = set(range(len(data))) - (current_sample | covered)
    assert not remaining
    assert len(covered) == 2 < len(ps)
    assert any(not prediction(data, ps, selected, x, theta) for x in data)
    # count=countstar=2 makes the log-ratio update well-defined and equal to1;
    # failure of coverage here is independent of the logzero/logone issue.
    assert gain > 1

    # Distinct unrelated boundary: all isolated k1 neighborhoods have gain1,
    # so an initial count=countstar=1 makes log(count)/log(countstar)=0/0.
    isolated = [F(0), F(10)]
    isolated_ps = prototypes(isolated, 1, F(1))
    assert {len(v) for v in neighborhoods(isolated, isolated_ps, F(1)).values()} == {1}

    print(json.dumps(dict(
        pdd_and_infinity_nndd_agree_on_reference_but_not_midpoint=True,
        printed_cpdd_guard_remains_true_at_full_coverage=True,
        shrunken_cover_can_leave_all_eligible_prototypes_uncoverable=True,
        partial_coverage_is_not_full_consistency=True,
        fast_cpdd_exhaustion_trace=dict(sample_size=4,selected_indices=sorted(selected),covered_indices=sorted(covered),remaining_indices=sorted(remaining),positive_gain=gain,uncovered_reference_count=len(ps)-len(covered)),
        dprime_exhaustion_alone_does_not_guarantee_consistency=True,
        unit_gain_log_ratio_is_undefined=True,
        scope='Finite rational source-boundary calculations and one declared pseudocode iteration; no historical implementation, learned model or benchmark executed.'
    ),indent=2))


if __name__ == '__main__':
    main()
