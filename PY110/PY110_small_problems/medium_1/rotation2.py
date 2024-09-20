'''
input: a number, and a count for last _ digits of that number
output: shifting the (count) to the right digit to the end
'''

def rotate_rightmost_digits(number, count):
    string = str(number)
    splice_left = string[:-count]
    splice_right = string[-count+1:]
    result = splice_left + splice_right + string[-count] 
    return int(result)
    
print(rotate_rightmost_digits(735291, 4)) 
