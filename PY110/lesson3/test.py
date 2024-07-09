def initialize_board():
    return {square : ' ' for square in range(1, 10)}

board = {
1: 'X', 
2: 'X', 
3: 'O', 
4: ' ', 
5: ' ', 
6: ' ', 
7: 'O', 
8: 'O', 
9: 'O',
}

def detect_winner(board):
    wins = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]              # diagonals
    ]
    
    for line in wins:
        if all(board[space] == "X" for space in line):
            return "player wins"
        
        elif all(board[space] == "O" for space in line):
            return "computer wins"
            
print(detect_winner(board))