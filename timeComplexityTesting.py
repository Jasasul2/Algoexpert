# Author : Ondřej Maceška 
# Date : 3.6.2022
"""
 A test file used to compare the speeds of algorhitms 
"""

import time 
from nonConstructibleChange import non_constructible_change, can_be_constructed, non_constructible_change_faster

input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
start_time = time.time()
print(non_constructible_change(input_array))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(non_constructible_change_faster(input_array))
print("--- %s seconds ---" % (time.time() - start_time))
