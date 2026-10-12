"""Exact, curator-derived boundary examples; not a replication of paper experiments."""
from fractions import Fraction as F
import json

# Fixed-parameter two-sample predictor: yhat_t=b*x_t+c*epsilon_(t-1).
# x=(1,4) can arise from squared lagged inputs; epsilon_0=0.
b = c = F(1, 2)
x1, x2, y1, y2 = map(F, (1, 4, 1, 3))
e1 = y1-b*x1
phi1, phi2 = (x1, F(0)), (x2, e1)
psi2 = tuple(phi2[i]-c*phi1[i] for i in range(2))
# Direct differentiation of yhat_2=b*x2+c*(y1-b*x1).
direct = (x2-c*x1, y1-b*x1)
assert psi2 == direct == (F(7, 2), F(1, 2))
assert phi2 == (F(4), F(1, 2)) and phi2 != psi2
e2 = y2-(b*x2+c*e1)
assert e2 == F(3, 4)

def inverse_update(v, lam=F(1)):
    """Equation 21, P_previous=I; return new P and one update increment."""
    den = lam+sum(z*z for z in v)
    p = [[((F(i == j)-v[i]*v[j]/den)/lam) for j in range(2)] for i in range(2)]
    delta = tuple(sum(p[i][j]*v[j] for j in range(2))*e2 for i in range(2))
    return p, delta

ppsi, dpsi = inverse_update(psi2)
pphi, dphi = inverse_update(phi2)
assert dpsi == (F(7,36), F(1,36))
assert dphi == (F(4,23), F(1,46)) and dphi != dpsi
# One common-state update comparison, not two complete adaptive trajectories.
# R_previous=I, gamma_previous=1, gamma_current=1/2 -> lambda=1.
def inverse2(m):
    det = m[0][0]*m[1][1]-m[0][1]*m[1][0]
    assert det != 0
    return [[m[1][1]/det,-m[0][1]/det],[-m[1][0]/det,m[0][0]/det]]
r = [[(F(i == j)+psi2[i]*psi2[j])/2 for j in range(2)] for i in range(2)]
assert [[z/2 for z in row] for row in inverse2(r)] == ppsi
# An invertible constant noise filter need not satisfy the stronger RELS condition.
# C(q^-1)=(1+0.9*q^-1)^2; C*(s)=(s+0.9)^2 has both roots -0.9.
root = -F(9,10)
assert abs(root) < 1
c_at_zero_frequency = (1+F(9,10))**2
positive_real_test = 1/c_at_zero_frequency-F(1,2)
assert positive_real_test == -F(161,722) < 0

# Pointwise multiplier <1 is not a uniform contraction proof for a nonlinear map.
# q(z)=z*(0.9+z^2)/(1+z^2), a specialization of source Eq.77 at y_previous=0.
z = F(2)
multiplier = (F(9,10)+z*z)/(1+z*z)
derivative = 1-F(1,10)*(1-z*z)/(1+z*z)**2
assert multiplier == F(49,50) < 1 and derivative == F(253,250) > 1
# This local derivative observation does not refute asymptotic invertibility.
print(json.dumps(dict(
    fixed_parameter_sensitivity=list(map(str,psi2)),
    raw_regressor=list(map(str,phi2)),
    common_state_rpe_increment=list(map(str,dpsi)),
    common_state_plr_increment=list(map(str,dphi)),
    covariance_inverse_forms_agree=True,
    invertible_noise_roots=[str(root),str(root)],
    strict_positive_real_test_at_zero=str(positive_real_test),
    rational_noise_multiplier=str(multiplier),
    rational_map_derivative=str(derivative),
    interpretation='Finite exact curator examples; no adaptive trajectories, convergence failure, empirical superiority or source erratum established.'
),indent=2))
