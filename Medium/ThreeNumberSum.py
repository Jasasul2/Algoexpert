# Author : Ondřej Maceška 
# Date : 2.7.2022
# Task : https://www.algoexpert.io/questions/three-number-sum

# O(n^2) time, O(n) space where 
def threeNumberSum(array, target_sum):
    """ Finds all triplets in a given array which sum up to a given sum 
        
    Args:
        array (int[]) : the given array
        target_sum(int) : the given sum 

    Returns:
        int[]: list containing all triplets which sum up to a given sum
    """
    triplets = []
    array.sort()

    for i in range(len(array) - 2):
        left_index = i + 1
        right_index = len(array) - 1
        num = array[i] 
        while(left_index < right_index):
            num2 = array[left_index]
            num3 = array[right_index]
            test_sum = num + num2 + num3
            if(test_sum == target_sum):
                triplets.append([num, num2, num3])
                right_index -= 1
            elif(test_sum < target_sum):
                left_index += 1
            else:
                right_index -= 1
    # Write your code here.
    return triplets

