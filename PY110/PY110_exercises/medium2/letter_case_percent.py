'''
input: a string 

output: 3 percentages
- percnt of char in string that are lowercase
- percent of char that are uppercase
- percent of char thats neither

rules:
- all 3 % should be returned as string with values between 0.00 and 100.00, rounded to 2 decimal points
- input string will always contain atleast 1 char
'''

def round(num):
    return str(f'{num*100:.2f}')

def letter_percentages(string):
    lower = 0
    upper = 0
    neither = 0
    for char in string:
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
        else:
            neither += 1
    total = lower + upper + neither

    expected_result = {}
    expected_result['lowercase'] = round(lower/total)
    expected_result['uppercase'] = round(upper/total)
    expected_result['neither'] = round(neither/total)
    return expected_result

#test cases

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)