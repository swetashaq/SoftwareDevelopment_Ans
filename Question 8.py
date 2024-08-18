import math # importing math module to use math.sqrt() function

def is_square_number(n): # defining a new function
    if n < 0:  
        return False  # Checking given number is negative or not

    sqrt_n = math.sqrt(n) # The function that calculates the square root. 
    
    return sqrt_n.is_integer() # to check if the root calculated is integer.

# Testing the function defined above
number = 36
# printing if the number is a square or not.
if is_square_number(number):
    print(f"{number} is a valid square number.")
else:
    print(f"{number} is not a square number.")