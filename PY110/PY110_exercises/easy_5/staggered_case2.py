'''
in: string
outt: the string with staggered capitalization, starting with first.
-ignore non alpha char, still be included in the return value
'''

def staggered_case(string):
    result = ''
    cap = 1
    for char in string:
        if char.isalpha():
            if cap == 1:
                result += char.upper()
                cap -= 1
            else:
                result += char.lower()
                cap += 1
        else:
            result += char
    return result
    

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")  