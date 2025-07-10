cost_and_sales = np.array([-500, 65, 24, 46, 87, 87, 65, 112, 98, 100, 61, 77])

print(np.where(cost_and_sales.cumsum() > 0))

sum = 0

for i in cost_and_sales:
  sum += i
  print(sum)

# (array([ 8,  9, 10, 11]),)

# -500
# -435
# -411
# -365
# -278
# -191
# -126
# -14
# 84
# 184
# 245
# 322

