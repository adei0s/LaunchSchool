'''
input: list of positive int
- mutiply all int together, divide the result by num of entries
output: result of operations as string, rounded to 3 decimals
'''

def multiplicative_average(l):
    product = 1
    for num in l:
        product *= num
    average = product / len(l)
    return f'{average:.3f}'

    
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")