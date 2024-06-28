import random

# random.choice() 

char_options = 'abcdef0123456789'

sections = [8, 4, 4, 4, 12]
    
def make_UUID():
    char_options = 'abcdef0123456789'
    sections = [8, 4, 4, 4, 12]
    lst = []
    
    for section in sections:
        chars = [random.choice(char_options) for char in range(section)]
        lst.append(''.join(chars))
        
    return '-'.join(lst)
    
print(make_UUID())