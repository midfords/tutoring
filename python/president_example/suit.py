from enum import Enum

class Suit(Enum):
    SPADES = "♠"
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    NONE = " "

    def __str__(self):
        return self.value
