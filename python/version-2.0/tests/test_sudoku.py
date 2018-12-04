import pytest
import random

from sudoku import size, evaluate, get, play, sector_size, guess, verify

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
    width, height = size(board)
    result = evaluate(board, width, height, 0, 0)
    assert(result == 1)

def test_given_nonempty_cell_when_evaluating_then_the_existing_random_value_is_returned():
    value = random.randint(2, 4)
    board = [
        value, 0,  0, 0,
        0, 0,  0, 0,
        
        0, 0,  0, 0,
        0, 0,  0, 0
    ]
    width, height = size(board)
    result = evaluate(board, width, height, 0, 0)
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
    width, height = size(board)
    result = evaluate(board, width, height, 5, 5)
    assert(result == value)

def test_given_empty_cell_and_all_value_known_horizontally_when_evaluating_then_missing_value_is_returned():
    board = [
        0, 2,  3, 4,
        0, 0,  0, 0,
        
        0, 0,  0, 0,
        0, 0,  0, 0
    ]
    width, height = size(board)
    result = evaluate(board, width, height, 0, 0)
    assert(result == 1)

def test_given_empty_cell_and_all_value_known_vertically_when_evaluating_then_missing_value_is_returned():
    board = [
        0, 0,  0, 0,
        2, 0,  0, 0,
        
        3, 0,  0, 0,
        1, 0,  0, 0
    ]
    width, height = size(board)
    result = evaluate(board, width, height, 0, 0)
    assert(result == 4)

def test_given_empty_cell_and_all_value_known_within_sector_when_evaluating_then_missing_value_is_returned():
    board = [
        0, 3,  0, 0,
        4, 1,  0, 0,
        
        0, 0,  0, 0,
        0, 0,  0, 0
    ]
    width, height = size(board)
    result = evaluate(board, width, height, 0, 0)
    assert(result == 2)

def test_given_empty_cell_and_all_values_known_within_sector_when_evaluating_arbitrary_size_board_then_missing_value_is_returned():
    board = [
        1, 5, 6,  0, 0, 0,
        2, 4, 0,  0, 0, 0,
        
        0, 0, 0,  0, 0, 0,
        0, 0, 0,  0, 0, 0,
        
        0, 0, 0,  0, 0, 0,
        0, 0, 0,  0, 0, 0
    ]
    width, height = size(board)
    result = evaluate(board, width, height, 2, 1)
    assert(result == 3)

def test_given_empty_cell_and_all_values_known_across_down_and_in_sector_when_evaluating_then_missing_value_is_returned():
    board = [
        4, 0, 6,  0, 0, 0,
        0, 0, 0,  5, 2, 0,
        
        0, 0, 0,  0, 0, 0,
        0, 0, 0,  0, 0, 0,
        
        0, 0, 0,  0, 0, 0,
        0, 0, 1,  0, 0, 0
    ]
    width, height = size(board)
    result = evaluate(board, width, height, 2, 1)
    assert(result == 3)

def test_given_empty_cell_and_all_values_known_across_down_and_in_sector_when_playing_then_missing_value_is_set():
    board = [
        4, 0, 6,  0, 0, 0,
        0, 0, 0,  5, 2, 0,
        
        0, 0, 0,  0, 0, 0,
        0, 0, 0,  0, 0, 0,
        
        0, 0, 0,  0, 0, 0,
        0, 0, 1,  0, 0, 0
    ]
    width, height = size(board)
    play(board, width, height, 2, 1)
    result = get(board, width, 2, 1)
    assert(result == 3)

def test_given_empty_cell_where_almost_all_options_are_taken_when_evaluating_then_missing_value_is_returned():
    board = [
        4, 0, 6,  0, 1, 0,
        0, 0, 0,  5, 0, 0,
        
        0, 0, 0,  0, 3, 0,
        0, 0, 0,  0, 4, 0,
        
        0, 0, 0,  0, 5, 0,
        0, 0, 1,  0, 6, 0
    ]
    width, height = size(board)
    play(board, width, height, 2, 1)
    result = get(board, width, 2, 1)
    assert(result == 3)

def test_given_board_with_nine_by_nine_when_calculate_sector_size_then_three_by_three_is_returned():
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
    horizontally, vertically = sector_size(board)
    assert(horizontally == 3)
    assert(vertically == 3)

def test_given_empty_cell_where_only_one_option_remains_after_scanning_sector_then_that_option_is_returned():
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
    width, height = size(board)
    result = evaluate(board, width, height, 8, 4)
    assert(result == 1)

played = False
played_board = []

def mock_play_returns_true_then_false(board, width, height, x, y, ignore = []):
    global played
    global played_board
    was_played = played
    played = True
    played_board = board
    if not was_played:
        return True
    return False

def test_given_empty_cell_that_requires_a_guess_when_guessing_then_the_first_option_is_selected_and_play_is_called():
    global played
    global played_board
    board = [
        0, 0,  1, 0,
        2, 0,  0, 0,
        
        3, 0,  0, 0,
        1, 0,  0, 0
    ]
    width, height = size(board)
    guess(board, width, height, 1, 0, mock_play_returns_true_then_false)
    assert(played == True)
    result = get(played_board, width, 1, 0)
    assert(result == 3)

    played = False
    played_board = []
    board = [
        0, 0,  3, 0,
        2, 0,  0, 0,
        
        3, 0,  0, 0,
        1, 0,  0, 0
    ]
    width, height = size(board)
    guess(board, width, height, 1, 0, mock_play_returns_true_then_false)
    assert(played == True)
    result = get(played_board, width, 1, 0)
    assert(result == 1)

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

def test_given_empty_cell_that_requires_a_guess_when_guessing_recursively_then_play_fills_in_addition_cells():
    board = [
        0, 0,  0, 2,
        2, 0,  0, 0,
        
        3, 2,  0, 1,
        1, 4,  0, 0
    ]
    width, height = size(board)
    copy_of_board = guess(board, width, height, 1, 0, play)
    print_board(copy_of_board, width, height)
    result = get(copy_of_board, width, 1, 1)
    assert(result == 3)

def test_given_an_invalid_row_on_a_partially_complete_board_when_verifying_then_false_is_returned():
    board = [
        2, 3,  4, 2,
        0, 0,  0, 0,
        
        3, 2,  1, 4,
        1, 0,  0, 0
    ]
    width, height = size(board)
    result = verify(board, width, height)
    assert(result == False)

def test_given_an_invalid_column_on_a_partially_complete_board_when_verifying_then_false_is_returned():
    board = [
        2, 1,  4, 3,
        1, 0,  0, 0,
        
        3, 2,  1, 4,
        2, 0,  0, 0
    ]
    width, height = size(board)
    result = verify(board, width, height)
    assert(result == False)

# Plans:
#   Test board verification method to ensure that it catches
# 
#   1) when a row contains a number more than once.
#   2) when a column contains a number more than once.
#   3) when a sector contains a number more than once.