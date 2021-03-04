from Sudoku_read import random_board



def solve(bo):
    find = find_empty(bo)  # puts the empty position value row and col in find var
    if not find:  # if not find means it catches None from find_empty function
        return True
    else:
        row, col = find

    for i in range(1, 10):  # loop from 1 to 9
        if valid(bo, i, (row, col)):  # calling the valid function and inserting the parameters
            bo[row][col] = i  # put the value of i in the empty space which is in the range of 1 to 9

            if solve(bo):  # calling the function inside itself for recursion
                return True

            bo[row][col] = 0  # resetting the value to 0 to try another number since the program backtracked
    return False


# checking if the number is valid or not
def valid(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:  # pos[0] = row and pos[1] = col
            return False

    # check for column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check 3*3 box for similar number
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


# print the board
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0:
            print(" - - - - - - - - - - - - - -")

        for j in range(len(bo[0])):

            if j % 3 == 0:
                print(" | ", end="")
            if j == 8:
                print(str(bo[i][j]) + " | ")


            else:
                print((bo[i][j]), end=" ")
    print(" - - - - - - - - - - - - - -")

def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return row, col  # row, col
    return None

board1 = random_board()
print_board(board1)
solve(board1)
print("______________________")
print_board(board1)
