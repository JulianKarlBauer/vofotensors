import vofotensors
from pprint import pprint
from vofotensors.abc import d1
import sympy as sp

N4 = vofotensors.fabric_tensors.N4s_parametric['cubic']['d1']

pprint(N4)

# Mathematica

# matrix = {{1/5 - 2 d1,  d1 + 1/15,  d1 + 1/15,           0,           0,           0},
# { d1 + 1/15, 1/5 - 2 d1,  d1 + 1/15,           0,           0,           0},
# { d1 + 1/15,  d1 + 1/15, 1/5 - 2 d1,           0,           0,           0},
# {         0,          0,          0, 2 d1 + 2/15,           0,           0},
# {         0,          0,          0,           0, 2 d1 + 2/15,           0},
# {         0,          0,          0,           0,           0, 2 d1 + 2/15}};

# Result: -1/15 <= d1 <= 2/45

substitutions = ['-1/15', '2/45']

for expr in substitutions:
    print()
    print('d1=', expr)
    pprint(N4.subs({d1: sp.sympify(expr)}))

w = sp.symbols('w', real=True)

low = N4.subs({d1: sp.sympify(substitutions[0])})
high = N4.subs({d1: sp.sympify(substitutions[1])})

combined = w*low + (sp.S(1)-w) * high
