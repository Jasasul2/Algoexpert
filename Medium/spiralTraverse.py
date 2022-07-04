# Author : Ondřej Maceška 
# Date : 3.7.2022
# Task : https://www.algoexpert.io/questions/spiral-traverse


# O(n) time, O(n) space, where n is the length of the array
def spiral_traverse(array):
    """ Traverses an array in a spiral way, adding its elements to a new array
    Args:
        array ([]) : given array 

    Returns:
        [] : new array
    """
    new_array = []
    r = len(array[0]) - 1      # Border
    d = len(array) - 1         # Border
    l = 0                      # Border
    u = 1                      # Border 
    i = 0                      # Y Iterator
    j = 0                      # X Iterator
    moving = "R" # also D, L, U stands for right, down, left and up 
    while(len(new_array) != len(array) * len(array[0])):
        num = array[i][j]
        print(num)
        new_array.append(num)
        if(moving == "R"):
            if(j < r):
                j += 1
            else:
                moving = "D"
                i += 1
                r -= 1
        elif(moving == "D"):
            if(i < d):
                i += 1
            else:
                moving = "L"
                j -= 1
                d -= 1
        elif(moving == "L"):
            if(j > l):
                j -= 1
            else:
                moving = "U"
                i -= 1
                l += 1
        elif(moving == "U"):
            if(i > u):
                i -= 1
            else:
                moving = "R"
                j += 1
                u += 1
                
    return new_array
