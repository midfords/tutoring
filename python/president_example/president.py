import random
import curses
from typing import List

from suit import Suit
from value import Value
from hand import Hand
from card import CardFactory, CardComparer, Card

ORDER = [
    Value.THREE,
    Value.FOUR,
    Value.FIVE,
    Value.SIX,
    Value.SEVEN,
    Value.EIGHT,
    Value.NINE,
    Value.TEN,
    Value.JACK,
    Value.QUEEN,
    Value.KING,
    Value.ACE,
    Value.TWO,
    Value.JOKER,
]

def print_instructions():
    pass

def generate_deck() -> List[Card]:
    factory = CardFactory(CardComparer(ORDER))

    deck = []
    for s in list(Suit)[:-1]:
        for v in list(Value)[:-1]:
            deck.append(factory.generate(s, v))

    deck.append(factory.generate(Suit.NONE, Value.JOKER))
    deck.append(factory.generate(Suit.NONE, Value.JOKER))

    random.shuffle(deck)

    return deck


def play_game():
    pass


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.curs_set(0)

    stdscr.bkgd(' ', curses.color_pair(1))

    stdscr.clear()

    rows, cols = stdscr.getmaxyx()

    while 1:
        ch = stdscr.getch()
        stdscr.erase()

        if (ch == curses.KEY_LEFT):
            cols -= 1
        elif (ch == curses.KEY_RIGHT):
            cols += 1
        elif (ch == curses.KEY_DOWN):
            rows += 1
        elif (ch == curses.KEY_UP):
            rows -= 1

        try: 
            stdscr.addstr(rows, cols, "+")
        except:
            rows = 0
            cols = 0
        stdscr.refresh()







if __name__ == "__main__":
    curses.wrapper(main)

