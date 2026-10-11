"""Original finite probability witnesses; no data fitting or author-code execution."""
import itertools
import json
import math


def normalize(weights):
    total = sum(weights)
    return [w / total for w in weights]


def entropy(q):
    return -sum(v * math.log(v) for v in q if v)


def softmax(logits):
    return normalize([math.exp(x - max(logits)) for x in logits])


states = list(itertools.product((-1, 1), repeat=3))
h = [0.1, -0.2, 0.25]
J = {(0, 1): 0.7, (0, 2): 0.4, (1, 2): -0.3}
logw = [sum(a * b for a, b in zip(h, s)) + sum(v * s[i] * s[j] for (i, j), v in J.items()) for s in states]
p = normalize([math.exp(w) for w in logw])
logZ = math.log(sum(math.exp(w) for w in logw))


def bound(q):
    return sum(a * b for a, b in zip(q, logw)) + entropy(q)


def product_q(means):
    return [math.prod((1 + m * v) / 2 for m, v in zip(means, s)) for s in states]


def block_q(fields, m3):
    pairs = list(itertools.product((-1, 1), repeat=2))
    q12 = normalize([math.exp(J[0, 1] * a * b + fields[0] * a + fields[1] * b) for a, b in pairs])
    return [q12[pairs.index(s[:2])] * (1 + m3 * s[2]) / 2 for s in states]


def means(q):
    return [sum(w * s[i] for w, s in zip(q, states)) for i in range(3)]


q0 = block_q(h[:2], 0.0)
m = means(q0)
m3 = math.tanh(h[2] + J[0, 2] * m[0] + J[1, 2] * m[1])
q1 = block_q(h[:2], m3)
q2 = block_q([h[0] + J[0, 2] * m3, h[1] + J[1, 2] * m3], m3)
bounds = [bound(q) for q in (q0, q1, q2)]
assert bounds[0] <= bounds[1] <= bounds[2] <= logZ + 1e-12
kl = sum(q * math.log(q / v) for q, v in zip(q2, p))
assert abs(logZ - bound(q2) - kl) < 1e-12
m = means(q2)
corr12 = sum(q * s[0] * s[1] for q, s in zip(q2, states)) - m[0] * m[1]
assert corr12 > 0.1
naive = product_q(m)
naive_corr = sum(q * s[0] * s[1] for q, s in zip(naive, states)) - m[0] * m[1]
assert abs(naive_corr) < 1e-12

# One exact singleton update increases the same variational objective.
mn = [0.2, -0.4, 0.3]
qn0 = product_q(mn)
mn[0] = math.tanh(h[0] + J[0, 1] * mn[1] + J[0, 2] * mn[2])
qn1 = product_q(mn)
assert bound(qn1) >= bound(qn0)

# Synchronous mean-field updates can decrease the bound (two ferromagnetic spins).
def two_bound(ms):
    return 2 * ms[0] * ms[1] + sum(entropy([(1 + m) / 2, (1 - m) / 2]) for m in ms)

sync_before = [0.6, -0.6]
sync_after = [math.tanh(2 * sync_before[1]), math.tanh(2 * sync_before[0])]
assert two_bound(sync_after) < two_bound(sync_before)

# Exact binary auxiliary-link identity needs a coupling-dependent multiplicative constant.
aux = []
for coupling in [-0.8, 0.0, 0.6]:
    a = 0.5 * math.acosh(math.exp(2 * abs(coupling)))
    b = math.copysign(a, coupling)
    C = math.exp(-abs(coupling)) / 2
    original = []
    augmented = []
    for u, v in itertools.product((-1, 1), repeat=2):
        original.append(math.exp(coupling * u * v))
        augmented.append(sum(math.exp((a * u + b * v) * w) for w in (-1, 1)))
    err = max(abs(x - C * y) for x, y in zip(original, augmented))
    assert err < 1e-12
    assert max(abs(x - y) for x, y in zip(normalize(original), normalize(augmented))) < 1e-12
    aux.append(dict(coupling=coupling,constant=C,unnormalized_identity_error=err,log_partition_offset=math.log(C)))

# A two-level HME at one fixed input: input-only path weights versus observed-label posteriors.
top = [0.3, 0.7]
child = [[0.8, 0.2], [0.4, 0.6]]
mu = [[0.1, 0.9], [0.65, 0.4]]
prior = [top[i] * child[i][j] for i, j in itertools.product(range(2), repeat=2)]
mu_flat = [x for row in mu for x in row]
py1 = sum(a * b for a, b in zip(prior, mu_flat))
posterior = [a * b / py1 for a, b in zip(prior, mu_flat)]
assert abs(sum(prior) - 1) < 1e-12 and abs(sum(posterior) - 1) < 1e-12
posterior_top = [sum(posterior[2 * i:2 * i + 2]) for i in range(2)]
posterior_child = [[posterior[2 * i + j] / posterior_top[i] for j in range(2)] for i in range(2)]
assert max(abs(posterior[2 * i + j] - posterior_top[i] * posterior_child[i][j]) for i, j in itertools.product(range(2), repeat=2)) < 1e-12
def log_likelihood(eta0):
    gate = softmax([eta0, math.log(top[1])])
    return math.log(sum(gate[i] * child[i][j] * mu[i][j] for i, j in itertools.product(range(2), repeat=2)))

eps = 1e-6
fd = (log_likelihood(math.log(top[0]) + eps) - log_likelihood(math.log(top[0]) - eps)) / (2 * eps)
gate_gradient = posterior_top[0] - top[0]
assert abs(fd - gate_gradient) < 1e-9

# Uniform mixing does not turn a mixture of distinct Gaussian experts into one Gaussian expert.
at_zero_mixture = math.exp(-2) / math.sqrt(2 * math.pi)
at_zero_mean_expert = 1 / math.sqrt(2 * math.pi)
assert abs(at_zero_mixture - at_zero_mean_expert) > 0.3

print(json.dumps(dict(
    scope='Fixed finite distributions and one or two variational coordinate updates; no model fitting, author code or benchmark.',
    structured_bounds=bounds,log_partition=logZ,structured_kl=kl,
    structured_retained_covariance=corr12,fully_factorized_covariance=naive_corr,
    singleton_bounds=[bound(qn0),bound(qn1)],synchronous_bound_change=two_bound(sync_after)-two_bound(sync_before),
    auxiliary_link=aux,hme_probability_y1=py1,hme_input_path_weights=prior,hme_posterior_path_weights=posterior,
    hme_gate_gradient=gate_gradient,hme_gradient_finite_difference_error=abs(fd-gate_gradient),
    gaussian_mixture_mean_expert_density_gap=at_zero_mean_expert-at_zero_mixture,
),indent=2))
