# Solving Sudoku using backtracking algrithom
# board much be a solvable board.
board = [
    [0, 0, 0, 0, 5, 0, 0, 0, 8],
    [0, 9, 5, 0, 0, 6, 0, 0, 1],
    [0, 4, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 3, 1, 0, 9, 0, 6, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 8, 0, 4, 0, 3, 7, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 7, 0],
    [9, 0, 0, 6, 0, 0, 5, 3, 0],
    [8, 0, 0, 0, 7, 0, 0, 0, 0]
]


# Solver will be recursive and check it self
def solver(bo):
    zero = find_zero(bo)  # row, column
    if not zero:
        return True
    else:
        row, col = zero

    # check values 1 through 9
    # Run through Checker.
    for i in range(1, 10):
        if checker(bo, i, (row, col)):
            bo[row][col] = i

            if solver(bo):
                return True

            bo[row][col] = 0

    return False


# Checker will look if the number is allowed.
# no numbers in row, column or sub box can be the same.
def checker(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check internal box
    sub_box_row = pos[1] // 3
    sub_box_col = pos[0] // 3

    for i in range(sub_box_col * 3, sub_box_col * 3 + 3):
        for j in range(sub_box_row * 3, sub_box_row * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


# Print the board
def print_baord(bo):
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





# Find a square with a zero (empty) and set as our current target.
# loop through the board and find the position of zero
def find_zero(bo):
    for i in range(len(bo)):  # number of rows
        for j in range(len(bo[0])):  # number of columns
            if bo[i][j] == 0:
                return (i, j)  # row, column
    return False

print_baord(board)
solver(board)
print('                         ')
print_baord(board)
