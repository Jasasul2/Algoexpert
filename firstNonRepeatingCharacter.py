# Author : Ondřej Maceška 
# Date : 27.6.2022
# Task : https://www.algoexpert.io/questions/first-non-repeating-character


# O(n) time, O(1) space
def firstNonRepeatingCharacter(string:str) -> int:
    """ Returns the index of the first non-repeating character in the string
        
    Args:
        string (str) : the given string
    Returns:
        int : the index of the first non-repeating character in the string
    """
    counter = {}
    for char in string[::-1]:
        counter[char] = counter.get(char, 0) + 1

    for key in list(counter.keys())[::-1]:
        if(counter[key] == 1):
            return string.index(key)
    return -1
