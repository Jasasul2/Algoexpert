# Author : Ondřej Maceška 
# Date : 2.7.2022
# Task : https://www.algoexpert.io/questions/smallest-difference

# O(n * log(n) + m * log(m)) time, O(1) space, 
# where n is the length of the first array and m is the length of the second array
def smallest_difference(array_one, array_two):
    """ Finds the smallest difference between 
        one int from array_one and one int from array_two
    Args:
        array_one (int[ ]) : given array 1
        array_two (int[ ]) : given array 2

    Returns:
        int[] : two values, on from each array, having the smallest difference
    """
    array_one.sort()
    array_two.sort()
    i, j = 0, 0
    min1, min2 = array_one[0], array_two[0]
    smallest_diff = abs(min1 - min2)
    while(i < len(array_one) and j < len(array_two)):
        num1 = array_one[i]
        num2 = array_two[j]
        diff = abs(num1 - num2)
        if(diff < smallest_diff):
            smallest_diff = diff
            min1 = num1
            min2 = num2
            if(diff == 0):
                break 
        if(num1 < num2):
            i += 1 
        else:
            j += 1
    return [min1, min2]
            
    