'''
input: an int
output: a list containing all int between 1 and the input integer (inclusive)
'''

def sequence(n):
    # return [num for num in range(1, n+1)]
    return list(range(1, n+1))

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])  