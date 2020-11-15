from typing import List

from suit import Suit
from value import Value


class Card():

    def __init__(self, suit: Suit, value: Value, comparer):
        self.__comparer = comparer
        self.value = value
        self.suit = suit

    def __eq__(self, other) -> bool:
        return self.__comparer.eq(self, other)

    def __ne__(self, other) -> bool:
        return self.__comparer.ne(self, other)

    def __lt__(self, other) -> bool:
        return self.__comparer.lt(self, other)

    def __le__(self, other) -> bool:
        return self.__comparer.le(self, other)

    def __gt__(self, other) -> bool:
        return self.__comparer.gt(self, other)

    def __ge__(self, other) -> bool:
        return self.__comparer.ge(self, other)


class CardComparer():

    def __init__(self, order: List[Value]):
        self.__order = order

    def eq(self, card: Card, other: Card) -> bool:
        return self.__order.index(card.value) == self.__order.index(other.value)

    def ne(self, card: Card, other: Card) -> bool:
        return self.__order.index(card.value) != self.__order.index(other.value)

    def lt(self, card: Card, other: Card) -> bool:
        return self.__order.index(card.value) < self.__order.index(other.value)

    def le(self, card: Card, other: Card) -> bool:
        return self.__order.index(card.value) <= self.__order.index(other.value)

    def gt(self, card: Card, other: Card) -> bool:
        return self.__order.index(card.value) > self.__order.index(other.value)

    def ge(self, card: Card, other: Card) -> bool:
        return self.__order.index(card.value) >= self.__order.index(other.value)


class CardFactory():

    def __init__(self, comparer: CardComparer):
        self.__comparer = comparer

    def generate(self, suit: Suit, value: Value):
        return Card(suit, value, self.__comparer)
