# todo solve not found libraries
import random
import numpy as np


# randomly returns a string with the starting player: 'user' or 'pc'
def starting_one():
    players = ['user', 'pc']
    return players[random.randrange(0, 2)]


# returns true is the given coordinates match with an empty space in the playground
def empty_cell(plg, x, y):              # todo maybe put similar functions toguether with if: statement
    return plg[2-y][x] == 0


def empty_cell_pc(x, y):
    return plg[x][y] == 0


# updates the variable plg filling the position (x,y) with or 1 or -1
def update_plg_user(bin, x, y):
    plg[2 - y][x] = bin


def update_plg_pc(bin, x, y):
    plg[x][y] = bin


# returns the name of the winner or an empty string if there is still no winner in the game
def who_wins():
    winner = ''
    plg_a = np.array(plg)

    if np.trace(plg_a) == 3 or np.trace(np.fliplr(plg_a)) == 3:  # checking the diagonals
        winner = 'user'
    elif np.trace(plg_a) == -3 or np.trace(np.fliplr(plg_a)) == -3:
        winner = 'pc'
    else:
        for i in range(3):
            if plg_a.sum(axis=1)[i] == 3 or plg_a.sum(axis=0)[i] == 3:  # before 'or': check X axis, after check Y axis)
                winner = 'user'
                break
            elif plg_a.sum(axis=1)[i] == -3 or plg_a.sum(axis=0)[i] == -3:
                winner = 'pc'
                break
            else:
                winner = ''

    return winner


# asks the user for the x,y coordinates of his/her move, checks if x,y are inside the playground and return them.
def user_move():
    options = ['1', '2', '3']
    choosen_x = ''
    choosen_y = ''
    while choosen_x not in options:
        # check if its an integer
        choosen_x = input("Indicate de X coordinate of your move (1,2,3)")
    while choosen_y not in options:
        # check if its an integer
        choosen_y = input("Indicate de Y coordinate of your move (1,2,3)")

    return (int(choosen_x) - 1), (int(choosen_y) - 1)


# This function does the pc strategic move (included the check for empty cells)
def pc_move():
    # attaking ->> looking for alignment of two '-1' and putting the third
    found = False
    plg_a = np.array(plg)

    if np.trace(plg_a) == -2:  # checking oportunity in diagonal
        found = True
        if plg[0][0] == 0:
            return 0, 0
        elif plg[1][1] == 0:
            return 1, 1
        else:
            return 2, 2
    elif np.trace(np.fliplr(plg_a)) == -2:  # checking oportunity in other diagonal
        found = True
        if plg[2][0] == 0:
            return 2, 0
        elif plg[1][1] == 0:
            return 1, 1
        else:
            return 0, 2
    else:
        for i in range(3):
            if plg_a.sum(axis=1)[i] == -2:  # checking opportunity in horitzontal (x3 rows)
                found = True
                if plg[i][0] == 0:
                    return i, 0
                    break
                elif plg[i][1] == 0:
                    return i, 1
                    break
                else:
                    return i, 2
                    break
            elif plg_a.sum(axis=0)[i] == -2:  # checking opportunity in vertical (x3 columns)
                found = True
                if plg[0][i] == 0:
                    return 0, i
                    break
                elif plg[1][i] == 0:
                    return 1, i
                    break
                else:
                    return 2, i
                    break

    # defending ->> looking for alignment of two '1' and blocking the third
    if np.trace(plg_a) == 2:  # checking oportunity in diagonal
        found = True
        if plg[0][0] == 0:
            return 0, 0
        elif plg[1][1] == 0:
            return 1, 1
        else:
            return 2, 2
    elif np.trace(np.fliplr(plg_a)) == 2:  # checking oportunity in other diagonal
        found = True
        if plg[2][0] == 0:
            return 2, 0
        elif plg[1][1] == 0:
            return 1, 1
        else:
            return 0, 2
    else:
        for i in range(3):
            if plg_a.sum(axis=1)[i] == 2:  # checking opportunity in horitzontal (x3 rows)
                found = True
                if plg[i][0] == 0:
                    return i, 0
                    break
                elif plg[i][1] == 0:
                    return i, 1
                    break
                else:
                    return i, 2
                    break
            elif plg_a.sum(axis=0)[i] == 2:  # checking opportunity in vertical (x3 columns)
                found = True
                if plg[0][i] == 0:
                    return 0, i
                    break
                elif plg[1][i] == 0:
                    return 1, i
                    break
                else:
                    return 2, i
                    break
    # There's no opportunity to win or block: RANDOM GAME
    if not found:
        pc_x = random.randrange(0, 3)
        pc_y = random.randrange(0, 3)
        while not empty_cell_pc(pc_x, pc_y):
            pc_x = random.randrange(0, 3)
            pc_y = random.randrange(0, 3)
        return pc_x, pc_y

