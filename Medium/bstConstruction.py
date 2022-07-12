# Author : Ondřej Maceška 
# Date : 11.7.2022
# Task : https://www.algoexpert.io/questions/bst-construction


# Binary Search Tree
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1


    # O(n * log(n)) time, O(1) space
    def insert(self, value):
        """ Inserts a new node with a given value to the binary tree
        
        Args:
            value (int) : a given value to insert

        Returns:
            BST : self 
        """
        self.count += 1 
        node = self 
        while(node.value):
            if(value < node.value):
                if(not node.left):
                    node.left = BST(None)
                node = node.left
            else:
                if(not node.right):
                    node.right = BST(None)
                node = node.right
        node.value = value

        return self


    # O(n * log(n)) time, O(1) space
    def contains(self, value):
        """ Returns a bool whether a given value is contained in the binary tree
        
        Args:
            value (int) : a given value to find

        Returns:
            bool : True if the value is found  
        """
        node = self
        while(node):
            if(value == node.value):
                return True 
            elif(value < node.value):
                node = node.left
            else:
                node = node.right 
        return False
            


    # O(n * log(n)) time, O(1) space
    def remove(self, value, parent_node = None):
        """ Removes a node with a given value from the binary tree
        
        Args:
            value (int) : a given value to find and remove 
            parent_node : the parent node of the tree 

        Returns:
            BST : self 
        """
        current_node = self 
        while current_node:
            # Searching --------------
            if(value < current_node.value):
                parent_node = current_node
                current_node = current_node.left 
            elif(value > current_node.value):
                parent_node = current_node
                current_node = current_node.right
            else:
                # Replacing ---------- 
                # Middle 
                if(current_node.left and current_node.right):
                     current_node.value = current_node.right.get_min_value()
                     current_node.right.remove(current_node.value, current_node)
                # Root 
                elif parent_node is None:
                    if(current_node.left):
                        current_node.value = current_node.left.value 
                        current_node.right = current_node.left.right 
                        current_node.left = current_node.left.left 
                    elif(current_node.right):
                        current_node.value = current_node.right.value 
                        current_node.right = current_node.right.right 
                        current_node.left = current_node.right.left 
                    else:
                        return self 
                # Single
                elif (parent_node.left == current_node):
                    parent_node.left = current_node.left if current_node.left else current_node.right 
                # Single
                elif (parent_node.right == current_node):
                    parent_node.right = current_node.left if current_node.left else current_node.right
                break
                
        return self

    def get_min_value(self):
        current_node = self
        while(current_node.left):
            current_node = current_node.left
        return current_node.value 
