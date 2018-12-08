import datetime

from sudoku import size, evaluate, get, play, verify, fill, guess

easy = [
    9, 0, 6,  3, 4, 0,  8, 1, 0,
    0, 5, 1,  7, 0, 0,  3, 0, 0,
    4, 7, 0,  0, 9, 1,  0, 0, 5,

    0, 0, 0,  9, 0, 3,  0, 0, 2,
    0, 0, 2,  0, 8, 7,  0, 0, 0,
    1, 0, 7,  2, 0, 0,  6, 0, 0,

    0, 8, 5,  0, 0, 9,  1, 0, 0,
    0, 3, 4,  0, 6, 0,  0, 0, 9,
    0, 1, 0,  5, 0, 8,  7, 0, 6
]

medium = [
    0, 0, 0,  0, 0, 0,  0, 0, 0,
    0, 0, 4,  3, 2, 8,  0, 0, 0,
    6, 0, 0,  1, 0, 5,  0, 2, 9,

    0, 0, 2,  0, 0, 1,  9, 6, 0,
    4, 9, 0,  0, 0, 0,  0, 7, 1,
    0, 1, 8,  9, 0, 0,  4, 0, 0,

    5, 4, 0,  2, 0, 3,  0, 0, 7,
    0, 0, 0,  6, 1, 7,  8, 0, 0,
    0, 0, 0,  0, 0, 0,  0, 0, 0
]

invalid_medium = [
    4, 0, 0,  0, 0, 0,  0, 0, 0,
    0, 0, 4,  3, 2, 8,  0, 0, 0,
    6, 0, 0,  1, 0, 5,  0, 2, 9,

    0, 0, 2,  0, 0, 1,  9, 6, 0,
    4, 9, 0,  0, 0, 0,  0, 7, 1,
    0, 1, 8,  9, 0, 0,  4, 0, 0,

    5, 4, 0,  2, 0, 3,  0, 0, 7,
    0, 0, 0,  6, 1, 7,  8, 0, 0,
    0, 0, 0,  0, 0, 0,  0, 0, 0
]

hard = [
    0, 0, 0,  2, 4, 7,  0, 0, 0,
    0, 0, 0,  1, 0, 0,  0, 7, 0,
    1, 9, 7,  0, 0, 3,  5, 0, 0,

    0, 0, 0,  0, 0, 1,  0, 0, 3,
    0, 5, 0,  0, 0, 0,  0, 6, 0,
    0, 0, 0,  0, 0, 0,  9, 0, 8,

    6, 0, 5,  0, 0, 0,  0, 0, 4,
    0, 3, 0,  9, 0, 8,  0, 0, 0,
    0, 0, 9,  0, 7, 0,  3, 0, 0,
]

evil = [
    0, 8, 0,  0, 0, 0,  0, 4, 0,
    9, 0, 0,  0, 0, 0,  0, 6, 0,
    0, 0, 0,  0, 1, 0,  0, 0, 0,

    0, 0, 0,  9, 3, 6,  0, 0, 0,
    1, 0, 2,  0, 0, 0,  0, 0, 0,
    7, 0, 0,  0, 0, 0,  0, 0, 0,

    0, 3, 0,  6, 0, 8,  0, 0, 0,
    0, 0, 0,  7, 0, 0,  2, 0, 0,
    0, 0, 0,  0, 0, 0,  1, 0, 0,
]

large = [
     1,  2,  0,  0,   0,  0,  0,  3,   0,  0,  6,  0,
     0,  5,  8,  0,   0,  7,  6,  0,  11,  0,  0,  0,
     0,  0, 12,  4,   0,  0, 10,  0,   0,  9,  0,  0,

     0,  0,  0,  0,   0,  0,  2,  0,   0,  0,  0,  0,
     0, 11,  0,  0,   0,  0,  0,  0,  10,  0,  0,  5,
     0,  7,  4,  0,   0,  0,  0,  0,   0,  0,  8,  0,

    10,  0,  0,  0,   0,  0,  0,  0,   0,  0,  0,  0,
     2,  0,  0,  0,   0,  0,  0,  0,   0,  0,  7,  0,
     0,  3,  9,  8,   0,  0, 12,  0,   4,  0,  5,  6,

     9,  0,  5,  0,   0,  0,  0,  0,   0,  0,  0,  0,
     0,  0,  0,  0,  11,  0,  0,  0,   0, 12,  0,  0,
     6,  0,  0,  0,   0,  0,  8,  0,   2,  0,  0,  7,
]

