"""Chosen generated-kernel algebra; no author implementation or model fitting."""
import json
from math import isclose
# A scalar one-position feature branch and generated-kernel branch share input x.
theta=2.;phi=3.
def forward(x):return (theta*x)*(phi*x)
x=1.5
feature_path=phi*x*theta;kernel_path=theta*x*phi
full_derivative=feature_path+kernel_path
numerical=(forward(x+1e-6)-forward(x-1e-6))/2e-6
assert isclose(full_derivative,numerical,rel_tol=1e-7)
assert not isclose(full_derivative,feature_path)
assert isclose(forward(2*x),4*forward(x)) and not isclose(forward(2*x),2*forward(x))
# Positive normalized vertical/horizontal filters form a rank-one spatial kernel.
v=[.25,.75];h=[.6,.4];kernel=[[a*b for b in h] for a in v]
assert isclose(sum(map(sum,kernel)),1)
det=kernel[0][0]*kernel[1][1]-kernel[0][1]*kernel[1][0];assert isclose(det,0,abs_tol=1e-12)
assert all(x>0 for row in kernel for x in row) # An impulse spreads; not one exact shift.
nonseparable=[[.5,0],[0,.5]];assert nonseparable[0][0]*nonseparable[1][1]>.0
# Table1 means are sums of squared pixel errors; this subtraction is not a significance test.
patch_cnn=[11.480,105.242,101.880];patch_dynamic=[11.114,101.983,98.790];whole_dynamic=[12.340,117.316,118.402]
assert all(a<b for a,b in zip(patch_dynamic,patch_cnn))
assert all(a>b for a,b in zip(whole_dynamic,patch_cnn))
print(json.dumps(dict(feature_branch_derivative=feature_path,kernel_branch_derivative=kernel_path,full_derivative=full_derivative,generated_kernel=kernel,separable_determinant=det,nonseparable_target_determinant=.25,patch_cnn_minus_dynamic=[a-b for a,b in zip(patch_cnn,patch_dynamic)],whole_dynamic_minus_patch_cnn=[a-b for a,b in zip(whole_dynamic,patch_cnn)]),sort_keys=True))
