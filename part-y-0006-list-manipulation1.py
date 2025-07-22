ages = [55, 47, 95, 78, 17, 65, 16, 54, 21, 12, 44, 14, 100, 8]

childs = [age for age in ages if age < 18]

adults = [age for age in ages if age >= 18]

print(childs)

print(adults)

# [17, 16, 12, 14, 8]
# [55, 47, 95, 78, 65, 54, 21, 44, 100]
