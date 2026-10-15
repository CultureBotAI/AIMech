"""Original exact PESC-F and resource-framework boundary diagnostics.

Derived from JMLR2016 Sections3/5, Algorithm2, AppendixB.4 and SELECTIVELY
read author source at b5722e5134becc10523ff8f4bd8ef453b40faf69. No author
source is imported or executed. These tests are not a PESC/EP/GP optimizer.
All arithmetic below is Fraction/integer; output is deterministic stdout JSON.
"""
from fractions import Fraction as F
from itertools import product
import json


def paper_full(elapsed, slow, gamma):
    assert slow > 0
    return elapsed / slow > gamma


def pinned_code_full(elapsed, slow, gamma):
    # Complement of the inspected source's strict fast condition.
    assert elapsed >= 0 and slow >= 0 and gamma >= 0
    return not (elapsed * gamma < slow)


def gram(rows):
    return [[sum(a*b for a,b in zip(x,y)) for y in rows] for x in rows]


def serial_diagnostic(steps, gamma, slow, fast, evaluation):
    # Original deterministic state-machine diagnostic. Start just after an
    # initial slow update; count it explicitly, then one evaluation per loop.
    elapsed, bo, evaluations = F(0), slow, F(0)
    modes = []
    for _ in range(steps):
        elapsed += evaluation
        evaluations += evaluation
        full = pinned_code_full(elapsed, slow, gamma)
        modes.append('full' if full else 'partial')
        bo += slow if full else fast
        elapsed = F(0) if full else elapsed + fast
    return {'steps':steps,'gamma':str(gamma),'slow':str(slow),'fast':str(fast),
            'evaluation':str(evaluation),'modes':modes,'bo_time':str(bo),
            'evaluation_time':str(evaluations),'bo_to_evaluation_ratio':str(bo/evaluations)}


