"""Original arithmetic illustrating configuration-method source boundaries."""
import json
import math


def calculate():
    arithmetic_cost = (1 + 9) / 2
    geometric_cost = math.exp((math.log(1) + math.log(9)) / 2)
    assert arithmetic_cost == 5 and math.isclose(geometric_cost, 3)
    incumbent_all = (1 + 10) / 2
    challenger_common = 6
    incumbent_common = 10
    assert incumbent_all < challenger_common < incumbent_common
    gains, costs = [1, 3], [1, 10]
    no_overhead = [g / c for g, c in zip(gains, costs)]
    with_overhead = [g / (c + 10) for g, c in zip(gains, costs)]
    assert no_overhead[0] > no_overhead[1]
    assert with_overhead[0] < with_overhead[1]
    sizes = [4, 16, 64]
    transformed = [(math.log2(n) - math.log2(4)) / (math.log2(64) - math.log2(4)) for n in sizes]
    assert transformed == [0, .5, 1]
    increasing_loss = [1 - (1 - s) ** 2 for s in [0, .5, 1]]
    assert increasing_loss == [0, .75, 1]
    bmin, bmax, eta, s = 3, 81, 3, 3
    printed_start = bmax / bmin * eta ** -s
    physical_start = bmax * eta ** -s
    assert printed_start == 1 and physical_start == 3
    assert printed_start * eta ** s == 27
    assert physical_start * eta ** s == bmax
    target_loss, trial_loss = 1, 2
    retained = 'target' if target_loss < trial_loss else 'trial'
    assert retained == 'target'
    return dict(smac_cost_aggregation=dict(arithmetic=arithmetic_cost,geometric=geometric_cost),
                blocked_comparison=dict(incumbent_all=incumbent_all,incumbent_common=incumbent_common,challenger_common=challenger_common),
                fabolas_cost_weighting=dict(no_overhead=no_overhead,overhead10=with_overhead),
                fidelity_coordinate=dict(counts=sizes,normalized_log2=transformed),
                unsigned_loss_basis=dict(coefficient=-1,values=increasing_loss),
                dehb_budget_units=dict(printed_start=printed_start,physical_start=physical_start,printed_terminal=27,physical_terminal=81),
                same_budget_selection=dict(target_loss=target_loss,trial_loss=trial_loss,retained=retained))


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
