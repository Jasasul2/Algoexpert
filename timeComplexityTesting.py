# Author : Ondřej Maceška 
# Date : 3.6.2022
"""
 A test file used to compare the speeds of algorhitms 
"""

import time 
from insertionSort import insertion_sort, insertion_sort_slower
from random import randint

input_array = [randint(0, 10000000) for _ in range(10000)]
array1, array2 = input_array.copy(), input_array.copy()

start_time = time.time()
insertion_sort(array1)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
insertion_sort_slower(array2)
print("--- %s seconds ---" % (time.time() - start_time))
