import sys

def equal_float(a, b):
    return abs(a - b) <= sys.float_info.epsilon
    print(a)
    print(b)


import math

x = 2.75
x.as_integer_ratio()
print(x)
s = 14.25.hex()
f = float.fromhex(s)
t = f.hex()
print(s, f, t)

import math
q = math.pi * (5 ** 2)
s = math.hypot(5, 12)
z = math.modf(13.732)

print(q)
print(s)
print(z)