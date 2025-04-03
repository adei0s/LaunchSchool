'''
input: string consist of first name, space, last name
output: new string of last name, comma, first name
'''

def swap_name(s):
    names = s.split()
    return f'{names[1]}, {names[0]}'
    
print(swap_name('Joe Roberts') == "Roberts, Joe")   # True