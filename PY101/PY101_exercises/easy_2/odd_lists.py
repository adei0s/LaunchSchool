def oddities(lst):
    new_lst = []
    for idx in range(0, len(lst), 2):
        new_lst.append(lst[idx])
    return new_lst
    
# bonus:
def oddities(lst):
    return lst[::2]

def oddities(lst):
    return [lst[idx] for idx in range(0,len(lst),2)]
    
print(oddities([2, 3, 4, 5, 6]))