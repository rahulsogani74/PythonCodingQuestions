""" 
This script calculates the factorial of a given number using recursion and prints the result. 
It ensures that the factorial function is called only if the input number is greater than or equal to 1.
"""


# Take user input for the number
num = int(input("Enter Your Number: "))

# Define a function to calculate the factorial
def factorial(num):
    # Base case: if num is 1, return 1
    if num == 1:
        return 1
    # Recursively call the factorial function
    # and multiply the result with the current num
    num *= factorial(num - 1)
    return num

# Check if the input number is greater than or equal to 1
if num >= 1:
    # Call the factorial function and print the result
    print("Factorial of", num, "is", factorial(num))
