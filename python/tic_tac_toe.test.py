#
# Tic Tac Toe Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import time
import unittest
from unittest.mock import patch

from tic_tac_toe import get_position
from tic_tac_toe import put_piece
from tic_tac_toe import check_for_win
from tic_tac_toe import create_empty_board

class TestTicTacToe(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '2'])
    def test_get_position(self, mock_input):
        expected = (1,2)
        actual = get_position([[" "," "," "],[" "," "," "],[" "," "," "]])

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['5', '1', '3'])
    def test_get_position_out_of_range(self, mock_input):
        expected = (1,3)
        actual = get_position([[" "," "," "],[" "," "," "],[" "," "," "]])

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1', '1', '2', '2'])
    def test_get_position_taken(self, mock_input):
        expected = (2,2)
        actual = get_position([["o"," "," "],[" "," "," "],[" "," "," "]])

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['$', '2', '3'])
    def test_get_position_invalid(self, mock_input):
        expected = (2,3)
        actual = get_position([[" "," "," "],[" "," "," "],[" "," "," "]])

        self.assertEqual(expected, actual)

    def test_put_piece(self):
        expected = [["o"," "," "],[" "," "," "],[" "," "," "]]
        mock_board = [[" "," "," "],[" "," "," "],[" "," "," "]]
        put_piece(mock_board, 1, 1, "o")
        
        self.assertEqual(expected, mock_board)

    def test_check_for_win_in_progress(self):
        expected = 0
        actual = check_for_win([["o","x","x"],[" ","o"," "],["o"," ","x"]])
        
        self.assertEqual(expected, actual)

    def test_check_for_win_o_win(self):
        expected = 1
        actual = check_for_win([["o"," ","x"],["o","o","x"],["o","x"," "]])
        
        self.assertEqual(expected, actual)

    def test_check_for_win_x_win(self):
        expected = 2
        actual = check_for_win([["x","x","x"],[" ","o","o"],[" "," ","o"]])
        
        self.assertEqual(expected, actual)

    def test_check_for_win_diagonal(self):
        expected = 1
        actual = check_for_win([["o","x"," "],[" ","o","x"],[" ","o","x"]])
        
        self.assertEqual(expected, actual)

    def test_check_for_win_with_full_board(self):
        expected = 1
        actual = check_for_win([["x","o","o"],["o","x","o"],["x ","x","o"]])
        
        self.assertEqual(expected, actual)

    def test_check_for_win_tie_game(self):
        expected = 3
        actual = check_for_win([["o","x","o"],["x","x","o"],["o","o","x"]])
        
        self.assertEqual(expected, actual)

    def test_create_empty_board(self):
        expected = [[" "," "," "],[" "," "," "],[" "," "," "]]
        actual = create_empty_board()

        self.assertEqual(expected, actual)


if __name__=='__main__':
    unittest.main()
