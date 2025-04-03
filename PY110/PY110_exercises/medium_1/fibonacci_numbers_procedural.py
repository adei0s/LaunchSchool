'''
input: a num
output: the nth fibonacci number 
- a list with n elements
- for idx in lst add to previous total

'''

def fibonacci(n):
    fib_lst = [0, 1,]
    for num in range(2, n+1):
        next_num = fib_lst[num-1] + fib_lst[num-2]
        fib_lst.append(next_num)
        
    return fib_lst[n]
    

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True