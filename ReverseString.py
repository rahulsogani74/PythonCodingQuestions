""" 
This code snippet reverses the characters in the list my_str by swapping the characters at each 
index with their corresponding character from the end of the list until reaching the center. 
Finally, it prints the reversed list.
"""


my_str = ["h", "e", "l", "l", "o"]

# Initialize the index of the last character
end_index = len(my_str) - 1

# Loop through half of the list
for index, s in enumerate(my_str):
    # Swap characters at the current index with their corresponding character from the end of the list
    if index < end_index:
        my_str[index], my_str[end_index] = my_str[end_index], my_str[index]
        # Move towards the center of the list
        end_index -= 1

print(my_str)
