
def printBoard(board):
	print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
	print("-+-+-")
	print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
	print("-+-+-")
	print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])

def checkWin(board):
	# Check for winner
	win = " "
	if board[0][0] == board[0][1] == board[0][2]:
		win = board[0][0]
	elif board[1][0] == board[1][1] == board[1][2]:
		win = board[1][0]
	elif board[2][0] == board[2][1] == board[2][2]:
		win = board[2][0]
	elif board[0][0] == board[1][0] == board[2][0]:
		win = board[0][0]
	elif board[0][1] == board[1][1] == board[2][1]:
		win = board[0][1]
	elif board[0][2] == board[1][2] == board[2][2]:
		win = board[0][2]
	elif board[0][0] == board[1][1] == board[2][2]:
		win = board[0][0]
	elif board[0][2] == board[1][1] == board[2][0]:
		win = board[0][2]

	if win == "X":
		return 1 # X wins
	elif win == "O":
		return 2 # O wins

	# Check for tie game
	tie = True
	for i in range(len(board)):
		for j in range(len(board[i])):
			tie = tie and board[i][j] != " "
	if tie:
		return -1;

	# Game is not finished
	return 0

def takeTurn(board, turn):
	print(turn + "s turn.")
	x = int(input("Enter row. "))
	y = int(input("Enter column. "))
	while not validMove(board, x, y):
		print("Spot already taken! Try again.")
		x = int(input("Enter row. "))
		y = int(input("Enter column. "))
	board[x][y] = turn

def validMove(board, x, y):
	return x>=0 and x<=2 and y>=0 and y<=2 and board[x][y] == " "

def printWinner(player):
	print("Player " + player + " wins!")

def main():

	board = [
		[" "," "," "],
		[" "," "," "],
		[" "," "," "] ]
	playerOneTurn = True

	printBoard(board)
	while checkWin(board) == 0:
		if playerOneTurn:
			takeTurn(board, "X")
		else:
			takeTurn(board, "O")
		playerOneTurn = not playerOneTurn
		printBoard(board)

	if checkWin(board) == 1: # X wins
		printWinner("X")
	elif checkWin(board) == 2: # O wins
		printWinner("O")
	else: # Tie game
		print("Tied game.")

main()