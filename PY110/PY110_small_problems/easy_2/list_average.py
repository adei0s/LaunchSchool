'''
input: a list of integers
output: average of all the int in the list rounded down to whole num
'''

def average(nums_list):
    return int(sum(nums_list)/len(nums_list))
    
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)  