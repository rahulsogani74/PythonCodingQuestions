""" 
These two code blocks achieve the same result: finding pairs of elements in the arrs list whose 
sum equals the target value b. The first block uses nested loops to iterate over all possible pairs, 
while the second block uses a dictionary to store seen values and their indices, allowing for a more 
efficient solution.
"""



arrs = [1, 2, 3, 4, 5]
b = 7

# Using nested loops
for i in range(len(arrs)):
    for j in range(i + 1, len(arrs)):
        if arrs[i] + arrs[j] == b:
            print(f"Index {i}, Value {arrs[i]} and Index {j}, Value {arrs[j]}")

# Using a dictionary to store seen values
arrs = [1, 2, 3, 4, 5]
b = 7
seen = {}

for index, num in enumerate(arrs):
    complement = b - num
    if complement in seen:
        print(f"Index {seen[complement]}, Value {arrs[seen[complement]]} and Index {index}, Value {num}")
    seen[num] = index
