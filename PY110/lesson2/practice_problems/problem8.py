dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

'''
iterate thru product subdict
if subdict[type] is fruit:
    return subdict[color]
if subdict[type] is veg:
    return subdict[size]
'''

def produce(item_description):
    if item_description['type'] == 'fruit':
        return [color.capitalize() for color in item_description['colors']]
    if item_description['type'] == 'vegetable':
        return item_description['size'].upper()
        
# for item in dict1:
#     for description in item.values():
#         print(produce(description))

new_list = [produce(description) for description in dict1.values()]

print(new_list)