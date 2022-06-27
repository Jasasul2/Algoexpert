# Author : Ondřej Maceška 
# Date : 3.6.2022
# Task : https://www.algoexpert.io/questions/two-number-sum


# O(n) time, O(n) space 
def two_number_sum(array, target_sum):
    """ returns the first pair of numbers from 
    the given array which add up to the target sum
        
    Args:
        array (int[ ]) : given array
        target_sum (int) : target sum 

    Returns:
        int[ ] : the first two ints that add up to the target_sum
    """
    dictionary = {}
    for num in array: 
        needed_match = target_sum - num  
        if needed_match in dictionary:
            return [needed_match, num]
        else:
            # True signifies that the number has been explored 
            dictionary[num] = True
    return []
