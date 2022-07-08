# Author : Ondřej Maceška 
# Date : 3.6.2022

"""
 A test file used to compare the speeds of algorhitms 
"""

import time 
from arrayOfProducts import array_of_products, array_of_products_faster
from random import randint

input_array = [randint(1, 2) for _ in range(1000)]
#input_array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
#array1, array2 = input_array.copy(), input_array.copy()

start_time = time.time()
print(array_of_products(input_array))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(array_of_products_faster(input_array))
print("--- %s seconds ---" % (time.time() - start_time))
