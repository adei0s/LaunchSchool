'''
input: a list
output: list with 2 elements, splitting the input list in half. middle element goes in the first list
'''

def halvsies(l):
    half = (len(l)+1)//2
    lst1 = l[:half]
    lst2 = l[half:]
    print([lst1, lst2])
    return [lst1, lst2]
    
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])