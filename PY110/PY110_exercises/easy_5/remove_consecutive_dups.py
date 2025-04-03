'''
in: sequence of int
- filter out where same values occure, retain only initual
out: refined seq
'''

def unique_sequence(nums):
    seen = []
    for num in nums:
        if num not in seen:
            seen.append(num)
    return seen
    
original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)