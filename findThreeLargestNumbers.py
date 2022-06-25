# Author : Ondřej Maceška 
# Date : 25.6.2022
# Task : https://www.algoexpert.io/questions/find-three-largest-numbers

# O(n) time, O(1) space (only the space given)
def find_three_largest_numbers_alt(array):
    max_three = []
    for _ in range(3):
        largest = max(array)
        max_three.append(largest)
        array.remove(largest)
    return sorted(max_three)
