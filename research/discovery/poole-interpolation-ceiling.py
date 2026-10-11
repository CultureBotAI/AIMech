"""Enumerate Poole2019 Eq. (11) on a finite joint distribution; no fitting."""
from itertools import product
from math import log
import json

M, K, ALPHA, OFF_SCORE = 20, 2, 0.5, 1e-6

def ratio(x1, x2, y):
    s1 = 1.0 if x1 == y else OFF_SCORE
    s2 = 1.0 if x2 == y else OFF_SCORE
    return s1 / (ALPHA * (s1 + s2) / K + (1 - ALPHA) / M)

joint = sum(log(ratio(x1, x2, x1)) for x1, x2 in product(range(M), repeat=2)) / M**2
product_term = sum(ratio(x1, x2, y) for x1, x2, y in product(range(M), repeat=3)) / M**3
value = 1 + joint - product_term
result = dict(M=M, K=K, alpha=ALPHA, exp_f_equal=1.0, exp_f_unequal=OFF_SCORE,
              q_y=1/M, joint_log_ratio=joint, product_ratio=product_term,
              I_alpha=value, stated_ceiling=log(K/ALPHA),
              conservative_ceiling=1+log(K/ALPHA), true_MI=log(M))
assert result['stated_ceiling'] < value < result['conservative_ceiling'] < result['true_MI']
if __name__ == '__main__':
    print(json.dumps(result, indent=2))
