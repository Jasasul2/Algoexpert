# Author : Ondřej Maceška 
# Date : 27.6.2022
# Task : https://www.algoexpert.io/questions/insertion-sort


# O(n) time, O(n) space
def run_length_encoding(string) -> str:
    """ Viz. the task 
        
    Args:
        string (str) : the given string

    Returns:
        string : the encoded string
    """
    encoded_string = ""
    current_count = 1
    current_char = string[0]
    for i in range(1, len(string)):
        current_char = string[i]
        previous_char = string[i - 1]
        if(current_char != previous_char or current_count == 9):
            encoded_string += str(current_count)
            encoded_string += previous_char
            current_count = 0
        current_count += 1
        
    encoded_string += str(current_count)
    encoded_string += current_char
    return encoded_string 
