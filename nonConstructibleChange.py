# Author : Ondřej Maceška 
# Date : 4.6.2022

# Solution 1 ---------------------------------
# nonsesical bruteforce algorithm 
def can_be_constructed(counter, target):
    current_target = target
    if(current_target in counter):
        return True 
    while (current_target > 1):
        while(not current_target in counter):
            current_target -= 1
        counter[current_target] -= 1
        if(counter[current_target] == 0):
            del counter[current_target]
        rest = target - current_target
        return True if rest == 0 else can_be_constructed(counter.copy(), rest)
    return False
                

def non_constructible_change(coins):
    if (len(coins) == 0):
        return 1
    
    counter = {}
    for coin in coins:
        counter[coin] = counter.get(coin, 0) + 1
        
    result = 1
    found = False
    while not found:
        result += 1
        found = not can_be_constructed(counter.copy(), result)   
        
    return result

# Solution 2 ---------------------------------
# O(nlogn) time, O(1) space where n is the number of coins
def non_constructible_change_faster(coins):
    sorted_coins = sorted(coins)
    max_change = 0
    
    for coin in sorted_coins:
        if(coin > (max_change + 1)):
            return max_change + 1
        max_change += coin 
        
    return max_change + 1
    