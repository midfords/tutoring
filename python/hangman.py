# 
# Hangman Errors
#
# Python tutoring exercise.
# Sean Midford, 2020
#

from getpass import getpass


def process_guess(guess, progress, secret):
    if guess not in progress and guess in secret:
        progress.append(guess)

def is_game_lost(misses):
    return misses >= 6

def is_game_won(progress, secret):
    return len(set(progress) - set(secret)) == 0

def is_game_over(misses, progress, secret):
    return is_game_lost(misses) or is_game_won(progress, secret)

def print_hangman(misses):
    print(" _______")
    print("|/  |   `")

    print("|", end="")
    if misses > 0:
        print("   o")
    else:
        print()

    print("|", end="")
    if misses == 2:
        print("   |")
    elif misses == 3:
        print("  /|")
    elif misses >= 4:
        print("  /|\\")
    else:
        print()

    print("|", end="")
    if misses == 5:
        print("  /")
    elif misses >= 6:
        print("  / \\")
    else:
        print()

    print("|________")
    print("|/\\/\\/\\/\\|")


def print_progress(progress, secret):
    output = map(lambda c: c in progress or c == " ", secret)

    print(output)
    for c in secret:
        if c in progress:
            print(c, end="")
        elif c == " ":
            print(" ", end="")
        else:
            print("_", end="")
    print()


def print_result(misses):
    if is_game_lost(misses):
        print("Game over!)
    else:
        print("Congratulations!")

def print_secret(secret):
    print("The word was: " + secret)

def play_game():
    secret = getpass("Enter secret word: ")
    progress = []
    misses = 0

    while not is_game_over(misses, progress, secret):
        guess = input("Enter guess: ")

        process_guess(guess, progress, secret)

        if guess not in secret and guess not in progress:
            misses += 1

        print_progress(progress, secret)
        print_hangman(misses)

    print_secret(secret)
    print_result(misses)

def play_again():
    play = input("Play again? [y/n]")
    return play == "y"

def main():
    print("Welcome to hangman!")

    while True:
        play_game()
        if not play_again():
            break;

    print("Thanks for playing!")


main()
