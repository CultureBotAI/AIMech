"""Constructed T-Few objective distinctions, not model training."""
import json,math


def result():
    wrong=[[.8,.2],[.5]];tokens=[p for row in wrong for p in row]
    token_ul=-sum(math.log1p(-p) for p in tokens)/len(tokens)
    sequence_ul=-sum(math.log1p(-math.prod(row)) for row in wrong)/len(wrong)
    assert not math.isclose(token_ul,sequence_ul)
    gold=[.6,.6];other=[.5]
    joint=[math.prod(gold),math.prod(other)]
    beta=[sum(map(math.log,row))/len(row) for row in [gold,other]]
    normalized=[math.exp(x) for x in beta]
    assert joint[0]<joint[1] and normalized[0]>normalized[1]
    probabilities=[p/sum(normalized) for p in normalized]
    ln=-math.log(probabilities[0])
    grad_beta=[probabilities[0]-1,probabilities[1]];eps=1e-5
    def loss(scores):return -scores[0]+math.log(sum(math.exp(x) for x in scores))
    finite=[]
    for i in range(2):
        a,b=beta[:],beta[:];a[i]+=eps;b[i]-=eps
        finite.append((loss(a)-loss(b))/(2*eps))
    assert all(math.isclose(x,y,abs_tol=1e-10) for x,y in zip(grad_beta,finite))
    # A token shared by correct and incorrect strings can receive opposing terms.
    p=.8;lm_derivative=-1/p;ul_derivative=1/(1-p)
    assert lm_derivative<0<ul_derivative
    return dict(token_average_unlikelihood=token_ul,whole_sequence_unlikelihood=sequence_ul,
                joint_candidate_probabilities=joint,geometric_mean_token_scores=normalized,
                candidate_softmax=probabilities,length_normalized_loss=ln,
                beta_gradient=grad_beta,finite_difference=finite,
                illustrative_shared_prefix_derivatives=dict(lm=lm_derivative,ul=ul_derivative))


if __name__=='__main__':print(json.dumps(result(),indent=2,sort_keys=True))
