import pytest
import logging
from sudoku import evaluate

logging.basicConfig(level=logging.INFO)

def test_given_cell_is_already_filled_when_evaluating_then_known_is_returned():
    board = [1, 2,  3, 4,  4, 3,  2, 1]
    result, value = evaluate(board, 1, 1)
    assert(result == 'known')
    assert(value == 3)

def test_given_cell_is_empty_and_only_one_option_exists_horizontally_then_valid_is_returned():
    board = [0, 2,  3, 4,  4, 3,  2, 1]
    result, value = evaluate(board, 0, 0)
    assert(result == 'valid')
    assert(value == 1)
