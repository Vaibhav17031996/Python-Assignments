# Using the Math Module for Calculations
import math

num = int(input("Enter a number: "))

if num < 0:
    print("Square root: Undefined for negative numbers.")
else:
    sqrt = math.sqrt(num)
    print(f"Square root: {sqrt}")

if num <= 0:
    print("Logarithm: Undefined for zero and negative numbers.")
else:
    log = math.log(num)
    print(f"Logarithm: {log}")    

sine = math.sin(num)
print(f"Sine: {sine}")
