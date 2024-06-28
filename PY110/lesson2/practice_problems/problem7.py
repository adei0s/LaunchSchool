lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# iterate thru lst
# iterate thru sublist
# check if multiple of 3

def mult_three(lst):
    return [num for num in lst if num % 3 == 0]

new_lst = [mult_three(sublist) for sublist in lst]

print(new_lst)