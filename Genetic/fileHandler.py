def writeMaze(maze, indivuo):
  labirinto = maze
  with open('path.txt', 'a') as file: 
    for x in labirinto:
        for y in x:
         file.write(y + ' ')
            
        file.write('\n')
    file.write('\n')


def writeFile(lista, maze): 
    pos = (0,0)
    labirinto = maze
    for individuo in lista:
        for i, gene in enumerate(individuo.cromossomo):
           
            if i >= individuo.salva_index: 
                break
            if gene == "L":
                labirinto[pos[0]][pos[1]-1] = "-"
                pos = (pos[0], pos[1]-1)

            if gene == "R":
                labirinto[pos[0]][pos[1]+1] = "-"
                pos = (pos[0], pos[1]+1)

            if gene == "UP":
                labirinto[pos[0]-1][pos[1]] = "-"
                pos = (pos[0]-1, pos[1])

            if gene == "DOWN":
                labirinto[pos[0]+1][pos[1]] = "-"
                pos = (pos[0]+1, pos[1])

            if gene == "LUP":
                labirinto[pos[0]-1][pos[1]-1] = "-"
                pos = (pos[0]-1, pos[1]-1)
                                      
            if gene == "RUP":
                labirinto[pos[0]-1][pos[1]+1] = "-"
                pos = (pos[0]-1, pos[1]+1)

            if gene == "LDOWN":
                labirinto[pos[0]+1][pos[1]-1] = "-"    
                pos = (pos[0]+1, pos[1]-1)

            if gene == "RDOWN":
                labirinto[pos[0]+1][pos[1]+1] = "-"   
                pos = (pos[0]+1, pos[1]+1)

       
        writeMaze(labirinto, individuo)