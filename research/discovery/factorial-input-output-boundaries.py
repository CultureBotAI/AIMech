"""Original finite probability checks; no author code, training or benchmark."""
import itertools
import json
import math


def normalize(weights):
    total = sum(weights)
    assert total > 0
    return [w / total for w in weights]


def gaussian(y, mean, variance):
    return math.exp(-0.5 * (y - mean) ** 2 / variance) / math.sqrt(2 * math.pi * variance)


paths = list(itertools.product(range(2), repeat=3))
priors = [[0.6, 0.4], [0.35, 0.65]]
transitions = [[[0.85, 0.15], [0.25, 0.75]], [[0.7, 0.3], [0.1, 0.9]]]
weights = [[-0.8, 0.9], [-0.4, 0.7]]
observations = [0.1, 0.7, -0.2]
variance = 0.8


def path_prior(m, path):
    return priors[m][path[0]] * math.prod(transitions[m][path[t-1]][path[t]] for t in range(1, 3))


joint = [[path_prior(0, a) * path_prior(1, b) * math.prod(
    gaussian(observations[t], weights[0][a[t]] + weights[1][b[t]], variance)
    for t in range(3)) for b in paths] for a in paths]
likelihood = sum(map(sum, joint))
posterior = [[v / likelihood for v in row] for row in joint]
marginals = [[sum(row) for row in posterior], [sum(row[j] for row in posterior) for j in range(8)]]
dependence = max(abs(posterior[i][j] - marginals[0][i] * marginals[1][j]) for i in range(8) for j in range(8))
states = list(itertools.product(range(2), repeat=2))
alpha = [priors[0][a] * priors[1][b] * gaussian(observations[0], weights[0][a] + weights[1][b], variance) for a, b in states]
for t in range(1, 3):
    alpha = [gaussian(observations[t], weights[0][a] + weights[1][b], variance) * sum(
        alpha[k] * transitions[0][c][a] * transitions[1][d][b] for k, (c, d) in enumerate(states)) for a, b in states]
assert abs(sum(alpha) - likelihood) < 1e-14

q = [[path_prior(m, path) for path in paths] for m in range(2)]


def elbo():
    return sum(q[0][i] * q[1][j] * (math.log(joint[i][j]) - math.log(q[0][i]) - math.log(q[1][j])) for i in range(8) for j in range(8))


bound_values = [elbo()]
unary_error = 0.0
for _ in range(5):
    for m in range(2):
        other = 1 - m
        mean_other = [sum(q[other][j] * weights[other][p[t]] for j, p in enumerate(paths)) for t in range(3)]
        unary = [[math.exp(weights[m][s] * (observations[t] - mean_other[t]) / variance - 0.5 * weights[m][s] ** 2 / variance) for s in range(2)] for t in range(3)]
        update = normalize([path_prior(m, p) * math.prod(unary[t][p[t]] for t in range(3)) for p in paths])
        generic = normalize([math.exp(sum(q[other][j] * math.log(joint[i][j] if m == 0 else joint[j][i]) for j in range(8))) for i in range(8)])
        unary_error = max(unary_error, max(abs(a-b) for a, b in zip(update, generic)))
        q[m] = update
        bound_values.append(elbo())
        assert bound_values[-1] >= bound_values[-2] - 1e-12
kl = sum(q[0][i] * q[1][j] * math.log(q[0][i] * q[1][j] / posterior[i][j]) for i in range(8) for j in range(8))
assert abs(math.log(likelihood) - elbo() - kl) < 1e-12
assert unary_error < 1e-12
temporal = [[sum(q[0][k] for k, p in enumerate(paths) if p[0] == a and p[1] == b) for b in range(2)] for a in range(2)]
temporal_dependence = abs(temporal[0][0] - sum(temporal[0]) * sum(row[0] for row in temporal))
assert dependence > 0.01 and temporal_dependence > 0.001

# Euclidean orthogonality is insufficient for an unequal diagonal covariance.
v, w, precisions = [1, 1], [1, -1], [1, 0.5]
ordinary_dot = sum(a*b for a, b in zip(v, w))
precision_dot = sum(a*b*c for a, b, c in zip(v, w, precisions))
orthogonal_joint = normalize([math.exp(-0.5 * sum(precisions[d] * (a*v[d]+b*w[d])**2 for d in range(2))) for a, b in states])
orthogonal_gap = abs(orthogonal_joint[0] - (orthogonal_joint[0]+orthogonal_joint[1]) * (orthogonal_joint[0]+orthogonal_joint[2]))
assert ordinary_dot == 0 and precision_dot == 0.5 and orthogonal_gap > 0.001

