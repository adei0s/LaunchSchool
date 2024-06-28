lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# iterate thru dict in lst
# iterate thru item in dict
# key = value+1

# def increment_value(dict1):
#     new_dict = {key: value + 1 for key, value in dict1.items()}
#     return new_dict
    
# new_lst = [increment_value(item) for item in lst] 


new_lst = [{key: value + 1 for key, value in dict1.items()}
                           for dict1 in lst]
                           
print(new_lst)
