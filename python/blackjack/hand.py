#
# Blackjack - Hand class
#
# Python tutoring exercise.
# Sean Midford, 2020
#
from random import randint
from card import Card

class Hand:
    """
    Hand of cards.
    """

    def __init__(self):
        """This function initializes a new hand with two random cards.
        """
        self.hand = [Card(), Card()]

    def add_card(self):
        """This function gets a new random card and adds it to the player's hand.

        Hint: Use the get_card() function to pick the random card.

        Parameters
        -------
        hand : List[(int, str)]
            The player's hand, represented as a list of tuples.
        """
        pass

    def get_total_value(self) -> int:
        """This function gets the total value of all card in the hand.

        Returns
        -------
        int
            The total value of all cards in the hand.
        """
        pass

    def print_hand(self, dealer: bool = False):
        """This function prints out each card in the hand. If the dealer argument is set to true,
        then only the first card is printed out.

        Parameters
        -------
        dealer : bool
            Whether this is a dealer hand or player hand.
        """
        pass
