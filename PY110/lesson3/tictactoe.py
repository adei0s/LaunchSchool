'''
display an empty board
set up dictionary for postions player/computer can play on the board via key 1-9
prompt play to make a play
    check that the play is possible, if not possible prompt move again
        print board state if possible move
        check that the play is not a winning move
            return result if winning move

computer moves with a random move, move is a possible move (on a empty square)
    check that the move is not a winning move
        return result if winning move
        
if board is full, display a tie

ask if want to play again

'''

import pdb
import random
import os

WINS = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
    [1, 5, 9], [3, 5, 7]              # diagonals
]

def prompt(message):
    print(f' ==> {message}')

def display_board(board):
    
    os.system('clear')
    prompt(f"You are X. Computer is O.")
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('---+---+---')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('---+---+---')
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('')
    
def initialize_board():
    return {square : ' ' for square in range(1, 10)}
    
def empty_spaces(board):
    return [key for key, value in board.items() if value == ' ']
    
def join_or(sequence, delimiter=', ', word='or'):
    match len(sequence):
        case 0:
            return ''
        case 1:
            return str(sequence[0])
        case 2:
            return f"{sequence[0]} {word} {sequence[1]}"

    leading_items = delimiter.join(str(item) for item in sequence[0:-1])
    return f'{leading_items}{delimiter}{word} {sequence[-1]}'
    
def player_move(board):
    while True:
        valid_moves = [str(num) for num in empty_spaces(board)]
        prompt(f'choose a space on {join_or(valid_moves)}')
        move = input()
        if move in valid_moves:
            break
        else:
            prompt(f"that's not a valid move, try again.")
        
    board[int(move)] = 'X'
    
def computer_move(board):
    if len(empty_spaces(board)) == 0:
        return
    
    breakpoint()
    if offense(board):
        move = offense(board)
    elif defense(board):
        move = defense(board)
    elif board[5] == " ":
        move = 5
    
    else:
        move = random.choice(empty_spaces(board))
    
    board[move] = 'O'

    
def detect_winner(board):
    for line in WINS:
        if all(board[space] == "X" for space in line):
            return "player wins!"
        
        elif all(board[space] == "O" for space in line):
            return "computer wins!"
      
      
def defense(board):
    for line in WINS:
        count = 0
        for space in line:
            if board[space] == "X":
                count += 1
        if count == 2:
            for space in line:
                if board[space] == " ":
                    print(board[space])
                    return space
                    
def offense(board):
    for line in WINS:
        count = 0
        for space in line:
            if board[space] == "O":
                count += 1
        if count == 2:
            for space in line:
                if board[space] == " ":
                    print(board[space])
                    return space
    
    
# play loop

def play():
    while True:    
        #display empty board
        
        board = initialize_board()
        display_board(board)
        
        #prompt player to make a play
        
        while len(empty_spaces(board)) != 0:
            
            player_move(board)
            
            if detect_winner(board):
                display_board(board)
                print(detect_winner(board))
                break
                
            computer_move(board)
            
            if detect_winner(board):
                display_board(board)
                print(detect_winner(board))
                break
            
            display_board(board)
        
            
        if len(empty_spaces(board)) == 0:
            display_board(board)
        
            prompt("it's a tie!")
            
        prompt("Play again? (y or n)")
        answer = input().lower()
    
        if answer[0] != 'y':
            break
    
    prompt('Thanks for playing!')
    
# start game
    
play()