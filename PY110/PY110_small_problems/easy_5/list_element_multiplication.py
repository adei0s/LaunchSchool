'''
in: 2 list of integers of same length
out: new list where each element is product of oreesponding element from 2 lists
'''

def multiply_items(list1, list2):
    return [list1[idx] * list2[idx] for idx in range(len(list1))]
    # return [num1 * num2 for num1, num2 in zip(list1, listt2)]
    
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True