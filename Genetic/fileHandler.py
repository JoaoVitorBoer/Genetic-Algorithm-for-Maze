def writeMaze(maze, indivuo):
  with open('path.txt', 'a') as file: 
    for x in maze:
        file.writelines(x)



def writeFile(lista, maze): 
    pos = (0,0)

    for i, individuo in enumerate(lista):
        #file.write(f'Geração {individuo.geracao} \n')
        for gene in individuo.cromossomo:
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

        writeMaze(maze, individuo)