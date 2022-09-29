def writeMaze(maze, geracao):
  labirinto = maze
  with open('stepByStep.txt', 'a') as file: 
    file.write(f'Geracao -> {geracao} \n')
    for x in labirinto:
        for y in x:
         file.write(y + ' ')
            
        file.write('\n')
    file.write('\n')


def writeFile(lista, maze): 
    pos = (0,0)
    maze_aux = maze
    for individuo in lista:
        for i, gene in enumerate(individuo.cromossomo):
            if i > individuo.salva_index:
                break

            if gene == "L":
                maze_aux[pos[0]][pos[1]-1] = "-"
                pos = (pos[0], pos[1]-1)

            if gene == "R":
                maze_aux[pos[0]][pos[1]+1] = "-"
                pos = (pos[0], pos[1]+1)

            if gene == "UP":
                maze_aux[pos[0]-1][pos[1]] = "-"
                pos = (pos[0]-1, pos[1])

            if gene == "DOWN":
                maze_aux[pos[0]+1][pos[1]] = "-"
                pos = (pos[0]+1, pos[1])

            if gene == "LUP":
                maze_aux[pos[0]-1][pos[1]-1] = "-"
                pos = (pos[0]-1, pos[1]-1)

            if gene == "RUP":
                maze_aux[pos[0]-1][pos[1]+1] = "-"
                pos = (pos[0]-1, pos[1]+1)

            if gene == "LDOWN":
                maze_aux[pos[0]+1][pos[1]-1] = "-"
                pos = (pos[0]+1, pos[1]-1)

            if gene == "RDOWN":
                maze_aux[pos[0]+1][pos[1]+1] = "-"
                pos = (pos[0]+1, pos[1]+1)

        writeMaze(maze_aux, individuo.geracao)
        maze_aux = maze
        pos = (0,0)