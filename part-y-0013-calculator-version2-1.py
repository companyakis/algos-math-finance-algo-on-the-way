import numbers

def calculator(x, y, sign):

  if (not isinstance(x, numbers.Number) or not isinstance(y, numbers.Number)):

    print("Wrong data types. Only numeric values!..")

    return

  if (sign == "+"):

    print(f"{x} + {y} = {x + y}") 

  elif (sign == "-"):

    print(f"{x} - {y} = {x - y}") 

  elif (sign == "*"):

    print(f"{x} * {y} = {x * y}")

  elif (sign == "/" and y != 0):

    print(f"{x} / {y} = {x / y}")

  elif (sign == "/" and y == 0):

    print("Divisor can't be zero!")

  elif (sign == "%" and y != 0):

    print(f"Remainder => {x} % {y} = {x % y}")

  else:
    
    print("Unknown selection or wrong data types! Try again later...")
