#
# Hangman
#
# Python tutoring exercise.
# Sean Midford, 2020
#
from typing import Set
from getpass import getpass

def print_menu():
    """This function prints out the main menu. The menu options are: 
        "New Game"
        "Quit"
    """
    pass

def get_menu_choice() -> int:
    """This function gets the user's menu choice. This function should return 1 for "New Game" (input 'N')
        or 0 for "Quit" (input 'Q'). If the user enters an invalid character, the function should ask
        the user to re-enter a menu choice.

    Returns
    -------
    int
        The menu choice code.
    """
    pass

def print_hangman(misses: int):
    """This function prints the hangman board. The number of missed guesses is passed in to the 
    function. The number of misses can be in the range of [0, 6] (where 0 is no misses, so the
    hangman is empty). The misses should be printed according to:

        0 -> No misses, empty hangman
        1 -> Head only
        2 -> Head and body
        3 -> Head, body and 1 arm
        4 -> Head, body and 2 arms
        5 -> Head, body, 2 arms and 1 leg
        6 -> Head, body, 2 arms and 2 legs

    Parameters
    ----------
    misses : int
        The number of misses used to print the hangman board.
    """
    pass

def print_guesses(guesses: Set[str]):
    """This function prints all of the player's guesses.

    Parameters
    ----------
    guesses : Set[str]
        The guesses to be printed.
    """
    pass

def print_result(result: int):
    """This function prints the final hangman game result. The result can be:
        1 -> player wins.
        2 -> player looses.

    Parameters
    ----------
    result : int
        The result to be printed.
    """
    pass

def get_guess(guesses: Set[int]) -> str:
    """This function gets a lowercase letter guess from the user. The function should stop the user from picking
    a letter that is already in the guesses set. The function should only return upper case letters, so if the
    player enters 'e', the function should return 'E'. The function should also not allow invalid characters to
    be entered (ie. numbers, symbols and sequences of more than one character).

    Example sequence:

        guesses: {E, R, T, U}

        Enter in a guess: abc
        Invalid! (More than one character entered)

        Enter in a guess: 1
        Invalid! (Numbers are not allowed)

        Enter in a guess: e
        Invalid! (Letter is already in guesses)

        Enter in a guess: q

        function returns 'Q'

    Parameters
    ----------
    guesses : Set[str]
        The set of guesses.

    Returns
    -------
    str
        The player's next guess.
    """
    pass

def add_guess(guesses: Set[str], guess: str):
    """This function adds a new guess into the guesses Set.

    Parameters
    ----------
    guesses : Set[str]
        The set of guesses.
    guess : str
        The guess to be added.
    """
    pass

def print_partial_secret(guesses: Set[str], secret: str):
    """This function prints the player's progress so far by printing only the letters that the user
    has already guessed. All other characters must be replaced by the underscore ("_") character. The
    space (" ") character should always be shown to the user.
    For example:

        guesses: {A, B, C, D}
        secret: "CAT"
        print: "CA_"

        guesses: {O, D}
        secret: "DOG HOUSE"
        print: "DO_ _O___"

    Parameters
    ----------
    guesses : Set[str]
        The player's guesses.
    secret: str
        The secret phrase.
    """
    pass

def get_secret() -> str:
    """This function gets a secret word to start a new game. The secret word should contain only letters
    and spaces. All lower case letters should also be converted to upper case.

    Hint: use the hidden_input function.

    Returns
    -------
    str
        The secret phrase.
    """
    pass

def check_guess(secret: str, guess: str) -> bool:
    """This function checks if the player's guess is in the secret. If it is, return True,
    otherwise False.

    Parameters
    ----------
    secret : str
        The secret phrase.
    guess : str
        The player's guess.

    Returns
    -------
    bool
        True if the guess is in the secret, otherwise False.
    """
    pass

def check_for_win(guesses: Set[str], secret: str, misses: int) -> int:
    """This function checks if all letters in the secret are in the guesses set. If all the letters in secret are
    in guesses, the player wins. If the misses number is >= 6, the player loses. Otherwise, the game is still in progress.
    The function should return a number for the final result:
        0 -> game is still in progress.
        1 -> player wins.
        2 -> player loses.

    Parameters
    ----------
    guesses : Set[str]
        The player's guesses.
    secret : str
        The secret phrase.
    misses : int
        The player's misses count.

    Returns
    -------
    int
        A code for the game win state.
    """
    pass

def hidden_input(msg: str = "") -> str:
    return getpass(msg)

def play_game():
    secret = get_secret()

    guesses = set()
    misses, result = 0, 0

    while result == 0:
        print_hangman(misses)
        print_partial_secret(guesses, secret)
        print_guesses(guesses)

        guess = get_guess(guesses)
        add_guess(guesses, guess)

        if not check_guess(secret, guess):
            misses += 1

        result = check_for_win(guesses, secret, misses)

    print_result(result)
    print("The secret phrase was: ", secret)

def main():
    print("Welcome to Hangman!")

    while 1:
        print_menu()
        choice = get_menu_choice()

        if choice != 0:
            play_game()
        else:
            break

    print("Exited successfully.")


if __name__ == "__main__":
    main()
