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
    """
    This class represents a player's game board. It contains variables to manage size, ships
    and the Cell objects that make up the board.
    """

    def __init__(self, size: int, hide_ships: bool=False):
        self.__size = size
        self.__ships = []
        self.__board = self.__init_board(size, hide_ships)

    def __init_board(self, size: int, hide_ship: bool) -> List[List[Cell]]:
        """Helper method for __init__. Creates a list of rows based on size.
        """
        pass

    def __init_row(self, size: int, hide_ship: bool) -> List[Cell]:
        """Helper method for __init__. Creates a list of cells based on size.
        """
        pass

    def __init_cell(self, hide_ship: bool) -> Cell:
        """Helper method for __init__. Creates a cells and sets the hide_ship property.
        """
        pass

    def __str__(self) -> str:
        """This method returns the string representation of the BattleshipBoard object. 
        This method is called when print() or str() function is invoked on an object. 
        The output string should print the board, with each cell's contents (miss or hit for example).

        Returns
        -------
        str
            The string representation of the object.
        """
        pass

    def __place_ship(
        self, point: Point, direction: Direction, size: int, i: int, points: Set[Point]) -> Ship:
        if i <= 0:
            return

        if point.x not in range(self.__size) or point.y not in range(self.__size):
            raise ValueError(f"Invalid ship placement at {point} with direction {direction}. Ship is out of board range.")
        if self.__board[point.x][point.y].is_ship():
            raise ValueError(f"Invalid ship placement at {point} with direction {direction}. Another ship is on this point.")

        points.add(point)

        next_point = copy(point)
        PointConverter.increment_point(next_point, direction)
        self.__place_ship_aux(next_point, direction, size, i - 1, points)

        self.__board[point.x][point.y].ship = True
        return Ship(size, points)

    def place_ship(self, point: Point, direction: Direction, size: int):
        """Places a new ship on the board of a certain size. The ship placement starts at
        the point (x and y) and moves in some direction (North, East, South or West).

        Hint: Use __place_ship method.

        Parameters
        ----------
        point : Point
            The point (x and y) to start placing the ship.
        direction : Direction
            The direction the ship is being placed.
        size: int
            The size of the ship.
        """
        pass

    def get_ship(self, point: Point) -> Ship:
        """Returns the ship at some point. If no ship is at that point, return None.

        Parameters
        ----------
        point : Point
            The point (x and y) on the board to get the ship.
        Returns
        -------
        Ship
            The Ship object containing the point.
        """
        pass

    def hit(self, point: Point) -> (bool, bool, Ship):
        """Hit the cell at the point. Returns three status variables for the result.
        If a ship was hit, return the first boolean as True.
        If a ship was sunk, return the second boolean as True.
        If a ship was hit, return the third result as the Ship object that was hit.
        Raise an exception if the point is out of bounds.

        Parameters
        ----------
        point : Point
            The point (x and y) on the board to hit.
        Returns
        -------
        (bool, bool, Ship)
            The result of the hit (hit ship, sunk ship, and Ship object).
        Raises
        ------
        ValueError
            If the point is out of range [0, self.__size].
        """
        pass

    def is_game_over(self) -> bool:
        """This method checks if all the ships on the BattleshipBoard are sunk. If at least
        one ship remains, it is not a game over.

        Returns
        -------
        bool
            If it is a game over (all ships have been sunk).
        """
        pass

    def reveal(self):
        """This method reveals all ships on the board. It should iterate over each Cell object in
        self.__board and set the hide_ship value to False.
        """
        pass
