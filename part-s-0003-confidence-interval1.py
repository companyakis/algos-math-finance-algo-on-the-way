import numpy as np 

np.random.seed(2025)

# min-max price expectations, and 5000 price data

price_expectations = np.random.randint(50, 100, 5000)

print(price_expectations[: 10])

mean_price_expectations = np.mean(price_expectations)

print(mean_price_expectations)

std_price_expectations = np.std(price_expectations)

print(std_price_expectations)

"""
[80 68 80 62 53 69 62 82 72 87]
74.6766
14.437825751822883
"""
