from sudoku import evaluate, update, size, remaining, get

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

board = easy
count = remaining(board)
rows, columns, options = size(board)
attempts = 0
while count > 0:
    attempts += 1
    for y in range(options):
        for x in range(options):
            result, value = evaluate(board, x, y)
            if result == 'valid':
                update(board, x, y, value)
    count = remaining(board)

for y in range(options):
    line = ''
    for x in range(options):
        line = line + str(get(board, x, y))
    print(line)

print(attempts)