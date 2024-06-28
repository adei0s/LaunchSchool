dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# for key, value in dict1
# for item in value list
# if char in item in aeiou
# new list.append(char)

def list_of_vowels(dict1):
    new_lst = [char for key in dict1
                    for word in dict1[key]
                    for char in word if char in 'aeiou']
                    
    return new_lst
    
print(list_of_vowels(dict1))