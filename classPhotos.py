# Author : Ondřej Maceška 
# Date : 22.6.2022
# Task : https://www.algoexpert.io/questions/class-photos


# O(n logn) time, O(1) space (only the space given)
def classPhotos(redShirtHeights, blueShirtHeights):
    """ viz. the task
        
    Args:
        redShirtHeights (int[ ]) : given array 1
        blueShirtHeights (int[ ]) : given array 2

    Returns:
        boolean : if the arrays meet the criteria
    """
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    higher = blueShirtHeights if blueShirtHeights[0] > redShirtHeights[0] else redShirtHeights    
    lower = blueShirtHeights if higher == redShirtHeights else redShirtHeights 
    for high, low in zip(higher, lower):
        if(high <= low):
            return False
    return True
