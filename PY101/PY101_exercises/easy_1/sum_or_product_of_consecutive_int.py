def prompt(msg):
    print(f'==> {msg}')
    
def valid_int(num):
    try:
        int(num)
    except ValueError:
        print("invlaid input. please enter a valid number:")
        return True
    else:
        if int(num) <= 0:
            print("integer must be greater than 0:")
            return True
    return False
    
def calculate_sum(num):
    total = 0
    for number in range(1, integer+1):
        total += number
    return total
    
def calculate_product(num):
    total = 1
    for number in range(1, integer+1):
        total *= number
    return total


prompt('Please enter an integer greater than 0:')
num = input()

while valid_int(num):
    num = input()
    
integer = int(num)
    
prompt('Enter "s" to compute the sum, or "p" to compute the product')
sum_or_product = input().lower()

if sum_or_product == "s":
    print(f'The sum of the integers between 1 and {integer} is {calculate_sum(integer)}.')

elif sum_or_product == "p":
    print(f'The product of the integers between 1 and {integer} is {calculate_product(integer)}.')
    
else:
    prompt('invalid input. Enter "s" to compute the sum, or "p" to compute the product')

