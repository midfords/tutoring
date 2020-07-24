#
# Battleship
#
# Python tutoring exercise.
# Sean Midford, 2020
#
from player import Player, Human, Computer
from board import BattleshipBoard


def print_instructions():
    """This method prints all the instructions for the game.
    """

def print_status(player1_board: BattleshipBoard, player2_board: BattleshipBoard):
    """This method prints a status screen. It prints out both players' BattleshipBoards
    and any other important information. Print the player2_board before the player1_board.

    Parameters
    ----------
    player1_board : BattleshipBoard
        Player 1's BattleshipBoard.
    player2_board : BattleshipBoard
        Player 2's BattleshipBoard.
    """

def process_turn(player: Player, board: BattleshipBoard, opponent: BattleshipBoard):
    """Process the player's next turn. If the player hits a ship allow them to take another
    turn. If the opponent game overs, stop asking the user for next turns. Print the status
    in between each next turn call.

    Parameters
    ----------
    player : Player
        The player to process the next turn for.
    player1_board : BattleshipBoard
        Player 1's BattleshipBoard.
    player2_board : BattleshipBoard
        Player 2's BattleshipBoard.
    """
    pass

def process_game_over(player1_board: BattleshipBoard, player2_board: BattleshipBoard, message: str):
    """Process a game over. Reveal and print both BattleshipBoards and print the message.

    Parameters
    ----------
    player1_board : BattleshipBoard
        Player 1's BattleshipBoard.
    player2_board : BattleshipBoard
        Player 2's BattleshipBoard.
    message : str
        The game over message to print.
    """
    pass

def play_game(player1: Player, player2: Player, player1_board: BattleshipBoard, player2_board: BattleshipBoard):
    while 1:
        process_turn(player1, player1_board, player2_board)
        if player2_board.is_game_over():
            process_game_over(player1_board, player2_board, "You win!")
            break

        process_turn(player2, player2_board, player1_board)
        if player1_board.is_game_over():
            process_game_over(player1_board, player2_board, "You lose.")
            break

def main():
    player1 = Human()
    player2 = Computer()

    player1_board = BattleshipBoard()
    player2_board = BattleshipBoard(hide_ships=True)

    sizes = [5, 4, 3, 2, 2]
    player1.place_ships(sizes, player1_board)
    player2.place_ships(sizes, player2_board)

    print_instructions()
    print_status(player1_board, player2_board)
    play_game(player1, player2, player1_board, player2_board)

if __name__ == "__main__":
    main()

