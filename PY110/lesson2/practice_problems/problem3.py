lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# convert num to strings function
# iterate through list, iterate thru sublist
# sort sublist

def num_to_str(num):
    return str(num)
    

    
new_list = [sorted(sublist, key = num_to_str) for sublist in lst]
    
print(new_list)

