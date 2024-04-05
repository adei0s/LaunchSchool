#give txt

# initialize a new txtstr
# intiialize a repeat space
# iterate through txt

# if the char is non-alphabetic, and repeat is false, char is space
# repeat is true

# else char is char

def clean_up(txt):
    result = ""
    repeat = False
    
    for char in txt:
        if char.isalpha():
            result += char
            repeat = False
        elif repeat == False:
            result += " "
            repeat = True
        pass
    
    return result
    
print(clean_up("---what's my +*& line?"))