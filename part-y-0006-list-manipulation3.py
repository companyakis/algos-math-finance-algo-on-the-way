sales_monthly = [12_500, 43_450, 9_000, 16_400, 17_600, 8_400]

monthly_premiums = [0.15 * sale if sale > 10_000 else 0 for sale in sales_monthly]

print(monthly_premiums)

# [1875.0, 6517.5, 0, 2460.0, 2640.0, 0]

