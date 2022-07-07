# Author : Ondřej Maceška 
# Date : 7.7.2022

"""
 A test file used to visually represent the results of the findLongestPeak.py algorithms
"""

import time 
from findLongestPeak import longest_peak, longest_peak_algoexpert
from random import randint
import matplotlib.pyplot as plt
  

def plot_peak(input_tuple):
    print(input_tuple)
    x = [i for i in range(input_tuple[1] - len(input_tuple[0]), input_tuple[1])]
    y = input_tuple[0]
    plt.plot(x, y, color='brown', linewidth = 3,
         marker='o', markerfacecolor='red', markersize=8)
    plt.xlabel('Indexes')
    plt.ylabel('Height')
    plt.title('plot_peak_graph')
    plt.show()
    
if(__name__ == "__main__"):
    input_array = [randint(-5, 5) for _ in range(10000)]

    start_time = time.time()
    results1 = longest_peak(input_array)
    print("--- %s seconds ---" % (time.time() - start_time))
    plot_peak(results1)
    start_time = time.time()
    results2 = longest_peak_algoexpert(input_array)
    print("--- %s seconds ---" % (time.time() - start_time))
    plot_peak(results2)