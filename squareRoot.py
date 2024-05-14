""" 
This code snippet calculates the square root of a given number (num) using two different methods. 
The first method iterates to find the square root, and the second method uses the math.sqrt() function. 
Finally, it prints the square root of the number. 
"""


import math

num = 169
sqr = 0

# Find the square root of the number through iteration
while sqr * sqr < num:
    sqr += 1

# Check if the square of the found value is equal to the given number
if sqr * sqr == num:
    print("Square root of", num, "is", sqr)
else:
    print("Square root doesn't exist")

# Alternatively, use the math.sqrt() function to find the square root
sqrt = math.sqrt(num)
print(sqrt)
