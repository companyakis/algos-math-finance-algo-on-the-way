"""
The results of a mathematics exam at a university follow a normal distribution. The average score for the exam is 75, and the standard deviation is 5.

Based on this information, what is the probability that a randomly selected student will score between 80 and 85?
"""

from scipy.stats import norm

print(norm.cdf(85, 75, 5) - norm.cdf(80, 75, 5)) # 0.13590512198327787

