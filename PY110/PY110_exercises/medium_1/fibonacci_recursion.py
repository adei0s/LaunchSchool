'''
input: n
output: nth fib number


fibonacci(4) = fibonacci(3) + fib(2)
fib(3) = fib(2) + fib(1)
fib(2) = fib(1)
'''



def fibonacci(n):
    # define base condition
    if n <= 2: # when n is less than 2
        return 1 # the result of fibonacci(n) function is 1
    
    return fibonacci(n-1) + fibonacci(n-2) # the result of fibonacci(n) is:
    
print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)