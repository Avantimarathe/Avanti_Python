def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    user_input = int(input("Enter a non-negative integer: "))
    if user_input < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {user_input} is {factorial(user_input)}")
except ValueError:
    print("Invalid input! Please enter an integer.")