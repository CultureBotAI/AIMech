"""Finite fixed-parameter witnesses; no data fitting or author-code reproduction."""
from itertools import product
from math import cosh, exp, log, pi, prod, tanh
import json


def mean_field_phases():
    # One output y and one hidden h, conditional on any fixed external input.
    # F=J*y*h, |J|<1. The free product-family optimum is m_y=m_h=0:
    # the mean-field fixed-point map is a contraction. Clamped y=+1 is exact.
    j = 0.8
    z_free = sum(exp(j*y*h) for y, h in product((-1, 1), repeat=2))
    z_pos = sum(exp(j*h) for h in (-1, 1))
    exact = log(z_pos / z_free)
    bound_free, bound_pos = 2*log(2), log(z_pos)
    surrogate = bound_pos - bound_free
    assert bound_free < log(z_free) and surrogate > exact
    exact_pos_moment = sum(h*exp(j*h) for h in (-1, 1))/z_pos
    exact_free_moment = sum(y*h*exp(j*y*h) for y, h in product((-1, 1), repeat=2))/z_free
    exact_gradient = exact_pos_moment-exact_free_moment
    mf_gradient = tanh(j)  # clamped 1*tanh(J) minus free 0*0
    eps = 1e-6
    fd = (log(2*cosh(j+eps))-log(2*cosh(j-eps)))/(2*eps)
    assert abs(exact_gradient) < 1e-14 and abs(fd-mf_gradient) < 1e-9
    field = 0.7
    p_plus = exp(field)/(exp(field)+exp(-field))
    correct_heatbath = 1/(1+exp(-2*field))
    displayed_heatbath = 1/(1+exp(field))
    assert abs(p_plus-correct_heatbath) < 1e-14
    assert abs(p_plus-displayed_heatbath) > 0.4
    return dict(exact_log_conditional=exact, difference_of_phase_bounds=surrogate,
                excess_over_true_log_conditional=surrogate-exact,
                exact_gradient=exact_gradient, mean_field_gradient=mf_gradient,
                gradient_finite_difference_error=abs(fd-mf_gradient),
                correct_binary_heatbath=correct_heatbath,
                displayed_baseline_heatbath=displayed_heatbath)


def emission_context():
    # Source's one-sided Gaussian model, with explicit initial law and endpoints.
    n, lag = 5, 2
    initial = {-1: .7, 1: .3}
    transition = {(-1,-1): .8, (-1,1): .2, (1,-1): .3, (1,1): .7}
    u, v = {-1: -.4, 1: .7}, {-1: 1.1, 1: -.2}
    x = (.3, -.8, 1.4)
    states = list(product((-1,1), repeat=n))
    def prior(s, include_initial=True):
        return (initial[s[0]] if include_initial else 1)*prod(transition[s[t],s[t+1]] for t in range(n-1))
    def emission(t,a,b):
        return -.5*log(2*pi)-.5*(x[t]-u[a]-v[b])**2
    def joint_log(s):
        return log(prior(s))+sum(emission(t,s[t],s[t+lag]) for t in range(n-lag))
    # Binary expansion by the four orthogonal basis functions for each factor.
    constant = .5*sum(log(initial[a]) for a in (-1,1))
    unary = [0.0]*n
    unary[0] = .5*sum(a*log(initial[a]) for a in (-1,1))
    edges = {}
    for i,k,table in [(t,t+1,{(a,b):log(transition[a,b]) for a,b in product((-1,1),repeat=2)}) for t in range(n-1)]+[(t,t+lag,{(a,b):emission(t,a,b) for a,b in product((-1,1),repeat=2)}) for t in range(n-lag)]:
        constant += sum(table.values())/4
        unary[i] += sum(a*f for (a,b),f in table.items())/4
        unary[k] += sum(b*f for (a,b),f in table.items())/4
        edges[i,k] = edges.get((i,k),0)+sum(a*b*f for (a,b),f in table.items())/4
    def expanded(s):
        return constant+sum(h*z for h,z in zip(unary,s))+sum(j*s[i]*s[k] for (i,k),j in edges.items())
    error = max(abs(joint_log(s)-expanded(s)) for s in states)
    normalized_prior = sum(prior(s) for s in states)
    no_initial_mass = sum(prior(s,False) for s in states)
    assert abs(normalized_prior-1)<1e-14 and abs(no_initial_mass-2)<1e-14
    assert error < 1e-13
    k = -(u[1]-u[-1])*(v[1]-v[-1])/4
    assert abs(edges[0,2]-k)<1e-14
    # State index2 receives the delayed-emission contribution from observation0.
    delayed = sum(b*emission(0,a,b) for a,b in product((-1,1),repeat=2))/4
    wrong_current = sum(b*emission(2,a,b) for a,b in product((-1,1),repeat=2))/4
    assert abs(delayed-wrong_current)>.1
    weights={(a,b):exp(joint_log((a,-1,b,1,-1))) for a,b in product((-1,1),repeat=2)}
    odds=weights[1,1]*weights[-1,-1]/(weights[1,-1]*weights[-1,1])
    assert abs(odds-exp(4*k))<1e-12
    return dict(hidden_paths=len(states),prior_mass=normalized_prior,
                mass_without_initial_factor=no_initial_mass, expansion_error=error,
                long_range_coupling=k, conditional_odds_ratio=odds,
                delayed_unary=delayed, wrongly_current_indexed_unary=wrong_current,
                observed_sequence_density=sum(exp(joint_log(s)) for s in states))


def memory_context():
    # Fixed prefix length3; condition on that path shape. Fair P emissions,
    # deterministic copying C emissions, one separately normalized active row.
    def output(prefix, mode):
        memory=list(prefix);suffix=[]
        while memory:suffix.append(memory.pop(-1 if mode=='stack' else 0))
        return ''.join(prefix)+''.join(suffix)
    stack={output(p,'stack'):1/8 for p in product('ab',repeat=3)}
    queue={output(p,'queue'):1/8 for p in product('ab',repeat=3)}
    assert sum(stack.values())==sum(queue.values())==1
    assert all(s==s[::-1] for s in stack)
    assert all(s[:3]==s[3:] for s in queue)
    assert 'aabbaa' in stack and 'aabbaa' not in queue
    assert 'aabaab' in queue and 'aabaab' not in stack
    # E={end}, F={C}. t_e+t_f is not one unconditional normalized row.
    empty_row={'end':1,'C':0};full_row={'end':0,'C':1}
    union_row={s:empty_row[s]+full_row[s] for s in empty_row}
    assert sum(empty_row.values())==sum(full_row.values())==1
    assert sum(union_row.values())==2
    # Equal final counts do not make CP a legal path from empty memory.
    depth=0;underflow=False
    for state in 'CP':
        depth += 1 if state=='P' else -1
        underflow |= depth<0
    assert depth==0 and underflow
    return dict(stack_support=sorted(stack),queue_support=sorted(queue),
                active_transition_row_mass=1,unmasked_union_mass=sum(union_row.values()),
                balanced_counts_can_underflow=underflow)


if __name__ == '__main__':
    print(json.dumps(dict(mean_field=mean_field_phases(),emission_context=emission_context(),auxiliary_memory=memory_context()),indent=2))
