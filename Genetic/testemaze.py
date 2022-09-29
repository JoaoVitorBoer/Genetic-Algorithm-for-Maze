import random
from random import random as rand
from maze import cria_matriz



a = ['RDOWN', 'L', 'R', 'R', 'RDOWN', 'RUP', 'R', 'R', 'R', 'R', 'UP', 'DOWN', 'RDOWN', 'LDOWN', 'L', 'LDOWN', 'DOWN', 'R', 'LUP', 'RUP', 'L', 'DOWN', 'LDOWN', 'DOWN', 'UP', 'R', 'DOWN', 'RUP', 'LDOWN', 'RUP', 'RDOWN', 'R', 'LUP', 'R', 'LDOWN', 'LDOWN', 'RDOWN', 'DOWN', 'L', 'L', 'RUP', 'DOWN', 'UP', 'LDOWN', 'L', 'L', 'L', 'L', 'L', 'LUP', 'DOWN', 'UP', 'UP', 'UP', 'RUP', 'LUP', 'L', 'RDOWN', 'UP', 'RUP', 'L', 'L', 'RUP', 'RDOWN', 'RDOWN', 'RUP', 'R', 'UP', 'R', 'LUP', 'L', 'DOWN', 'R', 'R', 'LUP']
print(len(a))

with open("./Genetic/labirinto1.txt", 'r') as f:
       arquivo = f.readlines()
       tamanho_matriz, maze = cria_matriz(arquivo)
       pos = (0,0)

       for i, gene in enumerate(a):
            if i > 59: break
            if gene == "L":
               if pos[0] < 0 or pos[1]-1 < 0 or pos[0] > (tamanho_matriz-1) or pos[1]-1 > (tamanho_matriz -1): continue

               else:
                    if maze[pos[0]][pos[1]-1] == "0" or "C":
                        maze[pos[0]][pos[1]-1] = "-"
                        pos = (pos[0], pos[1]-1)

            if gene == "R":
                if pos[0] < 0 or pos[1]+1 < 0 or pos[0] > (tamanho_matriz-1) or pos[1]+1 > (tamanho_matriz -1): continue

                else:
                    if maze[pos[0]][pos[1]+1] == "0" or "C":
                        maze[pos[0]][pos[1]+1] = "-"
                        pos = (pos[0], pos[1]+1)

            if gene == "UP":
                if  pos[0]-1 < 0 or pos[1] < 0 or pos[0]-1 > (tamanho_matriz-1) or pos[1] > (tamanho_matriz -1): continue

                else:
                    if maze[pos[0]-1][pos[1]] == "0" or "C":
                        maze[pos[0]-1][pos[1]] = "-"
                        pos = (pos[0]-1, pos[1])

            if gene == "DOWN":
                if  pos[0]+1 < 0 or pos[1] < 0 or pos[0]+1 > (tamanho_matriz-1) or pos[1] > (tamanho_matriz -1): continue
                else:
                    if maze[pos[0]+1][pos[1]] == "0" or "C":
                        maze[pos[0]+1][pos[1]] = "-"
                        pos = (pos[0]+1, pos[1])

            if gene == "LUP":
                if  pos[0]-1 < 0 or pos[1]-1 < 0 or pos[0]-1 > (tamanho_matriz-1) or pos[1]-1 > (tamanho_matriz -1): continue
                else:
                    if maze[pos[0]-1][pos[1]-1] == "0" or "C":
                        maze[pos[0]-1][pos[1]-1] = "-"
                        pos = (pos[0]-1, pos[1]-1)
                                            
            if gene == "RUP":
                if  pos[0]-1 < 0 or pos[1]+1 < 0 or pos[0]-1 > (tamanho_matriz-1) or pos[1]+1 > (tamanho_matriz -1): continue
                else:
                    if maze[pos[0]-1][pos[1]+1] == "0" or "C":
                        maze[pos[0]-1][pos[1]+1] = "-"
                        pos = (pos[0]-1, pos[1]+1)

            if gene == "LDOWN":
                if  pos[0]+1 < 0 or pos[1]-1 < 0 or pos[0]+1 > (tamanho_matriz-1) or pos[1]-1 > (tamanho_matriz -1): continue
                else:
                    if maze[pos[0]+1][pos[1]-1] == "0" or "C": 
                        maze[pos[0]+1][pos[1]-1] = "-"    
                        pos = (pos[0]+1, pos[1]-1)

            if gene == "RDOWN":
                if  pos[0]+1 < 0 or pos[1]+1 < 0 or pos[0]+1 > (tamanho_matriz-1) or pos[1]+1 > (tamanho_matriz-1): continue
                else:
                    if maze[pos[0]+1][pos[1]+1] == "0" or "C":
                        maze[pos[0]+1][pos[1]+1] = "-"   
                        pos = (pos[0]+1, pos[1]+1)
     
with open('path2.txt', 'a') as file: 
    for x in maze:
        for y in x:
         file.write(y + ' ')
            
        file.write('\n')
    
