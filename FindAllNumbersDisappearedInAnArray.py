""" 
This code snippet implements an algorithm to find all the missing numbers in an array. 
It marks elements as negative based on their value as indices, and then retrieves the 
indices of the remaining positive elements, adding 1 to each index to get the missing numbers. 
Finally, it prints the result.
"""


arr = [4, 3, 2, 7, 8, 2, 3, 1]

# Mark elements as negative based on their value as indices
for num in arr:
    index = abs(num) - 1
    if arr[index] > 0:
        arr[index] *= -1

# Retrieve the indices of positive elements
result = []
for index, num in enumerate(arr):
    if num > 0:
        result.append(index + 1)

print(result)
