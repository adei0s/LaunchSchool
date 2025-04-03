def multiply(num1, num2):
    return num1 * num2
    
def power(num, n):
    result = 1
    for number in n:
        result = multiply(result, num)