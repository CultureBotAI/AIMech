#!/usr/bin/env python3
"""Original bounded EI/EGO evidence checks; stdlib only, deterministic stdout.

Not author code, a general-purpose EI implementation, an EGO optimizer, a
benchmark, or a proof of global convergence. Gaussian computations use floats;
the small ordinary-kriging example and finite discrete raw improvements use
Fraction. The quadrature comparison is numerical, with a stated tail bound;
its discretization error is checked empirically, not certified in general.
"""
from fractions import Fraction as F
import json
import math


def phi(z):
    return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)


def Phi(z):
    return math.erfc(-z / math.sqrt(2)) / 2


def ei_min(mean, sd, incumbent):
    if not all(math.isfinite(x) for x in (mean, sd, incumbent)) or sd < 0:
        raise ValueError("finite mean/incumbent and nonnegative finite sd required")
    delta = incumbent - mean
    if sd == 0:
        return max(delta, 0.0)
    z = delta / sd
    return delta * Phi(z) + sd * phi(z)


def ei_max(mean, sd, incumbent):
    return ei_min(-mean, sd, -incumbent)


def close(a, b, tol=1e-11):
    assert math.isclose(a, b, rel_tol=0, abs_tol=tol), (a, b, tol)


def simpson_ei(delta, sd, panels=20000):
    # All callers use -4 <= delta/sd <= 4. Integrand has no interior kink.
    lower, upper = -10.0, delta / sd
    assert -4 <= upper <= 4 and panels % 2 == 0
    step = (upper - lower) / panels
    def value(z):
        return (delta - sd * z) * phi(z)
    weighted = [value(lower), value(upper)]
    weighted.extend((4 if i % 2 else 2) * value(lower + step * i)
                    for i in range(1, panels))
    result = step * math.fsum(weighted) / 3
    # Absolute omitted integral below -10 is <= this expression.
    tail_bound = abs(delta) * Phi(-10) + sd * phi(10)
    return result, tail_bound


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def mv(matrix, vector):
    return [dot(row, vector) for row in matrix]


