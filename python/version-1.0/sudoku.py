import math
import logging

def all_options():
    return [1, 2, 3, 4]

def get(board, x, y):
    return board[y * 4 + x]

def row(board, y):
    used = []
    for x in range(4):
        current = get(board, x, y)
        if current != 0:
            used.append(current)
    return used

def column(board, x):
    used = []
    for y in range(4):
        current = get(board, x, y)
        if current != 0:
            used.append(current)
    return used

def sector(board, x, y):
    used = []
    across = math.floor(x / 2) * 2
    down = math.floor(y / 2) * 2
    for b in range(down, down + 2):
        for a in range(across, across + 2):
            current = get(board, a, b)
            if current != 0:
                used.append(current)
    return used

def evaluate(board, x, y):
    options = all_options()
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
        return 'unknown', 0
    return 'invalid', 0