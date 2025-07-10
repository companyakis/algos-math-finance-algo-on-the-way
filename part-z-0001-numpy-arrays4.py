import numpy as np

ages = [22, 9, 11, 44, 87, 95, 3, 21, 87, 66, 24, 17, 45]

np_ages = np.array(ages)

print(np_ages.max())
print(np_ages.min())

print(np_ages.mean())

print(np_ages.sum())

print(np_ages.std())

print(np_ages.cumsum())

print(np_ages.argmax())

print(np_ages.argmin())

# 95
# 3
# 40.84615384615385
# 531
# 31.368397016120326
# [ 22  31  42  86 173 268 271 292 379 445 469 486 531]
# 5
# 6
