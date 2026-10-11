"""Original finite examples of search-space and halving conventions."""
import itertools
import json
import math


def calculate():
    grid = list(itertools.product(range(3), range(4), range(2)))
    assert len(grid) == 24 and len({x[0] for x in grid}) == 3
    ceiling_counts, floor_counts = [3], [3]
    for _ in range(2):
        ceiling_counts.append(math.ceil(ceiling_counts[-1] / 2))
        floor_counts.append(math.floor(floor_counts[-1] / 2))
    assert ceiling_counts == [3, 2, 1] and floor_counts == [3, 1, 0]
    tied = [.5] * 4
    assert sum(x <= sorted(tied)[1] for x in tied) == 4
    # Illustrative power-of-two cohort with budget24 and three stages.
    sizes = [8, 4, 2]
    additional = [24 // (size * 3) for size in sizes]
    cumulative = list(itertools.accumulate(additional))
    assert additional == [1, 2, 4] and cumulative == [1, 3, 7]
    # A completed configuration may qualify before later results change rank.
    first = {'A': .2, 'B': .3}
    later = dict(first, C=.1, D=.05)
    first_promoted = sorted(first, key=first.get)[:1]
    hindsight_top = sorted(later, key=later.get)[:2]
    assert first_promoted == ['A'] and 'A' not in hindsight_top
    # Empty highest rung, eligible base rung: scan all rungs before fallback.
    rungs = {1: [], 0: ['eligible-base-candidate']}
    scanned = next((rungs[k][0] for k in [1, 0] if rungs[k]), 'new')
    inside_loop_fallback = rungs[1][0] if rungs[1] else 'new'
    assert scanned == 'eligible-base-candidate' and inside_loop_fallback == 'new'
    return dict(grid=dict(total=24,distinct_first_coordinate=3,repeats_per_first_coordinate=8),
                rounding=dict(ceiling=ceiling_counts,literal_floor=floor_counts,tied_threshold_retains=4),
                resources=dict(stage_sizes=sizes,additional=additional,cumulative=cumulative),
                asynchronous_ranking=dict(early_promoted=first_promoted,hindsight_top=hindsight_top),
                fallback=dict(after_full_scan=scanned,inside_first_iteration=inside_loop_fallback))


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
