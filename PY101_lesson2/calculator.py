# Ask user for the first number.
# Ask user for the second number.
# Ask user for an oppoeration to perform.
# perform the operation on the two numbers.
# print the result to the terminal.

def prompt(message):
    print(f"==> {message}")

def invalid_num(num_str):
    try:
        int(num_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator')

prompt("what's the first number: ")
num1 = input()

while invalid_num(num1):
    prompt("hmm.. that doesn't look like a valid number.")
    num1 = input()

prompt("what's the second number: ")
num2 = input()

while invalid_num(num2):
    prompt("hmm.. that doesn't look like a valid number.")
    num2 = input()

prompt("what operation would you like to perform?\n"
    "1) add 2) subtract 3) multiply 4) divide")
operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()

# print(f'{num1} {num2} {operation}')
match operation:
    case '1':
        result = int(num1) + int(num2)
    case '2':
        result = int(num1) - int(num2)
    case '3':
        result = int(num1) * int(num2)
    case '4':
        result = int(num1) / int(num2)

print(f'the result is: {result}')