# Author : Ondřej Maceška 
# Date : 22.6.2022
# Task : https://www.algoexpert.io/questions/minimum-waiting-time


# O(n logn) time, O(1) space (only the space given)
def minimum_waiting_time(queries):
    """ returns the minimum waiting time of queries
        
    Args:
        queries (int[ ]) : given queries

    Returns:
        int: the minimum waiting time of queries
    """
    queries.sort()
    waiting_time = 0
    total_waiting_time = 0
    for i in range(1, len(queries)):
        waiting_time = waiting_time + queries[i - 1]
        total_waiting_time += waiting_time
    return total_waiting_time