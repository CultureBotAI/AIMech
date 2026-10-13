"""Constructed algebra for the published CLARS denominator, not training."""
import json
import math


def norm(x):
    return math.sqrt(sum(a*a for a in x))


def mean(vectors):
    return [sum(v[j] for v in vectors)/len(vectors) for j in range(len(vectors[0]))]


def evaluate(w, gradients, gamma=0.2, eta=0.1):
    g = mean(gradients)
    denominator = sum(norm(x) for x in gradients)/len(gradients)
    if denominator == 0:
        raise ZeroDivisionError('The primary Eq. 5 supplies no all-zero fallback.')
    coefficient = gamma*eta*norm(w)/denominator
    step = [coefficient*x for x in g]
    return dict(mean_gradient=g, mean_norm=denominator,
                coherence=norm(g)/denominator, coefficient=coefficient,
                fresh_increment=step, fresh_norm=norm(step))


w = [3.0, 4.0]
coherent = evaluate(w, [[1.0, 0.0], [3.0, 0.0]])
assert math.isclose(coherent['coherence'], 1)
assert math.isclose(coherent['fresh_norm'], .1)
# Nonzero finite-population gradient variance despite coherence one.
assert sum(norm([x-y for x,y in zip(v, coherent['mean_gradient'])])**2
           for v in [[1.0,0.0],[3.0,0.0]])/2 == 1
orthogonal = evaluate(w, [[1.0, 0.0], [0.0, 1.0]])
assert math.isclose(orthogonal['coherence'], 1/math.sqrt(2))
assert math.isclose(orthogonal['fresh_norm'], .1/math.sqrt(2))
cancel = evaluate(w, [[1.0, 0.0], [-1.0, 0.0]])
assert cancel['coefficient'] > 0 and cancel['fresh_norm'] == 0
same_mean_a = evaluate(w, [[1.0, 0.0], [1.0, 0.0]])
same_mean_b = evaluate(w, [[3.0, 0.0], [-1.0, 0.0]])
assert same_mean_a['mean_gradient'] == same_mean_b['mean_gradient']
assert math.isclose(same_mean_b['fresh_norm'], same_mean_a['fresh_norm']/2)
scaled = evaluate(w, [[9.0, 0.0], [-3.0, 0.0]])
assert scaled['fresh_increment'] == same_mean_b['fresh_increment']
mean_squared_norm = (1.0**2+3.0**2)/2
squared_variant_norm = .2*.1*norm(w)/mean_squared_norm*2
assert math.isclose(squared_variant_norm, .04)
subbatch_means = [[1.0,0.0],[1.0,0.0]]
subbatch_estimate = evaluate(w, subbatch_means)
full_examples = evaluate(w, [[3.0,0.0],[-1.0,0.0],[3.0,0.0],[-1.0,0.0]])
assert math.isclose(subbatch_estimate['fresh_norm'],2*full_examples['fresh_norm'])
zero_weights = evaluate([0.0,0.0],[[1.0,0.0]])
assert zero_weights['fresh_norm'] == 0
try:
    evaluate(w, [[0.0,0.0],[0.0,0.0]])
except ZeroDivisionError:
    all_zero = 'undefined as stated'
else:
    raise AssertionError('A fallback was introduced.')
# Eq. 4 with illustrative zero-initial-extrapolation state v0=w0.
fresh = coherent['fresh_increment']
v1 = [x-d for x,d in zip(w,fresh)]
w1 = [v+.9*(v-v0) for v,v0 in zip(v1,w)]
displacement = norm([x-y for x,y in zip(w,w1)])
assert math.isclose(displacement,.19) and displacement > .1
print(json.dumps(dict(coherent=coherent, coherent_population_variance=1,
    orthogonal=orthogonal,cancellation=cancel,same_aggregate=[same_mean_a,same_mean_b],
    positive_rescaling=scaled,mean_squared_denominator_variant_norm=squared_variant_norm,
    subbatch_denominator= subbatch_estimate,full_example_denominator=full_examples,
    zero_weights=zero_weights,all_zero=all_zero,nesterov_first_displacement=displacement),indent=2))
