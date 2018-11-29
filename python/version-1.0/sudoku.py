import math
import logging

def size(board):
    options = math.floor(math.sqrt(len(board)))
    rows = math.floor(math.sqrt(options))
    columns = math.floor(options / rows)
    return rows, columns, options

def all_options(board):
    rows, columns, count = size(board)
    options = []
    for option in range(count):
        options.append(option + 1)
    return options

def get(board, x, y):
    rows, columns, options = size(board)
    return board[y * options + x]

def row(board, y):
    rows, columns, options = size(board)
    used = []
    for x in range(options):
        current = get(board, x, y)
        if current != 0:
            used.append(current)
    return used

def column(board, x):
    rows, columns, options = size(board)
    used = []
    for y in range(options):
        current = get(board, x, y)
        if current != 0:
            used.append(current)
    return used

def sector(board, x, y):
    rows, columns, options = size(board)
    used = []
    sectors_across = math.floor(options / columns)
    across = math.floor(x / sectors_across) * sectors_across
    sectors_down = math.floor(options / rows)
    down = math.floor(y / sectors_down) * sectors_down
    for b in range(down, down + rows):
        for a in range(across, across + columns):
            current = get(board, a, b)
            if current != 0:
                used.append(current)
    return used

def update(board, x, y, value):
    rows, columns, options = size(board)
    board[y * options + x] = value

def evaluate(board, x, y):
    options = all_options(board)
    current = get(board, x, y)
    if current != 0:
        return 'known', current
    row_exclusions = row(board, y)
    for current in row_exclusions:
        if current in options:
            options.remove(current)
    logging.info(options)
    if len(options) == 1:
        return 'valid', options[0]
    column_exclusions = column(board, x)
    for current in column_exclusions:
        if current in options:
            options.remove(current)
    logging.info(options)
    if len(options) == 1:
        return 'valid', options[0]
    sector_exclusions = sector(board, x, y)
    for current in sector_exclusions:
        if current in options:
            options.remove(current)
    logging.info(options)
    if len(options) == 1:
        return 'valid', options[0]
    if len(options) > 1:
        return 'unknown', options
    return 'invalid', 0