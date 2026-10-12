"""Finite curator checks for hPAM variants, franchise support and timestamp laws.

Uses synthetic counts and parameters; does not run historical author software.
"""
from itertools import product
from math import exp, lgamma, isclose
import json


def dm(alpha, counts):
    """Integrated ordered categorical observations (no multinomial coefficient)."""
    return exp(lgamma(sum(alpha)) - lgamma(sum(alpha) + sum(counts))
               + sum(lgamma(a + n) - lgamma(a) for a, n in zip(alpha, counts)))


DOCS = (0, 0, 1)
WORDS = (0, 1, 0)


def factors(choice, doc, word, variant):
    """Parameter-row identities enforce the model's actual sharing structure."""
    if variant == 1:
        supertopic, subtopic, level = choice
        emitter = 0 if level == 0 else 1 + supertopic if level == 1 else 3 + subtopic
        return [
            (('root', doc), (0.7, 1.3), supertopic),
            (('child', doc, supertopic), (0.4, 0.9), subtopic),
            (('level', supertopic, subtopic), (0.8, 0.8, 0.8), level),
            (('word', emitter), (0.6, 1.4), word),
        ]
    supertopic, subtopic = choice
    result = [(('root', doc), (0.5, 0.7, 1.3), supertopic + 1)]
    if supertopic == -1:
        emitter = 0
    else:
        result.append((('child', doc, supertopic), (0.4, 0.6, 0.9), subtopic + 1))
        emitter = 1 + supertopic if subtopic == -1 else 3 + subtopic
    result.append((('word', emitter), (0.6, 1.4), word))
    return result


def rows(assignments, variant, skip=None):
    table = {}
    for i, choice in enumerate(assignments):
        if i == skip:
            continue
        for key, alpha, index in factors(choice, DOCS[i], WORDS[i], variant):
            if key not in table:
                table[key] = (alpha, [0] * len(alpha))
            table[key][1][index] += 1
    return table


def joint(assignments, variant):
    value = 1.0
    for alpha, counts in rows(assignments, variant).values():
        value *= dm(alpha, counts)
    return value


def normalize(weights):
    total = sum(weights)
    return [value / total for value in weights]


def verify_variant(variant, choices):
    states = list(product(choices, repeat=len(WORDS)))
    masses = {state: joint(state, variant) for state in states}
    error = 0.0
    for state in states:
        for i in range(len(WORDS)):
            leave = rows(state, variant, skip=i)
            exact, predictive = [], []
            for choice in choices:
                candidate = list(state)
                candidate[i] = choice
                exact.append(masses[tuple(candidate)])
                value = 1.0
                for key, alpha, index in factors(choice, DOCS[i], WORDS[i], variant):
                    counts = leave.get(key, (alpha, [0] * len(alpha)))[1]
                    value *= (counts[index] + alpha[index]) / (sum(counts) + sum(alpha))
                predictive.append(value)
            error = max(error, max(abs(a - b) for a, b in zip(normalize(exact), normalize(predictive))))
    assert error < 1e-12
    return dict(states=len(states), conditionals=len(states) * len(WORDS), max_error=error)


def beta_integral(a, b):
    assert a > 0 and b > 0
    return exp(lgamma(a) + lgamma(b) - lgamma(a + b))


def beta_density(t, a, b):
    return t ** (a - 1) * (1 - t) ** (b - 1) / beta_integral(a, b)


def main():
    hpam1 = verify_variant(1, list(product(range(2), range(2), range(3))))
    hpam2 = verify_variant(2, [(-1, -1)] + [(s, t) for s in range(2) for t in (-1, 0, 1)])

    # One available full path in model1: root-level probability ~ Beta(1,2)
    # shared between documents. Match the marginal probability in model2,
    # but its document-local exit probabilities are independent Beta(1,2).
    shared_root_joint = 1 * 2 / (3 * 4)
    local_exit_joint = (1 / 3) ** 2
    assert isclose(shared_root_joint, 1 / 6)
    assert isclose(local_exit_joint, 1 / 9)

    # CRF subtopic prediction: three local customers all eat dish0. The
    # category has one menu for dish0 used by two tables; globally two menus
    # serve dish0 and three serve dish1. All concentrations equal one.
    # A new local table -> new category menu -> globally existing dish1
    # remains possible even though this category has never used dish1.
    new_table = 1 / (3 + 1)
    new_menu = 1 / (2 + 1)
    unseen_edge = new_table * new_menu * 3 / (5 + 1)
    new_dish = new_table * new_menu * 1 / (5 + 1)
    dish0 = 3 / 4 + new_table * (2 / 3 + new_menu * 2 / 6)
    assert isclose(unseen_edge, 1 / 24)
    assert isclose(new_dish, 1 / 72)
    assert isclose(dish0 + unseen_edge + new_dish, 1)

    # A two-time PAMTOT factor is normalized over two independent time
    # coordinates. Restricting both coordinates to the same value is a
    # different law. Normalizing each path's diagonal changes its odds.
    pairs = [((2, 1), (2, 1)), ((2, 1), (1, 2))]
    diagonal_mass, density = [], []
    for (a, b), (c, d) in pairs:
        diagonal_mass.append(beta_integral(a + c - 1, b + d - 1)
                             / (beta_integral(a, b) * beta_integral(c, d)))
        density.append(beta_density(0.25, a, b) * beta_density(0.25, c, d))
    repeated_odds = normalize(density)
    single_time_odds = normalize([v / z for v, z in zip(density, diagonal_mass)])
    assert all(isclose(a, b) for a, b in zip(diagonal_mass, (4 / 3, 2 / 3)))
    assert all(isclose(a, b) for a, b in zip(repeated_odds, (1 / 4, 3 / 4)))
    assert all(isclose(a, b) for a, b in zip(single_time_odds, (1 / 7, 6 / 7)))
    singular_exponent = (0.4 - 1) + (0.4 - 1)
    assert singular_exponent <= -1  # Nonintegrable near zero despite valid individual Betas.

    print(json.dumps(dict(
        hpam_model1=hpam1, hpam_model2=hpam2,
        cross_document_root_emission=dict(shared_level_joint=shared_root_joint,
                                         independent_local_exit_joint=local_exit_joint),
        franchise_predictive=dict(previously_unused_edge=unseen_edge, new_global_dish=new_dish,
                                  observed_dish=dish0),
        pamtot=dict(diagonal_integrals=diagonal_mass, repeated_time_path_probabilities=repeated_odds,
                    normalized_single_time_path_probabilities=single_time_odds,
                    valid_beta_product_boundary_exponent=singular_exponent),
    ), indent=2))


if __name__ == '__main__':
    main()
