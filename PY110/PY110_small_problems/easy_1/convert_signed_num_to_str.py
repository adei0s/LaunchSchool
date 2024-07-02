def integer_to_string(i):
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    nums = []
    while i > 10:
        nums.append(i % 10)
        i = i // 10
    nums.append(i)
    nums.reverse()
    chars = [DIGITS[num] for num in nums]
    return ''.join(chars) or '0'
    
def signed_integer_to_string(i):
    if i > 0:
        return '+' + integer_to_string(i)
    elif i < 0:
        return '-' + integer_to_string(i*-1)
    else:
        return '0'

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")    