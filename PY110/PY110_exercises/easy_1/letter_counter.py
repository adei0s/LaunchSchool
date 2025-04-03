'''
split string into list of "words"
set empty dict
iterate thru each word in the list, 
    count the number of char in the word
    dict(char#) = dict(char#).get(char#, 0) + 1
return new dict
'''

# def word_sizes(s):
#     list_s = s.split()
#     dict_s = {}
#     for word in list_s:
#         len_word = len(word)
#         dict_s[len_word] = dict_s.get(len_word, 0) + 1
#     return dict_s

def is_alpha(word):
    new_word = ''
    for char in word:
        if char.isalpha():
            new_word +=char
    return new_word

def word_sizes(words):
    words_lst = words.split()
    counts = {}
    
    for word in words_lst:
        word = is_alpha(word)
        word_size = len(word)
        if word_size not in counts:
            counts[word_size] = 0
        counts[word_size] += 1
        
    return counts
    