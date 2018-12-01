import math

def size(board):
    width = math.sqrt(len(board))
    height = math.floor(len(board) / width)
    return width, height