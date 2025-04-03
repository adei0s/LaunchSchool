def xor(item1, item2):
    if (item1 or item2) and (not item1 and item2):
        return True
    
    return False
    
    
# def xor(item1, item2):
#     return bool(item1) != bool(item2)