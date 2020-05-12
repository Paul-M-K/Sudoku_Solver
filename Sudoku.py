# Solving Sudoku using backtracking algrithom
# board much be a solvable board.
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Check if the board is valid and can be used.
def valid(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False


# Print the board
def Print_baord(bo):
    for i in range(len(bo)):
        # when numbers devisable by 3 appear print boarder
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end="")

            if j == len(bo[0]) - 1:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


Print_baord(board)

# Find a square with a zero (empty) and set as our current target.
# loop through the board and find the position of zero
def Find_zero(bo):
    for i in range(len(bo)): #number of rows
        for j in range(len(bo[0])): #number of columns
            if bo[i][j] == 0:
                return (i, j) # row, column



