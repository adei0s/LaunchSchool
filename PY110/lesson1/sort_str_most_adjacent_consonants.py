'''
input: a list of strings
sort the list by highest number of adjacent consonants in that string
if two strings contain same num of adjacent consonants, retain order
output: sorted new string

adjacent consonants:
    - next to each other in the same str
    - can have a space between them
    
questions: 
- do non-alpha numeric/punctuations count?
- can str be empty?
- is case important?
- ascending or descending? (descending based on test cases)
- single consonants in a str do not effect sort order, only adjacent consonants

data structure and algo
- a dictionary with consonant count: string
- sort the dictionary by key
- return values of dictionary

sub function: count number of adjacent consonants in string
- delete spaces
- itrate through string
max count = 0
counter = 0
- is char consonant? if yes, 
-   counter += 1
    if counter > max count, count = max count
  is char not a consonant? if yes, count = 0
  if max count == 1, max count = 0
return max count  

'''

def count_max_adjacent_consonants(string):
    string = ''.join(string.split())
    max_count = 0
    counter = 0
    for char in string:
        if char in 'bcdfghjklmnpqrstvwxyz':
            counter += 1
            if counter > max_count:
                max_count = counter
        else:
            counter = 0
    if max_count == 1:
        max_count = 0
    return max_count
    

def sort_consonant_count(my_list):
    my_list.sort(key=count_max_adjacent_consonants, reverse = True)
    return my_list
    
my_list = ['xxxa', 'xxxx', 'xxxb']
result = sort_consonant_count(my_list)

print(result)