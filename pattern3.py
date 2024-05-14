"""
    *
   * *
  * * *
 * * * *
* * * * *

This code will print a pattern of stars resembling a triangle with each row having 
one more star than the previous row. Adjust the value of n to change the size of the triangle.
"""

def print_triangle(n):
    # Loop through each row
    for i in range(n):
        # Print spaces for alignment
        for j in range(n - i - 1):
            print(" ", end="")
        # Print stars for the current row
        for k in range(i + 1):
            print("*", end=" ")
        # Move to the next line after printing each row
        print()

# Call the function with n = 5 to print the triangle
print_triangle(5)
