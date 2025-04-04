class Square:
    def __init__(self, marker = ' '):
        self.maker = marker

class Board:
    def __init__(self):
        self.square = {key: Square() for key in range(1, 10)}

    def display(self):
        print("+---+---+---+")
        print(f"| {self.square[1]} | {self.square[2]} | {self.square[3]} |")
        print("+---+---+---+")
        print(f"| {self.square[4]} | {self.square[5]} | {self.square[6]} |")
        print("+---+---+---+")
        print(f"| {self.square[7]} | {self.square[8]} | {self.square[9]} |")
        print("+---+---+---+")

class Player:
    def __init__(self):
        # STUB
        pass

    def choose(self):
        # player choose a move
        pass

    def mark(self):
        # player marks the board
        pass

class Human:
    def __init__(self):
        # STUB
        pass

class Computer:
    def __init__(self):
        # STUB
        pass

class TTTGame:
    def __init__(self):
        self.board = Board()
        self.player1 = Human()
        self.player2 = Computer()

    def play(self):
        self.display_welcome_message()

        while True:
            self.board.display()
            self.player_move()
            if self.game_over():
                break
            self.computer_move()
            if self.game_over():
                break

        self.board.display()
        self.display_result()
        self.display_goodbye_message()
        pass

    def display_welcome_message(self):
        print('Welcome')


    def display_goodbye_message(self):
        print('Goodbye')

    def player_move(self):
        pass
    def computer_move(self):
        pass

    def display_result(self):
        # print result
        pass

    def game_over(self):
        # check if game is over
        pass

game = TTTGame()
game.play()

