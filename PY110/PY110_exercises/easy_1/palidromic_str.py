'''
invert the char in the string
compare the strings
'''

def is_palidrome(s):
    return s == s[::-1]
        
'''
empty new str
iterate through s
if char is alpha numeric,
add casefold char to new str
'''
def is_real_palidrom(s):
    clean_str = ''
    for char in s:
        if char.isalnum():
            clean_str += char.casefold()
    return is_palidrome(clean_str)
    