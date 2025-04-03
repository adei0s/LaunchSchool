# given a str as function argument
# create variable for sum 
# iterate through each char in the str
#   get the UTF-16 value of the char
#   add to the sum
# return sum

def utf16_value(string):
    utf_sum = 0
    for char in string:
        utf_sum += ord(char)
    return utf_sum
