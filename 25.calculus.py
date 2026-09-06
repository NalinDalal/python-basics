# Calculus: Derivatives and Gradients using sympy
import sympy as sp
from sympy import log

# Derivative
x = sp.symbols("x")
f = x**2 + 3 * x + 2
f_prime = sp.diff(f, x)
print("Function:", f)
print("Derivative:", f_prime)

# Integral
f_int = sp.integrate(f, x)
print("Integral:", f_int)

f2 = log(x)
print(f2)
f2_int = sp.integrate(f2, x)
print("Integral:", f2_int)


# Gradient (for multivariable functions)
y = sp.symbols("y")
g = x**2 + y**2
gradient = [sp.diff(g, var) for var in (x, y)]
print("Function:", g)
print("Gradient:", gradient)