def calculate():
    rows = []
    for elapsed, slow in product([F(i,2) for i in range(9)], [F(1,2),F(1),F(2)]):
        gammas = [F(1,4),F(1,2),F(1),F(2),F(4)]
        printed = [paper_full(elapsed,slow,g) for g in gammas]
        code = [pinned_code_full(elapsed,slow,g) for g in gammas]
        assert all(a>=b for a,b in zip(printed,printed[1:]))
        assert all(a<=b for a,b in zip(code,code[1:]))
        for gamma,a,b in zip(gammas,printed,code):
            reciprocal=paper_full(elapsed,slow,1/gamma)
            assert b == (reciprocal or elapsed*gamma == slow)
            rows.append((elapsed,slow,gamma,a,b))
    assert len(rows)==135
    witness = [{'gamma':str(g), 'paper_full':paper_full(F(2),F(1),g),
                'pinned_code_full':pinned_code_full(F(2),F(1),g)}
               for g in [F(1,10),F(1),F(10)]]
    assert [x['paper_full'] for x in witness] == [True,True,False]
    assert [x['pinned_code_full'] for x in witness] == [False,True,True]
    # Equality differs even after reciprocal reparameterization: printed >,
    # code's full branch is >=. Endpoints are limits or separate settings.
    equality = {'elapsed':'2','slow':'1','code_gamma':'1/2',
                'paper_reciprocal_gamma':'2','paper_full':False,'code_full':True}
    assert not paper_full(F(2),F(1),F(2)) and pinned_code_full(F(2),F(1),F(1,2))
    assert paper_full(F(1),F(1),F(0)) and not pinned_code_full(F(1),F(1),F(0))
    assert pinned_code_full(F(10),F(0),F(0))  # initialized code zero duration
    try:
        F(10)/F(0)
        raise AssertionError('Expected zero denominator')
    except ZeroDivisionError:
        initialization = 'Literal printed initial ratio is undefined; inspected code multiplication with zero duration selects a first full update.'

    # Printed Algorithm2 ends its timer before the acquisition optimizer.
    start, ep_end, optimizer_end, next_time = map(F,[100,102,110,111])
    printed_duration, printed_elapsed = ep_end-start,next_time-ep_end
    complete_duration, complete_elapsed = optimizer_end-start,next_time-optimizer_end
    assert paper_full(printed_elapsed,printed_duration,F(1))
    assert not paper_full(complete_elapsed,complete_duration,F(1))
    timing = {'start':str(start),'ep_end':str(ep_end),'optimizer_end':str(optimizer_end),
              'next_decision':str(next_time),'printed_duration':str(printed_duration),
              'printed_elapsed':str(printed_elapsed),'full_duration':str(complete_duration),
              'elapsed_after_full_completion':str(complete_elapsed),
              'printed_ratio':str(printed_elapsed/printed_duration),
              'full_timer_ratio':str(complete_elapsed/complete_duration)}

    budget = serial_diagnostic(20,F(1,10),F(1),F(1),F(1,100))
    assert F(budget['bo_to_evaluation_ratio']) > F(1,10)

    # Exact bordered Cholesky example with positive Schur complement4.
    old_l=[[F(2),F(0)],[F(1),F(1)]]
    old_k=gram(old_l)
    v=[F(1),F(2)]
    cross=[sum(a*b for a,b in zip(row,v)) for row in old_l]
    c=F(9);schur=c-sum(x*x for x in v)
    new_l=[old_l[0]+[F(0)],old_l[1]+[F(0)],v+[F(2)]]
    expected=[old_k[0]+[cross[0]],old_k[1]+[cross[1]],cross+[c]]
    assert gram(new_l)==expected and schur==4
    assert F(5)-sum(x*x for x in v)==0
    assert F(4)-sum(x*x for x in v)<0
    changed_k=[[F(9),F(2)],[F(2),F(2)]]
    assert old_k != changed_k

    # Fixed Gaussian site plus updated predictive Gaussian: cache reuse does
    # not mean freezing the posterior and need not equal re-fitted sites.
    def posterior(prior_precision,prior_linear,site_precision,site_linear):
        variance=1/(prior_precision+site_precision)
        return variance*(prior_linear+site_linear),variance
    old=posterior(F(1),F(0),F(1),F(1))
    reused=posterior(F(2),F(2),F(1),F(1))
    alternative_site=posterior(F(2),F(2),F(2),F(0))
    assert old==(F(1,2),F(1,2)) and reused==(F(1),F(1,3))
    assert alternative_site==(F(1,2),F(1,4)) and reused!=alternative_site

    # One-pass resource order need not maximize a joint dispatch objective.
    # A uses either resource; B only r1. First A observation gives10, duplicate
    # A gives0 conditional on its pending observation, and B gives9.
    # Scores are stipulated finite utilities, not fitted GP acquisitions.
    greedy=F(10)+F(0);joint=F(9)+F(10)
    assert greedy==10 and joint==19 and joint>greedy
    # Being able to evaluate a utility for each task subset (source definition
    # of separable) is weaker than additive set utility.
    subset_utilities={'a':F(1),'b':F(1),'ab':F(3)}
    assert subset_utilities['ab'] != subset_utilities['a']+subset_utilities['b']
    return dict(
        scope='Seven original exact boundary categories; no author code import/execution, EP/GP fit, acquisition optimizer or performance benchmark.',
        arithmetic='Fraction and integer throughout; no floating tolerance.',
        category_count=7,
        timing_orientation=dict(grid_cases=len(rows),disagreeing_cases=sum(a!=b for _,_,_,a,b in rows),witness=witness,equality=equality,
            gamma_zero='At positive elapsed and duration, printed condition chooses full; pinned code chooses partial. Code all-full is represented by disabling fast_updates; no infinite-float runtime asserted.',initialization=initialization),
        timer_placement=timing, budget_counterexample=budget,
        bordered_cholesky=dict(old_matrix=[[str(x) for x in r] for r in old_k],new_factor=[[str(x) for x in r] for r in new_l],new_matrix=[[str(x) for x in r] for r in expected],schur_complement=str(schur),guards='Old block must remain unchanged and positive definite; zero Schur complement is singular and a negative complement is invalid.'),
        fixed_site_recombination=dict(old=[str(x) for x in old],reused_site_updated_gp=[str(x) for x in reused],alternative_refitted_site=[str(x) for x in alternative_site],scope='Illustrative Gaussian natural parameters; no assertion these site parameters arise from a particular PESC data set.'),
        resource_greedy_counterexample=dict(eligible={'r1':['A','B'],'r2':['A']},capacity={'r1':1,'r2':1},first_A_utility='10',duplicate_A_utility='0',B_utility='9',r1_first_greedy_total=str(greedy),joint_B_r1_A_r2_total=str(joint),scope='A stipulated finite task utility with pending-update diminishing value; refutes a universal globally optimal scheduling interpretation, not the source greedy procedure.'),
        separable_not_additive={k:str(v) for k,v in subset_utilities.items()},
        limitations=['Printed inequality and pinned code are retained as distinct source conventions, not silently repaired.', 'Artificial timing values do not reproduce author experiments or bound real runtime.', 'No posterior-approximation error, convergence or universal speedup guarantee.', 'Cholesky availability does not mean the inspected author GP cache actually uses a bordered update.'])


if __name__ == '__main__':
    print(json.dumps(calculate(),indent=2,sort_keys=True))
