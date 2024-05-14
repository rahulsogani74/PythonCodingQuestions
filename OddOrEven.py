""" 
This script prompts the user to input a number and then determines whether the number is even or odd. 
If the number is divisible by 2 without a remainder, it is considered even; otherwise, it is considered odd.
"""


# Take user input for a number
num = int(input("Give your number : "))

# Check if the number is even or odd
if num % 2 == 0:
    print("Given Number is Even")
else:
    print("Given Number is Odd")
