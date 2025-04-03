'''
input: a string
output: doubles everchar in the str, return a new str
'''

def repeater(s):
    new_str = [char * 2 for char in s]
    return ''.join(new_str)

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")    