lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]


def even_list(lst):
    new_lst = [num for num in lst if num % 2 == 0]
    return lst == new_lst

def even_dict(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        if even_list(value):
            new_dict[key] = value
    return new_dict

new_lst = [even_dict(dictionary) for dictionary in lst if even_dict(dictionary) == dictionary]

print(new_lst)


