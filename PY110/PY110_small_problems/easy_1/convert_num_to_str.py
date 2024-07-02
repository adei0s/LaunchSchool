def integer_to_string(i):
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    nums = []
    while i > 10:
        nums.append(i % 10)
        i = i // 10
    nums.append(i)
    nums.reverse()
    chars = [DIGITS[num] for num in nums]
    return ''.join(chars) or 0

