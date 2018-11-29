import logging

def all_options():
    return [1, 2, 3, 4]

def get(board, x, y):
    return board[y * 4 + x]

def row(board, y):
    options = all_options()
    used = []
    for x in range(4):
        current = get(board, x, y)
        if current != 0:
            used.append(current)
    for current in used:
        options.remove(current)
    return options

def column(board, x):
    options = all_options()
    used = []
    for y in range(4):
        current = get(board, x, y)
        if current != 0:
            used.append(current)
    for current in used:
        options.remove(current)
    return options

def evaluate(board, x, y):
    current = get(board, x, y)
    if current != 0:
        return 'known', current
    row_options = row(board, y)
    logging.info(row_options)
    if len(row_options) == 1:
        return 'valid', row_options[0]
    column_options = column(board, x)
    logging.info(column_options)
    if len(column_options) == 1:
        return 'valid', column_options[0]
    return 'invalid', 0