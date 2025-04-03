'''
input: string of digits
output: the number as an integer
- don't use conversion functions
- all char are positive numeric

separate str into list of char
convert char into int*
invert the list so the first element is 1s, second is 10s, etc.
digit place counter = 0
total = 0
for each char:
    value = char to the (digit counter) power of 10
    totol += value
return total

int conversion:
input char = match to int 1-9
return the int
'''

def convert(char):
    match char:
        case "1":
            char = 1
        case "2":
            char = 2
        case "3":
            char = 3
        case "4":
            char = 4
        case "5":
            char = 5
        case "6":
            char = 6
        case "7":
            char = 7
        case "8":
            char = 8
        case "9":
            char = 9
        case "0":
            char = 0
    return char
    
def string_to_integer(string):
    num_list = list(string)
    num_list.reverse()
    digitplace = 0
    total = 0
    for char in num_list:
        char = convert(char)
        value = char * (10**digitplace)
        digitplace += 1
        total += value
    return total
        
print(string_to_integer("4321"))

