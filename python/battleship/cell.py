#
# Battleship - Cell class
#
# Python tutoring exercise.
# Sean Midford, 2020
#
from colorama import Fore, Style

class Cell:
    """
    This class represents a cell on the BattleshipBoard. It contains variables to track
    if the cell has been shot and if the cell has a ship present. If self.__hide_ship is
    True, the cell should not reveal a ship.
    """

    def __init__(self, hide_ship: bool):
        self.__hit = False
        self.__ship = False
        self.__hide_ship = hide_ship

    def __str__(self):
        """This method returns the string representation of the Cell object. 
        This method is called when print() or str() function is invoked on an object. 
        The output string should print the contents of the cell (with ships and hit indicators).
        If self.__hide_ship is set to True, the output string should not reveal ships.

        Returns
        -------
        str
            The string representation of the object.
        """
        pass

    def __indicator(self, hit: bool) -> str:
        return f"{Fore.RED}●{Style.RESET_ALL}" if hit else "●"

    def shoot(self) -> bool:
        """Shoot the cell by setting the self.__hit variable to True. If the cell has already
        been shot before (self.__hit is already True), raise a ValueError. Return if the cell
        contains a ship (if the shot was successful).

        Returns
        -------
        bool
            Whether the cell contains a ship.
        Raises
        ------
        ValueError
            If the cell has already been hit.
        """
        pass
