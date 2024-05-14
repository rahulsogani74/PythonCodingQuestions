"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

This code prints a pattern where each row contains numbers from 1 to the row number. 
Adjust the value of n to change the number of rows in the pattern.
"""

def print_pattern(n):
    # Loop through each row
    for i in range(1, n + 1):
        # Loop through each column in the row
        for j in range(1, i + 1):
            # Print the number followed by a space
            print(j, end=" ")
        # Move to the next line after printing each row
        print()

# Call the function with n = 5 to print the pattern
print_pattern(5)
