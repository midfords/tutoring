from typing import List

from card import Card

class Hand():

    def __init__(self, cards: List[Card], hidden: bool = False):
        cards.sort()
        self.__cards = cards
        self.__hidden = hidden

    def __len__(self):
        return len(self.__cards)

    def __iter__(self):
        return iter(self.__cards)

    def sort(self):
        self.__cards.sort()

    def __str__(self):
        if len(self.__cards) == 0:
            return ""

        rows = []
        rows.append(self.__get_top_row_str())
        rows.append(self.__get_middle_value_row_str())
        rows.append(self.__get_middle_suit_row_str())
        rows.append(self.__get_middle_empty_row_str())
        rows.append(self.__get_middle_empty_row_str())
        rows.append(self.__get_bottom_suit_row_str())
        rows.append(self.__get_bottom_value_row_str())
        rows.append(self.__get_bottom_row_str())
        rows.append(self.__get_letter_legend_row_str())

        return "\n".join(rows)

    def __filter(self, value: str):
        return value if not self.__hidden else " " * len(value)

    def __get_top_row_str(self):
        out = ""
        for _ in self.__cards:
            out += "╭───"
        out += "─────╮"
        return out

    def __get_middle_empty_row_str(self):
        out = ""
        for _ in self.__cards:
            out += "│   "
        out += "     │"
        return out

    def __get_middle_suit_row_str(self):
        out = ""
        for card in self.__cards:
            out += "│" + self.__filter(str(card.suit)) + "  "
        out += "     │"
        return out

    def __get_middle_value_row_str(self):
        out = ""
        for card in self.__cards:
            out += "│" + self.__filter(str(card.value)) + "  "
        out += "     │"
        return out

    def __get_bottom_suit_row_str(self):
        out = ""
        for _ in self.__cards:
            out += "│   "
        out += "    " + self.__filter(str(self.__cards[len(self.__cards) - 1].suit)) + "│"
        return out

    def __get_bottom_value_row_str(self):
        out = ""
        for _ in self.__cards:
            out += "│   "
        out += "    " + self.__filter(str(self.__cards[len(self.__cards) - 1].value)) + "│"
        return out

    def __get_bottom_row_str(self):
        out = ""
        for _ in self.__cards:
            out += "╰───"
        out += "─────╯"
        return out

    def __get_letter_legend_row_str(self):
        out = "  "
        for i in range(len(self)):
            out += "{:<4d}".format(i + 1)
        return out

