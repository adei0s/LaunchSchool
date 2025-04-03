'''
input: two sorted lists
output: merged list in order, but do not apply sort on the list after merge
'''
def merge(lst1, lst2):
    cp1 = lst1.copy()
    cp2 = lst2.copy()
    merged = []
    while cp1 and cp2:
        if cp1[0] <= cp2[0]:
            merged.append(cp1.pop(0))
        else:
            merged.append(cp2.pop(0))
    return merged + cp1 + cp2

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)