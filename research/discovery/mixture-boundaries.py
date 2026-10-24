"""Portable exact finite mixture identity and boundary illustrations.

Original core is attributed to the supporting mixture source calculator; added
checks compare it with pinned sibling NAM and tower calculators. No author code
or benchmarks. Sibling loading reads only the two named source files and creates
no bytecode. Main execution prints deterministic JSON; importing this file does
not run checks. Nonrepresentation witnesses do not classify all coincidences.
"""
from fractions import Fraction as F
from itertools import permutations, product
import json
import hashlib
import importlib.util
from pathlib import Path
import sys

DEPENDENCIES = {
    'nam-boundaries.py': 'cb58dd0a41b32a7c4f12dcfc711963b39ff062b12f79d8fe6bf065b777714941',
    'tower-boundaries.py': 'd8e458ae28b7a679456a729231621f5ad35ac00bfa0d7bd52ee655d2f8423c47',
}


def load_sibling(name):
    path = Path(__file__).with_name(name)
    assert not path.is_symlink()
    assert hashlib.sha256(path.read_bytes()).hexdigest() == DEPENDENCIES[name]
    spec = importlib.util.spec_from_file_location('mixture_' + name.replace('-', '_'), path)
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module

def target(weights):
    total = sum(weights)
    return tuple(F(w, total) for w in weights)

def nam(p, order):
    n = len(p)
    assert sorted(order) == list(range(n)) and all(v > 0 for v in p) and sum(p) == 1
    P = [list(p) for _ in p]
    for k, a in enumerate(order[:-1]):
        tail = order[k+1:]
        q, s = p[a], sum(p[j] for j in tail)
        r = P[a][a]/q
        delta = r*min(q/s, s/q)
        P[a][a] -= delta*s
        for j in tail:
            P[a][j] += delta*p[j]
            P[j][a] += delta*q
        for i in tail:
            for j in tail:
                P[i][j] -= delta*p[j]*q/s
        if q >= s:
            break
    assert_kernel(p, P, reversible=True)
    assert sum(P[i][i] > 0 for i in range(n)) <= 1
    return P

def circle(p, order, shift):
    assert sum(p) == 1 and all(v > 0 for v in p)
    assert F(0) <= shift <= F(1)
    starts = [F(0)]*len(p)
    at = F(0)
    for j in order:
        starts[j] = at
        at += p[j]
    out = []
    for i in range(len(p)):
        row = []
        for j in range(len(p)):
            overlap = sum(max(F(0), min(starts[i]+p[i]+shift, starts[j]+p[j]+wrap)
                                       - max(starts[i]+shift, starts[j]+wrap))
                          for wrap in (-1,0,1,2))
            row.append(overlap/p[i])
        out.append(row)
    assert_kernel(p, out)
    return out

def average(A, B):
    return [[(a+b)/2 for a,b in zip(ar,br)] for ar,br in zip(A,B)]

def stationary(p, P):
    return all(sum(p[i]*P[i][j] for i in range(len(p))) == p[j] for j in range(len(p)))

def reversible(p, P):
    return all(p[i]*P[i][j] == p[j]*P[j][i] for i in range(len(p)) for j in range(len(p)))

def assert_kernel(p, P, reversible=False):
    assert all(all(v >= 0 for v in row) and sum(row) == 1 for row in P)
    assert stationary(p,P)
    if reversible:
        assert all(p[i]*P[i][j] == p[j]*P[j][i] for i in range(len(p)) for j in range(len(p)))

def udst(p, ascending_tail=None):
    anchor = max(range(len(p)), key=lambda i: p[i])
    if ascending_tail is None:
        ascending_tail = sorted((i for i in range(len(p)) if i != anchor), key=lambda i:(p[i],i))
    assert sorted([anchor]+list(ascending_tail)) == list(range(len(p)))
    assert all(p[ascending_tail[i]] <= p[ascending_tail[i+1]] for i in range(len(ascending_tail)-1))
    up = [anchor]+list(ascending_tail)
    down = [anchor]+list(reversed(ascending_tail))
    A, B = circle(p,up,max(p)), circle(p,down,max(p))
    assert all(p[i]*A[i][j] == p[j]*B[j][i] for i in range(len(p)) for j in range(len(p)))
    M = average(A,B)
    assert_kernel(p,M,reversible=True)
    assert sum(p[i]*M[i][i] for i in range(len(p))) == max(F(0),2*max(p)-1)
    return up,down,A,B,M

