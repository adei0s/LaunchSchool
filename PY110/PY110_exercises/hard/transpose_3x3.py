'''
input:
a 3x3 matric, nested list.
output:
a new list that is the input transposed

example:
matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True

data structure and algo:
L00, L01, L02
L10, L11, L12
L20, L21, L22

L[idx1][idx2] = L[idx2][idx1]
'''
matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

def transpose(matrix):
    return [[num[row] for num in matrix] 
            for row in range(len(matrix[0]))]
            
new_matrix = transpose(matrix)

print(new_matrix)