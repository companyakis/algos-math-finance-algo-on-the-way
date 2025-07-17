from fractions import Fraction

x = Fraction(4, 5)

print(x)

y = 0.8

print(x == y)

x_float = float(x)

print(x_float == y)

y_fraction = Fraction(y)

print(float(x) == float(y_fraction))

# 4/5
# False
# True
# True
