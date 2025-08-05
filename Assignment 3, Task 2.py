import math

# Step 1: Ask the user for a number as input
try:
    number = float(input("Enter a number: "))

    # Step 2: Perform calculations using the math module
    # Square root (only for non-negative numbers)
    if number >= 0:
        square_root = math.sqrt(number)
    else:
        square_root = "Undefined (square root of a negative number is not real)"

    # Natural logarithm (only for positive numbers)
    if number > 0:
        natural_log = math.log(number)
    else:
        natural_log = "Undefined (logarithm of non-positive number is not defined)"

    # Sine (valid for all real numbers)
    sine_value = math.sin(number)

    # Step 3: Display the results
    print("\nResults:")
    print(f"Square root of {number}: {square_root}")
    print(f"Natural logarithm (ln) of {number}: {natural_log}")
    print(f"Sine of {number} radians: {sine_value}")

except ValueError:
    print("Invalid input. Please enter a valid number.")