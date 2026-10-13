"""Finite source-boundary examples; no GRINCH implementation is executed."""
from itertools import combinations
import json


def connected(vertices, edges):
    vertices=set(vertices)
    if not vertices:return False
    reached={min(vertices)}
    while True:
        nxt=reached|{v for u,v in edges if u in reached and v in vertices}|{u for u,v in edges if v in reached and u in vertices}
        if nxt==reached:return reached==vertices
        reached=nxt


def main():
    # Paper model separation holds exactly for f(A,B)=connectivity(A union B).
    edges=set(combinations([0,1,2],2))
    score=lambda a,b:int(connected(set(a)|set(b),edges))
    # Tree ((0,3),(1,2)): v={0}, l={1}; candidates are not siblings.
    cross=score([0],[1]);v_sib=score([0],[3]);l_sib=score([1],[2])
    merge=cross>max(v_sib,l_sib)
    ascend_l=cross<l_sib
    ascend_v=cross<v_sib
    assert (cross,v_sib,l_sib)==(1,0,1)
    assert not any([merge,ascend_l,ascend_v])
    # Inspected Scala uses negated strict preference, which advances l on equality.
    scala_ascend_l=not(cross>l_sib)
    assert scala_ascend_l
    # Literal positive beam control after a completed outer iteration.
    graft_attempts=0;graft_beam=100000000
    assert graft_attempts<graft_beam
    print(json.dumps(dict(tied_paper_state=dict(tree=[[0,3],[1,2]],graph_edges=sorted(edges),scores=dict(cross=cross,v_sibling=v_sib,l_sibling=l_sib),literal_merge=merge,literal_ascend_l=ascend_l,literal_ascend_v=ascend_v,scala_ascend_l=scala_ascend_l),beam_predicate=dict(attempts=graft_attempts,configured_beam=graft_beam,exit_after_completed_outer_iteration=graft_attempts<graft_beam),limits="Standalone valid tree/score state and scalar predicates only. No insertion sequence, reachable author execution, algorithm-wide failure, theorem refutation, benchmark or universal correctness claim."),indent=2))


if __name__=='__main__':main()
