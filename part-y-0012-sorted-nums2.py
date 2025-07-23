numbers = [3, 11, 22, 43, 100, 96, 1454, 1333, 1, 7]

evens = []

odds = []

for num in numbers:

  if (num % 2 == 0):

    evens.append(num)

  else:

    odds.append(num)


print(f"Reverse sorted even numbers: {sorted(evens, reverse = True)}")

print(f"Reverse sorted odd numbers: {sorted(odds, reverse = True)}")

# Reverse sorted even numbers: [1454, 100, 96, 22]
# Reverse sorted odd numbers: [1333, 43, 11, 7, 3, 1]
