# Author : Ondřej Maceška 
# Date : 3.6.2022
"""
 A test file used to compare the speeds of algorhitms 
"""


import time 
from sortedSquaredArray import get_sorted_square_array_faster, get_sorted_square_array

start_time = time.time()
get_sorted_square_array([x for x in range(-1000, 1000)])
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
get_sorted_square_array_faster([x for x in range(-1000, 1000)])
print("--- %s seconds ---" % (time.time() - start_time))

    