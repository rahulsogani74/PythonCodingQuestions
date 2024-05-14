"""
1 
2  3
4  5  6
7  8  9  10
11 12 13 14  15

This code prints a pattern where each row contains consecutive numbers starting from 1 and 
incrementing by 1 in each row. Adjust the value of n to change the number of rows in the pattern.
"""

def print_pattern(n):
    num = 1  # Initialize the starting number
    # Loop through each row
    for i in range(1, n + 1):
        # Loop through each column in the row
        for j in range(1, i + 1):
            # Print the current number and increment it
            print(num, end=" ")
            num += 1
        # Move to the next line after printing each row
        print()

# Call the function with n = 5 to print the pattern
print_pattern(5)
