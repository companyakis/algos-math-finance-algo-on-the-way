quarterly_sales_by_months = np.array([[50000, 62000, 23000], [45000, 24000, 83000], [65000, 45000, 72000], [95000, 54700, 95600]])

quarterly_sales_by_months_exceeds_50000 = quarterly_sales_by_months > 50000

premium_by_months = quarterly_sales_by_months * 0.12 * quarterly_sales_by_months_exceeds_50000

print(premium_by_months)

# [[    0.  7440.     0.]
#  [    0.     0.  9960.]
#  [ 7800.     0.  8640.]
#  [11400.  6564. 11472.]]
