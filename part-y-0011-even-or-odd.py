numbers = [3, 11, 22, 43, 100, 96, 1454, 1333, 1, 7]

evens = []

odds = []

for num in numbers:

  if (num % 2 == 0):

    evens.append(num)

  else:

    odds.append(num)


print(f"Even numbers: {evens}")

print(f"Odd numbers: {odds}")

# Even numbers: [22, 100, 96, 1454]
# Odd numbers: [3, 11, 43, 1333, 1, 7]
