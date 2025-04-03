'''
input: a list
- contain atleast 2 integer
output: sorted list via bubble sort, mutate list in place

bubble sort:

finished = False

While not finished:
    finished = True
    for idx, item in enumerate list:
        if list[idx+1] < item:
            position 1 = item
            list[idx] = list[idx+1]
            list[idx+1] = position1
            finished = False
'''

def bubble_sort(lst):
    
    finished = False
    
    while not finished:
        finished = True
        for idx, item in enumerate(lst):
            if idx < len(lst)-1:
                if lst[idx+1] < item:
                    lst[idx], lst[idx + 1] = lst[idx + 1], item
                    finished = False

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected) 