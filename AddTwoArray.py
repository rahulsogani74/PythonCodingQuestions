""" 
This code snippet creates a new list arr3 by summing corresponding elements of arr1 and arr2 
using a while loop. It iterates over both arrays simultaneously and adds the elements at the 
same index position. Finally, it prints the resulting arr3.
"""

arr1 = [51, 16, 33, 2, 14, 21]
arr2 = [33, 9, 56, 21, 39, 21]
arr3 = []

# Using a while loop to iterate over both arrays simultaneously and sum corresponding elements
x = len(arr1)
i = 0

while x > i:
    arr3.append(arr1[i] + arr2[i])
    i += 1

print(arr3)
