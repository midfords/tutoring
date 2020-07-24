#
# Battleship - Point, PointConverter class
#
# Python tutoring exercise.
# Sean Midford, 2020
#
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


class PointConverter:
    """
    This class contains a collection of convenience functions for creating and 
    mutating Point objects.
    """

    def increment_point(point: Point, direction: Direction):
        """Increments a point by 1 in a certain direction. For example, if the
        direction is north, the point's x value should increment by -1.

        Parameters
        ----------
        point : Point
            The point to increment.
        direction : Direction
            The direction to increment the point by.
        """
        pass

    def from_coordinate(coordinate: str) -> Point:
        """Creates a Point object from a coordinate. The coordinate is made of one letter and
        one number (For example: "A0", "B4", "J5").

        Parameters
        ----------
        coordinate : str
            The coordinate string to make a Point object from.
        Returns
        -------
        Point
            The Point object.
        Raises
        ------
        ValueError
            If the coordinate string is not in the correct format.
        """
        pass

    def to_letter(pos: int) -> str:
        """Converts a number to a letter (For example: 0 to 'A', 5 to 'F') and returns it.

        Parameters
        ----------
        pos : int
            The number to convert to a letter.
        Returns
        -------
        str
            The letter representing the position.
        """
        pass

