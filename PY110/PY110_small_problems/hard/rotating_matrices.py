matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

def transpose(matrix):
    return [[num[row] for num in reversed(matrix)] 
            for row in range(len(matrix[0]))]
            
new_matrix = transpose(matrix)

print(new_matrix)