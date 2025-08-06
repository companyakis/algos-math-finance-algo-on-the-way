import numpy as np
from scipy.stats import bernoulli

p = 0.5 # heads or tails, 1 or 0

result = bernoulli.rvs(p) # rvs -> random variates

print(f"Result of a single trial: {result}")

number_of_trial = 1000

results = bernoulli.rvs(p, size = number_of_trial)

print(type(results))

print(results[: 10])

# Result of a single trial: 0
# <class 'numpy.ndarray'>
# [1 0 0 1 0 1 1 1 0 0]
