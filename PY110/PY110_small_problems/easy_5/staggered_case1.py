'''
in: string
outt: the string with staggered capitalization, starting with first.
'''

def staggered_case(string):
    to_upper = [char.upper() if idx % 2 == 0 and char.isalnum()
        else char.lower()
        for idx, char in enumerate(string)]
    return ''.join(to_upper)
    
    
string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "") 