"""Original finite arithmetic for source boundaries, not trained models or proofs."""
from math import isclose
import json

def calculate():
    alpha = 0.1
    features = [1.0, 2.0]
    initial = 1.0
    outcome = 3.0
    predictions = [initial * x for x in features] + [outcome]
    fixed = {}
    for lam in [0.0, 0.5, 1.0]:
        trace = 0.0
        increment = 0.0
        for i, x in enumerate(features):
            trace = x + lam * trace
            increment += alpha * (predictions[i + 1] - predictions[i]) * trace
        fixed[str(lam)] = initial + increment
    supervised_fixed = initial + alpha * sum((outcome - initial*x)*x for x in features)
    assert isclose(fixed['1.0'], supervised_fixed)
    assert isclose(fixed['0.0'], 1.3) and isclose(fixed['0.5'], 1.35)
    online, trace = initial, 0.0
    for i, x in enumerate(features):
        trace = x + trace
        next_prediction = online*features[i+1] if i+1 < len(features) else outcome
        online += alpha*(next_prediction-online*x)*trace
    assert isclose(online, 1.34) and not isclose(online, supervised_fixed)
    current, reward, discount, rate = 1.0, 2.0, 0.9, 0.25
    next_values = [2.0, 8.0]
    selected = 0
    backup = lambda continuation: current + rate*(reward+discount*continuation-current)
    sarsa = backup(next_values[selected])
    qlearning = backup(max(next_values))
    expected = backup(0.75*next_values[0] + 0.25*next_values[1])
    terminal = backup(0.0)
    assert isclose(sarsa, 1.7) and isclose(qlearning, 3.05)
    assert isclose(expected, 2.0375) and isclose(terminal, 1.25)
    old, queue, transmission, eta = 10.0, 2.0, 1.0, 0.5
    neighbor_values = [4.0, 9.0]
    route_backup = lambda t: old+eta*(queue+transmission+t-old)
    routed = route_backup(min(neighbor_values))
    assert isclose(routed, 8.5) and isclose(route_backup(max(neighbor_values)), 11.0)
    assert not isclose(routed, old+eta*(transmission+min(neighbor_values)-old))
    stale = [5.0, 20.0]
    actual_costs = [5.0, 1.0]
    selected_history = []
    for _ in range(10):
        action = min(range(2), key=lambda a: stale[a])
        selected_history.append(action)
        stale[action] += eta*(actual_costs[action]-stale[action])
    assert stale == [5.0, 20.0] and selected_history == [0]*10
    return dict(td_fixed_sequence_weights=fixed,td1_supervised_fixed=supervised_fixed,
                td1_online_consistent_weights=online,sarsa_selected_target=sarsa,
                qlearning_maximum_target=qlearning,expected_policy_target=expected,
                sarsa_terminal=terminal,qroute_minimum_cost_backup=routed,
                qroute_incorrect_maximum_backup=route_backup(max(neighbor_values)),
                greedy_unused_alternative=stale,
                interpretation='Fixed-weight equality does not imply equal online trajectories. Selected, maximum and expected action backups differ. Local cost backups include queue delay and use a minimum. An unused overestimated alternative can remain stale under greedy updating. These are finite examples, not convergence proofs or routing benchmarks.')

if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
