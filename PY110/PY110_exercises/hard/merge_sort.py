'''
input: a list
output: sorted list

to try:
- recursively break down a list's element into nested sub-lists
- combine those nested sublists back together in sorted order 
    - (use merge sorted list)
'''
    
def merge(lst1, lst2):
    cp1 = lst1.copy()
    cp2 = lst2.copy()
    merged = []
    while cp1 and cp2:
        if cp1[0] <= cp2[0]:
            merged.append(cp1.pop(0))
        else:
            merged.append(cp2.pop(0))
    return merged + cp1 + cp2
    
def merge_sort(lst):
    if len(lst) == 1:
        return lst
        
    list1 = lst[: len(lst)//2]
    list2 = lst[len(lst)//2: ]
    
    list1 = merge_sort(list1)
    list2 = merge_sort(list2)

    return merge(list1, list2)
    
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])