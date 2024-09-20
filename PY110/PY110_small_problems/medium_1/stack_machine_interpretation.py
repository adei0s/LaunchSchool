'''
[3, 6, 4]  ====> stack
MULT  ====> operation
7 ====> register

'''

    

# main

def minilang(s):
    # initialize the stack and register
    stack = []
    reg = 0
    # identify the strings for the commands
        # split commands into a list
    commands = s.split()
    for item in commands:
        if item == 'PUSH':
            stack.append(reg)
        elif item == 'ADD':
            reg += stack.pop()
        elif item == 'SUB':
            reg -= stack.pop()
        elif item == 'MULT':
            reg *= stack.pop()
        elif item == 'DIV':
            reg //= stack.pop()
        elif item == 'REMAINDER':
            reg %= stack.pop()
        elif item == 'POP':
            reg == stack.pop()
        elif item == 'PRINT':
            print(reg)
        else:
            try:
                reg = int(item)
            except:
                print('Error')
            else:
                reg = int(item)
            
    
minilang('5 PRINT PUSH 3 PRINT ADD PRINT')