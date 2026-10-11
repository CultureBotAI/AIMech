"""Small original finite checks; no author implementation, fitting, or benchmark."""
from itertools import product
from math import exp, prod, isclose
import json


def close(a, b):
    assert isclose(a, b, abs_tol=1e-12, rel_tol=1e-12), (a, b)


def field_check():
    states = list(product(range(2), repeat=4))
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    raw = {x: exp(1.1 * sum(x[i] == x[j] for i, j in edges)) for x in states}
    total = sum(raw.values())
    prior = {x: v / total for x, v in raw.items()}
    emission = lambda x, y: prod(.8 if a == b else .2 for a, b in zip(x, y))
    joint = {(x, y): prior[x] * emission(x, y) for x in states for y in states}
    close(sum(joint.values()), 1)
    for x in states:
        close(sum(joint[x, y] for y in states), prior[x])
    observed = (1, 0, 0, 1)
    evidence = sum(joint[x, observed] for x in states)
    posterior = {x: joint[x, observed] / evidence for x in states}
    conditional = []
    for distant in (0, 1):
        selected = {x: v for x, v in posterior.items() if x[1] == x[3] == 1 and x[2] == distant}
        conditional.append(sum(v for x, v in selected.items() if x[0] == 1) / sum(selected.values()))
    close(*conditional)
    mode = max(posterior, key=posterior.get)
    local = {x: v for x, v in posterior.items() if x[1] == mode[1] and x[3] == mode[3]}
    plug_in = sum(v for x, v in local.items() if x[0]) / sum(local.values())
    marginal = sum(v for x, v in posterior.items() if x[0])
    assert abs(plug_in - marginal) > 1e-3
    # Removing all label coupling recovers independent mixture observations.
    iid_evidence = sum((1 / 16) * emission(x, observed) for x in states)
    close(iid_evidence, .5 ** 4)
    return dict(evidence=evidence, local_conditionals=conditional, map_labels=mode,
                exact_site_marginal=marginal, fixed_neighbor_responsibility=plug_in,
                independent_mixture_evidence=iid_evidence)


def tree_check():
    # One root and four leaves: an actual quadtree, with an unobserved root.
    states = list(product(range(2), repeat=5))
    pi = [.7, .3]
    a = [[.65, .35], [.35, .65]]
    y = [None, 0, 0, 0, 1]
    b = [[1., 1.]] + [[.6 if h == obs else .4 for h in range(2)] for obs in y[1:]]
    weights = {x: pi[x[0]] * prod(a[x[0]][x[s]] * b[s][x[s]] for s in range(1, 5)) for x in states}
    evidence = sum(weights.values())
    exact = [sum(w for x, w in weights.items() if x[s]) / evidence for s in range(5)]
    messages = {s: [sum(a[h][k] * b[s][k] for k in range(2)) for h in range(2)] for s in range(1, 5)}
    root = [pi[h] * prod(messages[s][h] for s in range(1, 5)) for h in range(2)]
    close(sum(root), evidence)
    root = [v / evidence for v in root]
    marginals = [root]
    expected_same_edges = 0
    for s in range(1, 5):
        pair = [[root[h] * a[h][k] * b[s][k] / messages[s][h] for k in range(2)] for h in range(2)]
        marginals.append([sum(pair[h][k] for h in range(2)) for k in range(2)])
        expected_same_edges += sum(pair[h][h] for h in range(2))
    for s in range(5):
        close(marginals[s][1], exact[s])
    max_messages = {s: [max(a[h][k] * b[s][k] for k in range(2)) for h in range(2)] for s in range(1, 5)}
    root_mode = max(range(2), key=lambda h: pi[h] * prod(max_messages[s][h] for s in range(1, 5)))
    map_message = (root_mode,) + tuple(max(range(2), key=lambda k: a[root_mode][k] * b[s][k]) for s in range(1, 5))
    map_exact = max(weights, key=weights.get)
    assert map_message == map_exact
    mpm = tuple(int(p > .5) for p in exact)
    assert mpm != map_exact
    theta = expected_same_edges / 4
    assert theta > .5
    assert theta / 2 <= .5  # Extra |Lambda| denominator violates the source's restriction.
    return dict(evidence=evidence, state_one_marginals=exact, joint_map=map_exact,
                marginal_modes=mpm, expected_same_edge_fraction=theta,
                incorrectly_divided_by_state_count=theta / 2)


def ice_check():
    # Two iid Bernoulli(p) trials; first observed as 1, second unobserved.
    # Complete-data estimator p_hat is the sample mean on the closed domain [0,1].
    current = .4
    weights = [1 - current, current]
    estimator = [.5, 1.]
    ice_p = sum(w * h for w, h in zip(weights, estimator))
    em_p = (1 + current) / 2  # Maximizer of expected complete log likelihood.
    close(ice_p, em_p)
    # The invertible coordinate theta=p^2 preserves the exact EM maximizer,
    # but averaging the transformed complete-data estimator does not commute.
    em_theta = em_p ** 2
    ice_theta = sum(w * h * h for w, h in zip(weights, estimator))
    close(em_theta, .49)
    close(ice_theta, .55)
    assert ice_theta != em_theta
    # A second illustration: averaging class means vs expected sufficient statistics.
    average_ratio = .5 * (2 / 1) + .5 * (10 / 2)
    ratio_average = (.5 * 2 + .5 * 10) / (.5 * 1 + .5 * 2)
    close(average_ratio, 3.5)
    close(ratio_average, 4.)
    return dict(current_p=current, ice_p=ice_p, em_p=em_p,
                ice_in_squared_coordinate=ice_theta, em_in_squared_coordinate=em_theta,
                expected_complete_class_mean=average_ratio,
                expected_sum_over_expected_count=ratio_average)


if __name__ == '__main__':
    print(json.dumps(dict(hidden_field=field_check(), hidden_tree=tree_check(),
                         conditional_estimation=ice_check()), indent=2))
