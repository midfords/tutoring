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

    def __get_direction(self) -> Direction:
        d = {"N": Direction.NORTH, "E": Direction.EAST, "S": Direction.SOUTH, "W": Direction.WEST}

        while 1:
            choice = input("Enter direction: ")
            if choice == "N" or choice == "E" \
                or choice == "S" or choice == "W":
                return d[choice]
            else:
                print(f"Invalid direction {choice}.")

    def __get_point(self) -> Point:
        while 1:
            try:
                coord = input("Coordinate: ").upper()
                return PointConverter.from_coordinate(coord)
            except Exception as e:
                print(f"Invalid. {e}")

    def __place_ship(self, board: BattleshipBoard, size: int):
        while 1:
            point = self.__get_point()
            direction = self.__get_direction()

            try:
                board.place_ship(point, direction, size)
                break
            except Exception as e:
                print(e)

    def place_ships(self, sizes: List[int], board: BattleshipBoard):
        for size in sizes:
            self.__place_ship(board, size)
            print(board)

    def next_turn(self, hit: Callable) -> bool:
        while 1:
            try:
                point = self.__get_point()
                (hit_flag, ship_flag, ship) = hit(point)
                if ship_flag:
                    print(f"You sunk the {ship}!")
                return hit_flag
            except ValueError as e:
                print(e)


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

            try:
                board.place_ship(point, direction, size)
                break
            except:
                pass

    def place_ships(self, sizes: List[int], board: BattleshipBoard):
        for size in sizes:
            self.__place_ship(board, size)

    def __add_priority(self, point: Point, direction: Direction, front: bool=False):
        next_point = copy(point)
        next_point.increment(direction)
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
        print(f"priority list {self.priority}")

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
                    print(f"Sunk the {ship}. ")
                    self.hit_count -= (ship.size - 1)
                    if self.hit_count <= 0:
                        print("Done searching the area. ")
                        self.hit_count = 0
                        self.priority = []
                    else:
                        print(f"Continuing to search the area. Hit count {self.hit_count}")
                elif hit_flag:
                    print("Hit something.")
                    self.hit_count += 1
                    self.__add_direction_priorities(point)
                    if direction is not None:
                        print(f"Continuing {direction}.")
                        self.__add_priority(point, direction, front=True)
                    else:
                        print("Picking random direction.")
                        random.shuffle(self.priority)

                return hit_flag
            except:
                pass
