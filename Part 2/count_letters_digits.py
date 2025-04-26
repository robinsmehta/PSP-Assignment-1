#Write a Python program that accepts a string and calculates the number of digits and letters.
# Take input from the user
user_input = input("Enter a string: ")

# Initialize counters
letters = 0
digits = 0

# Loop through each character in the input
for char in user_input:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

# Display the results
print(f"Letters: {letters}")
print(f"Digits: {digits}")
