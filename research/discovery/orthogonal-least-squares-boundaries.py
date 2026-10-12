"""Exact curator calculations for unregularized forward OLS; not a benchmark."""
from fractions import Fraction as F
import importlib.util
from pathlib import Path
import json

spec = importlib.util.spec_from_file_location('pursuit', Path(__file__).with_name('pursuit-boundaries.py'))
pursuit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pursuit)
dot, sub, scale, fit = pursuit.dot, pursuit.sub, pursuit.scale, pursuit.fit

def forward_ols(d, y):
    selected, trace, r = [], [], y
    while True:
        candidates = []
        for j, g in enumerate(d):
            if j in selected:
                continue
            w = fit(d, g, selected)[1] if selected else g
            if dot(w, w) == 0:
                continue
            gain = dot(r, w) ** 2 / dot(w, w)
            candidates.append((j, gain))
        if not candidates or max(gain for _, gain in candidates) == 0:
            break
        j, gain = max(candidates, key=lambda item: item[1])
        before = dot(r, r)
        selected.append(j)
        coefficients, r = fit(d, y, selected)
        assert before - dot(r, r) == gain
        trace.append(dict(selected=list(selected), coefficients=coefficients, residual=r,
                          residual_energy=dot(r, r), gain=gain, err=gain / dot(y, y)))
    return trace

def certificates():
    e1, e2, e3 = [tuple(F(i == j) for i in range(3)) for j in range(3)]
    b = (F(12, 13), F(5, 13), F(0))
    d, y = [e1, b, e3], (F(10), F(4, 5), F(3, 5))
    o = forward_ols(d, y)
    m = pursuit.omp(d, y)
    assert o[1]['selected'] == [0, 1] and m[1]['selected'] == [0, 2]
    assert o[1]['gain'] == F(16, 25) and o[1]['residual_energy'] == F(9, 25)
    assert dot(m[1]['residual'], m[1]['residual']) == F(16, 25)
    scaled = forward_ols([scale(g, c) for g, c in zip(d, [F(2), F(-7), F(1, 3)])], y)
    assert [s['selected'] for s in scaled] == [s['selected'] for s in o]
    assert [s['residual'] for s in scaled] == [s['residual'] for s in o]
    db = [e1, e2, e3, (F(8, 9), F(4, 9), F(1, 9))]
    yb = sub(e1, db[3]); greedy = forward_ols(db, yb)
    assert greedy[-1]['selected'] == [1, 0, 2] and greedy[-1]['residual'] == (0, 0, 0)
    assert all(any(yb[i] * g[j] != yb[j] * g[i] for i in range(3) for j in range(i)) for g in db)
    # yb=e1-db[3] uses two columns; none can represent yb alone.
    degenerate = forward_ols([e1, e1, (F(0), F(0), F(0))], e2)
    assert degenerate == []
    assert forward_ols(d, (F(0), F(0), F(0))) == []
    yy = (F(1), F(2)); constant = (F(1), F(1))
    uncentered = dot(yy, constant) ** 2 / (dot(constant, constant) * dot(yy, yy))
    assert uncentered == F(9, 10)  # Constant fitting explains no centered variation.
    for step in o:
        prefix = o[:len(step['selected'])]
        assert 1 - sum(s['err'] for s in prefix) == step['residual_energy'] / dot(y, y)
    return dict(ols_versus_omp=dict(dictionary=d, signal=y, ols=o, omp=m),
                scaling_preserves_selection_and_residual=True, greedy_nonminimal_support=greedy,
                minimum_possible_support=2, zero_and_dependent_cases_handled=True,
                uncentered_constant_fit_err=uncentered,
                scope='Exact rational finite real inputs with lowest-index ties; source-derived algebra, not empirical evaluation.')

if __name__ == '__main__':
    print(json.dumps(certificates(), default=str, indent=2))
