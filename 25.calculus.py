# Calculus: Derivatives and Gradients using sympy
import sympy as sy
from sympy import log
from sympy.plotting import plot
import numpy as np

# Derivative
x = sy.symbols("x")
f = x**2 + 3 * x + 2
f_prime = sy.diff(f, x)
print("Function:", f)
print("Derivative:", f_prime)

# Integral
f_int = sy.integrate(f, x)
print("Integral:", f_int)
print("\n")

f2 = log(x)  # log to base e
# math.log(x, base)
print(f2)
f2_int = sy.integrate(f2, x)
print("Integral:", f2_int)

print("\n")

f3 = x**2 + x + 1
print(f3)
# Calculate definite integral (area under curve)
area = sy.integrate(f3, (x, 0, 1))
print("area b/w 0 and 1:", area)

print("\n")

# find the area between two curves  f(x) and  g(x)
f4 = x**2
g4 = x
print("f(x):", f4)
print("g(x):", g4)
# Find intersection points
intersections = sy.solve(f4 - g4, x)  # [0, 1]

# Integrate difference over the interval
area1 = sy.integrate(f4 - g4, (x, intersections[0], intersections[1]))
print("area under curve b/w 0-1:", abs(area1))  # Output: 1/6
print("\n")

# to plot the area under curve
x_array = np.linspace(0, 4, 1000)
f_array = sy.lambdify(x, f4)(x_array)
# plot(f4, (x, 0, sy.pi), fill={"x": x_array, "y1": f_array, "color": "green"})
plot(f4, (x, 0, 4))
print("\n")

# Gradient (for multivariable functions)
y = sy.symbols("y")
g = x**2 + y**2
gradient = [sy.diff(g, var) for var in (x, y)]
print("Function:", g)
print("Gradient:", gradient)
