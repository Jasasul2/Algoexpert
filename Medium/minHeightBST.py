# Author : Ondřej Maceška 
# Date : 12.7.2022
# Task : https://www.algoexpert.io/questions/min-height-bst


# O(n) time, O(n) space where n is the length of the array
def min_heght_bst(array, previous_node = None):
    """ Constructs a Binary Search Tree with minimum depth from the given array
        (Recursive)
        
    Args:
        array (int[]) : a given array 
        previous_node (BST) : a previous_node of BST 

    Returns:
        BST : the root of the tree
    """
    middle_index = len(array) // 2
    middle_value = array[middle_index]
    root = None
    if(not previous_node):
        previous_node = BST(middle_value)
        root = previous_node
    else:
        previous_node = previous_node.insert(middle_value)
    
    left_array = array[:middle_index]
    if(left_array):
        min_heght_bst(left_array, previous_node)

    right_array = array[middle_index + 1:]
    if(right_array):
        min_heght_bst(right_array, previous_node)

    return root
    
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
                return self.left
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
                return self.right
            else:
                self.right.insert(value)
