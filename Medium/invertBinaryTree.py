# Author : Ondřej Maceška 
# Date : 29.7.2022
# Task : https://www.algoexpert.io/questions/invert-binary-tree

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time, O(d) space, where d is the depth of the tree
def invert_binary_tree(tree):
    """ Inverts a binary tree (right children become left children and vice versa).
        
    Args:
        tree (BinaryTree) : a given binary tree
        
    Returns:
        None
    """
    if(tree and (tree.left or tree.right)):
        tree.left, tree.right = tree.right, tree.left
        invert_binary_tree(tree.left)
        invert_binary_tree(tree.right)

