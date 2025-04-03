from datetime import datetime as dt

def prompt(message):
    print(f'==> {message}')
    
prompt("what is your age?")
age = int(input())

prompt("At what age would you like to retire?")
retire_age = int(input())

today = dt.now().year

print(f"it's {today}. You will retire in {today - age + retire_age}.")
print(f"You have only {retire_age - age} of work to go!")
