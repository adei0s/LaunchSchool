def prompt(message):
    print(f'==> {message}')
    
def calculate(num1, num2, operation):
    match operation:
        case '+': return num1 + num2
        case '-': return num1 - num2
        case '*': return num1 * num2

prompt('Enter the first number')
num1 = float(input())

prompt('Enter the second number')
num2 = float(input())



print(calculate(num1, num2, '+'))


for operation in ['+', '-', '*']:
    task = f'{num1} {operation} {num2}'
    result = calculate(num1, num2, operation)
    print(f'==> {task} = {result}')


