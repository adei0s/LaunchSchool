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
    
# def calculate_sum(num):
#     total = 0
#     for number in num[0: num]:
#         total += number
#     return total
    
# def calculate_product(num):
#     total = 1
#     for number in num[0: num]:
#         total *= number
#     return total


prompt('Please enter a list of integers greater than 0 separated by space:')
num_list = input().split()

while invalid_list(num_list):
    num_list = input().split()


num_list = [int(num) for num in num_lst]

print(num_list)