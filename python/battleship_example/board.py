#
# Battleship - BattleshipBoard class
#
# Python tutoring exercise.
# Sean Midford, 2020
#
from cell import Cell
from ship import Ship
from point import Point, PointConverter
from direction import Direction
from typing import List, Set
from functools import reduce
from copy import copy

class BattleshipBoard:

    BOARD_SIZE = 10

    def __init__(self, hide_ships: bool=False, hide_output: bool=False):
        self.size = BattleshipBoard.BOARD_SIZE
        self.remaining_ships = []
        self.hide_ships = hide_ships
        self.hide_output = hide_output
        self.board = [[Cell(hide_ships) for _ in range(self.size)] for _ in range(self.size)]

    def __place_ship_aux(
        self, point: Point, direction: Direction, size: int, i: int, points: Set[Point]) -> Ship:
        if i <= 0:
            return

        if point.x not in range(self.size) or point.y not in range(self.size):
            raise ValueError(f"Invalid ship placement at {point} with direction {direction}. Ship is out of board range.")
        if self.board[point.x][point.y].is_ship():
            raise ValueError(f"Invalid ship placement at {point} with direction {direction}. Another ship is on this point.")

        points.add(point)

        next_point = copy(point)
        next_point.increment(direction)
        self.__place_ship_aux(next_point, direction, size, i - 1, points)

        self.board[point.x][point.y].place_ship()
        return Ship(size, points)

    def place_ship(self, point: Point, direction: Direction, size: int):
        ship = self.__place_ship_aux(point, direction, size, size, set())
        self.remaining_ships.append(ship)

    def is_game_over(self):
        return reduce(lambda a, b: a and len(b) == 0, self.remaining_ships, True)

    def __check_for_ship(self, point: Point) -> (bool, int):
        for ship in self.remaining_ships:
            if point not in ship:
                continue

            ship.remove(point)

            return (len(ship) == 0, ship)

        return (False, None)

    def hit(self, point: Point) -> (bool, bool, Ship):
        if point.x not in range(self.size) or point.y not in range(self.size):
            raise ValueError(f"Point {point} is out of range.")
        if self.board[point.x][point.y].is_hit():
            raise ValueError("Cell already hit.")

        hit_flag = self.board[point.x][point.y].hit_cell()
        sunk_flag, ship = self.__check_for_ship(point)

        return (hit_flag, sunk_flag, ship)

    def __get_coordinates_str(self):
        out = "   "
        for i in range(self.size):
            out += " " + str(i) + "  "
        return out

    def __get_top_row_str(self):
        out = "  ┌"
        for _ in range(self.size - 1):
            out += "───┬"
        out += "───┐"
        return out

    def __get_middle_row_str(self):
        out = "  ├"
        for _ in range(self.size - 1):
            out += "───┼"
        out += "───┤"
        return out

    def __get_row_str(self, row: int):
        out = PointConverter.to_letter(row) + " │"
        for col in range(self.size):
            out += str(self.board[row][col]) + "│"
        out += " " + PointConverter.to_letter(row)
        return out

    def __get_bottom_row_str(self):
        out = "  └"
        for _ in range(self.size - 1):
            out += "───┴"
        out += "───┘"
        return out

    def reveal(self):
        self.hide_ships = False
        for row in self.board:
            for cell in row:
                cell.hide_ship = False

    def __str__(self):
        rows = []

        rows.append(self.__get_coordinates_str())
        rows.append(self.__get_top_row_str())
        for i in range(self.size - 1):
            rows.append(self.__get_row_str(i))
            rows.append(self.__get_middle_row_str())
        rows.append(self.__get_row_str(self.size - 1))
        rows.append(self.__get_bottom_row_str())

        return "\n".join(rows)
