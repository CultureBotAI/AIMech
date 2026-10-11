"""Original finite arithmetic for source conventions; no models or author code."""
import json
import math
from fractions import Fraction


def calculate():
    # R=81, eta=3 gives s_max=4. Compare printed Algorithm1 with Table1.
    brackets = []
    for s in range(4, -1, -1):
        paper_n = math.ceil(Fraction(5 * 3**s, s + 1))
        code_n = (5 // (s + 1)) * 3**s
        brackets.append(dict(s=s, paper_algorithm_n=paper_n, table_and_pinned_code_n=code_n,
                             initial_resource=81 // 3**s,
                             paper_round_sizes=[paper_n // 3**i for i in range(s + 1)]))
    assert [b['paper_algorithm_n'] for b in brackets] == [81, 34, 15, 8, 5]
    assert [b['table_and_pinned_code_n'] for b in brackets] == [81, 27, 9, 6, 5]
    assert 81 * 3**4 > 81 and 81 / 3**4 == 1
    # BOHB paper permits overlapping better/worse sets at small sample counts.
    dim, n_min, count, q = 4, 5, 7, Fraction(15, 100)
    paper_good = max(n_min, q * count)
    paper_bad = max(n_min, count - paper_good)
    overlap = paper_good + paper_bad - count
    code_good = max(n_min, (15 * count) // 100)
    code_bad_actual = len(list(range(count))[code_good:code_good + max(n_min, (85 * count)//100)])
    assert overlap == 3 and code_bad_actual == 2 and code_bad_actual <= dim
    noninteger_product = (5 // 4) * Fraction(5, 2)**3
    noninteger_count = int(noninteger_product)
    assert noninteger_product == Fraction(125, 8) and noninteger_count == 15
    return dict(brackets=brackets,
                noninteger_reduction=dict(eta=2.5, s_max=4, s=3, product=float(noninteger_product), count=noninteger_count),
                initial_budget_sign=dict(printed_bohb=81 * 3**4, bounded_geometric=81 / 3**4, maximum=81),
                small_sample_kde=dict(dimension=dim, minimum= n_min, observations=count,
                                     paper_overlap=int(overlap), pinned_code_bad_set_size=code_bad_actual,
                                     pinned_code_model_construction_passes=code_bad_actual > dim),
                independent_sampling=dict(region_probability=.01, trials=100,
                                          probability_at_least_one_hit=1-(1-.01)**100,
                                          zero_mass_region_hit_probability=0))


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
