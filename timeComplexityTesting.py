# Author : Ondřej Maceška 
# Date : 3.6.2022
"""
 A test file used to compare the speeds of algorhitms 
"""

import time 
from findThreeLargestNumbers import find_three_largest_numbers, find_three_largest_numbers_alt
from random import randint

input_array = [randint(0, 10000000) for _ in range(1000000)]
start_time = time.time()
print(find_three_largest_numbers(input_array))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(find_three_largest_numbers_alt(input_array))
print("--- %s seconds ---" % (time.time() - start_time))
