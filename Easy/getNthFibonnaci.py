# Author : Ondřej Maceška 
# Date : 22.6.2022
# Task : https://www.algoexpert.io/questions/nth-fibonacci

# O(n) time, O(1) space (only the space given)
def getNthFib(n):
    """ Gets the nth number in fibonacci sequence
        
    Args:
        n (int) : index of the number we're looking for

    Returns:
        int : the number in the fibonacci sequence with index n - 1
    """
    a, b = 0, 1
    for _ in range(n - 1):
        prev_b = b 
        b = a + b
        a = prev_b
    return a