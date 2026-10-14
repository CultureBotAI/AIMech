"""Original exact finite checks of Neal 2024 NAM and ZDNAM constructions.

Stdlib only; no author code, randomness, network, files or timestamps. JSON stdout.
Row procedures interpret the mathematical pseudocode of Algorithms 2, 3 and 5.
Matrix constructions independently apply Eq19 or solve the Eq93 balance equations.
Finite cases are evidence, not a universal performance or convergence theorem.
"""
from fractions import Fraction as F
from itertools import product, permutations
from math import gcd, sqrt
import json


def norm(w):
    assert w and min(w) >= 0 and sum(w) > 0
    return [F(x, sum(w)) for x in w]


def verify(p, P):
    n = len(p)
    assert len(P) == n and all(len(row) == n for row in P)
    assert all(min(row) >= 0 and sum(row) == 1 for row in P)
    assert all(p[i]*P[i][j] == p[j]*P[j][i] for i in range(n) for j in range(n))
    assert after(p, P) == p


def after(p, P):
    return [sum(p[i]*P[i][j] for i in range(len(p))) for j in range(len(p))]


def nam_row(p, order, k):
    """Algorithm 2, including zero residual and final focal guards."""
    n = len(p); row = [None]*n; s = F(1); f = F(1); i = 0
    while order[i] != k:
        a = order[i]
        if f <= 0:
            row[a] = F(0)
        else:
            q = p[a]; s -= q
            if q >= s:
                row[a] = f; f = F(0)
            else:
                row[a] = (q/s)*f; f -= row[a]
        i += 1
    if f <= 0:
        row[k] = F(0)
        for a in order[i+1:]: row[a] = F(0)
    else:
        q = p[k]; s -= q
        if q > s:
            row[k] = (q-s)/q*f
            for a in order[i+1:]: row[a] = min(f, p[a]/q*f)
        else:
            row[k] = F(0)
            for a in order[i+1:]: row[a] = min(f, p[a]/s*f)
    assert all(v is not None for v in row)
    return row


def unam_row(p, order, k):
    """Algorithm 3, separate from general NAM row code."""
    assert all(p[a] <= p[b] for a,b in zip(order, order[1:]))
    row = [None]*len(p); s = F(1); f = F(1); i = 0
    while order[i] != k:
        a = order[i]; q = p[a]; s -= q
        row[a] = min(f, q/s*f); f -= row[a]; i += 1
    if i == len(p)-1:
        row[k] = f
    else:
        s -= p[k]; row[k] = F(0)
        for a in order[i+1:]: row[a] = min(f, p[a]/s*f)
    assert all(v is not None for v in row)
    return row


def am_step(p, P, a, tail):
    """Maximal singleton/tail Eq19 change; independent of row recurrences."""
    q = p[a]; s = sum(p[j] for j in tail)
    assert q > 0 and s > 0
    bounds = [P[a][a]/s]
    bounds += [P[j][k]*s/(p[k]*q) for j in tail for k in tail]
    delta = min(bounds)
    Q = [row[:] for row in P]
    Q[a][a] -= delta*s
    for j in tail:
        Q[a][j] += delta*p[j]
        Q[j][a] += delta*q
        for k in tail: Q[j][k] -= delta*p[k]*q/s
    verify(p, Q)
    return Q


def nam_matrix(p, order):
    """Positive-support full AM construction, not row-pseudocode assembly."""
    assert min(p) > 0 and sorted(order) == list(range(len(p)))
    P = [p[:] for _ in p]
    for i,a in enumerate(order[:-1]):
        tail = order[i+1:]
        P = am_step(p, P, a, tail)
        if all(P[j][k] == 0 for j in tail for k in tail): break
    return P


def solve(A, b):
    n = len(b); M = [[F(x) for x in row]+[F(v)] for row,v in zip(A,b)]
    for c in range(n):
        r = next(i for i in range(c,n) if M[i][c]); M[c],M[r] = M[r],M[c]
        d = M[c][c]; M[c] = [x/d for x in M[c]]
        for i in range(n):
            if i != c:
                q = M[i][c]; M[i] = [x-q*y for x,y in zip(M[i],M[c])]
    return [row[-1] for row in M]


