# Author : Ondřej Maceška 
# Date : 8.7.2022
# Task : https://www.algoexpert.io/questions/array-of-products

# O(n ^ 2) time, O(n) space
def array_of_products(array):
    """  Returns an array of products of each other value in the given array than the one on the index
    
    Args:
        array (int[]) : given array 

    Returns:
        int[] : product array
    """
    products = [1] * len(array)

    for i, num in enumerate(array):
        for j in range(len(products)):
            if(i != j):
                products[j] *= num
    return products 


# O(n) time, O(n) space
def array_of_products_faster(array):
    """  Returns an array of products of each other value in the given array than the one on the index
    
    Args:
        array (int[]) : given array 

    Returns:
        int[] : product array
    """
    products = [1 for _ in range(len(array))]

    left_running_product = 1
    for i in range(len(array)):
        products[i] = left_running_product
        left_running_product *= array[i]

    right_running_product = 1
    for i in reversed(range(len(array))):
        products[i] *= right_running_product
        right_running_product *= array[i]
    
    return products 
