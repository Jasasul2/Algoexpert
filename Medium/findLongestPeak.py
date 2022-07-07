# Author : Ondřej Maceška 
# Date : 7.7.2022
# Task : https://www.algoexpert.io/questions/longest-peak


# O(n) time, O(1) space
def longest_peak(array) -> int:
    """ Finds the longest peak in the given array by analysing the current monotonic trend
        Faster in most cases 
    Args:
        array (int[]) : given array 

    Returns:
        tuple(int[], int) : the longest peak and index of its last item
    """
    increasing = False
    decreasing = False
    max_peak_length = 0
    peak_length = 1
    reached_tip = False
    peak_end = 0
    for i in range(len(array) - 1):
        this = array[i]
        next = array[i + 1]
        
        if(next > this):
            if(decreasing):
                if(peak_length > max_peak_length):
                    max_peak_length = peak_length
                    peak_end = i + 1
                peak_length = 1
            increasing = True
            decreasing = False
            reached_tip = False
            peak_length += 1

        elif(next == this):
            if(decreasing and peak_length > max_peak_length):
                max_peak_length = peak_length
                peak_end = i + 1
            increasing = False
            decreasing = False
            reached_tip = False
            peak_length = 1
             
        else:
            if(increasing):
                reached_tip = True
                peak_length += 1
            if(decreasing and reached_tip):
                peak_length += 1
            increasing = False
            decreasing = True 
            if(i == len(array) - 2 and peak_length > max_peak_length):
                max_peak_length = peak_length
                peak_end = i + 1

    return(array[peak_end - max_peak_length:peak_end], peak_end)

def longest_peak_algoexpert(array) -> int:
    """ Finds the longest peak in the given array by finding the tips of the peaks
        A bit slower in most cases 
    Args:
        array (int[]) : given array 

    Returns:
        tuple(int[], int) : the longest peak and index of its last item
    """
    longest_peak_length = 0
    i = 1
    peak_end = 0
    while i < len(array) - 1:
        is_peak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not is_peak:
            i += 1
            continue
        
        left_index = i - 2
        while left_index >= 0 and array[left_index] < array[left_index + 1]: 
            left_index -= 1
        
        right_index = i + 2
        while right_index < len(array) and array[right_index] < array[right_index - 1]: 
            right_index += 1
            
        current_peak_length = right_index - left_index - 1
        if(current_peak_length > longest_peak_length):
            peak_end = right_index
        longest_peak_length = max(current_peak_length, longest_peak_length)
        i = right_index
    
    
    return(array[peak_end - longest_peak_length:peak_end], peak_end)