def zdnam_row(p, order, k, traces=None):
    """Algorithm 5 with explicit zero-tail branch, missing brackets restored."""
    n = len(p); assert all(p[a] >= p[b] for a,b in zip(order,order[1:]))
    row = [None]*n
    if p[k] >= F(1,2):
        row = [p[j]/p[k] if j != k else (2*p[k]-1)/p[k] for j in range(n)]
        if traces is not None: traces.append('current_half_or_more')
        return row
    if p[order[0]] >= F(1,2):
        row = [F(j == order[0]) for j in range(n)]
        if traces is not None: traces.append('other_half_or_more')
        return row
    s = F(1); f = F(1); i = 0
    while f > 0 and order[i] != k and p[order[i+1]] < s-p[order[i]]-p[order[i+1]]:
        a = order[i]; q = p[a]; s -= q
        row[a] = q/s*f; f -= row[a]; i += 1
    a = order[i]; q = p[a]; s -= q
    if f > 0 and s > 0 and i < n-1:
        b = order[i+1]; q2 = p[b]; s2 = max(F(0),s-q2)
        if q2 >= s2:
            A = (q+q2-s2)/2
            if k == a: row[a] = F(0); row[b] = f*A/q
            elif k == b: row[a] = f*A/q2; row[b] = F(0)
            if s2 <= 0:
                i += 2
                if traces is not None: traces.append('zero_tail_guard')
            else:
                B = (q-q2+s2)/(2*s2); C = (s2+q2-q)/(2*s2)
                if traces is not None: traces.append('completion_equality' if q2 == s2 else 'completion_strict')
                if k == a:
                    i += 2
                    while i < n: row[order[i]] = f*B*p[order[i]]/q; i += 1
                elif k == b:
                    i += 2
                    while i < n: row[order[i]] = f*C*p[order[i]]/q2; i += 1
                else:
                    row[a] = f*B; row[b] = f*C; i += 2
        else:
            assert k == a
            row[a] = F(0); i += 1
            while i < n: row[order[i]] = p[order[i]]/s*f; i += 1
    while i < n: row[order[i]] = F(0); i += 1
    assert all(x is not None for x in row), (p,order,k,row)
    return row


def zdnam_matrix(p, order):
    """Independent full-matrix AM prefix then solve three flow constraints."""
    n = len(p); a = order[0]
    if p[a] >= F(1,2):
        return [[(2*p[a]-1)/p[a] if i == a == j else p[j]/p[a] if i == a else F(j == a)
                 for j in range(n)] for i in range(n)]
    P = [p[:] for _ in p]
    for i,a in enumerate(order[:-1]):
        b = order[i+1]; tail = order[i+2:]; s2 = sum(p[j] for j in tail)
        if p[b] >= s2:
            assert s2 > 0
            f = sum(P[a][j] for j in order[i:])
            # A+B*s2=p[a], A+C*s2=p[b], B+C=1.
            A,B,C = solve([[1,s2,0],[1,0,s2],[0,1,1]],[p[a],p[b],1])
            for j in order[i:]:
                for k in order[i:]: P[j][k] = F(0)
            P[a][b] = f*A/p[a]; P[b][a] = f*A/p[b]
            for j in tail:
                P[a][j] = f*B*p[j]/p[a]; P[b][j] = f*C*p[j]/p[b]
                P[j][a] = f*B; P[j][b] = f*C
            return P
        P = am_step(p,P,a,order[i+1:])
    raise AssertionError('Finite positive-support completion was not reached')


def compatible_orders(p, up=False):
    return [o for o in permutations(range(len(p))) if all((p[a] <= p[b] if up else p[a] >= p[b]) for a,b in zip(o,o[1:]))]


