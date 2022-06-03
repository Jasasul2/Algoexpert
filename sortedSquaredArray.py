# Author : Ondřej Maceška 
# Date : 3.6.2022

# O(n * log(n)) time, O(n) space 
# Actually faster 
def get_sorted_square_array(array):
    return sorted([x * x for x in array])

# O(n) time, O(n) space 
# Actually slower
def get_sorted_square_array_faster(array):
    squares = [0 for _ in array]
    smallest_index = 0
    largest_index = len(array) - 1
    
    for i in reversed(range(len(array))):
        smallest_value = array[smallest_index]
        largest_value = array[largest_index]
        
        if abs(smallest_value) > abs(largest_value):
            squares[i] =  smallest_value * smallest_value
            smallest_index += 1
        else:
            squares[i] =  smallest_value * smallest_value
            largest_index -= 1
    
    return squares 