# Author : Ondřej Maceška 
# Date : 4.6.2022

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sum(root, sum_so_far, sum_list):
    sum_so_far += root.value
    if(root.left):
        branch_sum(root.left, sum_so_far, sum_list)
    if(root.right):
        branch_sum(root.right, sum_so_far, sum_list)
    if(not root.left and not root.right):
        sum_list.append(sum_so_far)
    

# O(n) time, O(n) space where n is the number of nodes in the binary tree 
def branchSums(root):
    """ returns a list of sum of all branches in the binary tree
        
    Args:
        root (BinaryTree) : given tree

    Returns:
        int[ ] : sums of all branches in the binary tree
    """
    sum_list = []
    branch_sum(root, 0, sum_list)
    return sum_list