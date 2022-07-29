# Author : Ondřej Maceška 
# Date : 28.7.2022
# Task : https://www.algoexpert.io/questions/reconstruct-bst

# Description :
# Gets an array repersenting a pre order traverse of bst, reconstructs the bst from it 
# Recursive

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n ^ 2) time, O(n) space
def reconstruct_bst(preOrderTraversalValues, root = None):
    """ Fills the given binary search tree with values from the given array representing a pre order of traverse
        
    Args:
        preOrderTraversalValues (int[]) : a given array representing a pre order of traverse
        array (BST) : the bst root 

    Returns:
        BST : root of the bst 
    """
    if(len(preOrderTraversalValues) >= 1):
        value = preOrderTraversalValues[0]
        if(not root):
            root = BST(value)
            root.value = value
        else:
            if(value < root.value):
                root.left = BST(value)
                root = root.left
            else:
                root.right = BST(value)
                root = root.right
                
        i = 1
        while(i < len(preOrderTraversalValues)):
            if(preOrderTraversalValues[i] >= value):
                reconstruct_bst(preOrderTraversalValues[i:], root)
                break 
            i += 1
        reconstruct_bst(preOrderTraversalValues[1:i], root)
        
    return root
