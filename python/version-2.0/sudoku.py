import math

def size(board):
    width = math.sqrt(len(board))
    height = math.floor(len(board) / width)
    return width, height

def get(board, x, y):
    return board[y * 4 + x]

def evaluate(board, x, y):
    value = get(board, x, y)
    if value != 0:
        return value