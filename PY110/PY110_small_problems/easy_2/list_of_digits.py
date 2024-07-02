'''
input: a positive int
output: list of digits in the number

convert int to str
make a list out of the str
conver each num in list to int
'''

def digit_list(n):
    return [int(num) for num in list(str(n))]
    
    
print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])     