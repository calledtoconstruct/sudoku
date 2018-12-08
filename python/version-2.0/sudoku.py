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

option_cache = {}

def options(width):
    global option_cache
    if width in option_cache:
        return option_cache.get(width).copy()
    options = []
    for x in range(width):
        options.append(x + 1)
    option_cache[width] = options.copy()
    return options

def get(board, width, x, y):
    return board[y * width + x]

def row_allows(board, width, y):
    available = options(width)
    for x in range(width):
        value = get(board, width, x, y)
        if value != 0:
            available.remove(value)
    return available

def column_allows(board, width, x):
    available = options(width)
    for y in range(width):
        value = get(board, width, x, y)
        if value != 0:
            available.remove(value)
    return available

def scan_sector(board, width, height, x, y, action, available):
    horizontally, vertically = sector_size(board)
    cells_horizontally = math.floor(width / horizontally)
    a = math.floor(x / cells_horizontally) * cells_horizontally
    cells_vertically = math.floor(height / vertically)
    b = math.floor(y / cells_vertically) * cells_vertically
    for vertical_index in range(b, b + cells_vertically):
        for horizontal_index in range(a, a + cells_horizontally):
            if horizontal_index != x or vertical_index != y:
                action(board, width, height, horizontal_index, vertical_index, available)

def sector_allows(board, width, height, x, y):
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

    row = row_allows(board, width, y)
    column = column_allows(board, width, x)
    sector = sector_allows(board, width, height, x, y)

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

def play(board, width, height, x, y, ignore_list = [], recurse = True):
    if get(board, width, x, y) != 0:
        return False
    ignore_list.append([x, y])
    changes_were_made = False
    updated = True
    while updated:
        updated = False
        ignore = ignore_list.copy()
        value = evaluate(board, width, height, x, y)
        if value != 0:
            set(board, width, x, y, value)
            return True
        if recurse:
            for index in range(width):
                if [index, y] not in ignore:
                    if play(board, width, height, index, y, ignore, False):
                        updated = True
                        changes_were_made = True
                if [x, index] not in ignore:
                    if play(board, width, height, x, index, ignore, False):
                        updated = True
                        changes_were_made = True
    return changes_were_made

def complete(board, width, height):
    for y in range(height):
        for x in range(width):
            value = get(board, width, x, y)
            if value == 0:
                return False
    return True

def fill(board, width, height, guess_action, fill_action, play_action):
    updated = True
    guess = False
    while updated:
        updated = False
        guess = False
        for y in range(height):
            for x in range(width):
                value = get(board, width, x, y)
                if value == 0:
                    if play_action(board, width, height, x, y):
                        updated = True
                    elif type(guess) is bool:
                        guess = [x, y]
    if complete(board, width, height):
        return board
    result = guess_action(board, width, height, guess[0], guess[1], guess_action, fill_action, play_action)
    if type(result) is list:
        return result
    return False

def guess(board, width, height, x, y, guess_action, fill_action, play_action, ignore = []):
    available = evaluate(board, width, height, x, y, True)
    print('at', x, ',', y, 'found options', available)
    for option in available:
        print('at', x, ',', y, 'guessing', option)
        copy_of_board = board.copy()
        set(copy_of_board, width, x, y, option)
        result = fill_action(copy_of_board, width, height, guess_action, fill_action, play_action)
        if type(result) is list:
            return result
    return False

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
