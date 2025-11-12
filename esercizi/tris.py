#autore: ing. Nevio Noviello

import random
import msvcrt
import os
import time


def printgrid(grid, pos, curs):
    for i in range(len(grid)):
        s = ''
        for j in range(len(grid)):
            if i == pos[0] and j == pos[1] and curs:
                s += ' ' + pos[2] + ' '
            else:
                s += ' ' + grid[i][j] + ' '
            if j < len(grid) - 1:
                s += '|'
        print(s)
        if i < len(grid) - 1:
            print('-' * (4 * len(grid) - 1))

def tris1v1():
    sym = [' ', 'X', 'O']
    player = 0
    grid = []
    pos = [0, 0, '*']

    ticks = 0
    curs = True

    for i in range(3):
        grid.append([])
        for j in range(3):
            grid[i].append(sym[player])

    player = random.randint(1, 2)
    #os.system("cls")
    print('current player', player, '->', sym[player])
    printgrid(grid, pos, curs)

    while True:
        time.sleep(0.01)
        ticks += 1
        if msvcrt.kbhit() or ticks >= 20:
            if ticks >= 20:
                ticks = 0
                curs = not curs
            else:
                tasto = msvcrt.getch().decode()
                if tasto == 'q':
                    print("Uscita dal programma.")
                    break
                elif tasto == 's' and pos[0] > 0:
                    pos[0] -= 1
                elif tasto == 'x' and pos[0] < len(grid) - 1:
                    pos[0] += 1
                elif tasto == 'z' and pos[1] > 0:
                    pos[1] -= 1
                elif tasto == 'c' and pos[1] < len(grid[0]) - 1:
                    pos[1] += 1
                elif tasto == ' ' and grid[pos[0]][pos[1]] == ' ':
                    grid[pos[0]][pos[1]] = sym[player]
                    if player == 1:
                        player = 2
                    else:
                        player = 1
            os.system("cls")
            print('current player', player, '->', sym[player])
            printgrid(grid, pos, curs)


if __name__ == '__main__':
    tris1v1()

