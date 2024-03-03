number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')

def multiply(x, y):
    return float(x) * float(y)
    
product = multiply(number1, number2)
print(f'{number1} * {number2} = {product}')
