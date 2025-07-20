from fractions import Fraction

try: 
    user_input = Fraction(input("Type your fraction (num_a / num_b): "))
    
    print(f"You entered: {float(user_input)}")
    
except ValueError:
    
    print("Please, use format => (number a) / (number b)... a and b must be numbers!")

except ZeroDivisionError:
    
    print("Divisor  can't be zero...")
