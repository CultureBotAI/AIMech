"""Constructed FiLM parameter-analogy boundaries; not visual-reasoning experiments."""
import json


def combine(a,b,c):return [x+y-z for x,y,z in zip(a,b,c)]


def result():
    first=[1.,.2];second=[2.,.4];third=[.5,-.1]
    composed=combine(first,second,third);feature=3.
    affine=lambda theta:theta[0]*feature+theta[1]
    affine_result=affine(composed)
    affine_combination=affine(first)+affine(second)-affine(third)
    assert abs(affine_result-affine_combination)<1e-12
    # Two successive scales create products even if every individual layer is linear.
    network=lambda theta:theta[1]*max(0.,theta[0])
    a,b,c=[1.,1.],[2.,2.],[0.,0.]
    output=network(combine(a,b,c));answer_combination=network(a)+network(b)-network(c)
    assert output==9 and answer_combination==5 and output!=answer_combination
    return dict(single_fixed_feature_affine_identity=dict(composed_parameters=composed,output=affine_result,output_combination=affine_combination),
                multilayer_counterexample=dict(parameter_combination_output=output,combination_of_outputs=answer_combination),
                interpretation='Parameter-space arithmetic neither proves output-space arithmetic nor semantic analogy correctness.')


if __name__=='__main__':print(json.dumps(result(),indent=2,sort_keys=True))
