""" 
This script takes three numbers as input from the user and then compares them to find and print the largest number.
"""


# Take user input for the first number
num1 = int(input("Enter Your First Number: "))

# Take user input for the second number
num2 = int(input("Enter Your Second Number: "))

# Take user input for the third number
num3 = int(input("Enter Your Third Number: "))

# Compare the numbers to find the largest one
if num1 > num2:
    if num1 > num3:
        print("Your First Number is the Largest.")
    else:
        print("Your Third Number is the Largest.")
elif num2 > num3:
    print("Your Second Number is the Largest.")
else:
    print("Your Third Number is the Largest.")
