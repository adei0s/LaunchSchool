import random

class Player:
    MOVES = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.move = None

class Human(Player):
    def __init__(self):
        super().__init__()
    def choose(self):
        prompt = 'Enter your move:'

        while True:
            choice = input(prompt).lower()
            if choice in Player.MOVES:
                break
            print("Not valid, try again.")
        self.move = choice

class Computer(Player):
    def __init__(self):
        super().__init__()
        
    def choose(self):
        self.move = random.choices(Player.MOVES)

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _welcome(self):
        print("Welcome to RPS!")

    def _goodbye(self):
        print("Goodbye!")

    def _display_winner(self):
        human_move = self._human.move
        computer_move = self._computer.move

        print(f'you choose: {self._human.move}')
        print(f'computer choose: {self._computer.move}')

        if ((human_move == 'rock' and computer_move == 'scissors') or
            (human_move == 'paper' and computer_move == 'rock') or
            (human_move == 'scissors' and computer_move == 'paper')):
            print('You win!')
            
        elif ((computer_move == 'rock' and human_move == 'scissors') or
              (computer_move == 'paper' and human_move == 'rock') or
              (computer_move == 'scissors' and human_move == 'paper')):
            print('Computer wins!')
            
        else:
            print("It's a tie")

    def _play_again(self):
        print("would you like to play again?")
        answer = input().lower()
        return answer.startswith('y')

    def play(self):
        self._welcome()

        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break
            self._goodbye()

a_game = RPSGame()
a_game.play()