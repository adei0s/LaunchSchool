'''
input: a string
ouput: True if all parenthesis in the string are balanced, False otherwise)
- balance means parenthesis occure in matching '(' and ')' pairs
'''

def is_balanced(s):
    count = 0
    for item in s:
        if item == '(':
            count += 1
        if item == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0
        

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)