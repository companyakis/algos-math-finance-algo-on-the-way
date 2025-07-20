from fractions import Fraction

try: 
    user_input = Fraction(input("Type your fraction (num_a / num_b): "))
    
    print(f"You entered: {float(user_input)}")
    
except ValueError:
    
    print("Zero division error! Divisor can't be zero...")

