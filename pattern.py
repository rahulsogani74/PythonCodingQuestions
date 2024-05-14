"""
*
* *
* * *
* * * *
* * * * *

This code will print a pattern of stars resembling a triangle with increasing number of 
stars in each row. Adjust the num_rows variable to change the height of the triangle.
"""

# Define the number of rows
num_rows = 5

# Loop through each row
for row in range(1, num_rows + 1):
    # Print '*' for each column in the row
    for col in range(1, row + 1):
        print("*", end=" ")
    # Move to the next line after printing each row
    print()
