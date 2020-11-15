#
# Mastermind
#
# Python tutoring exercise.
# Sean Midford, 2020
#
from typing import List
import random
from colorama import Fore, Back, Style

def create_secret() -> (int, int, int, int):
    return (
        random.randint(1, 8),
        random.randint(1, 8),
        random.randint(1, 8),
        random.randint(1, 8))

def create_secret_unique() -> (int, int, int, int):
    """This function creates a new 4 piece secret (in the range of [1, 8]).
    These values must be randomly selected, duplicate values are allowed.
    Example return: (4, 2, 2, 6)

    Returns
    -------
    (int, int, int, int)
        A secret of 4 values in the range of [1, 8].
    """
    secret = []

    while 1:
        a = random.randint(1, 8)
        if a not in secret:
            secret.append(a)
        if len(secret) == 4:
            break

    return tuple(secret)


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
    
    if guess == secret:
        return 1
    if turn >= 10:
        return 2
    else:
        return 0 


def get_guess(turn: int) -> (int, int, int, int):
    """This function gets 4 integers in the range of [1, 8] from the user. 
    The function should stop the user from picking a value that is not in 
    the range of [1, 8], or if the user enters in anything other than a 
    number. 

    Returns
    -------
    (int, int, int, int)
        A tuple of the player's 4 guesses.
    """
    result = []

    while 1:
        try:
            print(turn, end="")
            inp = input(" > ")
            result = [int(c) for c in inp]

            invalid = list(filter(lambda a: a < 1 or a > 8, result))
            if len(invalid) > 0:
                raise Exception("One or more numbers out of range.")
            elif len(result) != 4:
                raise Exception("Input did not contain 4 numbers.")
            else:
                break
        except Exception as e:
            print(e)
            print("! ", end="")

    return tuple(result)


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
    gcopy = list(guess)
    copy = list(secret)

    result = []
    if gcopy[0] == copy[0]:
        result.append(1)
        gcopy[0] = -1
        copy[0] = -1

    if gcopy[1] == copy[1]:
        result.append(1)
        gcopy[1] = -1
        copy[1] = -1

    if gcopy[2] == copy[2]:
        result.append(1)
        gcopy[2] = -1
        copy[2] = -1

    if gcopy[3] == copy[3]:
        result.append(1)
        gcopy[3] = -1
        copy[3] = -1

    if gcopy[0] != -1 and gcopy[0] in copy:
        i = copy.index(gcopy[0])
        copy[i] = -1
        result.append(0)

    if gcopy[1] != -1 and gcopy[1] in copy:
        i = copy.index(gcopy[1])
        copy[i] = -1
        result.append(0)

    if gcopy[2] != -1 and gcopy[2] in copy:
        i = copy.index(gcopy[2])
        copy[i] = -1
        result.append(0)

    if gcopy[3] != -1 and gcopy[3] in copy:
        i = copy.index(gcopy[3])
        copy[i] = -1
        result.append(0)

    return result

def print_guess(guess: (int, int, int, int)):
    """This function prints out the player's guess.

    Hint: use the print_piece function.

    (1, 3, 6, 4) > red, blue, cyan, yellow

    Parameters
    ----------
    guess : (int, int, int, int)
        The player's guess.
    """
    print_piece(guess[0], end="")
    print_piece(guess[1], end="")
    print_piece(guess[2], end="")
    print_piece(guess[3], end="")
    print(" |  ", end="")

def print_secret(secret: (int, int, int, int)):
    """This function prints out the player's guess.

    Hint: use the print_piece function.

    (1, 3, 6, 4) > red, blue, cyan, yellow

    Parameters
    ----------
    guess : (int, int, int, int)
        The player's guess.
    """
    print_piece(secret[0], end="")
    print_piece(secret[1], end="")
    print_piece(secret[2], end="")
    print_piece(secret[3])

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
    for i in result:
        if i == 1:
            print_piece(8, end="")
        else:
            print_piece(7, end="")

    print()


def print_final_result(result: int):
    """This function prints the final mastermind game result. The result can be:
        1 -> player wins.
        2 -> game over.

    Parameters
    ----------
    result : int
        The result to be printed.
    """
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    if result == 1:
        print("Correct, congratulations!")
    else:
        print("Sorry, you did not guess the combination!")


def print_welcome():
    """This functiokn prints out a simple welcome message to the player.
    """
    print("=-=-=-=  MASTERMIND  =-=-=-=-")
    print("  Instructions:  ")

    print(" ", end="")
    print_piece(8, end="")
    print(" Correct colour in correct position.")

    print(" ", end="")
    print_piece(7, end="")
    print(" Correct colour in incorrect position.")

    print_colours_menu()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print()


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
    print("1 ", end="")
    print_piece(1, end="  ")
    print("2 ", end="")
    print_piece(2, end="  ")
    print("3 ", end="")
    print_piece(3, end="  ")
    print("4 ", end="")
    print_piece(4)
    print("5 ", end="")
    print_piece(5, end="  ")
    print("6 ", end="")
    print_piece(6, end="  ")
    print("7 ", end="")
    print_piece(7, end="  ")
    print("8 ", end="")
    print_piece(8)


def print_piece(colour: int, end: str = "\n"):
    colours = [
        (Fore.RED, Back.RESET), (Fore.GREEN, Back.RESET),
        (Fore.BLUE, Back.RESET), (Fore.YELLOW, Back.RESET),
        (Fore.MAGENTA, Back.RESET), (Fore.CYAN, Back.RESET),
        (Fore.BLACK, Back.WHITE), (Fore.WHITE, Back.RESET)]

    assert(colour > 0 and colour <= len(colours))

    i = colour - 1
    print(
        f"{colours[i][0]}{colours[i][1]}", "⬤ ",
        f"{Style.RESET_ALL}", " ", end=end, sep="")


def play_game():
    secret = create_secret()

    turn = 1
    while 1:
        guess = get_guess(turn)

        print_guess(guess)
        result = get_result(guess, secret)
        print_result(result)

        result = check_for_win(guess, secret, turn)
        if result != 0:
            print_final_result(result)
            print("The combination was: ")
            print_secret(secret)
            break

        turn += 1


def main():
    print_welcome()
    play_game()


if __name__ == "__main__":
    main()
