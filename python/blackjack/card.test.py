#
# Blackjack - Card Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import unittest
from io import StringIO
from unittest.mock import patch

from card import Card


class TestCard(unittest.TestCase):

    def test_init_random_card(self):
        actual = { Card() for _ in range(10) }

        self.assertGreater(len(actual), 1, 
            'Card is likely not initializing random results.')

    def test_eq(self):
        first = Card()
        other = Card()

        first.suit = "Hearts"
        first.value = 1
        other.suit = "Hearts"
        other.value = 1

        self.assertTrue(first == other)

    def test_ne(self):
        first = Card()
        other = Card()

        first.suit = "Hearts"
        first.value = 1
        other.suit = "Spades"
        other.value = 2

        self.assertFalse(first == other)

    def test_get_card_value(self):
        actual = Card()

        actual.value = 5

        self.assertEqual(5, actual.get_card_value())

    def test_get_card_value_ace(self):
        actual = Card()

        actual.value = 1

        self.assertEqual(11, actual.get_card_value())

    def test_get_card_value_face(self):
        actual0 = Card()
        actual1 = Card()
        actual2 = Card()

        actual0.value = 11
        actual1.value = 12
        actual2.value = 13

        self.assertEqual(10, actual0.get_card_value())
        self.assertEqual(10, actual1.get_card_value())
        self.assertEqual(10, actual2.get_card_value())

    def __call_print_card(self, mock_stdout, card):
        card.print_card()
        actual = mock_stdout.getvalue()
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        return actual

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_card(self, mock_stdout):
        card = Card()

        card.suit = "Hearts"
        card.value = 5

        actual = self.__call_print_card(mock_stdout, card)

        self.assertIn("5", actual)
        self.assertIn("♥", actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_card_face(self, mock_stdout):
        cards = [Card(), Card(), Card(), Card()]

        cards[0].value = 1
        cards[1].value = 11
        cards[2].value = 12
        cards[3].value = 13

        actual = [self.__call_print_card(mock_stdout, c) for c in cards]

        self.assertIn("A", actual[0])
        self.assertIn("J", actual[1])
        self.assertIn("Q", actual[2])
        self.assertIn("K", actual[3])


if __name__ == '__main__':
    unittest.main()
