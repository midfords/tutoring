#
# Mastermind Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import unittest
from io import StringIO
from unittest.mock import patch

import mastermind as m

class TestMastermind(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_welcome(self, mock_stdout):
        m.print_welcome()
        actual = mock_stdout.getvalue()

        self.assertGreater(len(actual), 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_colours_menu(self, mock_stdout):
        m.print_colours_menu()
        actual = mock_stdout.getvalue()

        self.assertGreater(len(actual), 0)

        for i in range(1, 9):
            self.assertIn(str(i), actual)

        self.assertIn("\x1b[32m", actual)
        self.assertIn("\x1b[31m", actual)
        self.assertIn("\x1b[34m", actual)
        self.assertIn("\x1b[33m", actual)
        self.assertIn("\x1b[35m", actual)
        self.assertIn("\x1b[36m", actual)
        self.assertIn("\x1b[30m", actual)
        self.assertIn("\x1b[37m", actual)

    def __call_print_final_result(self, mock_stdout, result):
        m.print_final_result(result)
        actual = mock_stdout.getvalue()
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        return actual

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_final_result(self, mock_stdout):
        actual = []
        actual.append(self.__call_print_final_result(mock_stdout, 1))
        actual.append(self.__call_print_final_result(mock_stdout, 2))

        self.assertGreater(len(actual[0]), 0)
        self.assertGreater(len(actual[1]), 0)
        self.assertEqual(len(set(actual)), len(actual), 
            'Output did not differ for each final result code.')

    def test_create_secret_len(self):
        actual = m.create_secret()

        self.assertEqual(len(actual), 4)

    def test_create_secret_range(self):
        actual = m.create_secret()

        for e in actual:
            self.assertGreater(e, 0)
            self.assertLess(e, 9)

    def test_create_secret_random(self):
        actual = [ m.create_secret() for _ in range(10) ]

        self.assertGreater(len(set(actual)), 1, 
            'Create secret is likely not returning random results.')

    @patch('builtins.input', side_effect=['1', '2', '3', '4'])
    def test_get_guess(self, mock_input):
        expected = (1, 2, 3, 4)
        actual = m.get_guess()

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['9', '1', '2', '0', '3', '3'])
    def test_get_guess_out_of_range(self, mock_input):
        expected = (1, 2, 3, 3)
        actual = m.get_guess()

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['$', '5', '6', '$', '7', '8'])
    def test_get_guess_invalid(self, mock_input):
        expected = (5, 6, 7, 8)
        actual = m.get_guess()

        self.assertEqual(expected, actual)

    def test_check_for_win(self):
        expected = 1
        actual = m.check_for_win((1, 2, 3, 4), (1, 2, 3 ,4), 2)
        
        self.assertEqual(expected, actual)

    def test_check_for_win_last_turn(self):
        expected = 1
        actual = m.check_for_win((1, 2, 3, 4), (1, 2, 3 ,4), 10)
        
        self.assertEqual(expected, actual)

    def test_check_for_win_game_over(self):
        expected = 2
        actual = m.check_for_win((1, 2, 3, 4), (4, 3, 2 ,1), 10)
        
        self.assertEqual(expected, actual)

    def test_check_for_win_in_progress(self):
        expected = 0
        actual = m.check_for_win((1, 2, 3, 4), (2, 2, 4 ,4), 8)
        
        self.assertEqual(expected, actual)

    def __call_print_guess(self, mock_stdout, guess):
        m.print_guess(guess)
        actual = mock_stdout.getvalue()
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        return actual

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_guess(self, mock_stdout):
        actual = []
        actual.append(self.__call_print_guess(mock_stdout, (1, 2, 3, 4)))
        actual.append(self.__call_print_guess(mock_stdout, (5, 6, 7, 8)))

        self.assertGreater(len(actual[0]), 0)
        self.assertIn("\x1b[31m", actual[0])
        self.assertIn("\x1b[32m", actual[0])
        self.assertIn("\x1b[34m", actual[0])
        self.assertIn("\x1b[33m", actual[0])

        self.assertGreater(len(actual[1]), 0)
        self.assertIn("\x1b[35m", actual[1])
        self.assertIn("\x1b[36m", actual[1])
        self.assertIn("\x1b[30m", actual[1])
        self.assertIn("\x1b[37m", actual[1])

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_result(self, mock_stdout):
        m.print_result([0, 1, 1])
        actual = mock_stdout.getvalue()

        self.assertGreater(len(actual), 0)
        self.assertIn("\x1b[30m", actual)
        self.assertIn("\x1b[37m", actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_result_white_only(self, mock_stdout):
        m.print_result([1])
        actual = mock_stdout.getvalue()

        self.assertGreater(len(actual), 0)
        self.assertIn("\x1b[37m", actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_result_empty(self, mock_stdout):
        m.print_result([])
        actual = mock_stdout.getvalue()

        self.assertEqual(len(actual), 0)

    def test_get_result_no_matches(self):
        expected = []
        actual = m.get_result((5, 6, 7, 8), (1, 2, 3, 4))

        self.assertCountEqual(expected, actual)

    def test_get_result_all_match(self):
        expected = [1, 1, 1, 1]
        actual = m.get_result((1, 2, 3, 4), (1, 2, 3, 4))

        self.assertCountEqual(expected, actual)

    def test_get_result_some_match(self):
        expected = [1, 0, 0]
        actual = m.get_result((1, 2, 3, 4), (2, 1, 5, 4))

        self.assertCountEqual(expected, actual)

    def test_get_result_duplicate(self):
        expected = [1]
        actual = m.get_result((1, 2, 3, 4), (2, 2, 5, 6))

        self.assertCountEqual(expected, actual)

    def test_get_result_duplicate_guess(self):
        expected = [1]
        actual = m.get_result((2, 2, 5, 6), (1, 2, 3, 4))

        self.assertCountEqual(expected, actual)


if __name__=='__main__':
    unittest.main()
