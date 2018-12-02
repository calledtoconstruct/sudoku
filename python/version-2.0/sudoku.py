import math

def size(board):
    width = math.floor(math.sqrt(len(board)))
    height = math.floor(len(board) / width)
    return width, height

def sector_size(board):
    sqrt = math.sqrt(math.sqrt(len(board)))
    horizontally = math.floor(sqrt)
    vertically = math.ceil(sqrt)
    return horizontally, vertically

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

def sector_contains(board, x, y):
    width, height = size(board)
    available = options(width)
    horizontally, vertically = sector_size(board)
    cells_horizontally = math.floor(width / horizontally)
    a = math.floor(x / cells_horizontally) * cells_horizontally
    cells_vertically = math.floor(height / vertically)
    b = math.floor(y / cells_vertically) * cells_vertically
    for vertical_index in range(b, b + cells_vertically + 1):
        for horizontal_index in range(a, a + cells_horizontally + 1):
            value = get(board, horizontal_index, vertical_index)
            if value != 0:
                available.remove(value)
    return available

def evaluate(board, x, y):
    width, height = size(board)
    value = get(board, x, y)
    if value != 0:
        return value
    row = row_contains(board, y)
    if len(row) == 1:
        return row[0]
    column = column_contains(board, x)
    if len(column) == 1:
        return column[0]
    sector = sector_contains(board, x, y)
    if len(sector) == 1:
        return sector[0]
    available = []
    for value in options(width):
        if value in row and value in column and value in sector:
            available.append(value)
    if len(available) == 1:
        return available[0]