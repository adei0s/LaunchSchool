import random
# Insert this line at the top of the program.
VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f"==> {message}")

while True:
    prompt('Choose one: rock, paper, scissors')
    choice = input()
    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()
        
    computer_choice = random.choices(VALID_CHOICES)
    
    prompt(f"you chose {choice}, computer chose {computer_choice}")
    
    if ((choice == "rock" and computer_choice == "scissors") or
        (choice == "paper" and computer_choice == "rock") or
        (choice == "scissors" and computer_choice == "paper")):
        prompt("You win!")
    elif ((choice == "rock" and computer_choice == "paper") or
          (choice == "paper" and computer_choice == "scissors") or
          (choice == "scissors" and computer_choice == "rock")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")
        
    prompt("do you want to play again (y/n)?")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        
        prompt('please enter "y" or "n".')
        answer = input().lower()
        
    if answer[0] == 'n':
        break