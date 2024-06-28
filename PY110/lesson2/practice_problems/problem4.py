lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]
    

dict1 = {sublist[0] : sublist[1] for sublist in lst}

print(dict1)
