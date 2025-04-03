'''
in: a dict where both key and values are unique
out: invert dict so keys become value and values become keys
'''

def invert_dict(d):
    return {value: key for key, value in d.items()}