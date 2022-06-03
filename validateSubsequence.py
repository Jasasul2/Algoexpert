# Author : Ondřej Maceška 
# Date : 3.6.2022

# O(n) time, O(1) space 
def isValidSubsequence(array, sequence):
    # Cannot be a subsequence if its longer 
    if(len(sequence) > len(array)):
        return False 
        
    array_index = 0
    sequence_index = 0
    while(array_index < len(array)):
        num1 = array[array_index]
        num2 = sequence[sequence_index]
        if(num1 == num2):
            if(sequence_index == len(sequence) - 1):
                return True
            sequence_index += 1
        array_index += 1
    return False
