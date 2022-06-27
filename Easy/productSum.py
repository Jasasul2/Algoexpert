# Author : Ondřej Maceška 
# Date : 22.6.2022
# Task : https://www.algoexpert.io/questions/product-sum


# O(n) time, O(d) space, where d is the maximum depth of a special array
def productSum(array, depth = 1):
    """ Returns the product sum of an array with special arrays
        Recursive function
        
    Args:
        array (int) : array to make a product sum of 

    Returns:
        int : product sum 
    """
    sum = 0
    for n in array:
        if(isinstance(n, int)):
            sum += n 
        else:
            sum += productSum(n, depth + 1)
    return sum * depth 
