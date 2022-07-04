# Author : Ondřej Maceška 
# Date : 2.7.2022
# Task : https://www.algoexpert.io/questions/smallest-difference

# O(n * log(n) + m * log(m)) time, O(1) space, 
# where n is the length of the first array and m is the length of the second array
def smallest_difference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    i, j = 0, 0
    min1, min2 = arrayOne[0], arrayTwo[0]
    smallest_diff = abs(min1 - min2)
    while(i < len(arrayOne) and j < len(arrayTwo)):
        num1 = arrayOne[i]
        num2 = arrayTwo[j]
        diff = abs(num1 - num2)
        if(diff < smallest_diff):
            smallest_diff = diff
            min1 = num1
            min2 = num2
            if(diff == 0):
                break 
        if(num1 < num2):
            i += 1 
        else:
            j += 1
    return [min1, min2]
            
    