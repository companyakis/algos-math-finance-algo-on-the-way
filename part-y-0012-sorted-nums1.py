numbers = [3, 11, 22, 43, 100, 96, 1454, 1333, 1, 7]

evens = []

odds = []

for num in numbers:

  if (num % 2 == 0):

    evens.append(num)

  else:

    odds.append(num)


print(f"Sorted Even numbers: {sorted(evens)}")

print(f"Sorted Odd numbers: {sorted(odds)}")

# Sorted Even numbers: [22, 96, 100, 1454]
# Sorted Odd numbers: [1, 3, 7, 11, 43, 1333]
