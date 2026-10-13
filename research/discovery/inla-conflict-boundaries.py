"""Constructed checks, not an execution or reproduction of R-INLA."""
import json
import math


def mixture(weights):
    means = [0.0, 2.0]
    mean = sum(w * m for w, m in zip(weights, means))
    var = sum(w * (1.0 + m * m) for w, m in zip(weights, means)) - mean * mean
    return {"weights": weights, "mean": mean, "variance": var}


def main():
    # Local evidence probabilities 0.1, 0.9 under two equally weighted states.
    frozen = mixture([0.5, 0.5])
    updated = mixture([0.1, 0.9])
    assert frozen["mean"] == 1.0 and frozen["variance"] == 2.0
    assert math.isclose(updated["mean"], 1.8)
    assert math.isclose(updated["variance"], 1.36)
    eigenvalues = [100.0, 0.01]
    mean = [10.0, 0.1]
    tol = 1e-3
    absolute_rank = sum(v > tol for v in eigenvalues)
    relative_mask = [v > tol * max(eigenvalues) for v in eigenvalues]
    relative_rank = sum(relative_mask)
    retained_q = sum(m * m / v for m, v, keep in zip(mean, eigenvalues, relative_mask) if keep)
    full_q = sum(m * m / v for m, v in zip(mean, eigenvalues))
    assert (absolute_rank, relative_rank) == (2, 1)
    assert retained_q == 1.0 and math.isclose(full_q, 2.0)
    scale = 1e-3
    scaled_eigenvalues = [v * scale**2 for v in eigenvalues]
    assert sum(v > tol for v in scaled_eigenvalues) == 0
    assert sum(v > tol * max(scaled_eigenvalues) for v in scaled_eigenvalues) == 1
    # Shared nuisance b~N(0,1), independent e1,e2~N(0,1), A=b+e1, B=b+e2.
    # Var(A-B)=2, whereas independent copies of the marginal N(0,2) laws give 4.
    result = {
        "scope": "Constructed analytic examples only; no R-INLA runtime, empirical calibration or historical reproduction.",
        "frozen_nuisance_mixture": frozen,
        "posterior_as_prior_update": updated,
        "rank_thresholds": {
            "covariance_diagonal": eigenvalues,
            "mean": mean,
            "absolute_rank": absolute_rank,
            "relative_pseudoinverse_rank": relative_rank,
            "retained_quadratic": retained_q,
            "full_rank_quadratic": full_q,
            "mixed_convention_chi2_tail": math.exp(-retained_q / 2),
            "consistent_retained_chi1_tail": math.erfc(math.sqrt(retained_q / 2)),
            "consistent_full_rank_chi2_tail": math.exp(-full_q / 2),
            "scaled_absolute_rank": 0,
            "scaled_relative_rank": 1,
        },
        "shared_nuisance": {"marginal_variances": [2, 2], "cross_covariance": 1, "shared_difference_variance": 2, "independent_replication_difference_variance": 4},
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
