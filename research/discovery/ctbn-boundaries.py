#!/usr/bin/env python3
"""Original bounded CTBN evidence checks; not author code or a theorem prover.

Standard library only. Deterministic Fraction calculations, stdout JSON, no files,
timestamps, external imports or random sampling. State order is lexicographic.
Generator convention: row distributions evolve by p(t) = p(0) exp(t Q).
Finite state spaces and finite, nonnegative off-diagonal rates are assumed.
Each coordinate has exactly one local CIM and cannot be its own parent.
The dynamics graph may contain cycles between different coordinates.
"""

from fractions import Fraction as F
from itertools import product
import json


def matrix(rows):
    return [[F(x) for x in row] for row in rows]


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def multiply(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def row_times(p, q):
    return multiply([p], q)[0]


def validate_generator(q):
    assert q and all(len(row) == len(q) for row in q)
    assert all(sum(row, F(0)) == 0 for row in q)
    assert all(q[i][j] >= 0 for i in range(len(q))
               for j in range(len(q)) if i != j)


def amalgamate(cards, parents, tables):
    """Assemble local jump events; diagonals are derived, never multiplied."""
    assert len(cards) == len(parents) == len(tables)
    assert all(isinstance(n, int) and n > 0 for n in cards)
    for k, pars in enumerate(parents):
        assert len(set(pars)) == len(pars)
        assert all(0 <= p < len(cards) and p != k for p in pars)
        assert set(tables[k]) == set(product(*(range(cards[p]) for p in pars)))
        for q in tables[k].values():
            validate_generator(q)
            assert len(q) == cards[k]
    states = list(product(*(range(n) for n in cards)))
    index = {s: i for i, s in enumerate(states)}
    q = matrix([[0] * len(states) for _ in states])
    for i, state in enumerate(states):
        for k, pars in enumerate(parents):
            local = tables[k][tuple(state[p] for p in pars)][state[k]]
            for value, rate in enumerate(local):
                if value != state[k]:
                    target = list(state)
                    target[k] = value
                    q[i][index[tuple(target)]] += rate
        q[i][i] = -sum(q[i], F(0))
    validate_generator(q)
    return states, q


def pairwise_definition(states, parents, tables):
    """Separate pair-of-states implementation of the paper's p5 formula."""
    result = matrix([[0] * len(states) for _ in states])
    for i, a in enumerate(states):
        for j, b in enumerate(states):
            changed = [k for k in range(len(a)) if a[k] != b[k]]
            if len(changed) == 1:
                k = changed[0]
                result[i][j] = tables[k][tuple(a[p] for p in parents[k])][a[k]][b[k]]
        result[i][i] = -sum(result[i], F(0))
    return result


def event_distribution(state, parents, tables):
    """Guarded current-state competing-event probabilities, no path simulation."""
    events, disabled, local_exits = [], [], []
    for k, pars in enumerate(parents):
        row = tables[k][tuple(state[p] for p in pars)][state[k]]
        exit_rate = -row[state[k]]
        local_exits.append(exit_rate)
        if exit_rate == 0:
            disabled.append(k)
            continue  # no q_ij/q_i division and no candidate destination
        for j, rate in enumerate(row):
            if j != state[k] and rate > 0:
                events.append({"coordinate": k, "destination": j, "rate": rate,
                               "conditional_destination_probability": rate / exit_rate})
    total = sum(local_exits, F(0))
    if total == 0:
        return {"joint_exit_rate": total, "status": "absorbing_joint_state",
                "disabled_coordinates": disabled, "events": [],
                "finite_next_event": False}
    for event in events:
        k = event["coordinate"]
        event["component_selection_probability"] = local_exits[k] / total
        event["probability"] = event["rate"] / total
        assert (event["component_selection_probability"] *
                event["conditional_destination_probability"] == event["probability"])
    assert sum((e["probability"] for e in events), F(0)) == 1
    return {"joint_exit_rate": total, "status": "active_joint_state",
            "disabled_coordinates": disabled, "events": events,
            "finite_next_event": True}


def exp_negative_bounds(x, terms=20):
    """Rational bounds on exp(-x), using a positive exp(x) series and tail.

    After degree N, successive exp(x) tail terms have ratio at most x/(N+2).
    Its geometric bound encloses exp(x); reciprocals reverse the endpoints.
    """
    x = F(x)
    assert x >= 0 and terms + 2 > x
    term, partial = F(1), F(1)
    for k in range(1, terms + 1):
        term *= x / k
        partial += term
    next_term = term * x / (terms + 1)
    tail_upper = next_term / (1 - x / (terms + 2))
    return F(1) / (partial + tail_upper), F(1) / partial


def transition_bounds(q, t, terms=20):
    """Certified entrywise rational bounds via uniformization, not exact expm.

    R=I+Q/nu is stochastic. For every entry, the omitted Poisson-weighted
    R powers are between zero and the omitted Poisson probability mass.
    """
    validate_generator(q)
    t = F(t)
    assert t >= 0
    n, nu = len(q), max(-q[i][i] for i in range(len(q)))
    if nu == 0 or t == 0:
        ident = identity(n)
        return ident, ident, {"nu": nu, "t": t, "terms": 0, "tail_upper": F(0)}
    r = [[F(i == j) + q[i][j] / nu for j in range(n)] for i in range(n)]
    assert all(sum(row, F(0)) == 1 and min(row) >= 0 for row in r)
    power, accum, scalar, weight = identity(n), identity(n), F(1), F(1)
    a = nu * t
    for k in range(1, terms + 1):
        power = multiply(power, r)
        weight *= a / k
        scalar += weight
        accum = [[accum[i][j] + weight * power[i][j] for j in range(n)] for i in range(n)]
    exp_lo, exp_hi = exp_negative_bounds(a, terms + 4)
    tail_upper = max(F(0), 1 - exp_lo * scalar)
    lo = [[exp_lo * x for x in row] for row in accum]
    hi = [[min(F(1), exp_hi * x + tail_upper) for x in row] for row in accum]
    assert all(0 <= lo[i][j] <= hi[i][j] <= 1 for i in range(n) for j in range(n))
    assert all(sum(lo[i], F(0)) <= 1 <= sum(hi[i], F(0)) for i in range(n))
    return lo, hi, {"nu": nu, "t": t, "terms": terms, "tail_upper": tail_upper}


def binary(a, b):
    return matrix([[-a, a], [b, -b]])


def overlap(a, b):
    return max(a[0], b[0]) <= min(a[1], b[1])


def main():
    out = {"role": "original curator-written bounded mathematical evidence checks",
           "arithmetic": "Fractions throughout; transcendental values enclosed by rational intervals",
           "not_claimed": ["author-code replication", "training or benchmark execution",
                           "general theorem proof", "independent scientific approval"]}
    parents = [(1,), (0,)]  # order is (Z,W), matching Example 3.4
    tables = [{(0,): binary(5, 6), (1,): binary(7, 8)},
              {(0,): binary(1, 2), (1,): binary(3, 4)}]
    states, q = amalgamate([2, 2], parents, tables)
    expected = matrix([[-6, 1, 5, 0], [2, -9, 0, 7], [6, 0, -9, 3], [0, 8, 4, -12]])
    assert q == expected == pairwise_definition(states, parents, tables)
    events = [event_distribution(s, parents, tables) for s in states]
    for i, event in enumerate(events):
        assert event["joint_exit_rate"] == -q[i][i]
    out["example_3_4"] = {"locator": "PDF pp4-5, Example3.4 and amalgamation formula",
                          "state_order_Z_W": states, "derived_joint_generator": q,
                          "matches_printed_example_and_pairwise_definition": True,
                          "competing_event_distributions": events}

    # No parent dependence: two independent one-way switches with rates 1 and 2.
    pars = [(), ()]
    tabs = [{(): binary(1, 0)}, {(): binary(2, 0)}]
    states, q = amalgamate([2, 2], pars, tabs)
    assert q[0][3] == 0 and multiply(q, q)[0][3] / 2 == 2
    lo, hi, meta = transition_bounds(q, F(1, 2))
    ea, eb = exp_negative_bounds(F(1, 2)), exp_negative_bounds(F(1))
    closed = ((1 - ea[1]) * (1 - eb[1]), (1 - ea[0]) * (1 - eb[0]))
    assert 0 < lo[0][3] <= hi[0][3] < 1 and overlap((lo[0][3], hi[0][3]), closed)
    out["finite_interval_multiple_changes"] = {
        "state_order": states, "generator": q, "instantaneous_00_to_11_rate": q[0][3],
        "Q_squared_00_to_11": multiply(q, q)[0][3], "quadratic_series_coefficient": F(2),
        "time": F(1, 2), "uniformization_probability_bounds": [lo[0][3], hi[0][3]],
        "closed_form": "(1-exp(-t))*(1-exp(-2*t))",
        "closed_form_bounds": closed, "bounds_overlap": True, "calculation": meta,
        "interpretation": "A positive finite interval can contain sequential coordinate changes; a zero direct generator entry forbids only their single simultaneous jump."}

    # Parent U can enable a currently disabled child X; both eventually absorb.
    pars = [(), (0,)]
    tabs = [{(): binary(1, 0)}, {(0,): binary(0, 0), (1,): binary(2, 0)}]
    states, q = amalgamate([2, 2], pars, tabs)
    before, enabled, absorbed = (event_distribution(states[i], pars, tabs) for i in (0, 2, 3))
    assert before["joint_exit_rate"] == 1 and before["disabled_coordinates"] == [1]
    assert enabled["joint_exit_rate"] == 2 and enabled["disabled_coordinates"] == [0]
    assert absorbed["joint_exit_rate"] == 0 and not absorbed["finite_next_event"]
    lo, hi, meta = transition_bounds(q, F(1, 2))
    assert lo[0][3] > 0 and lo[3][3] <= 1 <= hi[3][3]
    zero = matrix([[0, 0], [0, 0]])
    zero_lo, zero_hi, zero_meta = transition_bounds(zero, F(100))
    assert zero_lo == zero_hi == identity(2)
    out["zero_exit_boundaries"] = {
        "state_order_U_X": states, "generator": q,
        "initially_disabled_child": before, "after_parent_switch": enabled,
        "absorbing_joint_state": absorbed, "finite_time_00_to_11_bounds": [lo[0][3], hi[0][3]],
        "calculation": meta, "all_zero_generator_transition": zero_lo,
        "all_zero_calculation": zero_meta,
        "interpretation": "Skip zero-rate local destination normalization; if the total joint exit rate is zero, stop rather than divide by zero or draw a finite exponential holding time. A local zero rate may change after a parent event."}

    # Empty dynamics graph, strictly positive independent flip rates, correlated P0.
    pars = [(), ()]
    tabs = [{(): binary(1, 1)}, {(): binary(1, 1)}]
    states, q = amalgamate([2, 2], pars, tabs)
    p0 = [F(3, 8), F(1, 8), F(1, 8), F(3, 8)]
    u = [F(1, 4)] * 4
    d = [p0[i] - u[i] for i in range(4)]
    assert min(p0) > 0 and row_times(u, q) == [0] * 4
    assert row_times(d, q) == [-4 * x for x in d]
    assert all(sum(d[i] for i, s in enumerate(states) if s[k] == v) == 0
               for k in range(2) for v in range(2))
    cov0 = p0[0] - F(1, 4)
    lo, hi, meta = transition_bounds(q, F(1, 4))
    p_lo, p_hi = row_times(p0, lo), row_times(p0, hi)
    exp_lo, exp_hi = exp_negative_bounds(F(1))
    analytic_cov = (exp_lo / 8, exp_hi / 8)
    numeric_cov = (p_lo[0] - F(1, 4), p_hi[0] - F(1, 4))
    assert cov0 == F(1, 8) and numeric_cov[0] > 0 and overlap(analytic_cov, numeric_cov)
    out["correlated_initial_law_counterexample"] = {
        "locator": "PDF p4 Definition3.2; p5 Definitions3.7-3.8 and Theorem3.9",
        "dynamics_graph": "two nodes, no edges", "state_order": states,
        "generator": q, "initial_distribution_full_support": p0,
        "time_zero_marginal_product_for_00": F(1, 4), "time_zero_joint_00": p0[0],
        "time_zero_covariance_of_zero_indicators": cov0,
        "uniform_product_initial_law_stationary": u,
        "centered_initial_law": d, "centered_mode_left_eigenvalue": -4,
        "exact_solution": "p(t) = (1/4,1/4,1/4,1/4) + exp(-4*t)*(1/8,-1/8,-1/8,1/8)",
        "each_one_time_marginal": [F(1, 2), F(1, 2)],
        "indicator_covariance_formula": "exp(-4*t)/8, strictly positive for every finite t>=0",
        "time": F(1, 4), "analytic_covariance_bounds": analytic_cov,
        "uniformization_covariance_bounds": numeric_cov, "bounds_overlap": True,
        "calculation": meta,
        "interpretation": "The p5 trajectory independence statement does not follow from the dynamics graph alone with the arbitrary initial BN allowed by Definition3.2. This example already violates independence at t=0, and also at positive time; it supplies no replacement general conditional-independence theorem."}

    # A valid finite CTMC can permit a simultaneous two-coordinate transition.
    simultaneous = matrix([[-1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    validate_generator(simultaneous)
    assert sum(a != b for a, b in zip(states[0], states[3])) == 2 and simultaneous[0][3] > 0
    out["continuous_time_alone_does_not_exclude_joint_jumps"] = {
        "state_order": states, "valid_finite_generator_outside_CTBN_single_coordinate_class": simultaneous,
        "interpretation": "The zero simultaneous-change rate is a CTBN structural restriction, not a consequence of continuous time alone."}

    # Printed background inconsistencies are retained, not silently adopted.
    qb = matrix([[F(-21, 100), F(1, 5), F(1, 100)],
                 [F(1, 20), F(-1, 10), F(1, 20)],
                 [F(1, 100), F(1, 5), F(-21, 100)]])
    embedded = [[F(0) if i == j else qb[i][j] / -qb[i][i] for j in range(3)] for i in range(3)]
    printed_embedded = matrix([[0, F(20, 21), F(1, 21)], [F(1, 2), 0, F(1, 2)], [F(20, 21), F(1, 21), 0]])
    printed_reconstructed = [[-qb[i][i] * (printed_embedded[i][j] - F(i == j)) for j in range(3)] for i in range(3)]
    derived_reconstructed = [[-qb[i][i] * (embedded[i][j] - F(i == j)) for j in range(3)] for i in range(3)]
    assert qb == derived_reconstructed and qb != printed_reconstructed
    # p9 Example5.2: h solves (-U)h=1, so initial mean is p0*h.
    minus_u = matrix([[4, -1], [-2, 7]])
    h = [F(4, 13), F(3, 13)]
    assert multiply(minus_u, [[x] for x in h]) == [[1], [1]]
    mean = sum(h, F(0)) / 2
    assert mean == F(7, 26) and 1 / mean == F(26, 7)
    out["printed_background_inconsistencies"] = {
        "pdf2_example2_2": {"original_Q": qb, "derived_embedded_chain": embedded,
                            "printed_embedded_chain": printed_embedded,
                            "printed_expression_reconstructs": printed_reconstructed,
                            "mismatch_rows_zero_based": [2]},
        "pdf3_two_time_joint": {"correct_row_convention_formula": "J_ij(s,t)=p_i(s)*[exp((t-s)*Q)]_ij",
                                "printed_row_vector_product": "p(s)*exp((t-s)*Q) is the marginal p(t), not the two-time joint matrix"},
        "pdf9_example5_2": {"minus_subsystem_generator": minus_u, "statewise_mean_exit_times": h,
                            "initial_subsystem_distribution": [F(1, 2), F(1, 2)],
                            "mean_holding_time": mean, "reciprocal_holding_intensity": 1 / mean,
                            "interpretation": "The displayed P0*(-U)^(-1)*1 is a time; the following example uses its reciprocal as an intensity. Singular/non-exitable subsystems require a separate treatment."}}
    print(json.dumps(out, indent=2, default=lambda x: str(x) if isinstance(x, F) else x))


if __name__ == "__main__":
    main()
