# Author : Ondřej Maceška 
# Date : 22.6.2022
# Task : https://www.algoexpert.io/questions/remove-duplicates-from-linked-list


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time, O(1) space (only the space given)
def removeDuplicatesFromLinkedList(linkedList):
    """ Removes all duplicates from given sorted linkedList
        
    Args:
        linkedList (LinkedList) : head of the given LinkedList 

    Returns:
        LinkedList : given linkedList where no values of nodes repeat
    """
    node = linkedList
    while(node.next):
        if(node.value == node.next.value):
            node.next = node.next.next
        else:
            node = node.next
    return linkedList
