'''
input: two list
output: list contanin all element from both input list, each element take in alternation

use zip?
'''

def interleave(lst1, lst2):
    new_lst = []
    for idx, item in enumerate(lst1):
        new_lst.append(item)
        new_lst.append(lst2[idx])
    return new_lst
    
'''    
further exploration

def interleave(lst1, lst2):
    zipped = zip(lst1, lst2)
    new_lst = []
    for item in zipped:
        new_lst.extend(item)
    return new_lst
'''

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected) 
        