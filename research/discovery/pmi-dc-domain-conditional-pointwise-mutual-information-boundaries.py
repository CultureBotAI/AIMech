#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 730: Domain Conditional PMI (Holtzman et al., EMNLP 2021)."""

import math


def verify_pmi_dc() -> None:
    # 1. Surface Form Competition & Domain Conditional PMI (Section 3.2 & Section 5.2):
    # Premise x: "The bar closed because"
    # Domain Premise x_domain: "because"
    # Option y_1 (incorrect but common surface form): "it was crowded."
    # Option y_2 (correct): "it was 3 AM."
    # Option y_2' (perturbed correct surface form competing with y_2): "it was 3:30AM."
    log_p_y_given_x = {"y1": -14.0, "y2": -16.0, "y2_prime": -20.0}
    log_p_y_given_domain = {"y1": -11.5, "y2": -15.5, "y2_prime": -19.5}

    # Direct LM probability argmax_i P(y_i | x) picks the wrong answer y_1:
    assert log_p_y_given_x["y1"] > log_p_y_given_x["y2"] > log_p_y_given_x["y2_prime"]

    # Domain Conditional PMI: PMI_DC(x, y, domain) = log (P(y | x) / P(y | x_domain)) = log P(y | x) - log P(y | x_domain)
    pmi_dc = {
        k: log_p_y_given_x[k] - log_p_y_given_domain[k]
        for k in log_p_y_given_x
    }
    # Both y_2 and y_2' beat y_1 under PMI_DC and attain invariant scores despite surface-form rarity!
    assert pmi_dc["y2"] > pmi_dc["y1"]
    assert pmi_dc["y2_prime"] > pmi_dc["y1"]
    assert math.isclose(pmi_dc["y2"], pmi_dc["y2_prime"], rel_tol=1e-12)

    # 2. Symmetry of PMI_DC and equivalence to Scoring-by-Premise P(x | y_i, domain) (Section 5.1):
    # P(y_i | x, domain) / P(y_i | domain) = P(x | y_i, domain) / P(x | domain)
    p_x_domain = 1e-5
    p_y_domain = {"y1": math.exp(-11.5), "y2": math.exp(-15.5)}
    p_joint = {k: math.exp(log_p_y_given_x[k]) * p_x_domain for k in ("y1", "y2")}
    p_x_given_y = {k: p_joint[k] / p_y_domain[k] for k in ("y1", "y2")}
    for k in ("y1", "y2"):
        lhs = math.exp(pmi_dc[k])
        rhs = p_x_given_y[k] / p_x_domain
        assert math.isclose(lhs, rhs, rel_tol=1e-12)
    print("Domain Conditional PMI verification passed.")


if __name__ == "__main__":
    verify_pmi_dc()
