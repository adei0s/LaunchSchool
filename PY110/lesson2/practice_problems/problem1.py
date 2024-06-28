# empty list
# iterate through munsters
# if gender is male, add to list




munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}


male_munsters = [ munsters[person]['age'] for person in munsters if munsters[person]['gender'] == 'male']
total = sum(male_munsters)

print(total)