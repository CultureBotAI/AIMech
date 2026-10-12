"""Exact finite checks of Tan et al. Eq. 16; no fitting or benchmark."""
from fractions import Fraction as F
import json


def distances(points, query, weights):
    return {
        label: sum(w * (x - z) ** 2 for x, z, w in zip(point, query, weights))
        for label, point in points.items()
    }


def main():
    # These means and variances are supplied illustrative numbers, not fitted.
    points = {"A": (F(2), F(0)), "B": (F(0), F(1))}
    query = (F(0), F(0))
    mean = (F(1, 10), F(1))
    variance = (F(100), F(1, 100))
    mean_squared = tuple(x * x for x in mean)
    second_moment = tuple(x * x + v for x, v in zip(mean, variance))
    euclidean = distances(points, query, (F(1), F(1)))
    prescribed = distances(points, query, mean_squared)
    alternative = distances(points, query, second_moment)
    assert euclidean == {"A": F(4), "B": F(1)}
    assert prescribed == {"A": F(1, 25), "B": F(1)}
    assert alternative == {"A": F(10001, 25), "B": F(101, 100)}
    assert min(euclidean, key=euclidean.get) == "B"
    assert min(prescribed, key=prescribed.get) == "A"
    assert min(alternative, key=alternative.get) == "B"
    # Searching all training points permits N2 to contain points outside N1.
    zero_weights = distances(points, query, (F(0), F(0)))
    assert set(zero_weights.values()) == {F(0)}
    # A zero-weight coordinate can collapse different input vectors.
    collapsed = distances({"origin": (F(0), F(0)), "offset": (F(5), F(0))}, query, (F(0), F(1)))
    assert collapsed["origin"] == collapsed["offset"] == 0
    sign_changed = distances(points, query, tuple((-x) ** 2 for x in mean))
    assert sign_changed == prescribed
    print(json.dumps({
        "supplied_mean": list(map(str, mean)),
        "supplied_variance": list(map(str, variance)),
        "euclidean_squared_distances": {k: str(v) for k, v in euclidean.items()},
        "squared_mean_distances": {k: str(v) for k, v in prescribed.items()},
        "second_moment_distances": {k: str(v) for k, v in alternative.items()},
        "one_neighbor_selections": {"first_stage_euclidean": "B", "prescribed_second_stage": "A", "second_moment_alternative": "B"},
        "zero_weights_collapse_distinct_points": True,
        "sign_change_preserves_this_distance": True,
        "scope": "Exact arithmetic for the neighborhood rule at supplied parameters; no variational fit, model training or predictive benchmark."
    }, indent=2))


if __name__ == "__main__":
    main()
