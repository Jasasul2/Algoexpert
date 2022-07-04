# Author : Ondřej Maceška 
# Date : 2.7.2022
# Task : https://www.algoexpert.io/questions/monotonic-array


# O(n) time, O(1) space
def is_monotonic(array):
    """ check if the array is monotonic 
    Args:
        array (int[]) : given array 

    Returns:
        bool : whether the array is monotonic or not 
    """
    if(len(array) <= 1):
        return True
    
    increasing = True
    j = 0
    while(array[j + 1] == array[j] and j < len(array) - 2):
        j += 1
    if(array[j + 1] < array[j]):
        increasing = False
        
    for i in range(j + 1, len(array) - 1):
        if(array[i + 1] > array[i] and not increasing):
            return False
        elif(array[i + 1] < array[i] and increasing):
            return False
           
    return True
