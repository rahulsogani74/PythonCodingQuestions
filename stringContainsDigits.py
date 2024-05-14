""" 
This function contains_only_digits checks if a given string contains only digits. 
It returns True if all characters in the string are digits, and False otherwise. 
The provided example demonstrates its usage.
"""


def contains_only_digits(string):
    """
    Check if a string contains only digits.

    Parameters:
        string (str): The string to check.

    Returns:
        bool: True if the string contains only digits, False otherwise.
    """
    return string.isdigit()

string = "123ss45"
if contains_only_digits(string):
    print("String contains only digits")
else:
    print("String does not contain only digits")
