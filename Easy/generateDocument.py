# Author : Ondřej Maceška 
# Date : 27.6.2022
# Task : https://www.algoexpert.io/questions/generate-document


# O(n + m) time, O(c) space, wehere n is the num of chars, 
# m is the length of the document and c is a num of unique chars 
def generate_document(characters:str, document:str) -> bool:
    """ Returns True if the document can be constructed from the characters
        
    Args:
        characters (str) : the available characters
        document (str) : the given document
    Returns:
        bool : whether or not the document can be constructed from the characters
    """
    if(len(document) == 0): return True

    counter = {}
    for char in characters:
        counter[char] = counter.get(char, 0) + 1

    for char in document:
        if(char in counter and counter[char] > 0):
            counter[char] -= 1
        else:
            return False
    return True
