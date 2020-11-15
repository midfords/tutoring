import curses
import logging

from copy import copy, deepcopy

# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

logging.basicConfig(filename='app.log')
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class Board:

    BLOCK = "  "

    def __init__(self, stdscr, h, w):
        self.__board = [[0 for _ in range(w//2)] for _ in range(h-1)]
        self.__history = []
        self.__stdscr = stdscr

    def on(self, row, col):
        self.__stdscr.addstr(
            row, col*2, Board.BLOCK, curses.color_pair(1)
        )

    def off(self, row, col):
        self.__stdscr.addstr(
            row, col*2, Board.BLOCK, curses.color_pair(0)
        )

    def toggle(self, row, col):
        if self.__board[row][col]:
            self.__stdscr.addstr(
                row, col*2, Board.BLOCK, curses.color_pair(0)
            )
        else:
            self.__stdscr.addstr(
                row, col*2, Board.BLOCK, curses.color_pair(1)
            )

        self.__board[row][col] = 0 if self.__board[row][col] else 1

    def __neighbours(self, row, col):
        count = 0
        if row - 1 >= 0 \
                and self.__board[row - 1][col] > 0:
            count += 1
        if row + 1 < len(self.__board) \
                and self.__board[row + 1][col] > 0:
            count += 1
        if col - 1 >= 0 \
                and self.__board[row][col - 1] > 0:
            count += 1
        if col + 1 < len(self.__board[0]) \
                and self.__board[row][col + 1] > 0:
            count += 1
        if row - 1 >= 0 and col - 1 >= 0 \
                and self.__board[row - 1][col - 1] > 0:
            count += 1
        if row + 1 < len(self.__board) and col - 1 >= 0 \
                and self.__board[row + 1][col - 1] > 0:
            count += 1
        if row - 1 >= 0 and col + 1 < len(self.__board[0]) \
                and self.__board[row - 1][col + 1] > 0:
            count += 1
        if row + 1 < len(self.__board) and col + 1 < len(self.__board[0]) \
                and self.__board[row + 1][col + 1] > 0:
            count += 1
        return count

    def cycle(self):
        self.__history.append(deepcopy(self.__board))
        log.debug(str(self.__board))
        log.debug(str(self.__history))

        for row in range(len(self.__board)):
            for col in range(len(self.__board[row])):
                count = self.__neighbours(row, col)

                if count > 0:
                    log.info(f"Found {count} neighbours for {row}, {col}")

                if self.__board[row][col] <= 0 and count == 3:
                    self.__board[row][col] = -1
                elif self.__board[row][col] > 0 and (count < 2 or count > 3):
                    self.__board[row][col] = 2

        for row in range(len(self.__board)):
            for col in range(len(self.__board[row])):
                if self.__board[row][col] == 2:
                    self.__board[row][col] = 1
                    self.toggle(row, col)
                    self.__board[row][col] = 0
                elif self.__board[row][col] == -1:
                    self.__board[row][col] = 0
                    self.toggle(row, col)
                    self.__board[row][col] = 1

    def undo(self):
        if len(self.__history) == 0:
            return

        self.__board = self.__history.pop()

        for row in range(len(self.__board)):
            for col in range(len(self.__board[row])):
                if self.__board[row][col] > 0:
                    self.on(row, col)
                else:
                    self.off(row, col)


def init_curses():
    curses.curs_set(0)
    curses.mousemask(1)
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(0, -1, -1) # empty
    curses.init_pair(1, 7, 7)  # white



def main(stdscr):
    init_curses()

    rows, cols = stdscr.getmaxyx()
    board = Board(stdscr, rows, cols)

    while 1:
        event = stdscr.getch()

        if event == curses.KEY_MOUSE:
            log.info("Processing mouse click.")
            _, mx, my, _, _ = curses.getmouse()
            board.toggle(my, mx//2)
        elif event == curses.KEY_RIGHT:
            log.info("Processing right key.")
            board.cycle()
        elif event == curses.KEY_LEFT:
            log.info("Processing left key.")
            board.undo()

if __name__ == "__main__":
    curses.wrapper(main)


# MOUSE DEMO

# import curses

# screen = curses.initscr() 
# curses.curs_set(0) 
# screen.keypad(1) 
# curses.mousemask(1)

# screen.addstr("This is a Sample Curses Script\n\n") 

# while True:
#     event = screen.getch() 
#     if event == ord("q"): break 
#     if event == curses.KEY_MOUSE:
#         _, mx, my, _, _ = curses.getmouse()
#         y, x = screen.getyx()
#         screen.addstr(1, 0, str(my))
#         screen.addstr(2, 0, str(mx))

# curses.endwin()



# COLOURS DEMO

# import curses

# def main(stdscr):
#     curses.start_color()
#     curses.use_default_colors()
#     for i in range(0, curses.COLORS):
#         curses.init_pair(i + 1, -1, i)
#     try:
#         for i in range(0, 255):
#             stdscr.addstr(f" {i} ", curses.color_pair(i))
#     except curses.ERR:
#         # End of screen reached
#         pass
#     stdscr.getch()

# curses.wrapper(main)


