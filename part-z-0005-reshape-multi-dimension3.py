quarterly_sales_by_months = np.array([[50000, 62000, 23000], [45000, 24000, 83000], [65000, 45000, 72000], [95000, 54700, 95600]])

quarterly_sales_by_months_exceeds_50000 = quarterly_sales_by_months > 50000

print(quarterly_sales_by_months_exceeds_50000)

sales_data_for_premium = quarterly_sales_by_months[quarterly_sales_by_months_exceeds_50000]

print(sales_data_for_premium)

# [[False  True False]
#  [False False  True]
#  [ True False  True]
#  [ True  True  True]]

# [62000 83000 65000 72000 95000 54700 95600]
