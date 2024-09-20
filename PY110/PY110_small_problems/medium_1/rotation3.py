'''
in: a number
- i[0] to the end 
- new i[0] in place and rotate the rest of the digit
- keep first 2 in place and rotate rest of digit
- until 2 digits left and rotate final digit
out: resulting number (max rotation)
'''
#import pdb

def rotate_rightmost_digits(number, count):
    string = str(number)
    splice_left = string[:-count]
    splice_right = string[-count+1:]
    result = splice_left + splice_right + string[-count] 
    return int(result)

def max_rotation(num):
    count = len(str(num))
    #breakpoint()
    for digit in range(count, 1, -1):
        num = rotate_rightmost_digits(num, digit)
    return num
    
print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)