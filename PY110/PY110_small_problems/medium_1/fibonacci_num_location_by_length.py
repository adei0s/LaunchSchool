'''
input: a number representing number of digits
output: the nth fibonacci number that has the number of digits
'''

import sys

sys.set_int_max_str_digits(50_000)

def find_fibonacci_index_by_length(digits):
    fib_idx = 1
    fib_n = 1
    prev1 = 1
    prev2 = 0
    
    while len(str(fib_n)) < digits:
        fib_n = prev1 + prev2
        prev2 = prev1
        prev1 = fib_n
        fib_idx += 1
        
    return fib_idx

print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)