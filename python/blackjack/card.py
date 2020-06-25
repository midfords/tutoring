#
# Blackjack - Card class
#
# Python tutoring exercise.
# Sean Midford, 2020
#
from random import randint

class Card:
    """
    Single card.
    """

    def __init__(self):
        """This function initializes a new card with a random value and a random suit.
        """
        self.value = self.__get_random_value()
        self.suit = self.__get_random_suit()

    def __eq__(self, other):
        """Check for equality by comparing the value and suit.
        """
        return isinstance(other, Card) \
            and self.suit == other.suit \
            and self.value == other.value

    def __hash__(self):
        """Ensure equal objects hash consistently.
        """
        return hash( (self.suit, self.value) )

    def __get_random_value(self) -> int:
        """This function gets a random value and returns an int representing it. 
        The function can return numbers in the range [1, 13] (representing Ace through King).

        Returns
        -------
        int
            The random value, represented as an integer.
        """
        pass

    def __get_random_suit(self) -> str:
        """This function gets a random suit and returns a string representing the suit. 
        The function can return "Hearts", "Diamonds", "Clubs" or "Spades".

        Returns
        -------
        str
            The random suit, represented as a string.
        """
        pass

    def get_card_value(self):
        """This function returns the value of the card. The function can return numbers 
        in the range [1, 10] (11, 12, 13 represent Jack, Queen and King, and are returned as
        the value 10).

        Returns
        -------
        int
            The card value, represented as an integer in the range [1, 10].
        """
        pass

    def print_card(self):
        """This function prints out the card including value and suit.
        The suit should be printed as a unicode character ( ♠ ♥ ♦ ♣ ).
        """
        pass
