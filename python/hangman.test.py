#
# Hangman Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import unittest
from io import StringIO
from unittest.mock import patch

import hangman as h


class TestHangman(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_menu(self, mock_stdout):
        h.print_menu()
        actual = mock_stdout.getvalue()

        self.assertGreater(len(actual), 0)

    @patch('builtins.input', side_effect=['N'])
    def test_get_menu_choice_new_game(self, mock_input):
        expected = 1
        actual = h.get_menu_choice()

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['Q'])
    def test_get_menu_choice_quit(self, mock_input):
        expected = 0
        actual = h.get_menu_choice()

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['$', '$', 'Q'])
    def test_get_menu_choice_invalid(self, mock_input):
        expected = 0
        actual = h.get_menu_choice()

        self.assertEqual(expected, actual)

    def __call_print_hangman(self, mock_stdout, misses):
        h.print_hangman(misses)
        actual = mock_stdout.getvalue()
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        return actual

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_hangman(self, mock_stdout):
        actual = [self.__call_print_hangman(i) for i in range(0, 7)]

        for a in actual:
            self.assertGreater(len(a), 0)

        self.assertEqual(len(set(actual)), len(actual), 
            'Output did not differ for each print_hangman call.')

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_guesses(self, mock_stdout):
        expected = ['A', 'B', 'C']
        h.print_guesses({'A', 'B', 'C'})
        actual = mock_stdout.getvalue()

        for e in expected:
            self.assertIn(e, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_guesses_empty(self, mock_stdout):
        h.print_guesses({})
        actual = mock_stdout.getvalue()

        self.assertEqual(len(mock_stdout), 0)

    def __call_print_result(self, mock_stdout, result):
        h.print_result(result)
        actual = mock_stdout.getvalue()
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        return actual

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_result(self, mock_stdout):
        actual = []
        actual.append(self.__call_print_result(mock_stdout, 1))
        actual.append(self.__call_print_result(mock_stdout, 2))

        self.assertGreater(len(actual[0]), 0)
        self.assertGreater(len(actual[1]), 0)
        self.assertEqual(len(set(actual)), len(actual),
                         'Output did not differ for each result code.')

    @patch('builtins.input', side_effect=['D'])
    def test_get_guess(self, mock_input):
        actual = h.get_guess({'A', 'B', 'C'})

        self.assertEqual('D', actual)

    @patch('builtins.input', side_effect=['d'])
    def test_get_guess_lower(self, mock_input):
        actual = h.get_guess({'A', 'B', 'C'})

        self.assertEqual('D', actual)

    @patch('builtins.input', side_effect=['$', '1', 'd'])
    def test_get_guess_invalid(self, mock_input):
        actual = h.get_guess({'A', 'B', 'C'})

        self.assertEqual('D', actual)

    @patch('builtins.input', side_effect=['A', 'B', 'C', 'D'])
    def test_get_guess_repeated(self, mock_input):
        actual = h.get_guess({'A', 'B', 'C'})

        self.assertEqual('D', actual)

    @patch('builtins.input', side_effect=['a', 'b', 'c', 'd'])
    def test_get_guess_repeated_lower(self, mock_input):
        actual = h.get_guess({'A', 'B', 'C'})

        self.assertEqual('D', actual)

    @patch('builtins.input', side_effect=['A'])
    def test_get_guess_empty(self, mock_input):
        actual = h.get_guess(set())

        self.assertEqual('A', actual)

    def test_add_guess(self):
        actual = {'A', 'B', 'C'}
        h.add_guess(actual, 'D')

        self.assertEqual(len(actual), 4)
        self.assertIn('D', actual)

    def test_add_guess_empty(self):
        actual = set()
        h.add_guess(actual, 'A')

        self.assertEqual(len(actual), 1)
        self.assertIn('A', actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_partial_secret(self, mock_stdout):
        h.print_partial_secret({'C', 'A', 'B'}, "CAT")
        actual = mock_stdout.getvalue()

        self.assertEqual(actual.count("C"), 1)
        self.assertEqual(actual.count("A"), 1)
        self.assertEqual(actual.count("_"), 1)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_partial_secret_empty(self, mock_stdout):
        h.print_partial_secret({}, "CAT")
        actual = mock_stdout.getvalue()

        self.assertEqual(actual.count("_"), 3)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_partial_repeated_chars(self, mock_stdout):
        h.print_partial_secret({'D', 'O', 'A'}, "BALLOON")
        actual = mock_stdout.getvalue()

        self.assertEqual(actual.count("O"), 2)
        self.assertEqual(actual.count("A"), 1)
        self.assertEqual(actual.count("_"), 4)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_partial_secret_spaces(self, mock_stdout):
        h.print_partial_secret({'T', 'H', 'B'}, "THIS HAS SPACES")
        actual = mock_stdout.getvalue()

        self.assertEqual(actual.count(" "), 2)

    @patch('builtins.input', side_effect=['CAT'])
    def test_get_secret(self, mock_input):
        expected = "CAT"
        actual = h.get_secret()

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["cat"])
    def test_get_secret_lower(self, mock_input):
        expected = "CAT"
        actual = h.get_secret()

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["123", "CAT"])
    def test_get_secret_invalid(self, mock_input):
        expected = "CAT"
        actual = h.get_secret()

        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["THIS HAS SPACES"])
    def test_get_secret_spaces(self, mock_input):
        expected = "THIS HAS SPACES"
        actual = h.get_secret()

        self.assertEqual(expected, actual)

    def test_check_guess(self):
        actual = h.check_guess("CAT", "A")

        self.assertTrue(actual)

    def test_check_guess_false(self):
        actual = h.check_guess("CAT", "B")

        self.assertFalse(actual)

    def test_check_for_win(self):
        actual = h.check_for_win({'A', 'B', 'C', 'T'}, "CAT", 1)

        self.assertEqual(actual, 1)

    def test_check_for_win_last_turn(self):
        actual = h.check_for_win({'C', 'B', 'A', 'T', 'Q', 'W', 'I', 'O'}, "CAT", 6)

        self.assertEqual(actual, 1)

    def test_check_for_win_in_progress(self):
        actual = h.check_for_win({'A', 'B', 'C', 'I'}, "CAT", 2)

        self.assertEqual(actual, 0)

    def test_check_for_win_game_over(self):
        actual = h.check_for_win({'Q', 'W', 'E', 'R', 'Y', 'U'}, "CAT", 6)

        self.assertEqual(actual, 2)


if __name__ == '__main__':
    unittest.main()
