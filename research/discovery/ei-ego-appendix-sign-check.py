#!/usr/bin/env python3
"""Original rational witness for a printed Appendix1 derivative sign; no I/O."""
from fractions import Fraction as F
import json

# Journal PDF36 / printed490, SHA356260d...: quadratic u^2/D - 2*c*u/D.
# Same R and y as the first calculator, but r=(1/2,1/4), compatible with
# p=1, theta=log(2)/2 and points 0,2,candidate -2 on a line.
R = [[F(1), F(1, 2)], [F(1, 2), F(1)]]
det = R[0][0] * R[1][1] - R[0][1] * R[1][0]
Rinv = [[R[1][1]/det, -R[0][1]/det], [-R[1][0]/det, R[0][0]/det]]
dot = lambda a, b: sum((x*y for x,y in zip(a,b)), F(0))
mv = lambda a, b: [dot(row,b) for row in a]
r, residual, mean = [F(1,2),F(1,4)], [F(-1),F(1)], F(1)
c = dot(r,mv(Rinv,residual))
D = 1-dot(r,mv(Rinv,r))
correct_y, printed_equation_y = mean+c,mean-c
quadratic = lambda y: ((y-mean)**2-2*c*(y-mean))/D
true_derivative = lambda y: 2*((y-mean)-c)/D
printed_derivative = lambda y: 2*((y-mean)+c)/D
assert c == F(-1,2) and D == F(3,4)
assert correct_y == F(1,2) and printed_equation_y == F(3,2)
assert true_derivative(correct_y)==0 and printed_derivative(printed_equation_y)==0
assert true_derivative(printed_equation_y) != 0
assert quadratic(correct_y) < quadratic(printed_equation_y)
print(json.dumps({
    'scope':'Original finite rational witness for this printed derivative only; not author code or an optimization run',
    'source_pdf_sha256':'356260d0303a7fa2c8cc4456f46ebc9f39c0bcf763b2e3982c2b78921eab4a57',
    'locator':'PDF36, journal p490, Appendix1 first quadratic and next displayed derivative',
    'c':str(c),'D':str(D),'Eq7_and_correct_stationary_prediction':str(correct_y),
    'printed_plus_sign_stationary_prediction':str(printed_equation_y),
    'quadratic_at_correct':str(quadratic(correct_y)),
    'quadratic_at_printed_stationary_point':str(quadratic(printed_equation_y)),
    'true_derivative_at_printed_stationary_point':str(true_derivative(printed_equation_y)),
    'finding':'The second term in the displayed derivative needs a minus to differentiate the immediately preceding quadratic. Eq7 and EI Eq15 are not contradicted.'
},indent=2,sort_keys=True))
