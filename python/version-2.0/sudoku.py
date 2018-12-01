import math

def size(board):
    width = math.floor(math.sqrt(len(board)))
    height = math.floor(len(board) / width)
    return width, height

def get(board, x, y):
    width, height = size(board)
    return board[y * width + x]

def row_contains(board, y):
    width, height = size(board)
    options = []
    for x in range(1, width + 1):
        options.append(x)
    print(options)
    for x in range(width):
        value = get(board, x, y)
        if value != 0:
            options.remove(value)
    return options

def evaluate(board, x, y):
    value = get(board, x, y)
    if value != 0:
        return value
    row = row_contains(board, y)
    if len(row) == 1:
        return row[0]