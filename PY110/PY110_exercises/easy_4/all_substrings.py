'''
input: a string
output: all substring of that string
'''

def leading_substrings(s):
    return [s[:idx + 1] for idx in range(len(s))]
    
def substrings(s):
    result = []
    for idx in range(len(s)):
        leading = leading_substrings(s[idx:(len(s))])
        result.extend(leading)
    return result
    
expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]
        
print(substrings('abcde') == expected_result) 