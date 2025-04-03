'''
given string of words separated by space
write function that swaps the first and last letter of every word

-word contain atleast 1 letter, str contain atleast 1 word

create new list
separate str into a list of words
set new var startswith and endswith
endswith + slice word + startswith

add to new list

join new list
'''

def swap(string):
    words_list = string.split()
    new_list = []
    for word in words_list:
        if len(word) == 1:
            new_list.append(word)
        else:
            startswith = word[:1]
            endswith = word[-1:]
            newword = endswith + word[1:-1] + startswith
            new_list.append(newword)
    return ' '.join(new_list)
    
    
print(swap('Oh what a wonderful day it is'))