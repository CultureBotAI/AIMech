"""Exact curator calculations for generalized-CVM and CVR boundaries.
No historical implementation, numerical optimizer or benchmark is executed.
"""
from fractions import Fraction as F
import json

def quadratic(a, k):
    return sum(a[i] * k[i][j] * a[j] for i in range(len(a)) for j in range(len(a)))

def regression_case(c):
    mu = F(1)
    a = [F(1, 2), F(1, 2)]
    k = [[1 + mu / c, F(-1)], [F(-1), 1 + mu / c]]
    q = quadratic(a, k)
    width = -c * q
    slacks = [mu * x for x in a]
    primal = c / mu * sum(x * x for x in slacks) + 2 * c * width
    dual = -q
    assert width == F(-1, 2)
    assert primal == c * c * dual == -c * mu / 2
    assert all(width + x == 0 for x in slacks)
    paired = sum(slacks)
    usual_loss = max(-width, F(0))
    assert paired == mu and usual_loss == mu / 2
    # q(t) = 4*(t-1/2)^2 + (mu/c)*(t^2+(1-t)^2).
    # Thus t=1/2 is the global simplex minimum, not a guessed stationary point.
    for t in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
        assert quadratic([t, 1-t], k) == 4 * (t-F(1, 2)) ** 2 + mu/c*(t*t+(1-t)**2)
    return dict(C=str(c), transformed_kernel=[[str(v) for v in row] for row in k], alpha=[str(x) for x in a], width=str(width), primal=str(primal), scaled_dual=str(c*c*dual), unscaled_dual=str(dual), mean_paired_slack=str(paired), usual_width_loss=str(usual_loss))

def shifted_stopping():
    # Base points0,2, K=[[0,0],[0,4]], linear term b=diagK.
    # Exact objective4t-4t^2 has optimum1 at t=1/2 for every eta.
    k = [[F(0),F(0)],[F(0),F(4)]]
    b = [F(0),F(4)]
    a = [F(1,2),F(1,2)]
    optimum = sum(x*y for x,y in zip(a,b))-quadratic(a,k)
    assert optimum == 1
    eta=F(10000); epsilon=F(1,1000)
    delta = [b[i]-k[i][i]+eta for i in range(2)]
    assert delta == [eta,eta]
    core_radius2=eta
    farthest2=eta+4
    expanded_radius2=(1+epsilon)**2*core_radius2
    assert farthest2 <= expanded_radius2
    assert core_radius2 <= optimum+eta <= expanded_radius2
    # At eta0, the identical one-point core has radius0 and fails the test.
    assert F(4) > (1+epsilon)**2*0
    return dict(eta=str(eta),epsilon=str(epsilon),core_center='0',optimal_center='1',core_unshifted_objective='0',optimal_unshifted_objective='1',core_radius_squared=str(core_radius2),optimal_radius_squared=str(optimum+eta),farthest_squared_distance=str(farthest2),expanded_radius_squared=str(expanded_radius2),same_core_fails_at_eta_zero=True)

if __name__ == '__main__':
    print(json.dumps(dict(status='passed',regression=[regression_case(F(1)),regression_case(F(2))],shifted_stopping=shifted_stopping(),scope='Exact rational algebra only; no optimizer, model, library runtime or benchmark execution.'),indent=2))
