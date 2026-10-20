#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 537:
Lagrange Coded Computing (LCC): Optimal Design for Resiliency, Security, and Privacy
(Yu, Li, Raviv, Mousavi Kalan, Soltanolkotabi, & Avestimehr, AISTATS 2019, PMLR 89:1215-1225).
"""

import itertools

MOD = 17


def mod_inv(a, p=MOD):
    return pow(a % p, p - 2, p)


def lagrange_eval(betas, values, z, p=MOD):
    """Evaluate Lagrange interpolation polynomial u(z) over F_p where u(betas[j]) = values[j]."""
    total = 0
    m = len(betas)
    for j in range(m):
        num = 1
        den = 1
        for k in range(m):
            if k != j:
                num = (num * (z - betas[k])) % p
                den = (den * (betas[j] - betas[k])) % p
        term = (values[j] * num * mod_inv(den, p)) % p
        total = (total + term) % p
    return total


def interpolate_poly_coeffs(xs, ys, deg, p=MOD):
    """Interpolate polynomial of degree <= deg from len(xs) = deg + 1 points over F_p."""
    # Evaluate polynomial at any target z directly via lagrange_eval
    assert len(xs) == deg + 1
    return xs, ys


def reed_solomon_decode_eval(alphas_resp, y_resp, deg, max_errors, target_betas, p=MOD):
    """Find the unique degree <= deg polynomial agreeing with y_resp on at least
    len(alphas_resp) - max_errors points, and evaluate it at target_betas.
    """
    n_resp = len(alphas_resp)
    req = deg + 1
    for subset_idxs in itertools.combinations(range(n_resp), req):
        sub_a = [alphas_resp[i] for i in subset_idxs]
        sub_y = [y_resp[i] for i in subset_idxs]
        # Count how many of the n_resp points lie on this degree <= deg interpolant
        matches = 0
        for i in range(n_resp):
            val = lagrange_eval(sub_a, sub_y, alphas_resp[i], p)
            if val == y_resp[i] % p:
                matches += 1
        if matches >= n_resp - max_errors:
            return [lagrange_eval(sub_a, sub_y, b, p) for b in target_betas]
    raise RuntimeError("Failed to decode Reed-Solomon codeword")


def main():
    # Section IV-A Illustrating Example (p. 6):
    # K = 2 data blocks (X1, X2), T = 1 privacy mask Z3, polynomial f(X) = X^2 (deg f = 2),
    # S = 1 straggler, A = 1 Byzantine adversary.
    K, T, deg_f, S, A = 2, 1, 2, 1, 1
    N_min = (K + T - 1) * deg_f + S + 2 * A + 1
    assert N_min == 8, f"Expected N_min=8 from Theorem 1 Eq. (1), got {N_min}"
    N = 8

    betas = [1, 2, 3]  # in F_17
    alphas = [4, 5, 6, 7, 8, 9, 10, 11]  # disjoint from betas[0:K] = [1, 2]

    # 1. Verify T = 1 information-theoretic privacy (Lemma 2, p. 6 & 11):
    # For any fixed (X1, X2) and any single worker i, as Z3 ranges uniformly over F_17,
    # the coded share tilde_X_i = u(alpha_i) takes every value in F_17 exactly once!
    X1, X2 = 6, 13
    for i in range(N):
        observed_shares = set()
        for z_mask in range(MOD):
            share = lagrange_eval(betas, [X1, X2, z_mask], alphas[i], MOD)
            observed_shares.add(share)
        assert len(observed_shares) == MOD, f"Worker {i} share is not uniform over F_17!"

    # 2. Verify S = 1 straggler resiliency and A = 1 Byzantine security (Theorem 1):
    Z3 = 9
    coded_shares = [lagrange_eval(betas, [X1, X2, Z3], a, MOD) for a in alphas]
    # Each worker computes f(tilde_X_i) = tilde_X_i^2 mod 17 (degree of f(u(z)) is 2*2 = 4)
    worker_outputs = [(x * x) % MOD for x in coded_shares]

    # Suppose worker 7 is a straggler (dropped), and worker 2 is Byzantine (adds +11 mod 17)
    alphas_resp = alphas[:7]
    y_resp = list(worker_outputs[:7])
    y_resp[2] = (y_resp[2] + 11) % MOD

    decoded = reed_solomon_decode_eval(
        alphas_resp, y_resp, deg=(K + T - 1) * deg_f, max_errors=A, target_betas=betas[:K]
    )
    true_y1 = (X1 * X1) % MOD
    true_y2 = (X2 * X2) % MOD
    assert decoded == [true_y1, true_y2], f"Expected {[true_y1, true_y2]}, got {decoded}"

    # 3. Verify Linear Regression recovery threshold R_LCC = 2*ceil(n/r) - 1 vs R_GC = n - r + 1 (Section VI, p. 7)
    n_workers, r_storage = 40, 10
    K_blocks = (n_workers + r_storage - 1) // r_storage
    r_lcc = 2 * K_blocks - 1
    r_gc = n_workers - r_storage + 1
    assert r_lcc == 7 and r_gc == 31 and r_lcc < r_gc

    print(
        f"[PASS] Round 537 LCC verified: N_min={N_min}, T=1 uniform-privacy=17/17, "
        f"decoded={decoded}=={[true_y1, true_y2]}, R_LCC={r_lcc} << R_GC={r_gc}"
    )


if __name__ == "__main__":
    main()
