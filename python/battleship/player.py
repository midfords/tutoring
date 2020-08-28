#
# Battleship - Player, Human, Computer class
#
# Python tutoring exercise.
# Sean Midford, 2020
#
from point import Point, PointConverter
from direction import Direction
from board import BattleshipBoard
from ship import Ship

import random
from abc import ABC, abstractmethod
from copy import copy
from typing import List, Callable

class Player(ABC):

    @abstractmethod
    def place_ships(self, sizes: List[int], board: BattleshipBoard):
        pass

    @abstractmethod
    def next_turn(self, hit: Callable):
        pass


class Human(Player):
    """
    This class represents a human player. It contains the methods to manage a player's turns
    and process turns and ship placements.
    """

    def __get_direction(self) -> Direction:
        """Gets the player's choice for a direction (North, East, South or West). Return a
        Direction enum value. If the player inputs an invalid choice, they should be asked
        to re-enter the direction.

        Returns
        -------
        Direction
            The player's choice for direction.
        """
        pass

    def __get_point(self) -> Point:
        """Gets the player's choice for a Point (x and y). Input the point as a coordinate
        (letter and number) and convert it to a Point. Then, return the Point. If the player 
        inputs an invalid choice, they should be asked to re-enter the point.

        Hint: Use PointConverter.from_coordinate()

        Returns
        -------
        Point
            The player's choice for the point.
        """
        pass

    def __place_ship(self, size: int, board: BattleshipBoard):
        """Place a ship onto the BattleshipBoard. If the user picks an invalid point or direction,
        prompt the user to re-enter the ship's position and direction.

        Hint: Use self.__get_direction() and self.__get_point()

        Parameters
        ----------
        size : int
            The ship size to place on the board.
        board : BattleshipBoard
            The board to place each ship onto.
        """
        pass

    def place_ships(self, sizes: List[int], board: BattleshipBoard):
        """Place each of the ships in the sizes list onto the BattleshipBoard.

        Hint: Use self.__place_ship(size, board)

        Parameters
        ----------
        sizes : List[int]
            The ship sizes to place on the board.
        board : BattleshipBoard
            The board to place each ship onto.
        """
        pass

    def next_turn(self, hit: Callable) -> bool:
        """Prompts the user for a point and calls the hit function with that point.
        If the hit function raises an exception, print the message and ask the user
        for a new point. If the player hit a space, tell them. If the user sunk a ship,
        tell them which ship was sunk. Return the hit response (first boolean value) 
        from the hit function.

        Parameters
        ----------
        hit : Callable
            The board hit function to call with the Point object.
        Returns
        -------
        bool
            If the player successfully hit a ship.
        """
        pass


class Computer(Player):

    def __init__(self):
        self.priority = []
        self.hit_count = 0
        self.turns = 0

    def __get_random_point(self) -> Point:
        while 1:
            x, y = random.randint(0, 9), random.randint(0, 9)
            if (x + y) % 2 == 0:
                return Point(x, y)

    def __get_random_direction(self) -> Direction:
        return random.choice(list(Direction))

    def __place_ship(self, board: BattleshipBoard, size: int):
        while 1:
            point = self.__get_random_point()
            direction = self.__get_random_direction()

            if board.place_ship(point, direction, size):
                break

    def place_ships(self, sizes: List[int], board: BattleshipBoard):
        for size in sizes:
            self.__place_ship(board, size)

    def __add_priority(self, point: Point, direction: Direction, front: bool=False):
        next_point = copy(point)
        PointConverter.increment_point(next_point, direction)
        next_priority = (direction, next_point)
        if front:
            self.priority.insert(0, next_priority)
        else:
            self.priority.append(next_priority)

    def __add_direction_priorities(self, point: Point):
        self.__add_priority(point, Direction.NORTH)
        self.__add_priority(point, Direction.EAST)
        self.__add_priority(point, Direction.SOUTH)
        self.__add_priority(point, Direction.WEST)

    def __get_next_turn(self) -> (Direction, Point):
        if len(self.priority) == 0:
            return (None, self.__get_random_point())
        else:
            return self.priority.pop(0)

    def next_turn(self, hit: Callable) -> bool:
        self.turns += 1
        while 1:
            try:
                direction, point = self.__get_next_turn()
                hit_flag, sunk_flag, ship = hit(point)

                if sunk_flag:
                    self.hit_count -= (ship.size - 1)
                    if self.hit_count <= 0:
                        self.hit_count = 0
                        self.priority = []
                elif hit_flag:
                    self.hit_count += 1
                    self.__add_direction_priorities(point)
                    if direction is not None:
                        self.__add_priority(point, direction, front=True)
                    else:
                        random.shuffle(self.priority)

                return hit_flag
            except:
                pass
