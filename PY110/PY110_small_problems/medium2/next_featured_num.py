'''
input: a number
output: next featured number

- a featured number is:
    multiple of 7
    is odd
    each number occur only once
    maximum 9876543201
    
take the given number:
    itterate up until it is a multiple of 7
    test to see if there are repeats
    if no repeat return number
    
to test for repeat nums:
    if list(str(num)) == set(str(num)) return true

'''

import pdb

def repeats(num):
    return len(list(str(num))) != len(set(str(num)))

# breakpoint()

error = "There is no possible number that fulfills those requirements."

def next_featured(num):
    num += 1
    while num < 9876543201:
        while num % 7 != 0 or num % 2 == 0 or repeats(num) :
            num += 1
        return num
    return error
    
# test cases

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error) 