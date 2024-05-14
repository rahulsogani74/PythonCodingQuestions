""" 
This code calculates the sum of all elements in the list my_list using a loop and then prints the total sum.
"""

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

total_sum = 0
for num in my_list:
    total_sum += num
    
print("Sum of the elements in the list:", total_sum)
