'''
input: list, serach item
output: idx of the search item, -1 if not exist
rules:
list given is always sorted

find the mid point for list, 
    if item > than mid, shift to right to find mid
    if item < than mid, shift to left to find mid
if item == mid,
    return idx of mid
'''

def binary_search(lst, item):
    high = len(lst)
    low = 0
    mid = high // 2
    while low <= high:
        mid = low+ (high - low) // 2
        if item < lst[mid]:
            high = mid -1
        elif item > lst[mid]:
            low = mid + 1
        else:
            return mid
    return -1
    
    
# def recursive_search(lst, item, idx=0):
#     if len(lst) == 1:
#         return (idx of item) or -1