ages = [22, 9, 11, 44, 87, 95, 3, 21, 87, 66, 24, 17, 45, 96, 14, 34]

np_ages = np.array(ages)

print(np_ages > 20)

print(np_ages[np_ages > 20])

print(np_ages[np_ages < 50])

# [ True False False  True  True  True False  True  True  True  True False
#   True  True False  True]

# [22 44 87 95 21 87 66 24 45 96 34]

# [22  9 11 44  3 21 24 17 45 14 34]
