# Author : Ondřej Maceška 
# Date : 4.6.2022
# Task : https://www.algoexpert.io/questions/branch-sums


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sum(node, sum_so_far, sum_list):
    sum_so_far += node.value
    if(node.left):
        branch_sum(node.left, sum_so_far, sum_list)
    if(node.right):
        branch_sum(node.right, sum_so_far, sum_list)
    if(not node.left and not node.right):
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