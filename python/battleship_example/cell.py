#
# Battleship - Cell class
#
# Python tutoring exercise.
# Sean Midford, 2020
#
from typing import List
from colorama import Fore, Style

class Cell:

    def __init__(self, hide_ship: bool):
        self.hit = False
        self.ship = False
        self.hide_ship = hide_ship

    def place_ship(self):
        self.ship = True

    def hit_cell(self) -> bool:
        if self.hit:
            raise ValueError("Space already hit.")

        self.hit = True
        return self.ship

    def is_hit(self) -> bool:
        return self.hit

    def is_ship(self) -> bool:
        return self.ship

    def __str__(self):
        if not self.hit and (not self.ship or self.hide_ship):
            return "   "
        elif not self.hit and self.ship and not self.hide_ship:
            return "[ ]"
        elif self.hit and not self.ship:
            return " ● "
        elif self.hit and self.ship and self.hide_ship:
            return f" {Fore.RED}●{Style.RESET_ALL} "
        elif self.hit and self.ship and not self.hide_ship:
            return f"[{Fore.RED}●{Style.RESET_ALL}]"
        else:
            raise ValueError(f"Unknown string for hit:{self.hit} ship:{self.ship} hide_ship:{self.hide_ship}")
