lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

# function for sum of odd number
# sort lst

def odd_sum(lst):
    odd_lst = [num for num in lst if num % 2 == 1]
    return sum(odd_lst)
    
result = sorted(lst, key = odd_sum)

print(result)