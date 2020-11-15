#
# Battleship - Ship class
#
# Python tutoring exercise.
# Sean Midford, 2020
#
from typing import Set
from point import Point

class Ship:

    SHIP_NAMES = {1: "Buoy", 2: "Destroyer", 3: "Cruiser", 4: "Battleship", 5: "Aircraft Carrier"}

    def __init__(self, size: int, points: Set[Point]):
        self.points = points
        self.size = size

    def __contains__(self, item: Point):
        return item in self.points

    def __len__(self):
        return len(self.points)

    def __str__(self):
        return Ship.SHIP_NAMES[self.size]

    def remove(self, point: Point):
        if point not in self.points:
            raise ValueError(f"Ship does not contain point {point}.")

        self.points.remove(point)

    def get_ship_name(size: int) -> str:
        return Ship.SHIP_NAMES[size] if size in Ship.SHIP_NAMES else "Unknown"