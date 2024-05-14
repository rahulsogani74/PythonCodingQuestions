""" 
This code snippet removes duplicates from the list my_list by converting it to a set 
(which automatically removes duplicates) and then back to a list. Finally, it prints the resulting unique list.
"""

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Convert the list to a set to remove duplicates, then convert it back to a list
unique_list = list(set(my_list))
print(unique_list)
