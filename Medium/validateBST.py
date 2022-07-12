# Author : Ondřej Maceška 
# Date : 11.7.2022
# Task : https://www.algoexpert.io/questions/validate-bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
# O(n) time, O(d) space, where n is the number of nodes and d is the depth of the tree
def validate_bst(tree, max = None, min = None):
    """ validates if a given tree is a correct BST tree
        
    Args:
        tree (BST) : a given BST node
        max (int) : maximum value this node can have
        min (int) : minimum value this node can have

    Returns:
        bool : whether a given tree is a correct BST tree 
    """
    print(tree.value)
    check = True 
    if(min and tree.value < min or max and tree.value >= max):
        return False 
    
    if(tree.left):
        check = False if tree.left.value >= tree.value else validate_bst(tree.left, max = tree.value, min = min)
        if(not check):
            return False 
        
    if(tree.right):
        check = False if tree.right.value < tree.value else validate_bst(tree.right, max = max, min = tree.value)
        
    return check 
