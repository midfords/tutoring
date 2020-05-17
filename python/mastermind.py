# 
# Mastermind
#
# Python tutoring exercise.
# Sean Midford, 2020
#
from typing import List
from colorama import Fore, Back, Style

def create_secret() -> (int, int, int, int):
    """This function creates a new 4 piece secret (in the range of [1, 8]).
    These values must be randomly selected, duplicate values are allowed.
    Example return: (4, 2, 2, 6)

    Returns
    -------
    (int, int, int, int)
        A secret of 4 values in the range of [1, 8].
    """
    pass

def check_for_win(guess: (int, int, int, int), secret: (int, int, int, int), 
                  turn: int) -> int:
    """This function checks the game board for a game over state or win state.
    A win happens if the 4 guess values exactly matches the 4 secret values.
    A game over happens if the number of turns is >= 10.
    If neither of these are true, then the game is still in progress.
        0 -> game is still in progress.
        1 -> player has won.
        2 -> game over.

    Parameters
    ----------
    guess : (int, int, int, int)
        The player's guess.
    secret : (int, int, int, int)
        The secret values.
    turn : int
        The player's current turn number.

    Returns
    -------
    int
        A code for the game win state.
    """
    pass

def get_guess() -> (int, int, int, int):
    """This function gets 4 integers in the range of [1, 8] from the user. 
    The function should stop the user from picking a value that is not in 
    the range of [1, 8], or if the user enters in anything other than a 
    number. 

    Returns
    -------
    (int, int, int, int)
        A tuple of the player's 4 guesses.
    """
    pass

def get_result(guess: (int, int, int, int), secret: (int, int, int, int)) -> List[int]:
    """This function compares the guess to the secret and generates a result. 
    The result is returned as a list of values in the range [0, 1]. If there
    is a value in guess that is also in secret, and in the same position, then
    a '1' is added to the result. If there is a value in guess that is also in
    secret, but not in the same position, then a '0' is added to the result. 
    A guess can only be counted once. For example, if the player's guess was:
        (2, 2, 2, 2)
    and the secret was:
        (1, 2, 3, 4)
    then the result would be [1] and not [1, 0, 0, 0].

    Result summary:
        1 -> correct value in correct position
        0 -> correct value in incorrect position

    Parameters
    ----------
    guess : (int, int, int, int)
        The player's guess.
    secret : (int, int, int, int)
        The secret values.

    Returns
    -------
    List[int]
        A list of values in range [0, 1] representing the result.
    """
    pass

def print_code(code: (int, int, int, int)):
    """This function prints out a 4 value code with colours.

    Hint: use the print_piece function.

    Parameters
    ----------
    code : (int, int, int, int)
        The 4 value code.
    """
    pass 

def print_result(result: List[int]):
    """This function prints out the turn result. For each '1' in the list, 
    print a white piece (colour code 8). For each '0' in the list, print a 
    black piece (colour code 7).

    Hint: use the print_piece function.

    Parameters
    ----------
    result : List[int]
        A list of values in range [0, 1] representing the result.
    """
    pass

def print_final_result(result: int):
    """This function prints the final mastermind game result. The result can be:
        1 -> player wins.
        2 -> game over.

    Parameters
    ----------
    result : int
        The result to be printed.
    """
    pass

def print_welcome():
    """This function prints out a simple welcome message to the player.
    """
    pass

def print_colours_menu():
    """This function prints out the colour menu. The menu options are: 
        1 -> "Red"
        2 -> "Green"
        3 -> "Blue"
        4 -> "Yellow"
        5 -> "Magenta"
        6 -> "Cyan"
        7 -> "Black"
        8 -> "White"

    Hint: use the print_piece function.
    """
    pass

def print_piece(colour: int, end: str = "\n"):
    colours = [
        (Fore.RED, Back.RESET), (Fore.GREEN, Back.RESET),
        (Fore.BLUE, Back.RESET), (Fore.YELLOW, Back.RESET),
        (Fore.MAGENTA, Back.RESET), (Fore.CYAN, Back.RESET),
        (Fore.BLACK, Back.WHITE), (Fore.WHITE, Back.RESET) ]

    assert(colour > 0 and colour <= len(colours))

    i = colour - 1
    print(
        f"{colours[i][0]}{colours[i][1]}", "⬤ ", 
        f"{Style.RESET_ALL}", " ", end=end, sep="")

def play_game():
    secret = create_secret()

    turn = 1
    while 1:
        print_colours_menu()
        guess = get_guess()
        print_code(guess)
        result = get_result(guess, secret)
        print_result(result)

        result = check_for_win(guess, secret, turn)
        if result != 0:
            print_final_result(result)
            print_code(secret)
            break

        turn += 1

def main():
    print_welcome()
    play_game()

if __name__ == "__main__":
    main()