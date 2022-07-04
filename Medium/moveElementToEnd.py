# Author : Ondřej Maceška 
# Date : 2.7.2022
# Task : https://www.algoexpert.io/questions/move-element-to-end

# O(n) time, O(1) space
def move_element_to_end(array, target):
    """ moves all elements equal to target
    Args:
        array (int[ ]) : given array 
        target (int) : given target

    Returns:
        int[] : the original modified array
    """
    left_index = 0
    right_index = len(array) - 1
    while(left_index < right_index):
        if(array[left_index] == target):
            while(array[right_index] == target and right_index > left_index):
                right_index -= 1
            swap(array, left_index, right_index)
        left_index += 1
    
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    