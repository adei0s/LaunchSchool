'''
input: string
output: all substring of that string
'''

def leading_substrings(s):
    return [s[:idx + 1] for idx in range(len(s))]
    
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
        
        