"""Finite curator checks of PPCA, principal curves and Oja learning.

Only scalar/vector arithmetic and analytic distribution moments are used.
These checks do not train models or reproduce the papers' empirical results.
"""
import json
import math


def close(a, b, tol=1e-11):
    assert math.isclose(a, b, rel_tol=tol, abs_tol=tol), (a, b)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def ppca_score(spectrum, loading, noise):
    # Centered covariance diagonal; one loading along its first axis.
    c = [loading**2 + noise, *([noise] * (len(spectrum)-1))]
    return sum(math.log(v) + s/v for s, v in zip(spectrum, c))


# PPCA: a diagonal covariance gives an exact, nondegenerate analytic example.
spectrum = [9.0, 4.0, 1.0]
noise = sum(spectrum[1:])/2
loading = math.sqrt(spectrum[0]-noise)
mean = loading*3/9
posterior_variance = noise/9
reconstruction = loading*mean
close(reconstruction, 13/6)
assert reconstruction < 3.0  # Orthogonal PCA reconstruction is (3,0,0).
close((loading/noise*posterior_variance)*3, mean)
close(loading/(loading**2)*9*mean, 3.0)
optimum_score = ppca_score(spectrum, loading, noise)
# Exact EM moments for old loading=1 and old variance=2.
old_w, old_noise = 1.0, 2.0
old_m = old_w**2 + old_noise
cross = spectrum[0]*old_w/old_m
second = old_noise/old_m + spectrum[0]*old_w**2/old_m**2
new_w = cross/second
new_noise = (sum(spectrum)-2*new_w*cross+new_w**2*second)/3
compact_noise = (sum(spectrum)-spectrum[0]*old_w/old_m*new_w)/3
close(new_w, 1.8)
close(new_noise, 43/15)
close(new_noise, compact_noise)
old_score = ppca_score(spectrum, old_w, old_noise)
new_score = ppca_score(spectrum, new_w, new_noise)
assert old_score > new_score > optimum_score  # Minus twice log likelihood/N, up to an additive constant.
# Zero loadings are a fixed EM point, even though this solution is worse.
zero_noise = sum(spectrum)/3
zero_new_w = 0.0/(1.0)
close(zero_new_w, 0)
zero_score = ppca_score(spectrum, 0, zero_noise)
assert zero_score > optimum_score
# Source's (2,1,1), q=2 example has a zero second loading.
tied_spectrum = [2.0, 1.0, 1.0]
tied_noise = tied_spectrum[-1]
tied_squared_loadings = [v-tied_noise for v in tied_spectrum[:2]]
assert tied_squared_loadings == [1.0, 0.0]
# Sign is a one-dimensional orthogonal latent rotation; covariance unchanged.
close(loading**2 + noise, (-loading)**2 + noise)

# Principal curves: independent centered Gaussian coordinates are self-consistent
# along either coordinate line, yet squared-distance risks differ (4 versus 1).
line_risks = {'first_axis': 1.0, 'second_axis': 4.0}
assert line_risks['second_axis'] > line_risks['first_axis']
# A top PCA line need not be self-consistent. X~Uniform(-1,1),
# Y=X^2-1/3+epsilon with independent centered Gaussian variance 0.01.
# This is a two-dimensional density, unlike a noiseless parabolic point set.
var_x, var_y, covariance = 1/3, 1/5-1/9+0.01, 0.0
assert var_x > var_y and covariance == 0
conditional_y_at_zero = -1/3
assert conditional_y_at_zero != 0
# On the positive-probability interval abs(X)<1/2, this mean is <= -1/12.
assert 0.5**2-1/3 < 0
assert (0.5-(-0.5))/2 == 0.5
# For the paper's CLOSED-CURVE extension under a 2D standard Gaussian,
# E(radius)=sqrt(pi/2), E(radius^2)=2; distance is Var(radius).
circle_radius = math.sqrt(math.pi/2)
circle_risk = 2 - math.pi/2
assert 0 < circle_risk < 1
# Arc averaging alone multiplies a circle radius by sinc(theta/2).
theta = math.pi/2
smoothing_factor = math.sin(theta/2)/(theta/2)
assert 0 < smoothing_factor < 1

# Oja: the truncated rule differs from explicit normalized Hebbian learning.
w, x, gain = [1.0, 0.0], [1.0, 2.0], 0.1
y = dot(w, x)
oja = [wi+gain*y*(xi-y*wi) for wi, xi in zip(w, x)]
hebb = [wi+gain*y*xi for wi, xi in zip(w, x)]
hebb_norm = math.sqrt(dot(hebb, hebb))
normalized = [v/hebb_norm for v in hebb]
close(dot(oja, oja), 1.04)
close(dot(normalized, normalized), 1)
assert oja != normalized
# A large scalar update can grow absolute weight instead of regulating it.
large_old, large_x, large_gain = 2.0, 1.0, 1.0
large_y = large_old*large_x
large_new = large_old+large_gain*large_y*(large_x-large_y*large_old)
close(large_new, -4.0)
assert abs(large_new) > abs(large_old)
# Uncentered second moment can select a different leading direction.
centered_covariance = [1.0, 3.0]
mean_input = [2.0, 0.0]
second_moment = [v+m*m for v, m in zip(centered_covariance, mean_input)]
assert centered_covariance.index(max(centered_covariance)) == 1
assert second_moment.index(max(second_moment)) == 0
# Mean ODE: a subleading eigenvector and zero remain stationary.
c = [4.0, 1.0]
def drift(z):
    cz = [v*zi for v, zi in zip(c, z)]
    energy = dot(z, cz)
    return [v-energy*zi for v, zi in zip(cz, z)]
assert drift([0, 1]) == [0, 0]
assert drift([0, 0]) == [0, 0]
# Analytic unit-sphere ODE flow gives the eigenvalue-gap ratio law.
z0, t = [0.8, 0.6], 0.5
raw = [zi*math.exp(v*t) for v, zi in zip(c, z0)]
scale = math.sqrt(dot(raw, raw));zt = [v/scale for v in raw]
close(zt[1]/zt[0], (z0[1]/z0[0])*math.exp((c[1]-c[0])*t))
close(dot(zt, drift(zt)), 0)

print(json.dumps({
    'ppca': {'noise_variance': noise, 'posterior_variance': posterior_variance,
             'posterior_mean_reconstruction_first_coordinate': reconstruction,
             'orthogonal_reconstruction_first_coordinate': 3.0,
             'old_score': old_score, 'new_score': new_score,
             'optimal_score': optimum_score, 'zero_loading_score': zero_score,
             'em_loading': new_w, 'em_noise': new_noise,
             'tied_squared_loadings': tied_squared_loadings},
    'principal_curves': {'self_consistent_line_risks': line_risks,
                         'pca_line_counterexample_variances': [var_x, var_y],
                         'conditional_y_at_x_zero': conditional_y_at_zero,
                         'closed_curve_radius': circle_radius,
                         'closed_curve_risk': circle_risk,
                         'arc_smoothing_factor': smoothing_factor},
    'oja': {'truncated_norm_squared': dot(oja, oja),
            'exact_normalized_norm_squared': dot(normalized, normalized),
            'large_gain_scalar_update': large_new,
            'centered_covariance': centered_covariance,
            'uncentered_second_moment': second_moment,
            'ode_ratio_at_half': zt[1]/zt[0]},
    'scope': 'Finite arithmetic and analytic moments only; no training, source code or empirical reproduction.'
}, indent=2))
