# Author : Ondřej Maceška 
# Date : 25.6.2022
# Task : https://www.algoexpert.io/questions/insertion-sort


# O(n^2) time, O(1) space (only the space given)
def insertion_sort(array):
    """ Gets an array and sorts it with insertion sort algorithm.
    Args:
        array (int[ ]) : given array

    Returns:
        int[ ] : sorted array
    """
    for i in range(1, len(array)):
        while(i > 0 and array[i] < array[i - 1]):
            swap(i, i - 1, array)
            i -= 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]