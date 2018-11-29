import pytest
import logging
from sudoku import evaluate, update

logging.basicConfig(level=logging.INFO)

def test_given_cell_is_already_filled_when_evaluating_then_known_is_returned():
    board = [
        1, 2,  3, 4,
        4, 3,  2, 1
    ]
    result, value = evaluate(board, 1, 1)
    assert(result == 'known')
    assert(value == 3)

def test_given_cell_is_empty_and_only_one_option_exists_horizontally_when_evaluating_then_valid_is_returned():
    board = [
        0, 2,  3, 4,
        4, 3,  2, 1
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
        4, 0,  2, 1,

        0, 4,  1, 2,
        2, 1,  4, 3
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
