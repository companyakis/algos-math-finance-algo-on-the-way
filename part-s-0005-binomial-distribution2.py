"""
A company's sales team is going to make a new product presentation to a client. Based on the company's historical data, the probability of a presentation resulting in a sale is 30%.

The sales team will make presentations to 4 different clients this week.

What is the probability that the sales team will convert exactly 2 of these 4 presentations into sales?

"""

import math

c = math.factorial(4) / (math.factorial(2) * math.factorial(2))

p = c * (0.3) ** (2) * (1 - 0.3) ** (4 - 2)

print(p) # 0.2646
