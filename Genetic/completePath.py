import random
from random import random as rand
from maze import cria_matriz


def generateCompletePathFile(cromossomo, maze, tamanho_matriz, index):

    pos = (0, 0)

    for i, gene in enumerate(cromossomo):

        if i > index:
            break

        if gene == "L":
            maze[pos[0]][pos[1]-1] = "-"
            pos = (pos[0], pos[1]-1)

        if gene == "R":
            maze[pos[0]][pos[1]+1] = "-"
            pos = (pos[0], pos[1]+1)

        if gene == "UP":
            maze[pos[0]-1][pos[1]] = "-"
            pos = (pos[0]-1, pos[1])

        if gene == "DOWN":
            maze[pos[0]+1][pos[1]] = "-"
            pos = (pos[0]+1, pos[1])

        if gene == "LUP":
            maze[pos[0]-1][pos[1]-1] = "-"
            pos = (pos[0]-1, pos[1]-1)

        if gene == "RUP":
            maze[pos[0]-1][pos[1]+1] = "-"
            pos = (pos[0]-1, pos[1]+1)

        if gene == "LDOWN":
            maze[pos[0]+1][pos[1]-1] = "-"
            pos = (pos[0]+1, pos[1]-1)

        if gene == "RDOWN":
            maze[pos[0]+1][pos[1]+1] = "-"
            pos = (pos[0]+1, pos[1]+1)

    with open('./completePath.txt', 'w') as file:
        for x in maze:
            for y in x:
                file.write(y + ' ')

            file.write('\n')
