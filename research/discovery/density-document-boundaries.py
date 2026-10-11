"""Finite curator calculations; no author software, model training or benchmarks."""
import json
import math
from itertools import product


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def gaussian(x, mu, sigma):
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2) / (math.sqrt(2 * math.pi) * sigma)


def mixture(x, logits, means, log_scales):
    z = sum(math.exp(v) for v in logits)
    weights = [math.exp(v) / z for v in logits]
    parts = [w * gaussian(x, m, math.exp(s)) for w, m, s in zip(weights, means, log_scales)]
    return sum(parts), weights, [v / sum(parts) for v in parts]


def finite_derivative(fn, values, index):
    hi, lo = values.copy(), values.copy()
    hi[index] += 1e-6
    lo[index] -= 1e-6
    return (fn(hi) - fn(lo)) / 2e-6


logits = [math.log(0.35), math.log(0.65)]
means = [-1.0, 1.2]
log_scales = [math.log(0.8), math.log(1.1)]
x = 0.7
density, weights, responsibilities = mixture(x, logits, means, log_scales)
nll_logit = [w - r for w, r in zip(weights, responsibilities)]
nll_mean = [r * (m - x) / math.exp(2 * s) for r, m, s in zip(responsibilities, means, log_scales)]
nll_scale = [r * (1 - (x - m) ** 2 / math.exp(2 * s)) for r, m, s in zip(responsibilities, means, log_scales)]
for values, analytic, fn in [
    (logits, nll_logit, lambda v: -math.log(mixture(x, v, means, log_scales)[0])),
    (means, nll_mean, lambda v: -math.log(mixture(x, logits, v, log_scales)[0])),
    (log_scales, nll_scale, lambda v: -math.log(mixture(x, logits, means, v)[0])),
]:
    for i, expected in enumerate(analytic):
        assert math.isclose(finite_derivative(fn, values, i), expected, abs_tol=1e-8)
raw_density_gradient = finite_derivative(lambda v: mixture(x, v, means, log_scales)[0], logits, 0)
assert math.isclose(raw_density_gradient, -density * nll_logit[0], abs_tol=1e-8)
assert not math.isclose(raw_density_gradient, -nll_logit[0], abs_tol=1e-4)

# Positive exponential scales can approach zero: positivity is not a lower bound.
shrinking_scale_densities = [gaussian(0, 0, math.exp(s)) for s in [-2, -4, -8]]
assert 0 < shrinking_scale_densities[0] < shrinking_scale_densities[1] < shrinking_scale_densities[2]
mean_density = 0.5 * gaussian(0, -2, 0.5) + 0.5 * gaussian(0, 2, 0.5)
near_mode_density = 0.5 * gaussian(2, -2, 0.5) + 0.5 * gaussian(2, 2, 0.5)
assert near_mode_density > mean_density
# Two equally weighted N((1,1), I) and N((-1,-1), I) components.
covariance = [[2, 1], [1, 2]]
trace_variance = 4
unscaled_scalar_term = 1 + 2
assert trace_variance != unscaled_scalar_term

# The RNADE supplement's Algorithm2 phi line is log-shaped, with positive
# quadratic term, then used as though it were an ordinary density.
literal_phi = [0.5 * m * m - 0.5 * math.log(2 * math.pi) for m in [0, 3]]
literal_responsibilities = [v / sum(literal_phi) for v in literal_phi]
assert literal_responsibilities[0] < 0 < 1 < literal_responsibilities[1]
correct_parts = [gaussian(0, m, 1) for m in [0, 3]]
correct_responsibilities = [v / sum(correct_parts) for v in correct_parts]
assert all(0 <= v <= 1 for v in correct_responsibilities)

# A two-word DocNADE with one sigmoid hidden unit and a binary output tree.
# W_A=log(3), W_B=0, c=0; output weight=4log(3), bias=-2log(3).
def hidden(prefix):
    return sigmoid(sum(math.log(3) if w == "A" else 0 for w in prefix))


def probability_b(prefix):
    return sigmoid(4 * math.log(3) * hidden(prefix) - 2 * math.log(3))


def sequence_probability(sequence):
    out = 1.0
    for i, word in enumerate(sequence):
        q = probability_b(sequence[:i])
        out *= q if word == "B" else 1 - q
    return out


joint = {"".join(s): sequence_probability(s) for s in product("AB", repeat=2)}
assert math.isclose(sum(joint.values()), 1)
assert math.isclose(joint["AB"], 3 / 8) and math.isclose(joint["BA"], 1 / 4)
assert hidden("AB") == hidden("BA")
count_probability = joint["AB"] + joint["BA"]
symmetrized_sequence_probability = count_probability / 2
assert math.isclose(count_probability, 5 / 8)
assert math.isclose(symmetrized_sequence_probability, 5 / 16)
average_nll = -(math.log(joint["AB"]) + math.log(joint["BA"])) / 2
mixture_nll = -math.log(symmetrized_sequence_probability)
assert average_nll > mixture_nll
# For observed left branch, -log(1-sigmoid(z)) has derivative sigmoid(z).
z = math.log(3)
left_loss = lambda v: -math.log(1 - sigmoid(v[0]))
correct_left_gradient = finite_derivative(left_loss, [z], 0)
assert math.isclose(correct_left_gradient, 3 / 4, abs_tol=1e-8)
literal_observed_branch_gradient = 1 - sigmoid(z)
assert not math.isclose(correct_left_gradient, literal_observed_branch_gradient)
# A full binary tree can be a comb: fullness alone does not imply log depth.
full_comb_leaves = 8
full_comb_max_depth = full_comb_leaves - 1
assert full_comb_max_depth > math.log2(full_comb_leaves)

print(json.dumps({
    "mdn": {"density": density, "responsibilities": responsibilities,
            "nll_logit_gradient": nll_logit, "nll_mean_gradient": nll_mean,
            "nll_log_scale_gradient": nll_scale, "raw_density_logit_gradient": raw_density_gradient,
            "positive_shrinking_scale_densities": shrinking_scale_densities,
            "density_at_mean": mean_density, "density_at_component_center": near_mode_density,
            "two_dimensional_mixture_covariance": covariance, "trace_variance": trace_variance,
            "literal_unscaled_variance_term": unscaled_scalar_term},
    "rnade_supplement": {"literal_phi_responsibilities": literal_responsibilities,
                          "normalized_gaussian_responsibilities": correct_responsibilities},
    "docnade": {"joint": joint, "full_document_hidden": hidden("AB"),
                "count_probability": count_probability, "symmetrized_sequence_probability": symmetrized_sequence_probability,
                "average_order_nll": average_nll, "symmetrized_sequence_nll": mixture_nll,
                "left_branch_nll_gradient": correct_left_gradient,
                "literal_actual_branch_probability_minus_zero": literal_observed_branch_gradient,
                "full_comb_leaves": full_comb_leaves, "full_comb_max_depth": full_comb_max_depth},
    "scope": "Finite curator calculations; printed-notation checks are not claims about author code or general empirical performance."
}, indent=2))
