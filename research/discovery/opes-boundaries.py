"""Original scalar comparison of published OPES/MES approximations.

Not an implementation of either optimizer or EP. With no observed-latent
constraints, pre-truncation N(0,1), threshold m=0 and one fixed threshold term,
OPES moment-matches and uses Gaussian entropy; MES uses truncated entropy.
The zero-noise row is an entropy-stage limiting case, not evaluation of the
source's sigma^-2 site matrix at zero. No expectation over maxima is estimated.
Sources: Hoffman/Ghahramani author-hosted workshop PDF pp2-3 Eqs5-7;
Wang/Jegelka official ICML2017 PDF p3 Eq6. No external code is imported.
"""
import json
import math


def calculate():
    phi0 = 1.0 / math.sqrt(2.0 * math.pi)
    ratio = phi0 / 0.5
    mean = -ratio
    variance = 1.0 - ratio * ratio
    assert math.isclose(variance, 1.0 - 2.0 / math.pi, rel_tol=0.0, abs_tol=2e-14)
    mes = math.log(2.0)
    rows = []
    for noise_variance in [0.0, 1.0]:
        opes = 0.5 * math.log((1.0 + noise_variance) / (variance + noise_variance))
        assert 0.0 < opes < mes
        rows.append({'noise_variance': noise_variance, 'opes_fixed_threshold_gaussian_entropy_term': opes, 'mes_latent_fixed_threshold_term': mes})
    # A moment-matched nondegenerate Gaussian has mass above its truncation bound.
    tail = 0.5 * math.erfc((0.0 - mean) / math.sqrt(2.0 * variance))
    assert 0.0 < tail < 0.5
    return {
        'scope': 'One scalar threshold, two noise values; finite arithmetic diagnostic of different operational entropy approximations, not whole acquisition, exact maximum conditioning, EP, an optimizer, or performance evidence.',
        'arithmetic': 'Python binary64 elementary functions; only isclose check has rel_tol=0 and abs_tol=2e-14; sign/ordering checks are strict.',
        'assumptions': {'pre_truncation_mean': 0.0, 'pre_truncation_variance': 1.0, 'maximum_threshold': 0.0, 'observed_latent_constraints': 'none; empty-data simplification'},
        'upper_truncated_latent_mean': mean,
        'upper_truncated_latent_variance': variance,
        'comparisons': rows,
        'moment_matched_latent_gaussian_mass_above_threshold': tail,
        'limits': ['The sampled global maximum may have a different conditional law from local truncation.', 'A difference in one integrand is not a proof of different argmax decisions for every dataset.', 'The noiseless row bypasses the source matrix formula requiring positive sigma squared.', 'No numerical integration, maximum samples, likelihood fitting or external author code executed.']
    }


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2, sort_keys=True))
