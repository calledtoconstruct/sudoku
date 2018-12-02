
from sudoku import size, evaluate, get, play

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

def missing_numbers(board, width, height):
    count = 0
    for y in range(height):
        for x in range(width):
            value = get(board, width, x, y)
            if value == 0:
                count += 1
    return count

def print_board(board, width, height):
    print('---------------------------')
    for y in range(height):
        line = ''
        for x in range(width):
            value = get(board, width, x, y)
            for space in range(len(str(width)) - len(str(value))):
                line += ' '
            line += ' '
            line += str(value)
        print(line)

board = medium
width, height = size(board)
missing = missing_numbers(board, width, height)
updated = True

print_board(board, width, height)

iterations = 0

while updated and missing > 0:
    iterations += 1
    updated = False
    for y in range(height):
        for x in range(width):
            value = get(board, width, x, y)
            if value == 0:
                if play(board, width, height, x, y):
                    updated = True
    missing = missing_numbers(board, width, height)

print_board(board, width, height)

if missing == 0:
    print('SOLVED! in', iterations, 'iterations.')
else:
    print('Gave up after', iterations, 'iterations.')