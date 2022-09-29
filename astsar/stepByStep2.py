def writeStep(maze):
  with open('a_starpath.txt', 'a') as file: 
    for x in maze:
        for y in x:
         file.write(y + ' ')
            
        file.write('\n')
    file.write('\n')


def writeFile(list, maze):
    for path in list:
        for pos in path:
            aux = maze
            aux[pos[0]][pos[1]] = "-" 
            writeStep(aux)
    