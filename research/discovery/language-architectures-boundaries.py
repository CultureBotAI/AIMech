"""Finite curator calculations for three language-model architectures.

Original toy parameters; no author implementation, model training or benchmark.
"""
import copy
import json
import math


def close(a, b, tol=1e-7):
    assert abs(a - b) < tol, (a, b)


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def mv(m, v):
    return [dot(row, v) for row in m]


def transpose(m):
    return list(zip(*m))


def softmax(x):
    e = [math.exp(v - max(x)) for v in x]
    return [v / sum(e) for v in e]


def diff(f, x, eps=1e-5):
    return (f(x + eps) - f(x - eps)) / (2 * eps)


# Shared nonlinear predictor still has node-dependent hidden activities.
base, node_embeddings, beta = 0.3, [0.4, -0.7], 0.8
hidden = [math.tanh(base + n) for n in node_embeddings]
def morin(b):
    root, child = [sigmoid(b * h) for h in hidden]
    return [root * child, root * (1 - child), 1 - root]
pm = morin(beta)
close(sum(pm), 1)
assert hidden[0] != hidden[1]
grad_beta = sum((sigmoid(beta * h) - 1) * h for h in hidden)
close(grad_beta, diff(lambda b: -math.log(morin(b)[0]), beta))

# LBL in the 2007 row-vector convention, with tied context/output R.
R = [[0.4, -0.3], [0.7, 0.2], [-0.5, 0.6]]
C = [[[0.5, 0.8], [-0.2, 0.3]], [[-0.4, 0.1], [0.9, 0.2]]]
br, bv, context, target = [0.1, -0.2], [0.2, -0.1, 0.05], [0, 1], 0
def predict(r, c, ctx=context):
    h = br.copy()
    for w, matrix in zip(ctx, c):
        h = [a + b for a, b in zip(h, mv(transpose(matrix), r[w]))]
    return h, softmax([dot(h, row) + bias for row, bias in zip(r, bv)])
h, p = predict(R, C)
row_logits = [sum(dot(R[w], mv(matrix, row)) for w, matrix in zip(context, C)) + dot(br, row) + bias for row, bias in zip(R, bv)]
for a, b in zip(p, softmax(row_logits)):
    close(a, b)
wrong_h = [br[k] + sum(mv(matrix, R[w])[k] for w, matrix in zip(context, C)) for k in range(2)]
assert any(abs(a - b) > 0.01 for a, b in zip(h, wrong_h))
assert any(abs(a - b) > 0.01 for a, b in zip(p, predict(R, C, list(reversed(context)))[1]))
close(sum(p), 1)
delta_mean = [R[target][k] - sum(p[j] * R[j][k] for j in range(3)) for k in range(2)]
def logp(r, c):
    return math.log(predict(r, c)[1][target])
for pos in range(2):
    for a in range(2):
        for b in range(2):
            def fc(value):
                c = copy.deepcopy(C)
                c[pos][a][b] = value
                return logp(R, c)
            close(R[context[pos]][a] * delta_mean[b], diff(fc, C[pos][a][b]))
analytic_r = [[((j == target) - p[j]) * h[k] for k in range(2)] for j in range(3)]
for w, matrix in zip(context, C):
    flow = mv(matrix, delta_mean)
    for k in range(2):
        analytic_r[w][k] += flow[k]
for j in range(3):
    for k in range(2):
        def fr(value):
            r = copy.deepcopy(R)
            r[j][k] = value
            return logp(r, C)
        close(analytic_r[j][k], diff(fr, R[j][k]))
output_only = (1 - p[target]) * h[0]
assert abs(output_only - analytic_r[target][0]) > 0.01

# HLBL disjoint leaf paths sum for a word with multiple codes.
logits = [math.log(0.6 / 0.4), math.log(0.8 / 0.2), math.log(0.3 / 0.7)]
def leaves(z):
    root, left, right = map(sigmoid, z)
    return [root * left, root * (1 - left), (1 - root) * right, (1 - root) * (1 - right)]
lp = leaves(logits)
word_mass = lp[0] + lp[2]
close(word_mass, 0.6)
close(word_mass + lp[1] + lp[3], 1)
responsibilities = [lp[0] / word_mass, lp[2] / word_mass]
multi_gradient = [-0.2, -0.16, -0.14]
for i in range(3):
    def loss(value):
        z = logits.copy()
        z[i] = value
        l = leaves(z)
        return -math.log(l[0] + l[2])
    close(multi_gradient[i], diff(loss, logits[i]))
close(multi_gradient[0], responsibilities[0] * (0.6 - 1) + responsibilities[1] * 0.6)
assert abs(multi_gradient[0] - (0.6 - 1)) > 0.1
# A complete binary tree can be a comb; exact all-word output cannot be log V.
assert 7 > math.log2(8)
print(json.dumps(dict(morin=dict(hidden=hidden, probabilities=pm, shared_beta_gradient=grad_beta), lbl=dict(predicted_feature=h, probabilities=p, tied_embedding_gradient=analytic_r, transpose_and_position_checks=True, central_difference_gradient_checks=True), hlbl=dict(leaf_probabilities=lp, combined_word_probability=word_mass, code_responsibilities=responsibilities, multiple_code_nll_gradient=multi_gradient), limitations='Finite examples establish algebraic boundaries only; no empirical performance or author-code claim.'), indent=2))
