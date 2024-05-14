""" 
This script implements a simple number guessing game where the user tries to guess a random target number between
1 and 100. The user can enter their guesses or choose to quit the game by typing 'Q'.
"""

import random

# Generate a random target number between 1 and 100
target = random.randint(1, 100)

# Start the guessing game loop
while True: 
    # Ask the user to guess the target number or quit
    user_choice = input("Guess the target or Quit(Q) : ")
    
    # Check if the user wants to quit
    if user_choice == "Q":
        break
    
    # Convert the user's input to an integer
    user_choice = int(user_choice)
    
    # Check if the user's guess matches the target
    if user_choice == target:
        print("Success : Correct Guess!!" )
        break
    elif user_choice < target:
        print("Your number was too small. Take a bigger guess...")
    else:
        print("Your number was too big. Take a smaller guess...")

# Display "Game Over" message when the game ends
print("--- Game Over ---")

