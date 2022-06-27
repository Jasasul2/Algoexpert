# Author : Ondřej Maceška 
# Date : 25.6.2022
# Task : https://www.algoexpert.io/questions/palindrome-check


# O(n) time, O(1) space (only the space given), much faster
def is_palindrome_v1(sequence) -> bool:
    """ Checks whether a sequence is a palindrome using slicing 
        
    Args:
        sequence ([]) : input sequence 

    Returns:
        bool : whether the given sequence is a palindrome
    """
    return sequence == sequence[::-1]

# O(n) time, O(1) space (only the space given)
def is_palindrome_v2(sequence) -> bool:
    """ Checks whether a sequence is a palindrome using two pointer indexes 
        
    Args:
        sequence ([]) : input sequence 

    Returns:
        bool : whether the given sequence is a palindrome
    """
    for i in range(len(sequence)//2):
        if(sequence[i] != sequence[len(sequence) - i - 1]):
            return False
    return True