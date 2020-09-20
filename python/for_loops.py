
board = [[1, 0, 1], [0, 1, 1], [1, 1, 1], [0, 0, 0]]

# Run through the indicies
for i in range(len(board)):
    print(i)

# Run though the items
for row in board:
    print(row)

# Run through indicies and items
for i, row in enumerate(board):
    print(i)
    print(row)

# Run though, ignoring one variable
for i, _ in enumerate(board):
    print(i)

# Unpack the sublists into variables
for i, j, k in board:
    print(i)
    print(j)
    print(k)

# Unpack board into variables
row1, row2, row3 = board
print(row1)
print(row2)
print(row3)

# Run through everything except the last item
for row in board[:-1]:
    print(row)

# Run through everything except the first item
for row in board[1:]:
    print(row)

