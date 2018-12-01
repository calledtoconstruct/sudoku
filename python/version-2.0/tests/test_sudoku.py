import pytest
import random

from sudoku import size, evaluate

def test_given_board_with_sixteen_entries_when_calculating_size_width_and_height_are_four():
    board = [
        0, 0,  0, 0,
        0, 0,  0, 0,
        
        0, 0,  0, 0,
        0, 0,  0, 0
    ]
    width, height = size(board)
    assert(width == 4)
    assert(height == 4)

def test_given_board_with_thirty_six_entries_when_calculating_size_width_and_height_are_six():
    board = [
        0, 0, 0,  0, 0, 0,
        0, 0, 0,  0, 0, 0,
        
        0, 0, 0,  0, 0, 0,
        0, 0, 0,  0, 0, 0,
        
        0, 0, 0,  0, 0, 0,
        0, 0, 0,  0, 0, 0
    ]
    width, height = size(board)
    assert(width == 6)
    assert(height == 6)

def test_given_nonempty_cell_when_evaluating_then_the_existing_value_is_returned():
    board = [
        1, 0,  0, 0,
        0, 0,  0, 0,
        
        0, 0,  0, 0,
        0, 0,  0, 0
    ]
    result = evaluate(board, 0, 0)
    assert(result == 1)

def test_given_nonempty_cell_when_evaluating_then_the_existing_random_value_is_returned():
    value = random.randint(2, 4)
    board = [
        value, 0,  0, 0,
        0, 0,  0, 0,
        
        0, 0,  0, 0,
        0, 0,  0, 0
    ]
    result = evaluate(board, 0, 0)
    assert(result == value)

def test_given_nonempty_cell_when_evaluating_arbitrary_size_board_then_the_existing_random_value_is_returned():
    value = random.randint(2, 4)
    board = [
        0, 0, 0,  0, 0, 0,
        0, 0, 0,  0, 0, 0,
        
        0, 0, 0,  0, 0, 0,
        0, 0, 0,  0, 0, 0,
        
        0, 0, 0,  0, 0, 0,
        0, 0, 0,  0, 0, value
    ]
    result = evaluate(board, 5, 5)
    assert(result == value)

def test_given_empty_cell_and_all_value_known_horizontally_when_evaluating_then_missing_value_is_returned():
    board = [
        0, 2,  3, 4,
        0, 0,  0, 0,
        
        0, 0,  0, 0,
        0, 0,  0, 0
    ]
    result = evaluate(board, 0, 0)
    assert(result == 1)
