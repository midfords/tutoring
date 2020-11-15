#
# Battleship - Point, PointConverter class
#
# Python tutoring exercise.
# Sean Midford, 2020
#
import re
from direction import Direction

class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __copy__(self):
        return Point(self.x, self.y)

    def increment(self, direction: Direction):
        if direction is Direction.NORTH:
            self.x -= 1
        elif direction is Direction.EAST:
            self.y += 1
        elif direction is Direction.SOUTH:
            self.x += 1
        elif direction is Direction.WEST:
            self.y -= 1
        else:
            raise ValueError(f"Direction {direction} is not recognized.")


class PointConverter:

    int_to_letter = lambda a: chr(a + ord("A"))
    letter_to_int = lambda a: ord(a) - ord("A")
    number_to_int = lambda a: int(a)

    def from_coordinate(coordinate: str) -> Point:
        if re.match(coordinate, "[A-J][0-9]$") is not None:
            raise ValueError("Coordinate must be formatted as /[A-J][0-9]$/.")

        x = PointConverter.letter_to_int(coordinate[0])
        y = PointConverter.number_to_int(coordinate[1])

        return Point(x, y)

    def to_letter(pos: int) -> str:
        return PointConverter.int_to_letter(pos)
