'''
input: 2 list, each containing a list of numbers
output: new list containing product of each pair of numbers from the arugment that have the same index
'''
'''
def multiply_list(lst1, lst2):
    return [num*lst2[idx] for idx, num in enumerate(lst1)]
    

using zip:
def multiply_list(lst1,lst2):
    return [a * b for a, b in zip(lst1, lst2)]
'''

def multiply_list(lst1, lst2):
    return [lst1[i] * lst2[i] for i in range(len(lst1))]



list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True