#Write a program to find the simple interest when the value of principle, rate of interest and time period is provided by the user.
# Take input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (per year in %): "))
time = float(input("Enter the time period (in years): "))

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Display the result
print(f"The Simple Interest is: {simple_interest:.2f}")
