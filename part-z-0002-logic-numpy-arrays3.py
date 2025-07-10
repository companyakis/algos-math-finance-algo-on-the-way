ages = [22, 9, 11, 44, 87, 95, 3, 21, 87, 66, 24, 17, 45, 96, 14, 34]

np_ages = np.array(ages)

age_search = (np_ages <= 30) | (np_ages > 70)

print(np_ages[age_search])

# [22  9 11 87 95  3 21 87 24 17 96 14]
