import math

def size(board):
    width = math.floor(math.sqrt(len(board)))
    height = math.floor(len(board) / width)
    return width, height

def options(width):
    options = []
    for x in range(1, width + 1):
        options.append(x)
    return options

def get(board, x, y, width = 0, height = 0):
    if width == 0 or height == 0:
        width, height = size(board)
    return board[y * width + x]

def row_contains(board, y):
    width, height = size(board)
    available = options(width)
    for x in range(width):
        value = get(board, x, y, width, height)
        if value != 0:
            available.remove(value)
    return available

def column_contains(board, x):
    width, height = size(board)
    available = options(width)
    for y in range(width):
        value = get(board, x, y, width, height)
        if value != 0:
            available.remove(value)
    return available

def evaluate(board, x, y):
    value = get(board, x, y)
    if value != 0:
        return value
    row = row_contains(board, y)
    if len(row) == 1:
        return row[0]
    column = column_contains(board, x)
    if len(column) == 1:
        return column[0]