# Input-conditioned chain, with transitions indexed [previous][current].
inputs = [0, 1, 0]
input_transitions = [[[0.8, 0.2], [0.3, 0.7]], [[0.2, 0.8], [0.6, 0.4]]]
emission_one = [[0.15, 0.75], [0.65, 0.25]]
io_paths = list(itertools.product(range(2), repeat=4))


def io_joint(path, output, observed=(0, 1, 2)):
    return priors[0][path[0]] * math.prod(input_transitions[u][path[t]][path[t+1]] * (
        (emission_one[u][path[t+1]] if output[t] else 1-emission_one[u][path[t+1]]) if t in observed else 1)
        for t, u in enumerate(inputs))


outputs = list(itertools.product(range(2), repeat=3))
output_probabilities = [sum(io_joint(p, y) for p in io_paths) for y in outputs]
assert abs(sum(output_probabilities) - 1) < 1e-12
y = (1, 0, 1)
observed_weights = [io_joint(p, y) for p in io_paths]
io_likelihood = sum(observed_weights)
state = priors[0][:]
forward = priors[0][:]
alphas = [forward[:]]
for t, u in enumerate(inputs):
    state = [sum(state[j] * input_transitions[u][j][i] for j in range(2)) for i in range(2)]
    forward = [sum(forward[j] * input_transitions[u][j][i] for j in range(2)) * (emission_one[u][i] if y[t] else 1-emission_one[u][i]) for i in range(2)]
    alphas.append(forward[:])
assert abs(sum(forward) - io_likelihood) < 1e-12
beta = [[0.0, 0.0] for _ in range(3)]
for t in reversed(range(3)):
    for i in range(2):
        emission = emission_one[inputs[t]][i] if y[t] else 1-emission_one[inputs[t]][i]
        beta[t][i] = emission * (1 if t == 2 else sum(input_transitions[inputs[t+1]][i][j] * beta[t+1][j] for j in range(2)))
pair_error = 0.0
for t, u in enumerate(inputs):
    for j, i in states:
        calculated = alphas[t][j] * input_transitions[u][j][i] * beta[t][i] / io_likelihood
        enumerated = sum(v for p, v in zip(io_paths, observed_weights) if p[t] == j and p[t+1] == i) / io_likelihood
        pair_error = max(pair_error, abs(calculated - enumerated))
assert pair_error < 1e-12
filtered = normalize(forward)
input_only_gap = max(abs(a-b) for a, b in zip(state, filtered))
missing_probability = sum(io_joint(p, y, observed=(2,)) for p in io_paths)
assert abs(missing_probability - sum(v for out, v in zip(outputs, output_probabilities) if out[2] == 1)) < 1e-12

# Special table update: two steps, shared input symbol, observed final state 0.
a = input_transitions[0]
short_paths = list(itertools.product(range(2), repeat=3))
raw = [priors[0][p[0]] * a[p[0]][p[1]] * a[p[1]][p[2]] * (p[2] == 0) for p in short_paths]
counts = [[sum(v * sum(p[t] == j and p[t+1] == i for t in range(2)) for p, v in zip(short_paths, raw)) / sum(raw) for i in range(2)] for j in range(2)]
updated = [normalize(row) for row in counts]
missing_old_factor = [normalize([counts[j][i]/a[j][i] for i in range(2)]) for j in range(2)]
table_gap = max(abs(updated[j][i]-missing_old_factor[j][i]) for j, i in states)
assert table_gap > 0.01

result = dict(fhmm_likelihood=likelihood, exact_forward_error=abs(sum(alpha)-likelihood), posterior_chain_dependence=dependence, structured_unary_update_error=unary_error, elbo_values=bound_values, final_kl=kl, bound_identity_error=abs(math.log(likelihood)-elbo()-kl), retained_temporal_dependence=temporal_dependence, euclidean_dot=ordinary_dot, precision_metric_dot=precision_dot, orthogonal_covariance_posterior_dependence=orthogonal_gap, io_output_probabilities=output_probabilities, io_forward_error=abs(sum(forward)-io_likelihood), emission_inclusive_beta_pair_error=pair_error, input_only_vs_output_conditioned_gap=input_only_gap, terminal_only_output_probability=missing_probability, table_update_omitted_old_transition_gap=table_gap)
print(json.dumps(result, indent=2))
