""" 
This script prompts the user to input a number and then determines whether the number is negative, 
zero, or positive based on the conditions provided.
"""


# Take user input for a number
num = int(input("Enter your number: "))

# Check if the number is negative, zero, or positive
if num < 0:
    print("Given Number is Negative")
elif num == 0:
    print("Given number is Zero")
else:
    print("Given number is Positive")
