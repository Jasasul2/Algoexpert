# Author : Ondřej Maceška 
# Date : 4.6.2022
# Task : https://www.algoexpert.io/questions/find-closest-value-in-bst


# Solution 1 ---------------------------------
# O(logn) time, O(logn) space
def find_closest_value_rec(tree, target, closest):
    if(abs(tree.value - target) < abs(closest - target)):
        closest = tree.value

    if(tree.left and target < tree.value):
        return find_closest_value_rec(tree.left, target, closest)
    elif(tree.right and target > tree.value):
        return find_closest_value_rec(tree.right, target, closest)
    return closest


# Solution 2 ---------------------------------
# O(logn) time, O(1) space
def find_closest_value_it(tree, target):
    closest = tree.value 
    current_node = tree

    while current_node is not None: 
        if(abs(current_node.value - target) < abs(closest - target)):
            closest = current_node.value
        if(target < current_node.value):
            current_node = current_node.left
        elif (target > current_node.value):
            current_node = current_node.right
        else:
            break
        
    return closest 


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
