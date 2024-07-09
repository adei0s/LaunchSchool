'''
input: two list
output: turn list into frozensets and find common elements
'''

def intersection(list1, list2):
    return frozenset(list1) & frozenset(list2)