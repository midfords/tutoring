from colorama import Fore, Back, Style

class Cell:

    def __init__(self):
        self.p = 0

    def __str__(self):
        colours = [(Fore.RED, Back.RESET), (Fore.BLUE, Back.RESET)]

        if self.p == 0:
            return "   "
        elif self.p == 1:
            return f"{colours[0][0]}{colours[0][1]} ⬤ {Style.RESET_ALL}"
        elif self.p == 2:
            return f"{colours[1][0]}{colours[1][1]} ⬤ {Style.RESET_ALL}"

    def __eq__(self, other):
        return self.p == other.p

    def set(self, player):
        self.p = player

class Board:

    def __init__(self):
        self.__board = [[Cell() for _ in range(7)] for _ in range(6)]
        self.__indicies = [0 for i in range(7)]

    def __str__(self):
        rows = []

        rows.append(self.__get_index_str())
        rows.append(self.__get_top_row_str())
        for i in range(len(self.__board) - 1, 0, -1):
            rows.append(self.__get_row_str(i))
            rows.append(self.__get_middle_row_str())
        rows.append(self.__get_row_str(0))
        rows.append(self.__get_bottom_row_str())

        return "\n".join(rows)

    def __get_index_str(self):
        out = " "
        for i in range(1, 8):
            out += " " + str(i) + "  "
        return out

    def __get_top_row_str(self):
        out = "┌"
        for _ in range(6):
            out += "───┬"
        out += "───┐"
        return out

    def __get_middle_row_str(self):
        out = "├"
        for _ in range(6):
            out += "───┼"
        out += "───┤"
        return out

    def __get_row_str(self, row: int):
        out = "│"
        for cell in self.__board[row]:
            out += str(cell) + "│"
        return out

    def __get_bottom_row_str(self):
        out = "└"
        for _ in range(6):
            out += "───┴"
        out += "───┘"
        return out

    def __traverse(self, row, col, x_mod, y_mod, piece):
        if row + y_mod < 0 or row + y_mod > 5 or col + x_mod < 0 or col + x_mod > 6:
            return 0
        if self.__board[row + y_mod][col + x_mod] != piece:
            return 0

        return self.__traverse(row + y_mod, col + x_mod, x_mod, y_mod, piece) + 1

    def __winner(self, col, row):
        piece = self.__board[row][col]
        return self.__traverse(row, col, 1, 0, piece) + 1 + self.__traverse(row, col, -1, 0, piece) >= 4 or \
            self.__traverse(row, col, 0, 1, piece) + 1 + self.__traverse(row, col, 0, -1, piece) >= 4 or \
            self.__traverse(row, col, 1, 1, piece) + 1 + self.__traverse(row, col, -1, -1, piece) >= 4 or \
            self.__traverse(row, col, 1, -1, piece) + 1 + self.__traverse(row, col, -1, 1, piece) >= 4

    def __tie(self):
        for i in self.__indicies:
            if i < 6:
                return False
        return True

    def place(self, col: int, player: int):
        if col < 1 or col > 7:
            raise ValueError("Column out of range.")

        row = self.__indicies[col - 1]

        if row >= 6:
            raise ValueError("Column is full.")

        self.__indicies[col - 1] += 1
        self.__board[row][col - 1].set(player)

        if self.__winner(col - 1, row):
            return 1
        elif self.__tie():
            return 2
        else:
            return 0


def pick_and_place(board, player: int):
    while 1:
        try:
            c = int(input("Pick column. "))
            if c < 1 or c > 7:
                raise ValueError("Out of range.")
            return board.place(c, player)
        except Exception as e:
            print(f"Invalid. {e}")

def run_game(board):
    while 1:
        print(board)
        print("Player 1 go.")
        result = pick_and_place(board, 1)
        if result == 1:
            print(board)
            print("Player 1 wins!")
            break
        elif result == 2:
            print(board)
            print("Tie game.")
            break

        print(board)
        print("Player 2 go.")
        result = pick_and_place(board, 2)
        if result == 1:
            print(board)
            print("Player 2 wins!")
            break
        elif result == 2:
            print(board)
            print("Tie game.")
            break

def main():
    board = Board()
    run_game(board)

if __name__ == "__main__":
    main()



