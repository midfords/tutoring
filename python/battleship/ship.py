#
# Battleship - Ship class
#
# Python tutoring exercise.
# Sean Midford, 2020
#
from typing import Set
from point import Point

class Ship:
    """
    This class represents a ship. It contains all the points the ship occupies as well as
    an indicator for the ships size. 
    """

    __SHIP_NAMES = {2: "Destroyer", 3: "Cruiser", 4: "Battleship", 5: "Aircraft Carrier"}

    def __init__(self, size: int, points: Set[Point]):
        self.__points = points
        self.__hit = set()
        self.__size = size

    def __contains__(self, item: Point):
        return item in self.__points and item not in self.__hit

    def __len__(self):
        return len(self.__points - self.__hit)

    def __str__(self):
        return Ship.__SHIP_NAMES[self.__size]

    def hit(self, point: Point):
        """Hit the ship at a certain point. If the point is in the ship, add that point
        to the self.__hit set. If the point is not in the ship, raise a ValueError.

        Parameters
        ----------
        point : Point
            The point (x and y) on the Ship to hit.
        Raises
        ------
        ValueError
            If the Ship object does not contain the point.
        """
        pass
