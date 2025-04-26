#Write a program to find the Euclidean distance between two coordinates. Take both the coordinates from the user as input.
import math

# Take input for the first coordinate
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Take input for the second coordinate
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display the result
print(f"The Euclidean distance between the points is: {distance:.2f}")
