import numpy as np

ages = [22, 9, 11, 44, 87, 95, 3, 21]

np_ages = np.array(ages)

print(type(np_ages))

print(np_ages.size)

print(np_ages.shape)

print(np_ages.ndim)

print(np_ages.dtype)

print(np_ages.nbytes)

# <class 'numpy.ndarray'>
# 8
# (8,)
# 1
# int64
# 64
