#
# Blackjack - Hand Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import unittest
from io import StringIO
from unittest.mock import patch

from card import Card
from hand import Hand


class TestHand(unittest.TestCase):

    def test_init_hand(self):
        actual = Hand()

        self.assertEqual(len(actual.hand), 2)

    def test_add_card(self):
        actual = Hand()

        actual.add_card()
        actual.add_card()

        self.assertEqual(len(actual.hand), 4)

    @patch('card.Card.get_card_value', return_value=4)
    def test_get_total_value(self, mock_card):
        actual = Hand()

        self.assertEqual(actual.get_total_value(), 8)

    @patch('card.Card.print_card')
    def test_print_hand(self, mock_card):
        actual = Hand()

        actual.print_hand()

        self.assertEqual(mock_card.call_count, 2)

    @patch('card.Card.print_card')
    def test_print_dealer_hand(self, mock_card):
        actual = Hand()

        actual.print_hand(dealer = True)

        self.assertEqual(mock_card.call_count, 1)


if __name__ == '__main__':
    unittest.main()
