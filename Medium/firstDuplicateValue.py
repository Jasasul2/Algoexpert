# Author : Ondřej Maceška 
# Date : 11.7.2022
# Task : https://www.algoexpert.io/questions/first-duplicate-value

# O(n) time, O(n) space
def first_duplicate_value(array):
    """ Gets an array of integers from 1 to n where n is the length of the array
        Returns the first duplicate value
    Args:
        array (int[]) : given array 

    Returns:
        int : the first duplicate value
    """
    seen = set()   
    for num in array:
        if(num in seen):
            return num 
        seen.add(num)
    return -1


# O(n) time, O(1) space
def first_duplicate_value_algoexpert(array):
    """ Gets an array of integers from 1 to n where n is the length of the array
        Returns the first duplicate value
    Args:
        array (int[]) : given array 

    Returns:
        int : the first duplicate value
    """
    print(array)
    for num in array:
        abs_num = abs(num)
        if(array[abs_num- 1] < 0):
            return abs_num
        array[abs_num - 1] *= -1
    return -1
