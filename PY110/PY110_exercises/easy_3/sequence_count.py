'''
input: 2 int, first in is a count, second is the starting number of a seq that the function will create
output: list containing the same number of elements as the count
- count will be >= 0
- starting can be any int
- if count is 0, return empty lst
'''

def sequence(count, init_num):
    return [num * init_num for num in range(1, count+1)]
    
print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True