'''
PEDAC }

understand the problem:

- top layer is single block
- each block suppoted by 4 lower block under

layer 1 is 1
layer 2 is 2x2 = 4
layer 3 is 3x3 = 9

questions: are sides equal blocks?
implicit rules:
layer number = side number 

Data structure:

- figure out how many layers the structure has by constructing one layer at the time
- for each layer, block num is layer num * layer num, total block num is total num + layer num
- if input - total block num is less than block num, return input - total block num

- maybe a list, each element representing idx layer num.
'''

def calculate_leftover_blocks(input_num):
    structure = []
    for layer in range(input_num):
        structure.append(layer*layer)
        next_layer = (layer+1)*(layer+1)
        if input_num - sum(structure) < next_layer:
            return input_num - sum(structure)
            
        
        

result = calculate_leftover_blocks(32)    

print(result)

# print(calculate_leftover_blocks(0) == 0)  # True
# print(calculate_leftover_blocks(1) == 0)  # True
# print(calculate_leftover_blocks(2) == 1)  # True
# print(calculate_leftover_blocks(4) == 3)  # True
# print(calculate_leftover_blocks(5) == 0)  # True
# print(calculate_leftover_blocks(6) == 1)  # True
# print(calculate_leftover_blocks(14) == 0) # True
    
    