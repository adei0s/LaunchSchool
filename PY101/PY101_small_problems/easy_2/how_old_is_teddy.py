import random

def how_old(name):
    if not name:
        name = 'Teddy'
    return (f'{name} is {random.randint(20, 100)} years old!')
    
name = input('please enter a name: \n')
    
print(how_old(name))
