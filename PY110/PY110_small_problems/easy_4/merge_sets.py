'''
input: 2 list
output: convert them to sets and return new set of union of both sets
'''

def merge_sets(list1, list2):
    return set(list1) | set(list2)