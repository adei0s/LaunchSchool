def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

# def is_dot_separated_ip_address(input_string):
#     dot_separated_words = input_string.split(".") # dot_sep_words = list of numbers in the IP address
#     while len(dot_separated_words) > 0:  # when dot_sep_words has atleast one number
#         word = dot_separated_words.pop() #
#         if not is_an_ip_number(word):
#             break

#     return True
    
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words)!= 4:
        return False
    while dot_separated_words:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False
    return True

ip = "1.24562.2.3"               
        
print(is_dot_separated_ip_address(ip))