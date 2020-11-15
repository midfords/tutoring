#
# Battleship
#
# Python tutoring exercise.
# Sean Midford, 2020
#
from player import Player, Human, Computer
from board import BattleshipBoard


def print_instructions():
    print("Battleship")
    print("[N]orth")
    print("[E]ast")
    print("[S]outh")
    print("[W]est")

def print_status(board: BattleshipBoard, comput: BattleshipBoard):
    print("\n\n")
    print(comput)
    print(board)

def play_game(board: BattleshipBoard, comput: BattleshipBoard, player1: Player, player2: Player):
    # global p1_total, p2_total
    while 1:
        print_status(board, comput)

        # print("--------------------")
        # print("PLAYER 1 TURN:")
        # print("--------------------")

        # p1_total += 1

        while player2.next_turn(comput.hit) and not comput.is_game_over():
            # p1_total += 1
            print_status(board, comput)
            print("Hit! Go again.")

        print_status(board, comput)

        if comput.is_game_over():
            comput.reveal()
            board.reveal()
            print_status(board, comput)
            print("You win!")
            break

        # print("--------------------")
        # print("PLAYER 2 TURN:")
        # print("--------------------")

        # p2_total += 1
        while player1.next_turn(board.hit) and not board.is_game_over():
            # p2_total += 1
            print_status(board, comput)
            print("Hit! Go again.")

        print_status(board, comput)

        if board.is_game_over():
            comput.reveal()
            board.reveal()
            print_status(board, comput)
            print("You lose.")
            break

# p1_total = 0
# p2_total = 0
# games = 0

def main():
    # global games

    auto = Computer()
    player1 = Human()
    player2 = Human()

    player1_board = BattleshipBoard(hide_ships=True, hide_output=False)
    player2_board = BattleshipBoard(hide_ships=True, hide_output=False)

    sizes = [5, 4, 3, 2, 2]
    auto.place_ships(sizes, player1_board)
    auto.place_ships(sizes, player2_board)

    print_instructions()
    play_game(player2_board, player1_board, player1, player2)

    # games += 1

if __name__ == "__main__":
    # for _ in range(50):
    main()

    # print("Player 1 average: " + str(p1_total / games))
    # print("Player 2 average: " + str(p2_total / games))

