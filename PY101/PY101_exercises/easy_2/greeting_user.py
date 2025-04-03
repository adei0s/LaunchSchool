# ask for user input name
# look for ! at the end of the name
# generate greeting
# if ! at the end of name generate yelling greeting

def prompt(message):
    print(f'==> {message}')
    

prompt("what is your name?")
name = input()

if name.endswith("!"):    # if name[-1] == "!"
    print(f'HELLO {name.upper()}! WHY ARE WE YELLING?')
else:
    print(f'Hello {name}.')

