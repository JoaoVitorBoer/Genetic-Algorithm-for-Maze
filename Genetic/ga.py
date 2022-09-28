import random
from random import random as rand
from maze import cria_matriz

class Individuo():
    def __init__(self, maze, tamanho_matriz, geracao=0):
        self.nota_avaliacao = 0
        self.tamanho_matriz = tamanho_matriz
        self.geracao = geracao
        self.cromossomo = []
        self.maze = maze
        self.pos = (0,0)
        self.possiveis_movimentos = ["L","R","UP","DOWN", "LUP", "RUP", "LDOWN", "RDOWN"]
        self.visitados = []

        for i in range(50):
            self.cromossomo.append(random.choice(self.possiveis_movimentos))
        #print(self.cromossomo)
    
    def avaliacao(self):
        for gene in self.cromossomo:
                if gene == "L":
                    if  self.pos[0] < 0 or self.pos[1]-1 < 0 or self.pos[0] > (self.tamanho_matriz-1) or self.pos[1]-1 > (self.tamanho_matriz -1): break
                
                    else:
                        if self.maze[self.pos[0]][self.pos[1]-1] == '0' or self.maze[self.pos[0]][self.pos[1]-1] == 'C':
                            if (self.pos[0],self.pos[1]-1) in self.visitados:
                                self.nota_avaliacao -= 0.5
                                self.pos = (self.pos[0],self.pos[1]-1)
                            elif (self.pos[0],self.pos[1]-1) not in self.visitados:
                                self.nota_avaliacao += 1 if self.maze[self.pos[0]][self.pos[1]-1] == '0' else 5 
                                self.pos = (self.pos[0],self.pos[1]-1)
                                self.visitados.append(self.pos)
                                
                        else: break

                if gene == "R":
                    if self.pos[0] < 0 or self.pos[1]+1 < 0 or self.pos[0] > (self.tamanho_matriz-1) or self.pos[1]+1 > (self.tamanho_matriz -1): break
                        
                    else: 
                            if self.maze[self.pos[0]][self.pos[1]+1] == '0' or self.maze[self.pos[0]][self.pos[1]+1] == 'C':
                                if (self.pos[0],self.pos[1]+1) in self.visitados:
                                    self.nota_avaliacao -= 0.5
                                    self.pos = (self.pos[0],self.pos[1]+1)
                                elif (self.pos[0],self.pos[1]+1) not in self.visitados:
                                    self.nota_avaliacao += 1 if self.maze[self.pos[0]][self.pos[1]+1] == '0' else 5 
                                    self.pos = (self.pos[0],self.pos[1]+1)
                                    self.visitados.append(self.pos)
                                    

                            else: break

                if gene == "UP":
                    if  self.pos[0]-1 < 0 or self.pos[1] < 0 or self.pos[0]-1 > (self.tamanho_matriz-1) or self.pos[1] > (self.tamanho_matriz -1): break
                        
                    else: 
                            if self.maze[self.pos[0]-1][self.pos[1]] == '0' or self.maze[self.pos[0]-1][self.pos[1]] == 'C':
                                if (self.pos[0]-1,self.pos[1]) in self.visitados:
                                    self.nota_avaliacao -= 0.5
                                    self.pos = (self.pos[0]-1,self.pos[1])
                                elif (self.pos[0]-1,self.pos[1]) not in self.visitados:
                                    self.nota_avaliacao += 1 if self.maze[self.pos[0]-1][self.pos[1]] == '0' else 5 
                                    self.pos = (self.pos[0]-1,self.pos[1])
                                    self.visitados.append(self.pos)
                                    
                            else: break

                if gene == "DOWN":
                    if  self.pos[0]+1 < 0 or self.pos[1] < 0 or self.pos[0]+1 > (self.tamanho_matriz-1) or self.pos[1] > (self.tamanho_matriz -1): break

                    else: 
                            if self.maze[self.pos[0]+1][self.pos[1]] == '0' or self.maze[self.pos[0]+1][self.pos[1]] == 'C':
                                if (self.pos[0]+1,self.pos[1]) in self.visitados:
                                    self.nota_avaliacao -= 0.5
                                    self.pos = (self.pos[0]+1,self.pos[1])
                                elif (self.pos[0]+1,self.pos[1]) not in self.visitados:
                                    self.nota_avaliacao += 1 if self.maze[self.pos[0]+1][self.pos[1]] == '0' else 5 
                                    self.pos = (self.pos[0]+1,self.pos[1])
                                    self.visitados.append(self.pos)
                                
                            else: break
        
                if gene == "LUP":
                    if  self.pos[0]-1 < 0 or self.pos[1]-1 < 0 or self.pos[0]-1 > (self.tamanho_matriz-1) or self.pos[1]-1 > (self.tamanho_matriz -1): break
                        
                           
                    else: 
                        if self.maze[self.pos[0]-1][self.pos[1]-1] == '0' or self.maze[self.pos[0]-1][self.pos[1]-1] == 'C':
                            if (self.pos[0]-1,self.pos[1]-1) in self.visitados:
                                    self.nota_avaliacao -= 0.5
                                    self.pos = (self.pos[0]-1,self.pos[1]-1)
                            elif (self.pos[0]+1,self.pos[1]) not in self.visitados:
                                    self.nota_avaliacao += 1 if self.maze[self.pos[0]-1][self.pos[1]-1] == '0' else 5 
                                    self.pos = (self.pos[0]-1,self.pos[1]-1)
                                    self.visitados.append(self.pos)
                            
                        else: break
                   
                if gene == "RUP":
                    if  self.pos[0]-1 < 0 or self.pos[1]+1 < 0 or self.pos[0]-1 > (self.tamanho_matriz-1) or self.pos[1]+1 > (self.tamanho_matriz -1): break
                        
                    else:
                            if self.maze[self.pos[0]-1][self.pos[1]+1] == '0' or self.maze[self.pos[0]-1][self.pos[1]+1] == 'C':
                                if (self.pos[0]-1,self.pos[1]+1)in self.visitados:
                                    self.nota_avaliacao -= 0.5
                                    self.pos = (self.pos[0]-1,self.pos[1]+1)
                                elif (self.pos[0]-1,self.pos[1]+1) not in self.visitados:
                                    self.nota_avaliacao += 1 if self.maze[self.pos[0]-1][self.pos[1]+1] == '0' else 5 
                                    self.pos = (self.pos[0]-1,self.pos[1]+1)
                                    self.visitados.append(self.pos)
                                    
                            else: break
                   
                if gene == "LDOWN":
                    if  self.pos[0]+1 < 0 or self.pos[1]-1 < 0 or self.pos[0]+1 > (self.tamanho_matriz-1) or self.pos[1]-1 > (self.tamanho_matriz -1): break
                        
                    else:
                        if self.maze[self.pos[0]+1][self.pos[1]-1] == '0' or self.maze[self.pos[0]+1][self.pos[1]-1] == 'C':
                            if (self.pos[0]+1,self.pos[1]-1) in self.visitados:
                                    self.nota_avaliacao -= 0.5
                                    self.pos = (self.pos[0]+1,self.pos[1]-1)
                            elif (self.pos[0]-1,self.pos[1]+1) not in self.visitados:                                    
                                self.nota_avaliacao += 1 if self.maze[self.pos[0]+1][self.pos[1]-1] == '0' else 5 
                                self.pos = (self.pos[0]+1,self.pos[1]-1)
                                self.visitados.append(self.pos)
                            
                        else: break
                    
                if gene == "RDOWN":
                    if  self.pos[0]+1 < 0 or self.pos[1]+1 < 0 or self.pos[0]+1 > (self.tamanho_matriz-1) or self.pos[1]+1 > (self.tamanho_matriz-1): break
                       
                    else: 
                         if self.maze[self.pos[0]+1][self.pos[1]+1] == '0' and (self.pos[0]+1, self.pos[1]+1) <= (self.tamanho_matriz-1, self.tamanho_matriz-1) and (self.pos[0]+1, self.pos[1]+1) > (0,0):
                            if (self.pos[0]+1,self.pos[1]+1) in self.visitados:
                                    self.nota_avaliacao -= 0.5
                                    self.pos = (self.pos[0]+1,self.pos[1]+1)
                            elif (self.pos[0]+1,self.pos[1]+1) not in self.visitados:                                    
                                self.nota_avaliacao += 1 if self.maze[self.pos[0]+1][self.pos[1]+1] == '0' else 5 
                                self.pos = (self.pos[0]+1,self.pos[1]+1)
                                self.visitados.append(self.pos)
                            
                         else: break     
        
    def crossover(self, outro_individuo):
        corte = round(rand()  * len(self.cromossomo))
        
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [Individuo( self.geracao + 1),
                  Individuo( self.geracao + 1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos
    
    def mutacao(self, taxa_mutacao):
        print("Antes %s " % self.cromossomo)
        for i in range(len(self.cromossomo)):
            if rand() < taxa_mutacao:
                for x in range(0,2):
                    if self.cromossomo[i][x] == 1:
                        self.cromossomo[i][x] = 0
                    elif self.cromossomo[i][x] == 0:
                        self.cromossomo[i][x] = -1
                    elif self.cromossomo[i][x] == -1:
                        self.cromossomo[i][x] == 1
        print("Depois %s " % self.cromossomo)
        return self
        
class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao, maze, tamanho_matriz):
        self.tamanho_populacao = tamanho_populacao
        self.tamanho_matriz = tamanho_matriz
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        self.maze = maze
        
    def inicializa_populacao(self):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(self.maze, self.tamanho_matriz))
        self.melhor_solucao = self.populacao[0]
        
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.nota_avaliacao,
                                reverse = True)
        
    def melhor_individuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
            
    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
           soma += individuo.nota_avaliacao
        return soma
    
    def seleciona_pai(self, soma_avaliacao):
        pai = -1
        valor_sorteado = rand() * soma_avaliacao
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].nota_avaliacao
            pai += 1
            i += 1
        return pai
    
    def visualiza_geracao(self): pass
        # melhor = self.populacao[0]
        # print("G:%s -> Valor: %s Espaço: %s Cromossomo: %s" % (self.populacao[0].geracao,
        #                                                        melhor.nota_avaliacao,
        #                                                        melhor.espaco_usado,
        #                                                        melhor.cromossomo))
    
    def resolver(self, taxa_mutacao):
        self.inicializa_populacao()
        
        for individuo in self.populacao:
            individuo.avaliacao()
        
        self.ordena_populacao()
        
        self.visualiza_geracao()
        
        for geracao in range(self.tamanho_populacao): ### while
            soma_avaliacao = self.soma_avaliacoes()
            nova_populacao = []
            
            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                pai1 = self.seleciona_pai(soma_avaliacao)
                pai2 = self.seleciona_pai(soma_avaliacao)
                
                filhos = self.populacao[pai1].crossover(self.populacao[pai2])
                
                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))
            
            self.populacao = list(nova_populacao)
            
            for individuo in self.populacao:
                individuo.avaliacao()
            
            self.ordena_populacao()
            
            self.visualiza_geracao()
            
            melhor = self.populacao[0]
            self.melhor_individuo(melhor)
        
        print("\nMelhor solução -> G: %s Valor: %s Espaço: %s Cromossomo: %s" %
              (self.melhor_solucao.geracao,
               self.melhor_solucao.nota_avaliacao,
               self.melhor_solucao.espaco_usado,
               self.melhor_solucao.cromossomo))
        
        return self.melhor_solucao.cromossomo

if __name__ == '__main__':
    with open("labirinto1.txt", 'r') as f:
        arquivo = f.readlines()
        tamanho_matriz, maze = cria_matriz(arquivo)
        print(maze[tamanho_matriz-1][tamanho_matriz-1])

        taxa_mutacao = 0.01
        tamanho_populacao = 100
        ag = AlgoritmoGenetico(tamanho_populacao, maze, tamanho_matriz)
        ag.resolver(taxa_mutacao)

        
    
    