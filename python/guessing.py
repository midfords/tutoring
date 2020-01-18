# 
# Guessing Errors
#
# Python tutoring exercise.
# Sean Midford, 2020
#

import random

def menu():
    print(" Number Guessing Game!")
    print(" ------------------- ")
    print("|   [Q]  Quit       |")
    print("|   [N]  New Game   |")
    print("|   [H]  Help       |")
    print(" ------------------- ")

    choice = input("Enter Choice:")
    return choice.upper()

def help():
    print()
    print(" | Help:")
    print(" | The objective of the game is to guess the correct number")
    print(" | in as few turns as possible. Each wrong guess will say")
    print(" | higher or lower to help you find the answer.")
    print(" | Numbers are chosen between -100 and 100.")
    print()

def game():
    number = random.randint(-100, 100)
    guesses = 0

    print()
    print("New game started.")
    print("-----------------")

    while True:
        guess = int(input("Enter Guess:"))
        guesses += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct! (" + str(guesses) + " guesses)")
            print()
            break

while True:
    choice = menu()

    if choice == "N":
        game()
    elif choice == "H":
        help()
    elif choice == "Q":
        break
    else:
        print("Invalid option. Please choose again:")

print("Thanks for playing!")