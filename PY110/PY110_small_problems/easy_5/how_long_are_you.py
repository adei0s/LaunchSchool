'''
in: string
out: list containing every word from the string, each word followed by a space and word's length
- if argment is empty str or no arg passed, function return an empty list
- all words in string sep by single space
'''

def word_lengths(words = ''):
    return [word + ' ' + str(len(word)) for word in words.split()]
        
print(word_lengths() == [])  