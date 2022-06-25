# Author : Ondřej Maceška 
# Date : 3.6.2022
"""
 A test file used to compare the speeds of algorhitms 
"""

import time 
from palindromeCheck import is_palindrome_v1, is_palindrome_v2
from random import randint

input_array = "aaaaab" * 6900000
#array1, array2 = input_array.copy(), input_array.copy()

start_time = time.time()
print(is_palindrome_v1(input_array))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print(is_palindrome_v2(input_array))
print("--- %s seconds ---" % (time.time() - start_time))
