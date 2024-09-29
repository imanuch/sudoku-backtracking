import time
from colorama import init, Fore
init(autoreset=True)


# Sudoku board initial
board = [
    [6, 7, 1, 0, 0, 0, 4, 9, 8],
    [0, 2, 0, 1, 9, 8, 5, 7, 6],
    [9, 0, 0, 4, 7, 6, 1, 2, 3],
    [0, 0, 7, 0, 0, 1, 8, 6, 4],
    [0, 0, 0, 0, 6, 0, 7, 3, 1],
    [1, 6, 0, 0, 4, 7, 2, 5, 9],
    [0, 0, 0, 0, 1, 0, 0, 4, 0],
    [0, 0, 0, 0, 5, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
board = [
    [6,7,1,0,0,0,4,9,8],
    [0,2,0,1,9,8,5,7,6],
    [9,0,0,4,7,6,1,2,3],
    [0,0,7,0,0,1,8,6,4],
    [0,0,0,0,6,0,7,3,1],
    [1,6,0,0,4,7,2,5,9],
    [0,3,0,0,1,0,0,4,0],
    [0,1,0,0,5,0,0,8,0],
    [0,0,6,7,8,0,3,1,5]
]
board = [
    [6,7,1,0,0,0,4,9,8],
    [0,2,0,1,9,8,5,7,6],
    [9,0,0,4,7,6,1,2,3],
    [0,0,7,0,0,1,8,6,4],
    [0,0,0,0,6,0,7,3,1],
    [1,6,0,0,4,7,2,5,9],
    [0,0,0,0,1,0,0,4,0],
    [0,0,0,0,5,0,0,8,0],
    [0,0,0,0,0,0,0,0,0]
]

def case_vide(grille):
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] == 0:
                return (i, j)  # row, col

    return None



def solve(grille):
    find = case_vide(grille)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(grille, i, (row, col)):
            grille[row][col] = i
            print_board(grille,row,col) #affichage de la grille
            #pause for a second
            #time.sleep(1)
            print("_________________________")
            print("_________________________")
            print("_________________________")
            if solve(grille):
                return True

            grille[row][col] = 0

    return False


def valid(grille, num, pos):
    # Check row
    for i in range(len(grille[0])):
        if grille[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(grille)):
        if grille[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if grille[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(grille,x,y):
    for i in range(len(grille)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grille[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grille[i][j])
            elif i==x and y==j:
                print(Fore.RED + str(grille[i][j]) + " ", end="")
            else : 
                print(str(grille[i][j]) + " ", end="")


def case_vide(grille):
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board,10,10)
solve(board)
print("_________________________")
print_board(board,10,10)