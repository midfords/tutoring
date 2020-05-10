#
# Tic Tac Toe Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import time
import unittest
from io import StringIO
from unittest.mock import patch

import tic_tac_toe as c

class TestTicTacToe(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_menu(self, mock_stdout):
        c.print_menu()
        actual = mock_stdout.getvalue()

        self.assertGreater(len(actual), 0)

    @patch('builtins.input', side_effect=['N'])
    def test_get_menu_choice_new_game(self, mock_input):
        expected = 1
        actual = c.get_menu_choice()

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Q'])
    def test_get_menu_choice_quit(self, mock_input):
        expected = 0
        actual = c.get_menu_choice()

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['$', 'Q'])
    def test_get_menu_choice_invalid(self, mock_input):
        expected = 0
        actual = c.get_menu_choice()

        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_board(self, mock_stdout):
        c.print_board([["o"," ","o"],["x"," "," "],["x"," "," "]])
        actual = mock_stdout.getvalue()

        self.assertGreater(len(actual), 0)
        self.assertEqual(actual.count("o"), 2)
        self.assertEqual(actual.count("x"), 2)
        self.assertEqual(actual.count(" "), 5)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_board_empty(self, mock_stdout):
        c.print_board([[" "," "," "],[" "," "," "],[" "," "," "]])
        actual = mock_stdout.getvalue()

        self.assertGreater(len(actual), 0)
        self.assertEqual(actual.count(" "), 9)

    def __call_print_result(self, mock_stdout, result):
        c.print_result(result)
        actual = mock_stdout.getvalue()
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        return actual

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_result(self, mock_stdout):
        actual = []
        actual.append(self.__call_print_result(mock_stdout, 1))
        actual.append(self.__call_print_result(mock_stdout, 2))
        actual.append(self.__call_print_result(mock_stdout, 3))

        self.assertGreater(len(actual[0]), 0)
        self.assertGreater(len(actual[1]), 0)
        self.assertGreater(len(actual[2]), 0)
        self.assertEqual(len(set(actual)), len(actual), 
            'Output did not differ for each result code.')

    @patch('builtins.input', side_effect=['0', '1'])
    def test_get_position(self, mock_input):
        expected = (0,1)
        actual = c.get_position([[" "," "," "],[" "," "," "],[" "," "," "]])

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['5', '0', '2'])
    def test_get_position_out_of_range(self, mock_input):
        expected = (0,2)
        actual = c.get_position([[" "," "," "],[" "," "," "],[" "," "," "]])

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['0', '0', '1', '1'])
    def test_get_position_taken(self, mock_input):
        expected = (1,1)
        actual = c.get_position([["o"," "," "],[" "," "," "],[" "," "," "]])

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['$', '1', '2'])
    def test_get_position_invalid(self, mock_input):
        expected = (1,2)
        actual = c.get_position([[" "," "," "],[" "," "," "],[" "," "," "]])

        self.assertEqual(expected, actual)

    def test_put_piece(self):
        expected = [["o"," "," "],[" "," "," "],[" "," "," "]]
        mock_board = [[" "," "," "],[" "," "," "],[" "," "," "]]
        c.put_piece(mock_board, 1, 1, "o")
        
        self.assertEqual(expected, mock_board)

    def test_check_for_win_in_progress(self):
        expected = 0
        actual = c.check_for_win([["o","x","x"],[" ","o"," "],["o"," ","x"]])
        
        self.assertEqual(expected, actual)

    def test_check_for_win_o_win(self):
        expected = 1
        actual = c.check_for_win([["o"," ","x"],["o","o","x"],["o","x"," "]])
        
        self.assertEqual(expected, actual)

    def test_check_for_win_x_win(self):
        expected = 2
        actual = c.check_for_win([["x","x","x"],[" ","o","o"],[" "," ","o"]])
        
        self.assertEqual(expected, actual)

    def test_check_for_win_diagonal(self):
        expected = 1
        actual = c.check_for_win([["o","x"," "],[" ","o","x"],[" ","x","o"]])
        
        self.assertEqual(expected, actual)

    def test_check_for_win_with_full_board(self):
        expected = 1
        actual = c.check_for_win([["x","o","o"],["o","x","o"],["x ","x","o"]])
        
        self.assertEqual(expected, actual)

    def test_check_for_win_tie_game(self):
        expected = 3
        actual = c.check_for_win([["o","x","o"],["x","x","o"],["o","o","x"]])
        
        self.assertEqual(expected, actual)

    def test_create_empty_board(self):
        expected = [[" "," "," "],[" "," "," "],[" "," "," "]]
        actual = c.create_empty_board()

        self.assertEqual(expected, actual)


if __name__=='__main__':
    unittest.main()
