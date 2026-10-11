"""Original finite boundary examples; not an author implementation or benchmark."""
import json


def fls(reactivate_affected):
    costs = {(0, 0): 2, (1, 0): 3, (0, 1): 1, (1, 1): 0}
    state, active, trace = (0, 0), [True, True], [(0, 0)]
    while any(active):
        for i in range(2):
            if not active[i]:
                continue
            candidate = tuple(1 - x if j == i else x for j, x in enumerate(state))
            if costs[candidate] < costs[state]:
                state = candidate
                trace.append(state)
                active[i] = True
                if reactivate_affected:
                    active = [True, True]
            else:
                active[i] = False
    return {"state": state, "cost": costs[state], "trace": trace,
            "improving_neighbor_remains": any(
                costs[tuple(1 - x if j == i else x for j, x in enumerate(state))] < costs[state]
                for i in range(2))}


def calculate():
    # Maximization: a strict rule cannot cross a flat step to a better value.
    plateau = {"start": 1, "flat": 1, "peak": 2}
    strict_stops = not plateau["flat"] > plateau["start"]
    # Glover/Hao's simple infeasible-state rule uses feasibility improvement
    # as eligibility, then objective quality, not maximum feasibility reduction.
    improving = [("A", 1, 12), ("B", 3, 8)]  # name, violation, cost
    chosen = min((v for v in improving if v[1] < 4), key=lambda v: v[2])
    no_improvement = [("C", 5, 100), ("D", 5, 7), ("E", 6, 0)]
    minimum_violation = min(v[1] for v in no_improvement)
    fallback = min((v for v in no_improvement if v[1] == minimum_violation), key=lambda v: v[2])
    weak, full = fls(False), fls(True)
    assert strict_stops and weak["improving_neighbor_remains"]
    assert not full["improving_neighbor_remains"] and full["cost"] == 0
    assert chosen[0] == "B" and fallback[0] == "D"
    return {"strict_hill_climbing_stops_on_flat_step": strict_stops,
            "fls_incomplete_reactivation": weak, "fls_complete_reactivation": full,
            "oscillation_feasibility_improving_choice": chosen[0],
            "oscillation_minimum_deterioration_choice": fallback[0],
            "interpretation": "Strict ascent cannot traverse this plateau. All FLS bits off does not certify full-neighborhood optimality with incomplete reactivation. The illustrated oscillation rule separates violation-based eligibility from objective ranking. These finite examples establish no global convergence or performance result."}


if __name__ == "__main__":
    print(json.dumps(calculate(), indent=2))
