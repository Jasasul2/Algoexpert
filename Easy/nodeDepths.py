# Author : Ondřej Maceška 
# Date : 9.6.2022
# Task : https://www.algoexpert.io/questions/node-depths


# O(n) time, O(h) space where n is the number of nodes in the binary tree and h is the height of the three
# Solution 1 - iterative, using stack 
def nodeDepths(root):
    currentDepth = 0
    currentDepthSum = 0

    toVisit = [(root, currentDepth)]
    while(len(toVisit) > 0):
        tuple = toVisit.pop(0)
        node = tuple[0]
        currentDepth = tuple[1]
        currentDepthSum += currentDepth
        if(node.left):
            toVisit.append((node.left, currentDepth + 1))
        if(node.right):
            toVisit.append((node.right, currentDepth + 1))
        
    return currentDepthSum

# O(n) time, O(h) space where n is the number of nodes in the binary tree and h is the height of the three
# Solution 2 - recursive, very smooth
def nodeDepths(root, depth = 0):
    if(root == None):
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.searched = False
        self.value = value
        self.left = None
        self.right = None
