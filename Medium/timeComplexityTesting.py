# Author : Ondřej Maceška 
# Date : 3.6.2022

"""
 A test file used to compare the speeds of algorhitms 
"""

import time 
from findLongestPeak import longest_peak, longest_peak_algoexpert
from random import randint

input_array = [randint(0, 100) for _ in range(10000000)]
#input_array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
#array1, array2 = input_array.copy(), input_array.copy()

start_time = time.time()
print(longest_peak(input_array))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(longest_peak_algoexpert(input_array))
print("--- %s seconds ---" % (time.time() - start_time))
