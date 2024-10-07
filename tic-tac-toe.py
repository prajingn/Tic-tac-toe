import random

# constants
PLAYER = 'X'
COMPUTER = 'O'

winner = 'NA'

# printBoard function
def printBoard():
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")

# checkFreeSpace function
def checkFreeSpaces():
    spaces = 9
    for i in range(3):
        for j in range(3):
            if board[i][j] != ' ':
                spaces -= 1
    return spaces

# playerMove function
def playerMove():
    while True:
        row = int(input("Enter row #(1-3): "))
        column = int(input("Enter column #(1-3): "))
        row -= 1
        column -= 1

        if board[row][column] == ' ':
            board[row][column] = PLAYER
            break
        else:
            print("Invalid move!")

# checkWinner function
def checkWinner():
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != ' ':
            return board[i][0]

    # Check rows
    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]

    # check diagonals
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != ' ':
        return board[0][0]

# computerMove function
def computerMove():
    if checkFreeSpaces != 0:
        options = [0, 1, 2]
        while True:
            x = random.choice(options)
            y = random.choice(options)

            if board[x][y] == ' ':
                board[x][y] = COMPUTER
                break
    else:
        printWinner('tie')

# printWinner function
def printWinner():
    if winner == 'X':
        print("You win!")
    elif winner == 'O':
        print("you lose! ")
    elif winner ==  'tie':
        print("Its a tie!")
    elif winner == 'NA':
        print("Its a tie!")

# Create 2d list 'board'
board = [[' ' for i in range(3)] for j in range(3)]

while winner == 'NA' and checkFreeSpaces() != 0:
    printBoard() # Print the board
    playerMove() # Player's move
    winner = checkWinner() # Checks for a winner
    if winner == None:
        winner = 'NA'

    if winner != 'NA' or checkFreeSpaces() == 0:
        break

    computerMove() # Computer's move
    winner = checkWinner() # Checks for a winner
    if winner == None:
        winner = 'NA'

    if winner != 'NA' or checkFreeSpaces() == 0:
        break

printBoard()
printWinner()