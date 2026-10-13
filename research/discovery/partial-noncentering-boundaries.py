"""Finite curator calculations, not Tan–Nott code or a fitted GLMM."""
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


def gaussian_boundary():
    # A proper beta prior is an explicit curator extension of the flat-prior
    # motivating example; it adds only to the beta precision block.
    d = [[1.4, .45], [.45, .9]]
    a = inv(d)
    x = [[[1., -1.], [1., .3], [1., 1.2]],
         [[1., -.7], [1., .2], [1., 1.5]]]
    p0 = [[.8, .1], [.1, .6]]
    precis = [[0.] * 6 for _ in range(6)]
    for i in range(2):
        for j in range(2):
            precis[i][j] = p0[i][j]
    transform = eye(6)  # (beta, a_1, a_2) -> (beta, u_1, u_2)
    ws, wrong, cross = [], [], []
    for k, z in enumerate(x):
        g = gram(z, [1 / .7] * len(z))
        w = mul(inv(add(g, a)), a)
        wrong_w = mul(a, inv(add(g, a)))
        b = add(eye(2), scale(w, -1))
        ws.append(w)
        cross.append(error(add(mul(g, w), scale(mul(a, b), -1)), [[0., 0.], [0., 0.]]))
        wrong.append(error(add(mul(g, wrong_w), scale(mul(a, add(eye(2), scale(wrong_w, -1))), -1)), [[0., 0.], [0., 0.]]))
        start = 2 + 2 * k
        for i in range(2):
            for j in range(2):
                precis[i][j] += g[i][j]
                precis[i][start+j] = g[i][j]
                precis[start+i][j] = g[i][j]
                precis[start+i][start+j] = g[i][j] + a[i][j]
                transform[start+i][j] = -b[i][j]
    tp = mul(mul(tr(transform), precis), transform)
    transformed_cross = max(abs(tp[i][j]) for i in range(6) for j in range(6) if i // 2 != j // 2)
    block_cov = [[0.] * 6 for _ in range(6)]
    for start in [0, 2, 4]:
        block = inv([row[start:start+2] for row in tp[start:start+2]])
        for i in range(2):
            for j in range(2):
                block_cov[start+i][start+j] = block[i][j]
    covariance_error = error(congr(transform, block_cov), inv(precis))
    assert max(cross) < 1e-12 and transformed_cross < 1e-12 and covariance_error < 1e-12
    assert max(wrong) > .01 and max(error(w, tr(w)) for w in ws) > .01
    return dict(W=ws,correct_order_cross_error=max(cross),reversed_order_cross_error=max(wrong),
                transformed_precision_cross_error=transformed_cross,pulled_back_covariance_error=covariance_error)


def poisson_boundary():
    z = [[1., -1.], [1., .3], [1., 1.2]]
    w = [[.35, .07], [-.03, .5]]
    b = add(eye(2), scale(w, -1))
    v = mul(z, w)  # C=I, no remaining fixed-only terms
    mb, ma = [.1, -.2], [.3, .1]
    sb, sa = [[.4, .08], [.08, .3]], [[.25, -.02], [-.02, .35]]
    prior_p = [[.7, .05], [.05, .8]]
    s, nuq = [[1.4, .2], [.2, 1.1]], 4.
    a = scale(inv(s), nuq)
    y, exposure = [1., 0., 2.], [.6, 1.1, .8]

    def moments(mbeta, salpha=sa, sbeta=sb, malpha=ma):
        m = [x + y for x, y in zip(mv(v, mbeta), mv(z, malpha))]
        cov = add(congr(v, sbeta), congr(z, salpha))
        return [e * math.exp(mj + cov[j][j] / 2) for j, (e, mj) in enumerate(zip(exposure, m))], m

    def expected_log_joint(mbeta, malpha, sbeta=sb, salpha=sa):
        expected, m = moments(mbeta, salpha, sbeta, malpha)
        res = [x - y for x, y in zip(malpha, mv(b, mbeta))]
        prior = -.5 * (dot(mbeta, mv(prior_p, mbeta)) + trace(mul(prior_p, sbeta)))
        cluster = -.5 * (dot(res, mv(a, res)) + trace(mul(a, add(salpha, congr(b, sbeta)))))
        # D terms and observation constants are independent of these Gaussian parameters.
        return prior + cluster + dot(y, m) - sum(expected)

    g, _ = moments(mb)
    residual = [x - y for x, y in zip(ma, mv(b, mb))]
    p_beta = add(prior_p, congr(tr(b), a), gram(v, g))
    p_alpha = add(a, gram(z, g))
    gb = [-x + y + z0 for x, y, z0 in zip(mv(prior_p, mb), mv(tr(b), mv(a, residual)), mv(tr(v), [yi-gi for yi, gi in zip(y, g)]))]
    ga = [-x + y for x, y in zip(mv(a, residual), mv(tr(z), [yi-gi for yi, gi in zip(y, g)]))]
    errors = []
    eps = 1e-5
    for block, grad in [('beta', gb), ('alpha', ga)]:
        for j in range(2):
            plus, minus = (mb[:] if block == 'beta' else ma[:]), (mb[:] if block == 'beta' else ma[:])
            plus[j] += eps
            minus[j] -= eps
            f1 = expected_log_joint(plus, ma) if block == 'beta' else expected_log_joint(mb, plus)
            f0 = expected_log_joint(minus, ma) if block == 'beta' else expected_log_joint(mb, minus)
            errors.append(abs((f1-f0)/(2*eps) - grad[j]))
    for block, precision in [('beta', p_beta), ('alpha', p_alpha)]:
        base = sb if block == 'beta' else sa
        for i, j in [(0, 0), (1, 1), (0, 1)]:
            plus, minus = [r[:] for r in base], [r[:] for r in base]
            for ii, jj in ([(i,j)] if i == j else [(i,j),(j,i)]):
                plus[ii][jj] += eps
                minus[ii][jj] -= eps
            f1 = expected_log_joint(mb, ma, sbeta=plus) if block == 'beta' else expected_log_joint(mb, ma, salpha=plus)
            f0 = expected_log_joint(mb, ma, sbeta=minus) if block == 'beta' else expected_log_joint(mb, ma, salpha=minus)
            expected = -.5 * precision[i][j] * (1 if i == j else 2)
            errors.append(abs((f1-f0)/(2*eps) - expected))
    new_cov = inv(p_beta)
    new_mean = [x+y for x,y in zip(mb, mv(new_cov, gb))]
    scale_increment = add(outer(residual), sa, congr(b, sb))
    assert max(errors) < 2e-8
    return dict(expected_counts=g,beta_precision=p_beta,beta_mean_proposal=new_mean,
                max_mean_and_covariance_derivative_error=max(errors),IW_scale_increment=scale_increment,
                note='Both block derivatives evaluated at one supplied old state, not a sequential fit.')


def logistic_boundary():
    def integrate(fun):
        n, lo, hi = 2000, -10., 10.
        h = (hi-lo)/n
        def f(x):
            return fun(x) * math.exp(-x*x/2)/math.sqrt(2*math.pi)
        return h/3 * (f(lo)+f(hi)+sum((4 if j%2 else 2)*f(lo+j*h) for j in range(1,n)))
    def sigmoid(x):
        return 1/(1+math.exp(-x))
    mu, sd = .4, .8
    def b0(m):
        return integrate(lambda x: math.log1p(math.exp(m+sd*x)))
    g = integrate(lambda x: sigmoid(mu+sd*x))
    f = integrate(lambda x: sigmoid(mu+sd*x)*(1-sigmoid(mu+sd*x)))
    h = 1e-3
    e1 = abs((b0(mu+h)-b0(mu-h))/(2*h)-g)
    e2 = abs((b0(mu+h)-2*b0(mu)+b0(mu-h))/h**2-f)
    assert e1 < 2e-8 and e2 < 2e-8
    return dict(G=g,F=f,first_derivative_error=e1,second_derivative_error=e2,
                note='Independent Simpson quadrature, not the source adaptive ten-node Gauss-Hermite implementation.')


if __name__ == '__main__':
    print(json.dumps(dict(gaussian=gaussian_boundary(),poisson=poisson_boundary(),logistic=logistic_boundary()),sort_keys=True,indent=2))
