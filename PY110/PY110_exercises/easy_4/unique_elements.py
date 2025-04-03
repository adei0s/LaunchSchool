'''
input: two list
output: elements that are unique to the first list
'''

def unique_from_first(list1, list2):
    return set(list1) - set(list2)