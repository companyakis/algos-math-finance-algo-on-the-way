# mustafa buyukdereli was here:)

# y = x ** 3 + 12 ** x + x ** 2 - 5

x, y = sym.symbols("x, y")

my_equation = x ** 3 + 12 ** x + x ** 2 - 5

display(sym.Eq(y, my_equation))
