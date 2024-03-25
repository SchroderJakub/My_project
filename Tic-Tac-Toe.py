import random

def create_board(size):
    return [[' ' for _ in range(size)] for _ in range(size)]

def print_board(board):
    size = len(board)
    print(" ", end=" ")
    for i in range(size):
        print(i, end=" ")
    print()
    for i in range(size):
        print(i, end=" ")
        for j in range(size):
            print(board[i][j], end=" ")
        print()

def check_win(board, symbol):
    size = len(board)
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    for j in range(size):
        if all(board[i][j] == symbol for i in range(size)):
            return True
    if all(board[i][i] == symbol for i in range(size)) or all(board[i][size-i-1] == symbol for i in range(size)):
        return True
    return False

def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def player_move(board, symbol):
    while True:
        try:
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            if 0 <= row < len(board) and 0 <= col < len(board) and board[row][col] == ' ':
                board[row][col] = symbol
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Invalid input! Please enter numbers.")

def computer_move(board, symbol):
    size = len(board)
    while True:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if board[row][col] == ' ':
            board[row][col] = symbol
            break

def main():
    size = 3
    board = create_board(size)
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    symbols = ['X', 'O']
    turn = 0
    while True:
        symbol = symbols[turn % 2]
        if symbol == 'X':
            player_move(board, symbol)
        else:
            computer_move(board, symbol)
        print_board(board)
        if check_win(board, symbol):
            print("You Win!")
            break
        elif is_full(board):
            print("It's a draw!")
            break
        turn += 1

if __name__ == "__main__":
    main()