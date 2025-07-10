cost_and_sales = np.array([-500, 65, 24, 46, 87, 87, 65, 112, 98, 100, 61, 77])

print(cost_and_sales.cumsum() > 0)

print(np.where(cost_and_sales.cumsum() > 0)[0][0])

# [False False False False False False False False  True  True  True  True]

# 8
