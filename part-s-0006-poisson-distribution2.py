/*
Question: A website receives an average of 2 visitors per minute (λ=2).

What is the probability that the website will receive exactly 3 visitors in any given minute?  

*/

import math

e_val = math.e 

lambda_val = 2

k = 3

p = ((lambda_val ** k) * (e_val ** (-lambda_val))) / (math.factorial(k))

print(p) # 0.1804470443154836

print(round(p, 4)) # 0.1804
