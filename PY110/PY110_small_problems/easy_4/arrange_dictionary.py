'''
input: dictionary
output: key sorted by values associated with each key
'''

# def order_by_value(my_dict):
#     return sorted(my_dict, key=lambda x: my_dict[x])

def get_value(item):
    return item[1]

def order_by_value(my_dict):
    sorted_items = sorted(my_dict.items(), key = get_value) 
    return [key for key, value in sorted_items]

my_dict = {'p': 8, 'q': 2, 'r': 6}

print(order_by_value(my_dict))