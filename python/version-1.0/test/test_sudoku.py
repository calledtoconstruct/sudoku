import pytest
import logging
from sudoku import evaluate, update, size, remaining

logging.basicConfig(level=logging.INFO)

def test_given_cell_is_already_filled_when_evaluating_then_known_is_returned():
    board = [
        1, 2,  3, 4,
        4, 3,  2, 1,

        3, 4,  1, 2,
        2, 1,  4, 3
    ]
    result, value = evaluate(board, 1, 1)
    assert(result == 'known')
    assert(value == 3)

def test_given_cell_is_empty_and_only_one_option_exists_horizontally_when_evaluating_then_valid_is_returned():
    board = [
        0, 2,  3, 4,
        0, 3,  2, 1,

        3, 4,  1, 2,
        2, 1,  4, 3
    ]
    result, value = evaluate(board, 0, 0)
    assert(result == 'valid')
    assert(value == 1)

def test_given_cell_is_empty_and_only_one_option_exists_vertically_when_evaluating_then_valid_is_returned():
    board = [
        0, 0,  3, 4,
        4, 3,  2, 1,

        3, 4,  1, 2,
        2, 1,  4, 3
    ]
    result, value = evaluate(board, 0, 0)
    assert(result == 'valid')
    assert(value == 1)

def test_given_cell_is_empty_and_only_one_option_exists_in_sector_when_evaluating_then_valid_is_returned():
    board = [
        0, 2,  0, 4,
        4, 3,  2, 1,

        0, 4,  1, 2,
        2, 1,  4, 3
    ]
    result, value = evaluate(board, 0, 0)
    assert(result == 'valid')
    assert(value == 1)

def test_given_cell_is_empty_and_multiple_options_exists_when_evaluating_then_unknown_is_returned():
    board = [
        0, 2,  0, 4,
        4, 0,  2, 0,

        0, 4,  1, 2,
        2, 0,  4, 3
    ]
    result, value = evaluate(board, 0, 0)
    assert(result == 'unknown')
    assert(value == [1, 3])

def test_given_cell_is_empty_when_updating_its_value_and_evaluating_then_known_is_returned():
    board = [
        0, 2,  0, 4,
        4, 0,  2, 1,

        0, 4,  1, 2,
        2, 1,  4, 3
    ]
    result, value = evaluate(board, 2, 0)
    assert(result == 'valid')
    assert(value == 3)
    update(board, 2, 0, 3)
    result, value = evaluate(board, 2, 0)
    assert(result == 'known')
    assert(value == 3)

def test_given_arbitrary_board_when_determining_size_then_rows_columns_and_options_are_computed():
    board = [
        1, 2,  3, 4,
        4, 3,  2, 1,

        3, 4,  1, 2,
        2, 1,  4, 3
    ]
    rows, columns, options = size(board)
    assert(rows == 2)
    assert(columns == 2)
    assert(options == 4)
    board = [
        1, 2, 3,  4, 5, 6,
        6, 5, 4,  3, 2, 1,

        3, 4, 5,  6, 1, 2,
        2, 1, 6,  5, 4, 3,

        4, 3, 1,  2, 6, 5,
        5, 6, 2,  1, 3, 4
    ]
    rows, columns, options = size(board)
    assert(rows == 2)
    assert(columns == 3)
    assert(options == 6)
    board = [
        1, 2, 3, 4,  5, 6, 7, 8,
        7, 8, 6, 5,  4, 3, 2, 1,

        3, 4, 5, 6,  1, 2, 8, 7,
        8, 7, 2, 1,  6, 5, 4, 3,

        4, 3, 1, 2,  7, 8, 5, 6,
        5, 6, 7, 8,  3, 4, 1, 2,

        2, 1, 4, 3,  8, 7, 6, 5,
        6, 5, 8, 7,  2, 1, 3, 4
    ]
    rows, columns, options = size(board)
    assert(rows == 2)
    assert(columns == 4)
    assert(options == 8)

def test_given_an_incomplete_board_when_calculating_the_remaining_cells_then_count_is_correct():
    board = [
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
    count = remaining(board)
    assert(count == 43)

def test_given_an_empty_cell_and_one_option_cannot_go_elsewhere_when_evaluating_then_valid_is_returned():
    board = [
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
    result, value = evaluate(board, 8, 4)
    assert(result == 'valid')
    assert(value == 1)
