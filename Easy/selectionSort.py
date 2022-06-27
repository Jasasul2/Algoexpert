# Author : Ondřej Maceška 
# Date : 25.6.2022
# Task : https://www.algoexpert.io/questions/selection-sort


# O(n^2) time, O(1) space (only the space given)
def selectionSort(array):
    """ Gets an array and sorts it with the selection sort algorithm.
    Args:
        array (int[ ]) : given array

    Returns:
        int[ ] : sorted array
    """
    for i in range(1, len(array)):
        max = array[0]
        max_index = 0
        for j in range(len(array) - i):
            if(array[j] > max):
                max = array[j]
                max_index = j 
        if(max > array[-i]):
            swap(max_index, -i, array)
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    print(array)