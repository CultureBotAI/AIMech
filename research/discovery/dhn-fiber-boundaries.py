"""Exact finite illustrations of the inspected 5 June 1997 DHN report.

Original rational calculations, not author-code execution or a speed benchmark.
No files, timestamps, random values, or third-party modules; JSON stdout only.
"""
from fractions import Fraction as F
from itertools import product
import json


def transition(weights, partitions, choices, flips):
    n, d = len(weights), len(partitions)
    assert all(w > 0 for w in weights)
    assert len(choices) == len(flips) == d and sum(choices) == 1
    assert all(w > 0 for w in choices) and all(0 <= t <= 1 for t in flips)
    assert all(sorted(x for line in partition for x in line) == list(range(n)) for partition in partitions)
    signs = list(product((-1, 1), repeat=d))
    states = [(z, x) for z in signs for x in range(n)]
    lookup = {state: i for i, state in enumerate(states)}
    mu = [F(weights[x], sum(weights) * 2 ** d) for z, x in states]
    matrix = [[F(0)] * len(states) for _ in states]
    for row, (z, x) in enumerate(states):
        for direction, selection in enumerate(choices):
            line = next(line for line in partitions[direction] if x in line)
            position = line.index(x) + z[direction]
            y = line[position] if 0 <= position < len(line) else x
            acceptance = min(F(1), F(weights[y], weights[x])) if 0 <= position < len(line) else F(0)
            for accepted, probability in [(True, acceptance), (False, 1 - acceptance)]:
                after = list(z)
                if accepted:
                    after[direction] *= -1
                for flip, flip_probability in [(True, 1 - flips[direction]), (False, flips[direction])]:
                    final = after[:]
                    if flip:
                        final[direction] *= -1
                    column = lookup[(tuple(final), y if accepted else x)]
                    matrix[row][column] += selection * probability * flip_probability
    assert all(sum(row) == 1 for row in matrix)
    assert all(sum(mu[i] * matrix[i][j] for i in range(len(states))) == mu[j] for j in range(len(states)))
    return states, matrix, mu


def reach(matrix, start):
    seen, todo = {start}, [start]
    while todo:
        for j, probability in enumerate(matrix[todo.pop()]):
            if probability and j not in seen:
                seen.add(j)
                todo.append(j)
    return seen


def irreducible(matrix):
    return all(len(reach(matrix, i)) == len(matrix) for i in range(len(matrix)))


def main():
    directed_cases = 0
    for n in range(2, 5):
        for weights in product((1, 2, 3), repeat=n):
            for theta in (F(1, 5), F(1, 2), F(4, 5)):
                states, matrix, mu = transition(weights, [[list(range(n))]], [F(1)], [theta])
                assert irreducible(matrix) and any(matrix[i][i] > 0 for i in range(len(states)))
                assert any(mu[i] * matrix[i][j] != mu[j] * matrix[j][i] for i in range(len(states)) for j in range(len(states)))
                directed_cases += 1
    states, deterministic, mu = transition([1] * 5, [[list(range(5))]], [F(1)], [F(0)])
    assert irreducible(deterministic) and all(row.count(F(1)) == 1 for row in deterministic)
    location = 0
    visits = []
    while location not in visits:
        visits.append(location)
        location = deterministic[location].index(F(1))
    assert location == 0 and len(visits) == 10
    _, no_final_flip, _ = transition([1] * 5, [[list(range(5))]], [F(1)], [F(1)])
    classes = sorted({tuple(sorted(reach(no_final_flip, i))) for i in range(len(states))})
    assert not irreducible(no_final_flip) and len(classes) == 6
    fiber_cases = 0
    partitions = [[[0, 1], [2, 3]], [[0, 2], [1, 3]]]
    for weights in product((1, 2), repeat=4):
        for flips in product((F(1, 5), F(3, 5)), repeat=2):
            fiber_states, matrix, mu = transition(weights, partitions, [F(1, 3), F(2, 3)], flips)
            assert irreducible(matrix) and any(matrix[i][i] > 0 for i in range(len(fiber_states)))
            fiber_cases += 1
    example = transition([1, 2, 4], [[[0, 1, 2]]], [F(1)], [F(1, 5)])
    print(json.dumps({
        'scope': 'Exact finite illustrations; not a general proof, convergence-rate computation, author replication, or independent scientific approval.',
        'directed_positive_target_cases': directed_cases,
        'checks': 'Stochastic rows, exact target invariance, irreducibility, positive self-loop (hence aperiodicity for each irreducible case), and failure of detailed balance for the one-dimensional cases.',
        'directed_example': {'weights': [1, 2, 4], 'theta': F(1, 5), 'states': example[0], 'transition': example[1], 'invariant': example[2]},
        'theta_zero_uniform_boundary': {'period': len(visits), 'cycle': [states[i] for i in visits]},
        'theta_one_uniform_boundary': {'closed_classes': [[states[i] for i in group] for group in classes]},
        'fiber_positive_target_cases': fiber_cases,
        'fiber_scope': 'Two directions on a 2 by 2 grid, four persistent sign vectors, positive selection probabilities 1/3 and 2/3; checked invariance, irreducibility and aperiodicity.',
        'limitations': 'No empirical results or total-variation/chi-square rate claims tested. Endpoint theta values illustrate why the reported ergodicity proposition uses 0<theta<1.'
    }, default=str, indent=2))


if __name__ == '__main__':
    main()
