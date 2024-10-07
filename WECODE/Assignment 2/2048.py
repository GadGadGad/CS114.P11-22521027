import sys

board = []

for i in range(4):
    input_line = sys.stdin.readline().strip().split()
    int_input = [int(num) for num in input_line]
    board.append(int_input)

move = sys.stdin.readline().strip()
# y tuong so bo lay tu ChatGPT:
# prompt: "With a simplified 2048 game (which does not generate new tiles after movement),
#  what is the logic for the move and merge ?"
# Ngoai ra em con search cach chuyen vi ma tran: https://www.geeksforgeeks.org/transpose-matrix-single-line-python/
def moveLeft(board):
    new_board = []
    for row in board:
        value_row = [num for num in row if num != 0]
        # print(value_row)
        for i in range(len(value_row) - 1):
            if value_row[i] == value_row[i + 1]:
                value_row[i] *= 2
                value_row[i + 1] = 0

        value_row = [num for num in value_row if num != 0]
        value_row += [0] * (4 - len(value_row))
        new_board.append(value_row)
    return new_board

def moveRight(board):
    new_board = []
    for row in board:
        value_row = [num for num in row if num != 0][::-1]
        for i in range(len(value_row) - 1):
            if value_row[i] == value_row[i + 1]:
                value_row[i] *= 2
                value_row[i + 1] = 0

        value_row = [num for num in value_row if num != 0]
        value_row += [0] * (4 - len(value_row))
        new_board.append(value_row[::-1])
    return new_board

def transpose(board):
    return [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]

def moveUp(board):
    return (transpose(moveLeft(transpose(board))))
def moveDown(board):
    return (transpose(moveRight(transpose(board))))

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

if move == 'U':
    print_board(moveUp(board))
elif move == 'L':
    print_board(moveLeft(board))
elif move == 'D':
    print_board(moveDown(board))
elif move == 'R':
    print_board(moveRight(board))
