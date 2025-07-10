ages = [22, 9, 11, 44, 87, 95, 3, 21, 87, 66, 24, 17, 45, 96, 14, 34]

np_ages = np.array(ages)

np_ages1 = np_ages.astype(np.float16)

print(np_ages1 * 1.12)

np_ages2 = np_ages / 2

np_ages2 = np_ages2.astype(np.int32)

print(np_ages2)

# [ 24.64  10.08  12.32  49.28  97.44 106.44   3.36  23.52  97.44  73.94
#   26.88  19.05  50.4  107.5   15.68  38.1 ]

# [11  4  5 22 43 47  1 10 43 33 12  8 22 48  7 17]
