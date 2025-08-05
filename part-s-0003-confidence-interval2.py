confidence_interval = 0.95 

z_value = 1.96

lower_limit = mean_price_expectations - z_value * (std_price_expectations / (len(price_expectations) ** 0.5))

print(lower_limit)

upper_limit = mean_price_expectations + z_value * (std_price_expectations / (len(price_expectations) ** 0.5))

print(upper_limit)

"""
74.2764038878076
75.07679611219238

"""
