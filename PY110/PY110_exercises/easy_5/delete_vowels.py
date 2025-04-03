'''
in: list of strings
out: list of the same string but with all vowels removed
'''

def remove_vowels(string_list):
    new_str_list = []
    for word in string_list:
        no_vowel = [char for char in word if char not in 'aeiouAEIOU']
        new_str_list.append(''.join(no_vowel))
    return new_str_list

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected) 