# prompt for a bill amount and tip rate
# calculate the ip
# print both the tip and total amount of the bill

def prompt(msg):
    print(f'==> {msg}')
    
#ask for bill amount

prompt("what is your bill amount in dollars?")
bill = float(input())

prompt("what is the tip rate?")
rate = float(input()) / 100

tip_amount = bill * rate
total_amount = bill + tip_amount

print(f'the tip is ${tip_amount}')
print(f'the total is ${total_amount}')