huge = [
     1,  0,  0,  0,   0,  0,  0,  3,   0,  0,  0,  0,   0,  0,  0, 14,
     0,  0,  0,  8,   0,  7,  0,  0,  14,  0,  0,  0,   0,  0,  5,  0,
     0,  0, 12,  0,   0,  0,  0,  0,   0,  9,  0,  0,  13,  0,  0,  0,
    16,  0,  0,  0,   0,  0, 12,  0,   0,  0,  0,  6,   0,  0,  0,  0,

     0,  0,  0,  0,   0,  0,  2,  0,   0,  0,  0,  0,   0,  0,  0,  0,
     0, 11,  0,  0,   0,  0,  0,  0,  15,  0,  0,  0,   0,  0,  0,  0,
     0,  0,  0,  0,   0,  0,  0,  0,   0,  0,  8,  0,   5,  0, 11,  0,
     0,  0,  7,  4,  15,  0,  0,  9,   0,  0,  0,  0,   0,  0,  0,  0,

    10,  0,  0,  0,   0,  0,  0,  0,   0,  0,  0,  0,   0,  0,  0,  0,
     0,  0,  0,  0,   0,  0,  0,  0,   0,  0,  7,  0,   6,  0,  0,  0,
     0,  3, 13,  0,   0,  0, 15,  0,   4,  0,  0,  0,   0,  0,  0, 10,
     0,  0,  0,  0,   5,  0,  0,  0,   0,  6,  0, 11,   0,  0,  0,  0,

     9,  0,  0,  0,   0,  0,  0,  0,   0,  0,  0,  0,   0, 10,  0,  0,
     0,  0,  0,  0,  11,  0,  0,  0,   0, 12,  0,  0,   2,  0,  0,  0,
     6,  0,  0,  0,   0,  0,  8,  0,   2,  0,  0,  7,   0,  0, 14,  0,
     4,  0,  0, 16,   0,  0,  0,  0,   0,  0,  0,  0,   3,  0,  0,  0,
]

def missing_numbers(board, width, height):
    count = 0
    for y in range(height):
        for x in range(width):
            value = get(board, width, x, y)
            if value == 0:
                count += 1
    return count

def draw(cells, left, between, right):
    return left + between.join(cells) + right
        
def print_board(board, width, height, clues):
    print('SUDOKU puzzle', width, 'x', height, 'with', clues, 'clues')
    value_width = len(str(width))
    cell_width = value_width + 2
    cell_line = '─' * cell_width
    lines = []
    for y in range(height):
        cells = []
        for x in range(width):
            value = get(board, width, x, y)
            padding = value_width - len(str(value))
            cell = ' ' + ' ' * padding + str(value) + ' '
            cells.append(cell)
        lines.append(draw(cells, '│', '│', '│\n'))
    print(
        draw([cell_line] * width, '┌', '┬', '┐\n') +
        draw([cell_line] * width, '├', '┼', '┤\n').join(lines) +
        draw([cell_line] * width, '└', '┴', '┘\n')
    )

board = huge

width, height = size(board)

valid_board = verify(board, width, height)
if not valid_board:
    raise ValueError('Invalid board to begin with.')

missing = missing_numbers(board, width, height)
clues = len(board) - missing
print_board(board, width, height, clues)

start = datetime.datetime.now()

board = fill(board, width, height, guess, fill, play)

end = datetime.datetime.now()
elapsed = end - start

missing = missing_numbers(board, width, height)

print_board(board, width, height, clues)

valid_board = verify(board, width, height)
if not valid_board:
    raise ValueError('Invalid solution.')

if missing == 0:
    print('SOLVED! in', elapsed, 'ms')
else:
    print('Gave up!')