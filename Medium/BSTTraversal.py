# Author : Ondřej Maceška 
# Date : 12.7.2022
# Task : https://www.algoexpert.io/questions/bst-traversal

# Description :
# Three methods to traverse a binary tree and return an array of its values

# O(n) time, O(n) space
def in_order_traverse(tree, array):    
    """ fills the given array with values from the given tree in order of traverse
        
    Args:
        tree (BST) : a given BST node
        array (int) : the array to fill

    Returns:
        int[] : filled array
    """
    if(tree.left):
        array = in_order_traverse(tree.left, array)    
    
    array.append(tree.value)
        
    if(tree.right):
        array = in_order_traverse(tree.right, array)

    return array


# O(n) time, O(n) space
def pre_order_traverse(tree, array):
    """ fills the given array with values from the given tree in the pre order of traverse
        
    Args:
        tree (BST) : a given BST node
        array (int) : the array to fill

    Returns:
        int[] : filled array
    """
    array.append(tree.value)
    
    if(tree.left):
        array = pre_order_traverse(tree.left, array)    
    
    if(tree.right):
        array = pre_order_traverse(tree.right, array)

    
    return array


# O(n) time, O(n) space
def post_order_traverse(tree, array):
    """ fills the given array with values from the given tree in the post order of traverse
        
    Args:
        tree (BST) : a given BST node
        array (int) : the array to fill

    Returns:
        int[] : filled array
    """
    if(tree.left):
        array = post_order_traverse(tree.left, array)    
    
    if(tree.right):
        array = post_order_traverse(tree.right, array)

    array.append(tree.value)
    
    return array
