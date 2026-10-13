"""Finite frozen-state arithmetic; no local optimization or source-code execution."""
import json
import math


def eye(n):
    return [[float(i == j) for j in range(n)] for i in range(n)]


def tr(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def scale(a, k):
    return [[k * x for x in row] for row in a]


def add(*args):
    return [[sum(a[i][j] for a in args) for j in range(len(args[0][0]))]
            for i in range(len(args[0]))]


def inv(a):
    n = len(a)
    m = [row[:] + e for row, e in zip(a, eye(n))]
    for j in range(n):
        k = max(range(j, n), key=lambda i: abs(m[i][j]))
        assert abs(m[k][j]) > 1e-12
        m[j], m[k] = m[k], m[j]
        d = m[j][j]
        m[j] = [x / d for x in m[j]]
        for i in range(n):
            if i != j:
                d = m[i][j]
                m[i] = [x - d * y for x, y in zip(m[i], m[j])]
    return [row[n:] for row in m]


def error(a, b):
    return max(abs(x - y) for ra, rb in zip(a, b) for x, y in zip(ra, rb))


def congr(a, b):
    return mul(mul(a, b), tr(a))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def mv(a, v):
    return [dot(row, v) for row in a]


def outer(a):
    return [[x * y for y in a] for x in a]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def gram(z, weights):
    return mul(tr(z), [[w * v for v in row] for row, w in zip(z, weights)])


def experiment():
    from itertools import combinations, product
    n, size, rho = 3, 2, .3
    mb = [.1, -.2]
    qb = [[.4, .08], [.08, .3]]
    pold = inv(qb)
    prior_p = [[.7, .05], [.05, .8]]
    prior_s = [[.9, .1], [.1, 1.2]]
    old_s = [[1.4, .2], [.2, 1.1]]
    # nu=3, n=3, r=2: IW degrees remain six throughout this supplied step.
    nuq = 6.
    a = scale(inv(old_s), nuq)
    rows = []
    for k in range(n):
        z = [[1., -1.+.1*k], [1., .3], [1., 1.2]]
        w = [[.35+.02*k, .07], [-.03, .5]]
        b = add(eye(2), scale(w, -1))
        v = mul(z, w)
        mi = [.3+.1*k, .1-.04*k]
        qi = [[.25+.02*k, -.02], [-.02, .35]]
        y, exposure = [1.+k, 0., 2.], [.6, 1.1, .8]
        m = [x+y for x,y in zip(mv(v, mb), mv(z, mi))]
        cov = add(congr(v, qb), congr(z, qi))
        g = [e*math.exp(mj+cov[j][j]/2) for j,(e,mj) in enumerate(zip(exposure,m))]
        residual = [x-y for x,y in zip(mi,mv(b,mb))]
        prec = add(congr(tr(b),a),gram(v,g))
        grad = [x+y for x,y in zip(mv(tr(b),mv(a,residual)),mv(tr(v),[yi-gi for yi,gi in zip(y,g)]))]
        second = add(outer(residual),qi,congr(b,qb))
        rows.append(dict(precision=prec,gradient=grad,second=second,local_covariance=qi))

    def targets(batch):
        factor = n/len(batch)
        p = add(prior_p,scale(add(*(rows[i]['precision'] for i in batch)),factor))
        g = [-x+factor*sum(rows[i]['gradient'][j] for i in batch) for j,x in enumerate(mv(prior_p,mb))]
        s = add(prior_s,scale(add(*(rows[i]['second'] for i in batch)),factor))
        h = [x+y for x,y in zip(mv(p,mb),g)]
        return p,g,s,h

    full = targets(list(range(n)))
    errors = []
    for batches in [list(combinations(range(n),size)),list(product(range(n),repeat=size))]:
        ts=[targets(batch) for batch in batches]
        avg_p=scale(add(*(t[0] for t in ts)),1/len(ts))
        avg_s=scale(add(*(t[2] for t in ts)),1/len(ts))
        avg_g=[[sum(t[1][j] for t in ts)/len(ts)] for j in range(2)]
        avg_h=[[sum(t[3][j] for t in ts)/len(ts)] for j in range(2)]
        errors += [error(avg_p,full[0]),error(avg_s,full[2]),error(avg_g,[[x] for x in full[1]]),error(avg_h,[[x] for x in full[3]])]
    assert max(errors)<1e-12
    batch=[0,2];p,g,s,h=targets(batch)
    pn=add(scale(pold,1-rho),scale(p,rho));qn=inv(pn)
    hn=[(1-rho)*x+rho*y for x,y in zip(mv(pold,mb),h)]
    mn=mv(qn,hn)
    simplified=[x+rho*y for x,y in zip(mb,mv(qn,g))]
    sn=add(scale(old_s,1-rho),scale(s,rho))
    omitted=scale(add(*(rows[i]['local_covariance'] for i in batch)),n/size)
    omitted_step=scale(omitted,rho)
    assert max(abs(x-y) for x,y in zip(mn,simplified))<1e-12
    assert omitted_step[0][0]>0 and omitted_step[1][1]>0
    # Fixed scores illustrate the conditional distinction in random reshuffling.
    scores=[1.,2.,7.]
    full_sum=sum(scores)
    unconditional=sum(n*x for x in scores)/n
    conditional_after_first_zero=sum(n*scores[i] for i in [1,2])/2
    assert unconditional==full_sum and conditional_after_first_zero!=full_sum
    # Printed Appendix B Gaussian weight fails even the constant-function test.
    bad_weight_integral=1/math.sqrt(2)
    return dict(
        sampling=dict(uniform_subset_and_iid_multiset_target_error=max(errors),
                      fixed_score_sum=full_sum,fresh_singleton_mean=unconditional,
                      conditional_remaining_mean_after_first_index_zero=conditional_after_first_zero),
        natural_step=dict(rho=rho,selected_clusters=batch,beta_precision=pn,beta_mean=mn,
                          mean_form_error=max(abs(x-y) for x,y in zip(mn,simplified)),
                          IW_scale=sn,IW_degrees=nuq,omitted_local_covariance_error=omitted_step),
        printed_gaussian_weight_integral=bad_weight_integral,
        limits='Supplied local Gaussian factors are not optimized. These calculations check finite frozen-state sums and one simultaneous global step, not the profiled-gradient envelope condition, convergence, source implementation or benchmark.'
    )


if __name__=='__main__':
    print(json.dumps(experiment(),sort_keys=True,indent=2))
