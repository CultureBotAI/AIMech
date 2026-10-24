#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 724: PTR (Han et al., AI Open 2022)."""

import math


def verify_ptr() -> None:
    # 1. Conjunctive Normal Form (CNF) rule composition of sub-prompts (Section 3.1-3.3, Eq. 1-6):
    # Disambiguate "person:parent" vs. "organization:parent" via 3 masked positions:
    # [MASK]_1: subject entity type f_{e_s} in {"person", "organization"}
    # [MASK]_2: relation phrase f_{e_s, e_o} in {"'s parent was", "was born in", "was founded by"}
    # [MASK]_3: object entity type f_{e_o} in {"person", "organization", "country"}
    p_m1 = {"person": 0.85, "organization": 0.15}
    p_m2 = {"'s parent was": 0.80, "was born in": 0.12, "was founded by": 0.08}
    p_m3 = {"person": 0.82, "organization": 0.10, "country": 0.08}

    # Joint class probability (Eq. 5): p(y | x) = prod_{j=1}^n p([MASK]_j = phi_j(y) | T(x))
    rules = {
        "per:parents": ("person", "'s parent was", "person"),
        "org:parents": ("organization", "'s parent was", "organization"),
        "per:country_of_birth": ("person", "was born in", "country"),
        "org:founded_by": ("organization", "was founded by", "person"),
    }
    class_probs = {
        rel: p_m1[m1] * p_m2[m2] * p_m3[m3]
        for rel, (m1, m2, m3) in rules.items()
    }
    assert max(class_probs, key=class_probs.get) == "per:parents"
    assert math.isclose(class_probs["per:parents"], 0.85 * 0.80 * 0.82, rel_tol=1e-12)
    assert class_probs["per:parents"] > 5.0 * class_probs["org:parents"]
    print("PTR verification passed.")


if __name__ == "__main__":
    verify_ptr()
