"""Constructed exact arithmetic, not author software or a web experiment."""
from fractions import Fraction
import json

n = 11
edges = {(h, a) for h in range(3) for a in range(7, 10)}
edges |= {(h, 10) for h in range(3, 7)}

def forward(h):
    return [sum(h[u] for u, v in edges if v == a) for a in range(n)]

def backward(a):
    return [sum(a[v] for u, v in edges if u == h) for h in range(n)]

hub = [1] * n
steps = []
for k in range(1, 4):
    authority = forward(hub)
    hub = backward(authority)
    ratio = Fraction(authority[10], authority[7])
    assert ratio == Fraction(4, 3) * Fraction(4, 9) ** (k - 1)
    steps.append(dict(iteration=k, authority=authority[7:], star_to_core=str(ratio)))
assert authority[7:] == [243, 243, 243, 64]
# Normalizing each nonzero vector by a common positive L2 factor changes
# magnitude but not these directions or coordinate ratios.
secondary = [int(i == 10) for i in range(n)]
paired_raw = backward(secondary)
assert forward(paired_raw) == [4 * x for x in secondary]
assert sum(x*x for x in paired_raw) == 4
paired_unit = [Fraction(x, 2) for x in paired_raw]
assert sum(x*x for x in paired_unit) == 1
assert forward(paired_unit) == [2 * x for x in secondary]
leading = [int(i in range(7, 10)) for i in range(n)]
assert forward(backward(leading)) == [9 * x for x in leading]
# The nonzero Gram blocks are 3*J_3 and [4]: eigenvalues 9,4,0,...,0.
# A nonnegative secondary mode is therefore possible despite a strict gap.
assert all(x >= 0 for x in secondary)
zero_mode = [int(i == 7) - int(i == 8) for i in range(n)]
assert any(zero_mode) and not any(backward(zero_mode))
v = [2, -3, 0, 1]
tails = lambda x: ([i for i,z in enumerate(x) if z > 0], [i for i,z in enumerate(x) if z < 0])
assert tails([-x for x in v]) == tails(v)[::-1]
print(json.dumps(dict(graph=dict(vertices=n,edges=sorted(edges)),
    authority_indegrees=[3,3,3,4], sequential_raw_steps=steps,
    normalization='Positive common L2 scaling preserves these directions and ratios; no zero-norm policy is inferred.',
    nonzero_gram_eigenvalues=[9,4], secondary_mode=secondary,
    raw_paired_norm_squared=4, unit_pair_factor='1/sqrt(4)=1/2',
    zero_mode_maps_to_zero=True, secondary_mode_can_be_one_sided=True,
    simultaneous_sign_reversal_exchanges_tails=True),indent=2))
