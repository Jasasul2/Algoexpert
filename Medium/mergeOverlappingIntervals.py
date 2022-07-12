# Author : Ondřej Maceška 
# Date : 11.7.2022
# Task : https://www.algoexpert.io/questions/merge-overlapping-intervals

# O(n * log(n)) time, O(n) space
def merge_overlapping_intervals(intervals):
    """ Gets an array of intervals (each is represented as an array of two integers)
        Merges all intervals which overlap and returns them in an array
        
    Args:
        array (int[int[]]) : given array of intervals

    Returns:
        int[int[] : the array of merged intervals
    """
    intervals.sort(key=lambda x : x[0])
    merged_intervals = []
    this_interval = intervals[0]
    
    for next_interval in intervals:
        if(next_interval[0] > this_interval[1]):
            merged_intervals.append(this_interval)
            this_interval = next_interval
        else:
            this_interval = [min(this_interval[0], next_interval[0]), 
                             max(this_interval[1], next_interval[1])]
            
    merged_intervals.append(this_interval)
            
    return merged_intervals
