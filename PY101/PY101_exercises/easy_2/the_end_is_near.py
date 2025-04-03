# given a string with words as argument to function
# separate words in the string into list
# return the second to last element in that list

def penultimate(string):
    if not string:
        string = input('please enter a string: \n')
    words = string.split()
    return words[(len(words)//2)]
        
string = input()
        
print(penultimate(string))