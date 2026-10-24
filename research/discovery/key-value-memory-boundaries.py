"""Chosen key/value read boundaries, not an implementation or empirical replication."""
import json,math

def read(keys,values,q):
 scores=[q*k for k in keys];weights=[math.exp(s-max(scores)) for s in scores];weights=[w/sum(weights) for w in weights]
 return sum(w*v for w,v in zip(weights,values))
keys=[math.log(2),0];values=[1,3];base=read(keys,values,1)
assert math.isclose(base,5/3) and math.isclose(read(keys[::-1],values[::-1],1),base)
unpaired=read(keys,values[::-1],1);duplicated=read([keys[0],keys[0],0],[1,1,3],1)
assert math.isclose(unpaired,7/3) and math.isclose(duplicated,7/5)
# The initial set keeps only slot0. A changed query cannot restore slot1.
restricted=read([keys[0]],[values[0]],-10);full=read(keys,values,-10);assert restricted==1 and full>2.99
q,o,R=1,base,2;after=R*(q+o);before=R*q+o;assert not math.isclose(after,before)
print(json.dumps(dict(read=base,paired_permutation_equal=True,unpaired_value_swap=unpaired,duplicate_slot_read=duplicated,later_query_restricted_read=restricted,later_query_full_read=full,transform_after_sum=after,transform_query_only=before,limits='Chosen one-dimensional examples; no hashing implementation, model fitting, author code or benchmark.'),indent=2))
