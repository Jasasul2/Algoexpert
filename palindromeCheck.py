# Author : Ondřej Maceška 
# Date : 25.6.2022
# Task : https://www.algoexpert.io/questions/palindrome-check


# O(n) time, O(1) space (only the space given), much faster
def is_palindrome_v1(string) -> bool:
    """ Checks whether a string is a palindrome using slicing 
        
    Args:
        string (string) : input string 

    Returns:
        bool : whether the given string is a palindrome
    """
    return string == string[::-1]

# O(n) time, O(1) space (only the space given)
def is_palindrome_v2(string) -> bool:
    """ Checks whether a string is a palindrome using two pointer indexes 
        
    Args:
        string (string) : input string 

    Returns:
        bool : whether the given string is a palindrome
    """
    for i in range(len(string)//2):
        if(string[i] != string[len(string) - i - 1]):
            return False
    return True