def affine_match(A, B, M):
    """Solve M=A+t(B-A), 0<=t<=1, exactly, reporting a rejection witness."""
    t = None
    for i in range(len(A)):
        for j in range(len(A)):
            change = B[i][j]-A[i][j]
            if change:
                proposed = (M[i][j]-A[i][j])/change
                if t is None:
                    t = proposed
                elif proposed != t:
                    return dict(matches=False, candidate_fraction=t, conflict_entry=[i,j], conflicting_fraction=proposed)
            elif M[i][j] != A[i][j]:
                return dict(matches=False, constant_entry_mismatch=[i,j], fixed_value=A[i][j], required_value=M[i][j])
    if t is None:
        return dict(matches=True, all_segment_same=True)
    return dict(matches=0 <= t <= 1, candidate_fraction=t, within_segment=0 <= t <= 1)

def stringify(value):
    if isinstance(value,F): return str(value)
    if isinstance(value,dict): return {str(k):stringify(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [stringify(v) for v in value]
    return value

def original_witnesses():
    p = target((4,3,2))
    up = sorted(range(3),key=lambda i:p[i]); down = list(reversed(up))
    U,D = nam(p,up),nam(p,down); M = average(U,D)
    assert_kernel(p,M,reversible=True)
    assert sum(M[i][i] > 0 for i in range(3)) == 2
    all_orders = [dict(order=list(o),matrix=nam(p,o)) for o in permutations(range(3))]
    assert all(M != x['matrix'] for x in all_orders)
    udnam_witness = dict(pi=p,up_order=up,down_order=down,UNAM=U,DNAM=D,UDNAM=M,
        positive_diagonals=sum(M[i][i]>0 for i in range(3)), all_six_single_NAM_orders=all_orders,
        interpretation='The mixture has two positive diagonal entries while each single NAM ordering has at most one; this one target disproves full construction equivalence. It does not assert disjoint kernel sets.')

    p = target((1,3,3,5))
    up1=(0,1,2,3);up2=(0,2,1,3);dn1=(3,2,1,0);dn2=(3,1,2,0)
    U1,U2,D1,D2 = nam(p,up1),nam(p,up2),nam(p,dn1),nam(p,dn2)
    assert U1 == U2 and D1 != D2
    A,B = average(U1,D1),average(U2,D2)
    assert A != B
    udnam_ties = dict(pi=p,up_orders=[up1,up2],down_orders=[dn1,dn2],UNAM=U1,
        DNAM_choices=[D1,D2],UDNAM_choices=[A,B],
        interpretation='UNAM is unchanged under this tie exchange; DNAM and hence UDNAM change. Each component and mixture remains reversible. A reverse-pair requirement is not needed for UDNAM reversibility.')

    p = target((1,1,1,1)); up,down,A,B,M = udst(p)
    certificates=[]
    # Equal interval lengths mean every possible order has exactly these shift breakpoints.
    # On each interval overlap lengths, hence every transition entry, are affine in shift.
    # The certificate solves all rows simultaneously for every point of each closed segment.
    breakpoints = [F(k,4) for k in range(5)]
    for order in permutations(range(4)):
        for left,right in zip(breakpoints,breakpoints[1:]):
            L,H = circle(p,order,left),circle(p,order,right)
            mid = circle(p,order,(left+right)/2)
            assert mid == average(L,H)
            solved=affine_match(L,H,M)
            assert not solved['matches']
            certificates.append(dict(order=order,left=left,right=right,solution=solved))
    uniform4 = dict(pi=p,up_order=up,down_order=down,UST_positive_orientation=A,DST_positive_orientation=B,
        UDST=M,HST_same_order=circle(p,up,F(1,2)),
        UDNAM=average(nam(p,up),nam(p,down)),
        all_24_orders_all_shift_certificate=certificates,orders=24,closed_affine_segments=96,
        interpretation='For this uniform4 target, no single circular shift in any order gives the UDST kernel. All shifts in [0,1] are covered by four affine pieces per order, including endpoints. Either orientation is covered by the full shift range. This is one counterexample, not a classification of all coincidences.')
    assert uniform4['UDNAM'] != M and uniform4['HST_same_order'] != M

    p = target((1,1,1)); chosen=(0,1,2)
    A = circle(p,chosen,max(p)); bad=average(A,A)
    assert stationary(p,bad) and not reversible(p,bad)
    paired = udst(p)[-1]
    wrong_ties=dict(pi=p,up_order=chosen,independently_tied_down_order=chosen,
        unpaired_mixture=bad,paired_reverse_mixture=paired,
        interpretation='Both same orders satisfy weak upward/downward probability sorting when all masses tie. They are not reverse-paired, so Eq101 and the reversibility conclusion do not follow. The bad mixture remains invariant, demonstrating precisely the missing pairing condition.')

    # Small positive-target suite: deterministic label tie rule and its exact reverse.
    cases=0
    for n in range(1,5):
        for weights in product(range(1,4),repeat=n):
            p=target(weights)
            up=sorted(range(n),key=lambda i:(p[i],i));down=list(reversed(up))
            M=average(nam(p,up),nam(p,down));assert_kernel(p,M,reversible=True)
            udst(p)
            cases+=1
    assert cases == 120
    result=dict(scope='Original exact Fraction calculations, not author software. Positive integer weights1..3 for lengths1..4 produce120 ordered vectors, including repeated normalized targets. One-state maximum-shift endpoint is a separately recognized identity extension. No float, efficiency, benchmark or general ergodicity claim.',
        positive_target_vectors=cases,udnam_distinction=udnam_witness,udnam_tie_policy=udnam_ties,
        udst_single_circle_distinction=uniform4,udst_unpaired_tie_failure=wrong_ties)
    return result


def mix(A, B, alpha=F(1, 2)):
    assert 0 <= alpha <= 1
    return [[alpha * a + (1 - alpha) * b for a, b in zip(ar, br)]
            for ar, br in zip(A, B)]


def after(p, A):
    return [sum(p[i] * A[i][j] for i in range(len(p))) for j in range(len(p))]


def self_mass(p, A):
    return sum(p[i] * A[i][i] for i in range(len(p)))


def all_shift_certificates(p, M, tower):
    """Exact affine interval solution for one fixed target and every ordering.

    Shift breakpoints are cumulative interval-boundary differences modulo one.
    Overlap lengths are affine between adjacent breakpoints; no finite shift
    grid is substituted for the all-shift statement on this one target.
    """
    certificates = []
    for order in permutations(range(len(p))):
        c = tower.starts([p[i] for i in order])
        breaks = sorted({F(0), F(1)} | {(a - b) % 1 for a in c for b in c})
        for lo, hi in zip(breaks, breaks[1:]):
            A, B = circle(p, order, lo), circle(p, order, hi)
            for fraction in [F(1, 3), F(1, 2), F(2, 3)]:
                value = circle(p, order, lo + fraction * (hi - lo))
                assert value == mix(B, A, fraction)
                assert value == tower.rows(tower.in_order(p, order, lo + fraction * (hi - lo)), p)
            solved = affine_match(A, B, M)
            assert solved['matches'] is False
            certificates.append(dict(order=order, left=lo, right=hi, solution=solved))
    return certificates


def main():
    nm, tw = load_sibling('nam-boundaries.py'), load_sibling('tower-boundaries.py')
    original = original_witnesses()
    counts = dict(positive_target_vectors=0, compatible_NAM_order_cases=0,
                  independent_UDNAM_tie_pairs=0, paired_UDST_order_cases=0,
                  one_state_UDST_endpoint_extensions=0,
                  arbitrary_fixed_NAM_mixing_weight_cases=0)
    for n in range(1, 5):
        for raw in product([1, 2, 3], repeat=n):
            p = list(target(raw))
            ups = [o for o in permutations(range(n)) if all(p[a] <= p[b] for a, b in zip(o, o[1:]))]
            downs = [o for o in permutations(range(n)) if all(p[a] >= p[b] for a, b in zip(o, o[1:]))]
            matrices = {}
            for order in sorted(set(ups + downs)):
                a = nam(p, order)
                assert a == nm.nam_matrix(p, order)
                assert a == [nm.nam_row(p, order, k) for k in range(n)]
                matrices[order] = a
                counts['compatible_NAM_order_cases'] += 1
            assert all(matrices[o] == matrices[ups[0]] for o in ups)
            for up in ups:
                for down in downs:
                    M = average(matrices[up], matrices[down])
                    assert_kernel(p, M, reversible=True)
                    assert self_mass(p, M) == (self_mass(p, matrices[up]) + self_mass(p, matrices[down])) / 2
                    assert self_mass(p, M) >= max(F(0), 2 * max(p) - 1)
                    counts['independent_UDNAM_tie_pairs'] += 1
            for alpha in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
                assert_kernel(p, mix(matrices[ups[0]], matrices[downs[0]], alpha), reversible=True)
                counts['arbitrary_fixed_NAM_mixing_weight_cases'] += 1
            for anchor in [i for i in range(n) if p[i] == max(p)]:
                tail_labels = [i for i in range(n) if i != anchor]
                for tail in permutations(tail_labels):
                    if not all(p[a] <= p[b] for a, b in zip(tail, tail[1:])):
                        continue
                    up, down = (anchor, *tail), (anchor, *reversed(tail))
                    A, B = circle(p, up, max(p)), circle(p, down, max(p))
                    for order, matrix in [(up, A), (down, B)]:
                        assert matrix == tw.rows(tw.in_order(p, order, max(p)), p)
                    assert all(p[i] * A[i][j] == p[j] * B[j][i] for i in range(n) for j in range(n))
                    M = average(A, B)
                    assert_kernel(p, M, reversible=True)
                    assert self_mass(p, M) == max(F(0), 2 * max(p) - 1)
                    opposite = average(tw.rows(tw.in_order(p, up, max(p), -1), p),
                                       tw.rows(tw.in_order(p, down, max(p), -1), p))
                    assert M == opposite
                    counts['paired_UDST_order_cases'] += 1
                    counts['one_state_UDST_endpoint_extensions'] += int(n == 1)
            counts['positive_target_vectors'] += 1

    p = list(target([4, 3, 2])); up, down = (2, 1, 0), (0, 1, 2)
    U, D = nam(p, up), nam(p, down); M = average(U, D)
    all_nam = [nam(p, o) for o in permutations(range(3))]
    assert all(sum(row[i] > 0 for i, row in enumerate(a)) == 1 and a != M for a in all_nam)
    circle_exclusion = all_shift_certificates(p, M, tw)
    assert len(circle_exclusion) == 42
    Z = nm.zdnam_matrix(p, down)
    H, S = circle(p, down, F(1, 2)), circle(p, down, max(p))
    liu = [[F(0) if i == j else p[j] / max(1 - p[i], 1 - p[j]) for j in range(3)] for i in range(3)]
    for i in range(3):
        liu[i][i] = 1 - sum(liu[i])
    assert_kernel(p, liu, reversible=True)
    assert M != Z and M != H and M != S and M != liu
    assert self_mass(p, M) == F(16, 315) and self_mass(p, Z) == self_mass(p, H) == self_mass(p, S) == 0
    composition = tw.matmul(U, D)
    assert_kernel(p, composition)
    assert composition != M and not reversible(p, composition)
    state_choice = [U[0], D[1], D[2]]
    assert not stationary(p, state_choice)
    nam_scope = dict(pi=p, mixture=M, stationary_self_mass=self_mass(p, M),
                     minimum_self_mass=F(0), ZDNAM=Z, HST=H, ST=S, Liu_modified_Gibbs=liu,
                     U_then_D=composition, U_then_D_reversible=False,
                     row_dependent_component_choice=state_choice, row_dependent_after=after(p, state_choice),
                     all_six_orders_all_shift_exclusion=circle_exclusion)

    p4 = list(target([1, 1, 1, 1])); order = (0, 1, 2, 3)
    _, _, A4, B4, ST4 = udst(p4)
    cert4 = all_shift_certificates(p4, ST4, tw)
    assert len(cert4) == 96
    nam4 = [nam(p4, o) for o in permutations(range(4))]
    assert all(a == nam4[0] and a != ST4 for a in nam4)
    z4 = nm.zdnam_matrix(p4, order)
    assert z4 == nam4[0] and z4 != ST4
    # Source Neal p49 gives uniform FSS/ZFSS as deterministic cycles. Each row
    # has one supported destination under any ordering, unlike the two mixtures.
    assert all(sum(x > 0 for x in row) == 2 for row in ST4)
    assert all(sum(x > 0 for x in row) == 3 for row in nam4[0])
    assert all(sum(x > 0 for x in row) == 1 for row in A4)
    uniform4 = dict(pi=p4, UDST=ST4, UDNAM=nam4[0], every_single_NAM_order_equal=True,
                    ZDNAM=z4, source_uniform_FSS_ZFSS_cycle_example=A4,
                    all_24_orders_all_shift_exclusion=cert4,
                    analytic_certificate='For equal quarter intervals, any shift has two consecutive cyclic offsets q,q+1 with probabilities 1-t,t. Matching two half-probability outputs requires t=1/2. No pair of consecutive residues modulo4 is closed under negation. Thus this single-shift kernel cannot be reversible in any order, whereas UDST is reversible. Boundary shifts have one supported destination and also cannot match.')

    p3 = list(target([1, 1, 1])); A3 = circle(p3, (0, 1, 2), F(1, 3)); B3 = circle(p3, (0, 2, 1), F(1, 3))
    quarter = mix(A3, B3, F(1, 4))
    assert_kernel(p3, quarter)
    assert not reversible(p3, quarter)
    bad_tower = [A3[0], B3[1], B3[2]]
    assert not stationary(p3, bad_tower)
    weight_scope = dict(pi=p3, paired_components=[A3, B3], unequal_fixed_mix=quarter,
                        unequal_fixed_mix_stationary=True, unequal_fixed_mix_reversible=False,
                        state_dependent_choice=bad_tower, after=after(p3, bad_tower))

    periodicity = []
    for n in range(2, 9):
        p = list(target([1] * n)); order = tuple(range(n))
        a = average(nam(p, order), nam(p, tuple(reversed(order))))
        b = udst(p)[-1]
        ac, bc = tw.graph_classes(a), tw.graph_classes(b)
        assert len(ac) == len(bc) == 1 and ac[0]['closed'] and bc[0]['closed']
        assert ac[0]['period'] == (2 if n == 2 else 1)
        assert bc[0]['period'] == (2 if n % 2 == 0 else 1)
        periodicity.append(dict(states=n, UDNAM_classes=ac, UDST_classes=bc))
    joint_states = list(product(range(2), repeat=2))
    joint_scan = [[F(other == (1 - state[0], 1 - state[1])) for other in joint_states] for state in joint_states]
    assert_kernel([F(1, 4)] * 4, joint_scan, reversible=True)
    joint_classes = tw.graph_classes(joint_scan)
    assert len(joint_classes) == 2 and all(x['closed'] and x['period'] == 2 for x in joint_classes)
    boundaries = []
    for w in [[1], [1, 1], [5, 3, 2], [6, 3, 1], [8, 1, 1]]:
        p = list(target(w)); up = sorted(range(len(p)), key=lambda i: (p[i], i)); down = list(reversed(up))
        a, b = average(nam(p, up), nam(p, down)), udst(p)[-1]
        assert_kernel(p, a, reversible=True); assert_kernel(p, b, reversible=True)
        assert self_mass(p, b) == max(F(0), 2 * max(p) - 1)
        boundaries.append(dict(weights=w, pi=p, UDNAM=a, UDST=b,
                               UDNAM_self_mass=self_mass(p, a), UDST_self_mass=self_mass(p, b),
                               minimum_self_mass=max(F(0), 2 * max(p) - 1)))

    output = dict(
        scope='Exact positive finite conditional kernels. Original source-agent witness output is retained without runtime metadata. Expanded tie, independent-component, all-shift and exploration checks use pinned unchanged sibling routines. No efficiency, float, author-code, all-target nonintersection or general convergence claim.',
        dependency_sha256=DEPENDENCIES,
        original_witnesses=original,
        expanded_counts=counts,
        UDNAM_scope=nam_scope,
        UDST_uniform4=uniform4,
        mixture_weight_boundaries=weight_scope,
        uniform_periodicity=periodicity,
        fixed_two_binary_coordinate_scan=dict(states=joint_states, matrix=joint_scan, classes=joint_classes),
        half_dominant_point_boundaries=boundaries,
        assumptions=['Use one complete positive target and current-independent component-selection probabilities at each fixed conditioning environment.',
                     'UDNAM mixes two reversible NAM kernels; independent valid ascending and descending tie policies preserve reversibility, although the mixture can change.',
                     'UDST uses one maximum anchor and a specified ascending tail with its exact reversal, including tied labels. Independent weak sorting does not establish reverse-flow pairing.',
                     'Equal mixture is part of each named method. Unequal constant weights remain invariant but need not remain reversible for UDST.',
                     'One-state UDST maximum shift equals total mass; its stay kernel is an explicitly guarded boundary extension.',
                     'The comparison with uniform FSS/ZFSS uses the source-described deterministic-cycle property; their implementation is not imported or executed here.'])
    print(json.dumps(stringify(output), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
