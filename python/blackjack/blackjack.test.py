#
# Blackjack Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import unittest
from io import StringIO
from unittest.mock import Mock, patch

from hand import Hand
from card import Card
import blackjack as b

class TestBlackjack(unittest.TestCase):

    @patch('builtins.input', side_effect=['500'])
    def test_get_bet(self, mock_input):
        actual = b.get_bet(1000)

        self.assertEqual(actual, 500)

    @patch('builtins.input', side_effect=['$', '500'])
    def test_get_bet_invalid(self, mock_input):
        actual = b.get_bet(1000)

        self.assertEqual(actual, 500)

    @patch('builtins.input', side_effect=['-500', '200'])
    def test_get_bet_negative(self):
        actual = b.get_bet(1000)

        self.assertEqual(actual, 200)

    @patch('builtins.input', side_effect=['500', '200'])
    def test_get_bet_insufficient_balance(self):
        actual = b.get_bet(200)

        self.assertEqual(actual, 200)

    def test_add_to_balance(self):
        actual = b.add_to_balance(100, 200)

        self.assertEqual(actual, 300)

    def test_subtract_from_balance(self):
        actual = b.subtract_from_balance(1000, 200)

        self.assertEqual(actual, 800)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_balance(self, mock_stdout):
        b.print_balance(500)
        actual = mock_stdout.getvalue()

        self.assertIn("500", actual)

    def __setup_hand_mock(self, total):
        hand = Mock()
        hand.get_total_value.return_value = total
        return hand

    def test_check_for_win(self):
        player = self.__setup_hand_mock(18)
        dealer = self.__setup_hand_mock(17)
        actual = b.check_for_win(player, dealer)

        self.assertTrue(actual)

    def test_check_for_win_dealer(self, player_mock, dealer_mock):
        player = self.__setup_hand_mock(18)
        dealer = self.__setup_hand_mock(19)
        actual = b.check_for_win(player, dealer)

        self.assertFalse(actual)

    def test_check_for_win_tie(self, player_mock, dealer_mock):
        player = self.__setup_hand_mock(18)
        dealer = self.__setup_hand_mock(18)
        actual = b.check_for_win(player, dealer)

        self.assertFalse(actual)

    def test_check_for_win_bust(self, player_mock, dealer_mock):
        player = self.__setup_hand_mock(22)
        dealer = self.__setup_hand_mock(22)
        actual = b.check_for_win(player, dealer)

        self.assertFalse(actual)

    def test_check_for_win_dealer_bust(self, player_mock, dealer_mock):
        player = self.__setup_hand_mock(18)
        dealer = self.__setup_hand_mock(22)
        actual = b.check_for_win(player, dealer)

        self.assertTrue(actual)

    def test_check_for_win_blackjack(self, player_mock, dealer_mock):
        player = self.__setup_hand_mock(21)
        dealer = self.__setup_hand_mock(21)
        actual = b.check_for_win(player, dealer)

        self.assertTrue(actual)

    def test_check_for_bankruptcy_positive(self):
        actual = b.check_for_bankruptcy(1000)

        self.assertFalse(actual)

    def test_check_for_bankruptcy_zero(self):
        actual = b.check_for_bankruptcy(0)

        self.assertTrue(actual)

    @patch('builtins.input', side_effect=['H'])
    def test_get_hit_choice_hit(self):
        actual = b.get_hit_choice()

        self.assertTrue(actual)

    @patch('builtins.input', side_effect=['P'])
    def test_get_hit_choice_pass(self):
        actual = b.get_hit_choice()

        self.assertFalse(actual)

    @patch('builtins.input', side_effect=['$', 'Z', 'H'])
    def test_get_hit_choice_invalid(self):
        actual = b.get_hit_choice()

        self.assertTrue(actual)

    @patch('blackjack.get_hit_choice', side_effect=[True, False])
    @patch('hand.Hand.get_total_value', side_effect=[16])
    @patch('hand.Hand.add_card')
    def test_run_player_hand(self, mock_hit, mock_total, mock_add):
        b.run_player_hand(Hand())

        self.assertEqual(mock_hit.call_count, 2)
        self.assertEqual(mock_add.call_count, 1)

    @patch('blackjack.get_hit_choice', side_effect=[True, True])
    @patch('hand.Hand.get_total_value', side_effect=[16, 25])
    @patch('hand.Hand.add_card')
    def test_run_player_hand_bust(self, mock_hit, mock_total, mock_add):
        b.run_player_hand(Hand())

        self.assertEqual(mock_hit.call_count, 2)
        self.assertEqual(mock_add.call_count, 2)

    @patch('hand.Hand.get_total_value', side_effect=[8, 13, 20])
    @patch('hand.Hand.add_card')
    def test_run_dealer_hand(self, mock_total, mock_add):
        b.run_dealer_hand(Hand())

        self.assertEqual(mock_add.call_count, 2)

    @patch('hand.Hand.get_total_value', side_effect=[17])
    @patch('hand.Hand.add_card')
    def test_run_dealer_hand_pass(self, mock_total, mock_add):
        b.run_dealer_hand(Hand())

        self.assertFalse(mock_add.called)

    @patch('hand.Hand.get_total_value', side_effect=[15, 25])
    @patch('hand.Hand.add_card')
    def test_run_dealer_hand_bust(self, mock_total, mock_add):
        b.run_dealer_hand(Hand())

        self.assertEqual(mock_add.call_count, 1)


if __name__ == '__main__':
    unittest.main()
