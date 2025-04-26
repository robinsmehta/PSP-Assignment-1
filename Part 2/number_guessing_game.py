''' Write a program to create a number guessing game for the user. The program should ask the user to input a number. The program specifications are as mentioned below.
The program should generate a random number for the answer. 
The program should prompt the user for a number input. 
The program should provide the feedback to the user after each guesses (e.g. “Too high”, “Too low” or “Correct number”). 
The program should check the user input for 5 times and allow the users to guess for at most 5 times if their input don’t match the answer number.
If the user is not able to guess the answer within 5 times, the program should display “Game Over” message and exit.'''

import random

# Generate a random number between 1 and 10
answer = random.randint(1, 10)

# Maximum number of attempts
max_attempts = 5

print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 10.")

# Loop for 5 attempts
for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))
    
    if guess == answer:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess < answer:
        print("Too low!")
    else:
        print("Too high!")
else:
    # This else belongs to the for-loop (not if!)
    print("Game Over! You've used all your attempts.")
    print(f"The correct number was {answer}.")
