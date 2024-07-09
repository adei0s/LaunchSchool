'''
intput: a string
output: all aplindromic substring of given string
- each substring reads same forward and backward
- sorted by order of appearance in input str
- dup substrings be included multiple times
- use substring function
- pay attention to cases
- single char are not palindromes
'''

def leading_substrings(s):
    return [s[:idx + 1] for idx in range(len(s))]
    
def substrings(s):
    result = []
    for idx in range(len(s)):
        leading = leading_substrings(s[idx:(len(s))])
        result.extend(leading)
    return result
    
def palindromes(s):
    substring_list = substrings(s)
    is_palindrome = []
    for word in substring_list:
        if (len(word) > 1) and (word == word[::-1]):
            is_palindrome.append(word)
    return is_palindrome
    
print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ]) 