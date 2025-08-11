# Calculate Factorial Using a Function

# Method 1: Using for loop
'''
    def factorial(n):
        if n < 0:
            return None        
        answer = 1
        for i in range(1, n+1):
            answer *= i
        return answer

    num = int(input("Enter a number: "))
    result = factorial(num)
    if result == None:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {num} is: {result}")
'''

# Method 2: Using While loop
'''
    def factorial(n):
        if n < 0:
            return None
        answer = 1
        while n > 1:
            answer *= n
            n -= 1
        return answer

    num = int(input("Enter a number: "))
    result = factorial(num)
    if result == None:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {num} is: {result}")
'''

# Method 3: Using Recursion
def factorial(n):
    if n < 0 :
        return None
    elif n in (0, 1):
        return 1
    else :
        return n * factorial(n-1)
    
num = int(input("Enter a number: "))
result = factorial(num)
if result == None:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is: {result}")