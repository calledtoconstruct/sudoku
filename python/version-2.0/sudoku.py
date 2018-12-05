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
    for x in range(width):
        options.append(x + 1)
    return options

def get(board, width, x, y):
    return board[y * width + x]

def row_contains(board, width, y):
    available = options(width)
    for x in range(width):
        value = get(board, width, x, y)
        if value != 0:
            available.remove(value)
    return available

def column_contains(board, width, x):
    available = options(width)
    for y in range(width):
        value = get(board, width, x, y)
        if value != 0:
            available.remove(value)
    return available

def scan_sector(board, width, height, x, y, action, available, ignore = []):
    horizontally, vertically = sector_size(board)
    cells_horizontally = math.floor(width / horizontally)
    a = math.floor(x / cells_horizontally) * cells_horizontally
    cells_vertically = math.floor(height / vertically)
    b = math.floor(y / cells_vertically) * cells_vertically
    for vertical_index in range(b, b + cells_vertically):
        for horizontal_index in range(a, a + cells_horizontally):
            if horizontal_index != x or vertical_index != y:
                action(board, width, height, horizontal_index, vertical_index, available)

def sector_contains(board, width, height, x, y):
    available = options(width)
    scan_sector(board, width, height, x, y, exclude_used_options, available)
    return available

def exclude_used_options(board, width, height, x, y, available):
    value = get(board, width, x, y)
    if value != 0:
        available.remove(value)

def accumulate_options(board, width, height, x, y, available):
    value = get(board, width, x, y)
    if value != 0:
        return
    options = evaluate(board, width, height, x, y, True)
    if type(options) is list:
        for value in options:
            if value in available:
                available.remove(value)
    elif type(options) is int:
        if options in available:
            available.remove(options)

def evaluate(board, width, height, x, y, quick = False):
    value = get(board, width, x, y)
    if value != 0:
        return value
    row = row_contains(board, width, y)
    if len(row) == 1:
        return row[0]
    column = column_contains(board, width, x)
    if len(column) == 1:
        return column[0]
    sector = sector_contains(board, width, height, x, y)
    if len(sector) == 1:
        return sector[0]
    available = []
    for value in options(width):
        if value in row and value in column and value in sector:
            available.append(value)
    if len(available) == 1:
        return available[0]

    if quick:
        return available

    scan_sector(board, width, height, x, y, accumulate_options, available)
    if len(available) == 1:
        return available[0]

    return 0

def set(board, width, x, y, value):
    board[y * width + x] = value

def play(board, width, height, x, y, ignore = []):
    if get(board, width, x, y) != 0:
        return False
    ignore.append([x, y])
    changes_were_made = False
    updated = True
    while updated:
        updated = False
        value = evaluate(board, width, height, x, y)
        if value != 0:
            set(board, width, x, y, value)
            return True
        for index in range(width):
            if [index, y] not in ignore:
                if play(board, width, height, index, y, ignore):
                    updated = True
                    changes_were_made = True
    return changes_were_made

def empty(board, width, height):
    count = 0
    for y in range(height):
        for x in range(width):
            value = get(board, width, x, y)
            if value == 0:
                count += 1
    return count

def fill(board, width, height, guess_action, play_action):
    updated = True
    while updated:
        updated = False
        for y in range(height):
            for x in range(width):
                value = get(board, width, x, y)
                if value == 0:
                    if play_action(board, width, height, x, y):
                        updated = True
    missing = empty(board, width, height)
    if missing > 0:
        guess_action(board, width, height, 0, 0, play_action)
    return board

def guess(board, width, height, x, y, action, ignore = []):
    options = evaluate(board, width, height, x, y, True)
    option = 0
    copy_of_board = board.copy()
    set(copy_of_board, width, x, y, options[option])
    # call fill method
    updated = True
    while updated:
        updated = False
        for y in range(height):
            for x in range(width):
                value = get(copy_of_board, width, x, y)
                if value == 0:
                    if action(copy_of_board, width, height, x, y):
                        updated = True
    return copy_of_board
    # recursively call guess??

def verify(board, width, height):
    for y in range(height):
        available = options(width)
        for x in range(width):
            value = get(board, width, x, y)
            if value != 0:
                if value not in available:
                    return False
                else:
                    available.remove(value)
    for x in range(width):
        available = options(width)
        for y in range(height):
            value = get(board, width, x, y)
            if value != 0:
                if value not in available:
                    return False
                else:
                    available.remove(value)
    horizontally, vertically = sector_size(board)
    for horizontal in range(horizontally):
        for vertical in range(vertically):
            columns = math.floor(width / horizontally)
            rows = math.floor(height / vertically)
            available = options(width)
            for x in range(columns):
                for y in range(rows):
                    value = get(board, width, horizontal * columns + x, vertical * rows + y)
                    if value != 0:
                        if value not in available:
                            return False
                        else:
                            available.remove(value)
    return True
