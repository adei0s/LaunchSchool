'''
in: dict, a list of keys
out: new dict contain only key/valuee pairs for the specific keys
'''

def keep_keys(input_dict, keys):
    return {key : value for key, value in input_dict.items() if key in keys}
    