def main():
    results = {"scope": {
        "role": "original curator-written finite illustrations; not author-code replication",
        "source": "Jones, Schonlau and Welch (1998), journal pp.461-475 and 487",
        "pdf_sha256": "356260d0303a7fa2c8cc4456f46ebc9f39c0bcf763b2e3982c2b78921eab4a57",
        "arithmetic": "Fraction for ordinary kriging/discrete raw improvement; floating math.erfc/exp/log elsewhere",
        "limits": "No model fitting, branch-and-bound implementation, noisy-EI extension, calibration, regret or convergence test."}}

    quadrature = []
    for sd in (0.25, 1.0, 2.0):
        for z in (-4.0, -1.0, 0.0, 1.0, 4.0):
            delta = sd * z
            closed = ei_min(-delta, sd, 0.0)
            integral, tail = simpson_ei(delta, sd)
            close(closed, integral, 1e-10)
            quadrature.append({"mean": -delta, "sd": sd, "incumbent": 0,
                               "closed": closed, "simpson": integral,
                               "absolute_difference": abs(closed - integral),
                               "omitted_tail_bound": tail})
    results["gaussian_integral"] = {"cases": quadrature, "absolute_tolerance": 1e-10,
        "relative_tolerance": 0, "panels": 20000,
        "scope": "15 moderate standardized finite cases; tail bound does not certify Simpson discretization error"}

    limits = []
    for mean in (-2.0, 0.0, 2.0):
        exact = ei_min(mean, 0, 0)
        assert exact == max(-mean, 0)
        small = [ei_min(mean, sd, 0) for sd in (0.1, 0.01, 0.001)]
        limits.append({"mean": mean, "incumbent": 0, "sd_zero": exact,
                       "sd_sequence": [0.1, 0.01, 0.001], "values": small})
    for args in [(0, -1, 0), (float("nan"), 1, 0), (0, float("inf"), 0)]:
        try:
            ei_min(*args)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid scalar accepted")
    results["zero_variance"] = {"cases": limits,
        "inference": "General zero-sd EI is max(incumbent-mean,0), not always zero. A deterministic sampled value is >= the sampled minimum, so its EI is zero."}

    identities = []
    for mean, sd, best in [(-1.5, 0.3, -1), (2.0, 1.2, 0), (0, 0, 1), (1, 0, 0)]:
        minimum = ei_min(mean, sd, best)
        maximum_of_negated = ei_max(-mean, sd, -best)
        close(minimum, maximum_of_negated)
        a, b = 3.0, -7.0
        transformed = ei_min(a * mean + b, a * sd, a * best + b)
        close(transformed, a * minimum)
        identities.append({"mean": mean, "sd": sd, "incumbent": best,
                           "min_ei": minimum, "negated_max_ei": maximum_of_negated,
                           "positive_affine_ei": transformed, "a": a, "b": b})
    results["sign_and_affine"] = identities

    derivatives = []
    for mean, sd, best in [(-0.5, 0.7, 0.2), (1, 2, -0.2), (0, 1, 0)]:
        h = 1e-5
        dm = (ei_min(mean + h, sd, best) - ei_min(mean - h, sd, best)) / (2 * h)
        ds = (ei_min(mean, sd + h, best) - ei_min(mean, sd - h, best)) / (2 * h)
        z = (best - mean) / sd
        close(dm, -Phi(z), 1e-9)
        close(ds, phi(z), 1e-9)
        derivatives.append({"mean": mean, "sd": sd, "incumbent": best,
                            "d_mean_finite_difference": dm, "d_mean_formula": -Phi(z),
                            "d_sd_finite_difference": ds, "d_sd_formula": phi(z)})
    upper = ei_min(-2, 3, 0)
    grid = [ei_min(mean, sd, 0) for mean in (-2, -1, 0, 2) for sd in (0, 0.1, 1, 3)]
    assert all(x <= upper + 1e-12 for x in grid)
    results["monotonicity"] = {"derivatives": derivatives, "finite_rectangle_upper": upper,
        "grid_case_count": len(grid), "limits": "Requires valid lower bound for mean and upper bound for sd; does not establish any EGO bounding routine."}

    # Source-compatible p=1 product-exponential correlations: observed (0,0),
    # (2,0), candidate (1,3), both theta=log(2)/2 give R01=1/2 and r=(1/4,1/4).
    # theta is fixed here: this is NOT a hyperparameter maximum-likelihood fit.
    R = [[F(1), F(1, 2)], [F(1, 2), F(1)]]
    Rinv = [[F(4, 3), F(-2, 3)], [F(-2, 3), F(4, 3)]]
    ones, y = [F(1), F(1)], [F(0), F(2)]
    denom = dot(ones, mv(Rinv, ones))
    mean = dot(ones, mv(Rinv, y)) / denom
    residual = [v - mean for v in y]
    sigma2 = dot(residual, mv(Rinv, residual)) / len(y)
    def predict(r):
        ri = mv(Rinv, r)
        predicted = mean + dot(r, mv(Rinv, residual))
        variance = sigma2 * (1 - dot(r, ri) + (1 - dot(ones, ri)) ** 2 / denom)
        return predicted, variance
    samples = [predict([R[j][i] for j in range(2)]) for i in range(2)]
    assert samples == [(F(0), F(0)), (F(2), F(0))]
    candidate = predict([F(1, 4), F(1, 4)])
    assert (mean, sigma2, candidate) == (F(1), F(2), (F(1), F(5, 2)))
    known_mean_variance = sigma2 * (1 - dot([F(1, 4)] * 2, mv(Rinv, [F(1, 4)] * 2)))
    assert known_mean_variance == F(11, 6)
    results["ordinary_kriging_exact"] = {"fixed_correlation_parameters": True,
        "mean": str(mean), "process_variance": str(sigma2),
        "sample_predictions": [[str(a), str(b)] for a, b in samples],
        "candidate_mean": str(candidate[0]), "candidate_variance": str(candidate[1]),
        "variance_omitting_unknown_mean_term": str(known_mean_variance),
        "inference": "Eq.9 includes constant-mean estimation uncertainty; no generic process-variance upper bound. Nonsingular exact-arithmetic interpolation gives zero sampled-point EI."}

    # Fixed known latent function equals the known incumbent. Observational
    # noise is hypothetical; the 1998 article does not prescribe this extension.
    noise = [{"noise_sd": tau, "latent_ei": 0.0,
              "measurement_ei": ei_min(0, tau, 0), "tau_over_sqrt_2pi": tau * phi(0)}
             for tau in (0.0, 0.5, 2.0)]
    for row in noise:
        close(row["measurement_ei"], row["tau_over_sqrt_2pi"])
    uncertain = []
    for correlation in (-1.0, 0.0, 1.0):
        # Two jointly Gaussian latent values both N(0,1), fixed incumbent
        # LOCATION. Improvement E[(F_inc-F_candidate)+] depends on covariance.
        difference_sd = math.sqrt(2 - 2 * correlation)
        uncertain.append({"correlation": correlation,
            "joint_difference_ei": ei_min(0, difference_sd, 0),
            "plug_in_incumbent_mean_ei": ei_min(0, 1, 0)})
    assert uncertain[0]["joint_difference_ei"] > uncertain[1]["joint_difference_ei"] > uncertain[2]["joint_difference_ei"]
    results["noise_and_uncertain_incumbent"] = {"known_latent_equal_incumbent": noise,
        "joint_gaussian_fixed_incumbent_location": uncertain,
        "limits": "Illustrative counterexamples, not a noisy-EI algorithm; a random minimum over several incumbent locations is more complicated still."}

    A = {"mean": -0.1, "sd": 0.01}
    B = {"mean": 0.0, "sd": 1.0}
    for row in (A, B):
        row["PI"] = Phi(-row["mean"] / row["sd"])
        row["EI"] = ei_min(row["mean"], row["sd"], 0)
    assert A["PI"] > B["PI"] and A["EI"] < B["EI"]
    C = {"mean": -2, "sd": 0.01, "EI": ei_min(-2, 0.01, 0)}
    D = {"mean": 3, "sd": 2, "EI": ei_min(3, 2, 0)}
    assert C["sd"] < D["sd"] and C["EI"] > D["EI"]
    results["criterion_distinctions"] = {"PI_and_mean_prefer_A_but_EI_prefers_B": [A, B],
        "variance_prefers_D_but_EI_prefers_C": [C, D]}

    raw_A, raw_B = F(1), F(1, 10) * 9
    log_A, log_B = math.log(10 / 9), 0.1 * math.log(10)
    assert raw_A > raw_B and log_A < log_B
    fixed_ei, best, offset = 0.5, 10.0, 100.0
    assert not (fixed_ei < 0.01 * best) and fixed_ei < 0.01 * (best + offset)
    results["nonlinear_transform_and_stopping"] = {
        "positive_two_candidate_distributions": {"incumbent": 10,
            "A": "Y=9 with probability 1", "B": "Y=1 with probability 1/10 and Y=10 otherwise",
            "raw_EI_A": str(raw_A), "raw_EI_B": str(raw_B), "log_EI_A": log_A, "log_EI_B": log_B},
        "translation_sensitive_literal_relative_stop": {"EI": fixed_ei, "best": best,
            "additive_offset": offset, "stop_before": False, "stop_after": True},
        "limits": "Nonlinear example is discrete, not Gaussian. It isolates magnitude/ranking, not the effect of refitting a transformed DACE model. Literal relative-threshold ambiguity is not repaired here."}
    print(json.dumps(results, indent=2, sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
