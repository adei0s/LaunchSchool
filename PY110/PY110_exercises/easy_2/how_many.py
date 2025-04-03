'''
input: a list
- counts the number of occurences of each element in a given list
output: print each element alonside the num of occurences

given a list
create a dictionary
iterate thru list, item = item count + 1, default 0
'''

def count_occurrences(lst):
    dict1 = {}
    for item in lst:
        dict1[item] = dict1.get(item, 0) + 1
    return dict1
        
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

result = count_occurrences(vehicles)


print(result)