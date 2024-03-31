# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

# take an integer as argument
# if the number is negative, get absolute value/positive of the number
# if the number is odd, return True
# if number is even , return false

# def is_odd(int_num):
#     absolute_num = abs(int_num)
#     if absolute_num % 2 != 0:
#         return True
#     elif absolute_num % 2 == 0:
#         return False
        
        
def is_odd(number):
    return abs(number) % 2 == 1
        
    