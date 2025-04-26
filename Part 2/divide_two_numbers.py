# Write a program that prompts the user for two integer values and displays the results of the first number divided by the second, with exactly two decimal places displayed.
# Take two integer inputs from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Check if the second number is zero to avoid division by zero
if num2 == 0:
    print("Error: Cannot divide by zero.")
else:
    result = num1 / num2
    # Display the result with exactly two decimal places
    print(f"The result is: {result:.2f}")
