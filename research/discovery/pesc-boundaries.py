"""Original bounded PESC source/identity diagnostics; no optimizer or EP solver.

Derived from fully read official ICML2015 main/supplement and selectively read
JMLR2016 core/appendix. Rational checks are exact; Gaussian/log arithmetic uses
binary64 with rel_tol=0, abs_tol=2e-14 where isclose is needed. Deliberately
printed source formulas are negative controls, not repaired author software.
No external implementation or model code is imported.
"""
from fractions import Fraction as F
from itertools import product
import json
import math


def ent(ps):
    return -sum(float(p) * math.log(float(p)) for p in ps if p)


def close(a, b):
    assert math.isclose(a, b, rel_tol=0.0, abs_tol=2e-14), (a, b)


def calculate():
    # Exact minimizer membership indicators, including c=0, ties and emptiness.
    counts = {'total': 0, 'unique_minimizer': 0, 'tied_minimizers': 0, 'empty_feasible_set': 0}
    for f0, f1, c0, c1 in product([-1, 0, 1], repeat=4):
        fs, cs = [f0, f1], [c0, c1]
        feasible = [i for i in range(2) if cs[i] >= 0]
        minimizers = [] if not feasible else [i for i in feasible if fs[i] == min(fs[j] for j in feasible)]
        indicated = [i for i in range(2) if cs[i] >= 0 and all(cs[j] < 0 or fs[j] >= fs[i] for j in range(2))]
        assert indicated == minimizers
        counts['total'] += 1
        counts['empty_feasible_set' if not minimizers else 'unique_minimizer' if len(minimizers) == 1 else 'tied_minimizers'] += 1
    assert counts == {'total': 81, 'unique_minimizer': 60, 'tied_minimizers': 12, 'empty_feasible_set': 9}

    # Independent binary signs U=[objective difference >=0], V=[constraint >=0].
    # A fixed feasible baseline is optimizer S=0 unless competitor is feasible
    # and strictly better, (U,V)=(0,1). This is a finite logical witness, not GP fit.
    joint = [(u, v, 0 if (u == 1 or v == 0) else 1, F(1, 4)) for u, v in product([0, 1], repeat=2)]
    hs = ent([F(3, 4), F(1, 4)])
    i_s_u = hs - F(1, 2) * math.log(2)
    i_s_v = i_s_u
    joint_info = hs
    conditional_e_cov = F(1, 3) - F(2, 3) * F(1, 3)
    assert conditional_e_cov == F(1, 9) and joint_info > i_s_u + i_s_v
    conditional_mi = 2 * ent([F(1, 3), F(2, 3)]) - math.log(3)
    close(joint_info - i_s_u - i_s_v, float(F(3, 4)) * conditional_mi)
    # Same coupling for independent standard-Gaussian Delta,C under Psi:
    # P(E)=3/4, E[Delta]=2phi(0)/3, E[C]=-2phi(0)/3,
    # E[Delta*C]=2/(3pi), so Cov=8/(9pi)>0.
    phi0 = 1 / math.sqrt(2 * math.pi)
    delta_mean = 2 * phi0 / 3
    c_mean = -delta_mean
    gaussian_cov = 2 / (3 * math.pi) - delta_mean * c_mean
    close(gaussian_cov, 8 / (9 * math.pi))

    # Log-variance scale in main2015 Eqs8/16 vs proper Gaussian entropy.
    actual_entropy_gain = 0.5 * math.log(4 / 1)
    printed_gain = math.log(4 / 1)
    close(printed_gain, 2 * actual_entropy_gain)

    # Gaussian quotient natural parameters: q=N(2,3), site precision1/6,
    # site linear parameter1/3. Positive cavity precision remains1/6.
    mu, var, site_prec, site_linear = F(2), F(3), F(1, 6), F(1, 3)
    cavity_var = 1 / (1 / var - site_prec)
    natural_diff = mu / var - site_linear
    cavity_mean = cavity_var * natural_diff
    original_printed_mean = 1 / natural_diff  # supp2015 Eq18, alsoEq28 form
    later_printed_mean = cavity_var / natural_diff  # JMLR2016 Eq39 form
    assert (cavity_var, cavity_mean, original_printed_mean, later_printed_mean) == (F(6), F(2), F(3), F(18))

    # Conditional total variance is residual plus propagated latent variance.
    # For K=1,kxx=1,kcross=1,V=1, reproducing the prior must give1.
    # Both printed propagation braces use plus inside the outer subtraction.
    propagation = []
    for vpost in [F(1), F(1, 2)]:
        correct = F(1) - F(1) + vpost
        printed = F(1) - (F(1) + vpost)
        assert correct == vpost and printed < 0
        propagation.append({'latent_variance': str(vpost), 'direct_total_variance': str(correct), 'printed_variance': str(printed)})

    # One-sided feasible Gaussian: C~N(0,1), C>=0.
    mills = 2 * phi0
    positive_var = 1 - mills * mills
    correct_site_precision = 1 / positive_var - 1
    printed_2015_precision = -1 / (1 / mills + 1)  # supp2015 Eq30 uses first derivative
    assert correct_site_precision > 0 > printed_2015_precision
    printed_2016_logz_mean_derivative = (0.5 - 1) * phi0 / (0.5 * 0.5)  # Eq54
    close(printed_2016_logz_mean_derivative, -mills)
    assert mills > 0 > printed_2016_logz_mean_derivative

    # Final candidate constraint marginal for independent Delta,C~N(0,1).
    # Under E: Delta>=0 OR C<0, E[C^2]=1, mean=-2phi0/3.
    exact_candidate_var = 1 - c_mean * c_mean
    hessian = -c_mean * c_mean
    direct_moment_variance = 1 + hessian
    close(exact_candidate_var, direct_moment_variance)
    printed_candidate_site_precision = -1 / (hessian + 1)  # missing inverse Hessian, suppp9/JMLR Eq62
    printed_candidate_var = 1 / (1 + printed_candidate_site_precision)
    assert exact_candidate_var > 0 > printed_candidate_var

    # Printed powered-factor SUM violates epsilon=1 no-damping claim even
    # up to proportional normalization: choose new-factor values1 and1/4.
    damping_ratios = [((a + 1) / a) for a in [F(1), F(1, 4)]]
    assert damping_ratios == [F(2), F(5)]

    # Later main Eq10 defines K as noise-free but omits training-noise term;
    # later Appendix A Eq29 explicitly includes it. One training point K=1,
    # kcross=1, kxx=1, observation variance1 gives predictive observation1.5.
    correct_noisy_predictive = F(1) - F(1) / (F(1) + F(1)) + F(1)
    literal_noiseless_matrix = F(1) - F(1) / F(1) + F(1)
    assert (correct_noisy_predictive, literal_noiseless_matrix) == (F(3, 2), F(1))

    # Constrained optimum of f(x)=x,c(x)=x-1/2 on[0,1] is1/2 with df/dx=1.
    boundary = {'domain': '[0,1]', 'objective': 'f(x)=x', 'constraint': 'c(x)=x-1/2>=0', 'unique_minimizer': '1/2', 'objective_gradient': '1', 'consequence': 'A constrained optimum need not have zero objective gradient; no optimizer execution used.'}
    return {
        'scope': 'Ten bounded diagnostic categories. Not an EP implementation, full formula audit, GP training, optimizer, convergence or performance test.',
        'arithmetic': 'Fraction for discrete and Gaussian natural-parameter identities; binary64 elementary functions for entropy/Gaussian constants; all isclose checks rel_tol=0 abs_tol=2e-14.',
        'category_count': 10,
        'finite_minimizer_indicator_cases': counts,
        'conditional_coupling': {'finite_states': [{'u':u,'v':v,'optimizer_s':s,'probability':str(w)} for u,v,s,w in joint], 'optimizer_entropy':hs, 'joint_information':joint_info, 'sum_separate_information':i_s_u+i_s_v,'conditional_indicator_covariance_given_s0':str(conditional_e_cov),'conditional_sign_information_given_s0':conditional_mi,'gaussian_conditional_mean_delta':delta_mean,'gaussian_conditional_mean_constraint':c_mean,'gaussian_conditional_covariance':gaussian_cov,'gaussian_covariance_exact_expression':'8/(9*pi)'},
        'entropy_half_factor': {'correct_gain':actual_entropy_gain,'printed2015_gain':printed_gain,'relation':'printed2015 gain is twice the Gaussian information approximation; common positive scaling leaves argmax unchanged'},
        'gaussian_cavity': {'cavity_variance':str(cavity_var),'correct_cavity_mean':str(cavity_mean),'supp2015_Eq18_literal_mean':str(original_printed_mean),'jmlr2016_Eq39_literal_mean':str(later_printed_mean)},
        'gaussian_propagation': propagation,
        'positive_feasibility_site': {'correct_logz_mean_derivative':mills,'jmlr2016_Eq54_literal_derivative':printed_2016_logz_mean_derivative,'correct_site_precision':correct_site_precision,'supp2015_Eq30_literal_precision':printed_2015_precision},
        'candidate_constraint_moment': {'correct_variance':exact_candidate_var,'direct_moment_variance':direct_moment_variance,'printed_variance':printed_candidate_var,'interpretation':'Uses zero standardized means, resolving the source beta subscript ambiguity identically; printed missing inverse-Hessian expression gives a negative variance.'},
        'damping_epsilon_one': {'printed_to_new_factor_ratios':[str(x) for x in damping_ratios],'consequence':'Different ratios at two inputs refute equality even up to a normalization constant.'},
        'training_noise': {'correct_noisy_predictive_variance':str(correct_noisy_predictive),'literal2016_main_Eq10_variance':str(literal_noiseless_matrix)},
        'constrained_boundary': boundary,
        'limits':['The indicator enumeration returns every tied minimizer; it does not supply a tie policy or a normalized optimizer density.','Empty feasible posterior draws require a model/algorithm policy; none is invented here.','The Gaussian coupling example is one finite conditional event, not a full PESC posterior calculation.','Printed-formula counterexamples preserve source caveats; no repaired full EP algorithm or author implementation is certified.','Later2016 report is selectively read, not all53 pages.']
    }


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2, sort_keys=True))
