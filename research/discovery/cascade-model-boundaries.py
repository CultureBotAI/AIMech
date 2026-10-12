"""Exact finite examples for cascade-model curation; no fitted-model evaluation."""
from fractions import Fraction as F
import json


def convolution(h, u):
    return [sum(h[j] * u[t-j] for j in range(min(t+1, len(h)))) for t in range(len(u))]


def rank(rows):
    a = [[F(x) for x in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        pivot = next((k for k in range(r, len(a)) if a[k][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = a[r][c]
        a[r] = [v/scale for v in a[r]]
        for k in range(len(a)):
            if k != r:
                scale = a[k][c]
                a[k] = [x-scale*y for x, y in zip(a[k], a[r])]
        r += 1
        if r == len(a):
            break
    return r


h, u = [F(1), F(2)], [F(1), F(2), F(-1)]
wiener = [z*z for z in convolution(h, u)]
hammerstein = convolution(h, [v*v for v in u])
assert wiener == [1, 16, 9] and hammerstein == [1, 6, 9]
# Rescaling the internal signal leaves the observed cascade unchanged.
c = F(3)
wiener_rescaled = [(z/c)**2 for z in convolution([c*x for x in h], u)]
hammerstein_rescaled = convolution([x/c for x in h], [c*v*v for v in u])
assert wiener_rescaled == wiener and hammerstein_rescaled == hammerstein
# Part II Example 2.1: equal current outputs need not give equal next outputs.
g = lambda x: x+x*x
states, step = [F(0), F(-1)], F(1, 4)
assert [g(x) for x in states] == [0, 0]
next_outputs = [g(x+step) for x in states]
assert next_outputs == [F(5, 16), F(-3, 16)]
# A zero derivative of input nonlinearity at equilibrium does not prevent
# the exact Hammerstein recurrence y_next=y+u^2 (Part II Eq. 2.31–2.32).
hammerstein_state = F(0)
hammerstein_path = []
for v in u:
    hammerstein_state += v*v
    hammerstein_path.append(hammerstein_state)
assert hammerstein_path == [1, 5, 6]
# Source-audit examples, not defining properties of either new concept.
# Part I printed p.13 property (2): H_(1,infty) and H_(2,infty) have
# rank 2, but H_(1,1) rank 1 for A=[[0,1],[0,0]], B=[[0],[1]], C=I.
# A^2=0, so all later Markov blocks vanish and these finite matrices
# represent the ranks of the infinite matrices exactly.
h1 = [[0], [1]]
h12 = [[0, 1], [1, 0]]
h22 = [[0, 1], [1, 0], [1, 0], [0, 0]]
ranks = [rank(h1), rank(h12), rank(h22)]
assert ranks == [1, 2, 2]
# Part II Eq.2.34 omits +u for y=x+x^3. At x=0,u=1 its displayed
# expression gives 1, whereas direct state/output substitution gives 2.
x, v = F(0), F(1)
exact_cubic = (x+v)+(x+v)**3
printed_cubic = x+x**3+3*x*x*v+3*x*v*v+v**3
assert exact_cubic-printed_cubic == 1

print(json.dumps({
    "wiener_output": list(map(str, wiener)),
    "hammerstein_output": list(map(str, hammerstein)),
    "rescaled_wiener_output": list(map(str, wiener_rescaled)),
    "rescaled_hammerstein_output": list(map(str, hammerstein_rescaled)),
    "wiener_branch_next_outputs": list(map(str, next_outputs)),
    "hammerstein_squared_input_path": list(map(str, hammerstein_path)),
    "source_hankel_ranks_H11_H1infty_H2infty": ranks,
    "source_cubic_formula_missing_term": str(exact_cubic-printed_cubic),
}, indent=2))
