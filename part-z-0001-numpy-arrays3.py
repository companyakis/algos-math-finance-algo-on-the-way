import numpy as np

ages = [22, 9, 11, 44, 87, 95, 3, 21, 87, 66, 24, 17, 45]

np_ages = np.array(ages)

print(np_ages[1])

print(np_ages[2:])

print(np_ages[:2])

print(np_ages[-1])

print(np_ages[-2])

print(np_ages[2:7:3])

print(np_ages[::-1])

# 9
# [11 44 87 95  3 21 87 66 24 17 45]
# [22  9]
# 45
# 17
# [11 95]
# [45 17 24 66 87 21  3 95 87 44 11  9 22]
