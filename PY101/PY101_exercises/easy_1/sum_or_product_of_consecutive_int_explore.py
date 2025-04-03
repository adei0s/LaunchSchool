def prompt(msg):
    print(f'==> {msg}')
    
def invalid_list(lst):
    try:
        valid_lst = [int(num) for num in lst]
    except ValueError:
        print("invlaid input. please enter a valid list:")
        return True
        
    if all(num > 0 for num in valid_lst):
        return False
        
    else: 
        print("only input positive integers:")
        return True
    
def calculate_sum(lst):
    total = 0
    for number in lst:
        total += number
    return total
    
def calculate_product(lst):
    total = 1
    for number in lst:
        total *= number
    return total


prompt('Please enter a list of integers greater than 0 separated by space:')
num_list = input().split()

while invalid_list(num_list):
    num_list = input().split()

print(num_list)
num_list = [int(num) for num in num_list]
    
prompt('Enter "s" to compute the sum, or "p" to compute the product')
sum_or_product = input().lower()

if sum_or_product == "s":
    print(f'The sum of the integers {num_list} is {calculate_sum(num_list)}.')

elif sum_or_product == "p":
    print(f'The product of the integers {num_list} is {calculate_product(num_list)}.')
    
else:
    prompt('invalid input. Enter "s" to compute the sum, or "p" to compute the product')

