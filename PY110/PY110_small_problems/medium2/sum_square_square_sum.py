'''
input: integer n

- difference of:

square of the sum of the first n pos integer

sum of the square of the first n pos integer

output:  difference


'''
    
def sum_square_difference(n):
    sum_of_n = sum(range(1, n+1))
    
    sum_of_square = 0
    
    for num in range(1, n+1):
        sum_of_square += num**2
        
    return sum_of_n**2 - sum_of_square

    
    
print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)