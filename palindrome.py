""" 
This script takes a number input from the user, then checks if the number is a palindrome or 
not by reversing it and comparing it with the original number. Finally, it prints whether the 
number is a palindrome or not.
"""


# Take input from the user
num = int(input("Enter a number: "))

# Initialize variables for storing the reverse of the number and a temporary variable
reverse = 0
temp = num

# Reverse the number
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10

# Check if the original number is equal to its reverse
if num == reverse:
    print('Palindrome')
else:
    print("Not Palindrome")
