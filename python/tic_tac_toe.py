# 
# Tic Tac Toe
#
# Python tutoring exercise.
# Sean Midford, 2020
#
from typing import List

def print_menu():
    """This function prints out the main menu. The menu options are: 
        "New Game"
        "Quit"
    """
    pass

def get_menu_choice() -> int:
    """This function gets the users menu choice. This function should return 1 for "New Game"
        or 0 for "Quit". If the user enters an invalid character, the function should ask
        the user to re-enter a menu choice.

    Returns
    -------
    int
        The menu choice code.
    """
    pass

def print_board(board: List[List[str]]):
    """This function prints the tic tac toe board. The board is stored as a list 
        of lists. For example:

            [[" ", " ", "x"], [" ", "o", ""], ["x", " ", "o"]]

        Represents the board:

             | |x
            -----
             |o| 
            -----
            x| |o

    Parameters
    ----------
    board : List[List[str]]
        The board to be printed.
    """
    pass

def print_result(result: int):
    """This function prints the final tic tac toe game result. The result can be:
        1 -> "o"s win.
        2 -> "x"s win.
        3 -> tie game.

    Parameters
    ----------
    result : int
        The result to be printed.
    """
    pass

def get_position(board: List[List[str]]) -> (int, int):
    """This function gets two integers, an x and y coordinate in the range of 1 to 3, 
    from the user. The function should stop the user from picking a position that has 
    already been taken, or a position that is not in the range of 1 to 3, or if the user
    enters in anything other than a number. For example, the board:

             | |x
            -----
             |o| 
            -----
            x| |o

    should only allow the following possible coordinates: 

        (1,1), (1,2), (2,1), (2,3), (3,2)

    Parameters
    ----------
    board : List[List[str]]
        The game board.

    Returns
    -------
    (int, int)
        A tuple of the x and y coordinates.
    """
    pass

def put_piece(board: List[List[str]], x: int, y: int, piece: str):
    """This function places a new piece onto the game board. The piece should be placed in
    the position specified by the x and y parameters.

    Parameters
    ----------
    board : List[List[str]]
        The game board.
    x: int
        The x coordinate.
    y: int
        The y coordinate.
    piece: str
        The current piece ("x" or "o") to place in the board.
    """
    pass

def check_for_win(board: List[List[str]]) -> int:
    """This function checks the game board for a game over state. This can happen if 
    the "o"s have won, the "x"s have won, or if it's a tie game (all positions filled
    but neither player has won). The function should return a number for the final result:
        0 -> game is still in progress.
        1 -> "o"s have won.
        2 -> "x"s have won.
        3 -> tie game.

    Parameters
    ----------
    board : List[List[str]]
        The game board.

    Returns
    -------
    int
        A code for the game win state.
    """
    pass

def create_empty_board() -> List[List[str]]:
    """This function creates a new 3x3 game board, filled with space characters (" ").

    Returns
    -------
    List[List[str]]
        An empty game board.
    """
    pass

def play_game():
    board = create_empty_board()

    piece = "o"
    while 1:
        result = check_for_win(board)

        if result != 0:
            print_result(result)
            break

        i, j = get_position(board)
        put_piece(board, i, j, piece)

        piece = "x" if piece is "o" else "o"

def main():
    print("Welcome to Tic Tac Toe!")

    while 1:
        print_menu()
        choice = get_menu_choice()

        if choice != 0:
            play_game()
        else:
            break;

    print("Exited successfully.")

if __name__ == "__main__":
    main()