'''
new empty list
initial total set to 0
iterate thru old list, add each item to total
append new list with the total num
'''

def running_total(lst):
    totals_lst = []
    total = 0
    for num in lst:
        total += num
        totals_lst.append(total)
    return totals_lst
    
    