def main():
    counts = dict(positive_nam_order_cases=0, nonnegative_target_vectors=0, descending_order_cases=0, zero_current_rows=0)
    traces = []; tie_differences = []; nam_support_checks = 0
    supported_tie_differences = []; positive_tie_cases = 0; positive_tie_differences = []
    for n in range(1,5):
        for w in product((1,2,3), repeat=n):
            p = norm(w)
            for order in permutations(range(n)):
                P = nam_matrix(p,order); R = [nam_row(p,order,k) for k in range(n)]
                assert P == R
                assert sum(P[i][i] > 0 for i in range(n)) <= 1
                counts['positive_nam_order_cases'] += 1
    for w in [[1,2,3,4,5],[4,3,3,2,1],[1,1,1,1,1],[8,1,1,1,1]]:
        p = norm(w)
        for order in permutations(range(len(p))):
            assert nam_matrix(p,order) == [nam_row(p,order,k) for k in range(len(p))]
            counts['positive_nam_order_cases'] += 1
    for n in range(1,6):
        for w in product((0,1,2),repeat=n):
            if not sum(w): continue
            p = norm(w); counts['nonnegative_target_vectors'] += 1
            support = [j for j in range(n) if p[j]]
            for order in [tuple(range(n)), tuple(reversed(range(n)))]:
                P = [nam_row(p,order,k) for k in range(n)]; verify(p,P)
                suborder = [support.index(j) for j in order if p[j]]
                subP = nam_matrix([p[j] for j in support],suborder)
                assert subP == [[P[j][k] for k in support] for j in support]
                nam_support_checks += 1
            up = tuple(sorted(range(n),key=lambda j:(p[j],j)))
            U = [unam_row(p,up,k) for k in range(n)]; verify(p,U)
            assert U == [nam_row(p,up,k) for k in range(n)]
            assert all(U[i][j] >= p[j] for i in range(n) for j in range(n) if i != j)
            first = None
            for order in compatible_orders(p):
                Z = [zdnam_row(p,order,k,traces) for k in range(n)]; verify(p,Z)
                suborder = [support.index(j) for j in order if p[j]]
                subZ = zdnam_matrix([p[j] for j in support],suborder)
                assert subZ == [[Z[j][k] for k in support] for j in support]
                assert sum(p[j]*Z[j][j] for j in range(n)) == max(F(0),2*max(p)-1)
                counts['descending_order_cases'] += 1
                counts['zero_current_rows'] += n-len(support)
                if first is not None and first != Z and not tie_differences:
                    tie_differences.append(dict(target=p,first_order=first_order,first=first,other_order=order,other=Z))
                if first is not None and any(first[j] != Z[j] for j in support) and not supported_tie_differences:
                    supported_tie_differences.append(dict(target=p,first_order=first_order,other_order=order))
                if first is None: first=Z; first_order=order
    # Broader strictly positive ties than the zero-inclusive two-weight grid.
    for n in range(2,5):
        for w in product((1,2,3,4),repeat=n):
            p = norm(w); U0 = Z0 = None
            for order in compatible_orders(p,up=True):
                U = [unam_row(p,order,k) for k in range(n)]
                if U0 is not None: assert U == U0
                U0 = U
            for order in compatible_orders(p):
                Z = [zdnam_row(p,order,k) for k in range(n)]
                if Z0 is not None and Z != Z0 and not positive_tie_differences:
                    positive_tie_differences.append(dict(target=p,first_order=Z0_order,first=Z0,other_order=order,other=Z))
                if Z0 is None: Z0 = Z; Z0_order = order
                positive_tie_cases += 1
    assert supported_tie_differences and positive_tie_differences
    tie_p = norm([1,3,3,5]); tie_orders = [(3,1,2,0),(3,2,1,0)]
    tie_dnam = [nam_matrix(tie_p,o) for o in tie_orders]
    assert tie_dnam[0] != tie_dnam[1]
    p = norm([4,3,2]); up = (2,1,0); down = (0,1,2)
    U = nam_matrix(p,up); D = nam_matrix(p,down); Z = zdnam_matrix(p,down)
    M = [[(U[i][j]+D[i][j])/2 for j in range(3)] for i in range(3)]; verify(p,M)
    all_nam = [nam_matrix(p,o) for o in permutations(range(3))]
    assert M not in all_nam and Z not in all_nam
    assert sum(M[i][i] > 0 for i in range(3)) == 2 and all(Z[i][i] == 0 for i in range(3))
    difference = [[D[i][j]-Z[i][j] for j in range(3)] for i in range(3)]
    trace = sum(difference[i][i] for i in range(3))
    pair_product = sum(difference[i][i]*difference[j][j]-difference[i][j]*difference[j][i] for i in range(3) for j in range(i+1,3))
    assert pair_product < 0 and all(sum(row)==0 for row in difference)
    wrong = [nam_row(p,(k,)+tuple(j for j in range(3) if j != k),k) for k in range(3)]
    assert after(p,wrong) != p
    print(json.dumps(dict(scope='Original exact rational finite cases. No author code, library sampler, full-gate, universal efficiency or convergence claim.',counts=counts,nam_supported_submatrix_checks=nam_support_checks,
        pseudocode_branches={x:traces.count(x) for x in sorted(set(traces))},
        zero_tail_limit='No exact zero-tail completion was reached in the checked normalized inputs; the explicit Algorithm 5 guard remains present. No floating-point correctness claim.',
        zdnam_zero_current_tie_order_difference=tie_differences,
        supported_ties=dict(additional_positive_descending_order_cases=positive_tie_cases,UNAM_tie_invariant_in_checked_cases=True,ZDNAM_positive_counterexample=positive_tie_differences,DNAM_counterexample=dict(target=tie_p,orders=tie_orders,kernels=tie_dnam),interpretation='Tie policy matters for both DNAM and ZDNAM. UNAM equivalence across ties was checked only within the enumerated cases; its general statement is separately supported by source Eq75.'),
        identity_boundary=dict(target=p,UNAM=U,DNAM=D,UDNAM=M,ZDNAM=Z,all_six_orders_NAM_diagonals=[[Q[i][i] for i in range(3)] for Q in all_nam],neither_UDNAM_nor_ZDNAM_is_single_order_NAM=True),
        eq95_difference=dict(matrix=difference,one_zero_eigenvalue=True,sum_other_two=trace,product_other_two=pair_product,opposite_signs=True,approximate_values_separately_labeled=[(float(trace)+sqrt(float(trace*trace-4*pair_product)))/2,(float(trace)-sqrt(float(trace*trace-4*pair_product)))/2]),
        current_dependent_order_negative_control=dict(target=p,kernel=wrong,target_after=after(p,wrong),invariant=False),
        half_mass_boundary=dict(target=norm([2,1,1]),NAM_down=nam_matrix(norm([2,1,1]),(0,1,2)),ZDNAM=zdnam_matrix(norm([2,1,1]),(0,1,2))),
        point_mass=dict(target=[1],NAM=nam_matrix([F(1)],(0,)),ZDNAM=zdnam_matrix([F(1)],(0,))),
        limits=['Finite enumeration is not a general proof.','Zero-mass outgoing rows checked as an algebraic extension; initial proposed identities can remain positive-support.','Order policies are fixed across rows of each target kernel; random mixtures require state-independent weights.','No claim that every nonzero-eigenvalue expression or floating guard is universally verified.']),default=str,indent=2))


if __name__ == '__main__': main()
