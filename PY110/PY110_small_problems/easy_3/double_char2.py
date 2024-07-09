'''
input: a string
output: double every consonent, return stri
'''
def double_consonants(s):
    new_str = [char * 2 if char.casefold() in 'bcdfghjklmnpqrstvwxyz' else char for char in s]
    return ''.join(new_str)
    
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")