# Author : Ondřej Maceška 
# Date : 22.6.2022
# Task : https://www.algoexpert.io/questions/tandem-bicycle

# O(n logn) time, O(1) space (only the space given)
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    """ Finds the biggest or smallest tandem speed 
        tandem_speed(a, b) = max(a, b)
        
    Args:
        redShirtSpeeds (int[ ]) : given array 1
        blueShirtSpeeds (int[ ]) : given array 2
        fastest (boolean) : what type of speed to find

    Returns:
        boolean either the biggest or smallest tandem speed
    """
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)
    return sum([max(s1, s2) for s1, s2 in zip(redShirtSpeeds, blueShirtSpeeds)])
