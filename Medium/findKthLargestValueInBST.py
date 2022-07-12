# Author : Ondřej Maceška 
# Date : 12.7.2022
# Task : https://www.algoexpert.io/questions/find-kth-largest-value-in-bst

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# -------------------- Variant 1 -------------------------
# O(n) time, O(1) space where n is the length of the array
def find_kth_largest_value_in_bst(tree, k) -> int:
    """ Finds the k-th largest in the given Binary Search Tree
        (Performs an in order traverse to find it) 
    Args:
        tree (BST) : a given tree
        k (int) : a given "index"

    Returns:
        int : the k-th largest value
    """
    return in_order_traverse(tree, [])[-k]

def in_order_traverse(tree, array):  
    """ Fills the given array with values from the given tree in order of traverse
        
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

# -------------------- Variant 2 ---------------------------
# O(h + k) time, O(1) space where h is the height of the bst
def find_kth_largest_value_in_bst_faster(tree, k) -> int:
    """ Finds the k-th largest in the given Binary Search Tree
        (Performs an in reverse order traverse to find it) 
        
    Args:
        tree (BST) : a given tree
        k (int) : a given "index"

    Returns:
        int : the k-th largest value
    """
    return in_reverse_order_traverse(tree, [], k)[k - 1]

def in_reverse_order_traverse(tree, array, k):        
    """ Fills the given array with values from the given tree in reverse order of traverse
        (Up the the k-th number )
    Args:
        tree (BST) : a given BST node
        array (int) : the array to fill

    Returns:
        int[] : filled array
    """  
    if(tree.right):
        array = in_reverse_order_traverse(tree.right, array, k)
        
    array.append(tree.value)
    if(len(array) == k):
        return array 
    
    if(tree.left):
        array = in_reverse_order_traverse(tree.left, array, k)    
    
    return array