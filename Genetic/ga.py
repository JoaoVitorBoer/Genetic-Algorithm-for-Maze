import random
from random import random as rand
from maze import cria_matriz
import sys

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
        self.comidas_encontradas = 0
        self.salva_index = -1

        for i in range(50):
            self.cromossomo.append(random.choice(self.possiveis_movimentos))      
           

    def avaliacao(self):
        for gene in self.cromossomo:
                if gene == "L":
                    if  self.pos[0] < 0 or self.pos[1]-1 < 0 or self.pos[0] > (self.tamanho_matriz-1) or self.pos[1]-1 > (self.tamanho_matriz -1): break
                
                    else:
                        if self.maze[self.pos[0]][self.pos[1]-1] == '0' or self.maze[self.pos[0]][self.pos[1]-1] == 'C':
                            if (self.pos[0],self.pos[1]-1) in self.visitados:
                                self.nota_avaliacao -= 1
                                self.pos = (self.pos[0],self.pos[1]-1)
                            elif (self.pos[0],self.pos[1]-1) not in self.visitados:
                                self.nota_avaliacao += 2 if self.maze[self.pos[0]][self.pos[1]-1] == '0' else 10
                                if self.maze[self.pos[0]][self.pos[1]-1] == 'C':
                                    self.comidas_encontradas += 1
                                    #self.visitados = []
                                self.pos = (self.pos[0],self.pos[1]-1)
                                self.visitados.append(self.pos)
                                
                        else: break

                if gene == "R":
                    if self.pos[0] < 0 or self.pos[1]+1 < 0 or self.pos[0] > (self.tamanho_matriz-1) or self.pos[1]+1 > (self.tamanho_matriz -1): break
                        
                    else: 
                            if self.maze[self.pos[0]][self.pos[1]+1] == '0' or self.maze[self.pos[0]][self.pos[1]+1] == 'C':
                                if (self.pos[0],self.pos[1]+1) in self.visitados:
                                    self.nota_avaliacao -= 1
                                    self.pos = (self.pos[0],self.pos[1]+1)
                                elif (self.pos[0],self.pos[1]+1) not in self.visitados:
                                    self.nota_avaliacao += 2 if self.maze[self.pos[0]][self.pos[1]+1] == '0' else 10
                                    if self.maze[self.pos[0]][self.pos[1]+1] == 'C':
                                        self.comidas_encontradas += 1
                                        #self.visitados = []
                                    self.pos = (self.pos[0],self.pos[1]+1)
                                    self.visitados.append(self.pos)
                                    

                            else: break

                if gene == "UP":
                    if  self.pos[0]-1 < 0 or self.pos[1] < 0 or self.pos[0]-1 > (self.tamanho_matriz-1) or self.pos[1] > (self.tamanho_matriz -1): break
                        
                    else: 
                            if self.maze[self.pos[0]-1][self.pos[1]] == '0' or self.maze[self.pos[0]-1][self.pos[1]] == 'C':
                                if (self.pos[0]-1,self.pos[1]) in self.visitados:
                                    self.nota_avaliacao -= 1
                                    self.pos = (self.pos[0]-1,self.pos[1])
                                elif (self.pos[0]-1,self.pos[1]) not in self.visitados:
                                    self.nota_avaliacao += 2 if self.maze[self.pos[0]-1][self.pos[1]] == '0' else 10 
                                    if self.maze[self.pos[0]-1][self.pos[1]] == 'C':
                                        self.comidas_encontradas += 1
                                        #self.visitados = []
                                    self.pos = (self.pos[0]-1,self.pos[1])
                                    self.visitados.append(self.pos)
                                    
                            else: break

                if gene == "DOWN":
                    if  self.pos[0]+1 < 0 or self.pos[1] < 0 or self.pos[0]+1 > (self.tamanho_matriz-1) or self.pos[1] > (self.tamanho_matriz -1): break

                    else: 
                            if self.maze[self.pos[0]+1][self.pos[1]] == '0' or self.maze[self.pos[0]+1][self.pos[1]] == 'C':
                                if (self.pos[0]+1,self.pos[1]) in self.visitados:
                                    self.nota_avaliacao -= 1
                                    self.pos = (self.pos[0]+1,self.pos[1])
                                elif (self.pos[0]+1,self.pos[1]) not in self.visitados:
                                    self.nota_avaliacao += 2 if self.maze[self.pos[0]+1][self.pos[1]] == '0' else 10
                                    if self.maze[self.pos[0]+1][self.pos[1]] == 'C':
                                        self.comidas_encontradas += 1
                                        #self.visitados = []
                                    self.pos = (self.pos[0]+1,self.pos[1])
                                    self.visitados.append(self.pos)
                                
                            else: break
        
                if gene == "LUP":
                    if  self.pos[0]-1 < 0 or self.pos[1]-1 < 0 or self.pos[0]-1 > (self.tamanho_matriz-1) or self.pos[1]-1 > (self.tamanho_matriz -1): break
                        
                           
                    else: 
                        if self.maze[self.pos[0]-1][self.pos[1]-1] == '0' or self.maze[self.pos[0]-1][self.pos[1]-1] == 'C':
                            if (self.pos[0]-1,self.pos[1]-1) in self.visitados:
                                    self.nota_avaliacao -= 1
                                    self.pos = (self.pos[0]-1,self.pos[1]-1)
                            elif (self.pos[0]+1,self.pos[1]) not in self.visitados:
                                    self.nota_avaliacao += 2 if self.maze[self.pos[0]-1][self.pos[1]-1] == '0' else 10 
                                    if self.maze[self.pos[0]-1][self.pos[1]-1] == 'C':
                                        self.comidas_encontradas += 1
                                       # self.visitados = []
                                    self.pos = (self.pos[0]-1,self.pos[1]-1)
                                    self.visitados.append(self.pos)
                            
                        else: break
                   
                if gene == "RUP":
                    if  self.pos[0]-1 < 0 or self.pos[1]+1 < 0 or self.pos[0]-1 > (self.tamanho_matriz-1) or self.pos[1]+1 > (self.tamanho_matriz -1): break
                        
                    else:
                            if self.maze[self.pos[0]-1][self.pos[1]+1] == '0' or self.maze[self.pos[0]-1][self.pos[1]+1] == 'C':
                                if (self.pos[0]-1,self.pos[1]+1)in self.visitados:
                                    self.nota_avaliacao -= 1
                                    self.pos = (self.pos[0]-1,self.pos[1]+1)
                                elif (self.pos[0]-1,self.pos[1]+1) not in self.visitados:
                                    self.nota_avaliacao += 2 if self.maze[self.pos[0]-1][self.pos[1]+1] == '0' else 10
                                    if self.maze[self.pos[0]-1][self.pos[1]+1] == 'C':
                                        self.comidas_encontradas += 1
                                        #self.visitados = []
                                    self.pos = (self.pos[0]-1,self.pos[1]+1)
                                    self.visitados.append(self.pos)
                                    
                            else: break
                   
                if gene == "LDOWN":
                    if  self.pos[0]+1 < 0 or self.pos[1]-1 < 0 or self.pos[0]+1 > (self.tamanho_matriz-1) or self.pos[1]-1 > (self.tamanho_matriz -1): break
                        
                    else:
                        if self.maze[self.pos[0]+1][self.pos[1]-1] == '0' or self.maze[self.pos[0]+1][self.pos[1]-1] == 'C':
                            if (self.pos[0]+1,self.pos[1]-1) in self.visitados:
                                    self.nota_avaliacao -= 1
                                    self.pos = (self.pos[0]+1,self.pos[1]-1)
                            elif (self.pos[0]-1,self.pos[1]+1) not in self.visitados:                                    
                                self.nota_avaliacao += 2 if self.maze[self.pos[0]+1][self.pos[1]-1] == '0' else 10 
                                if self.maze[self.pos[0]+1][self.pos[1]-1] == 'C':
                                        self.comidas_encontradas += 1
                                        #self.visitados = []
                                self.pos = (self.pos[0]+1,self.pos[1]-1)
                                self.visitados.append(self.pos)
                            
                        else: break
                    
                if gene == "RDOWN":
                    if  self.pos[0]+1 < 0 or self.pos[1]+1 < 0 or self.pos[0]+1 > (self.tamanho_matriz-1) or self.pos[1]+1 > (self.tamanho_matriz-1): break
                       
                    else: 
                         if self.maze[self.pos[0]+1][self.pos[1]+1] == '0' and (self.pos[0]+1, self.pos[1]+1) <= (self.tamanho_matriz-1, self.tamanho_matriz-1) and (self.pos[0]+1, self.pos[1]+1) > (0,0):
                            if (self.pos[0]+1,self.pos[1]+1) in self.visitados:
                                    self.nota_avaliacao -= 1
                                    self.pos = (self.pos[0]+1,self.pos[1]+1)
                            elif (self.pos[0]+1,self.pos[1]+1) not in self.visitados:                                    
                                self.nota_avaliacao += 2 if self.maze[self.pos[0]+1][self.pos[1]+1] == '0' else 10 
                                if self.maze[self.pos[0]+1][self.pos[1]+1] == 'C':
                                        self.comidas_encontradas += 1
                                        #self.visitados = []
                                self.pos = (self.pos[0]+1,self.pos[1]+1)
                                self.visitados.append(self.pos)
                            
                         else: break   
                self.salva_index += 1  
        
    def crossover(self, outro_individuo):
        corte = self.salva_index+1
     
        filho1 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        filho2 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]

        filhos = [Individuo(self.maze, self.tamanho_matriz, self.geracao + 1),
                  Individuo(self.maze, self.tamanho_matriz, self.geracao + 1)]

        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2

        #precisamos garantir o index para efetuar a mutação a partir de tal ponto, por isso avaliamos agora
        filhos[0].avaliacao()
        filhos[1].avaliacao()

        return filhos
    
    def mutacao(self, taxa_mutacao):

        trocas = ["L","R","UP","DOWN", "LUP", "RUP", "LDOWN", "RDOWN"]
        for i in range(len(self.cromossomo)):
            x = random.randint(1, 100)
            if x < taxa_mutacao:
                if self.cromossomo[i] == "L" and i > self.salva_index:
                    self.cromossomo[i] = random.choice(trocas)
             
                elif self.cromossomo[i] == "R" and i > self.salva_index: 
                    self.cromossomo[i] = random.choice(trocas)
                        #print("Mutou")
                elif self.cromossomo[i] == "UP" and i > self.salva_index:
                    self.cromossomo[i] = random.choice(trocas)
                        #print("Mutou")
                elif self.cromossomo[i] == "DOWN" and i > self.salva_index:
                    self.cromossomo[i] = random.choice(trocas)

                elif self.cromossomo[i] == "LUP" and i > self.salva_index:
                    self.cromossomo[i] = random.choice(trocas)
                        #print("Mutou")
                elif self.cromossomo[i] == "RUP" and i > self.salva_index:
                    self.cromossomo[i] = random.choice(trocas)

                elif self.cromossomo[i] == "LDOWN" and i > self.salva_index:
                    self.cromossomo[i] = random.choice(trocas)

                elif self.cromossomo[i] == "RDOWN" and i > self.salva_index:
                    self.cromossomo[i] = random.choice(trocas)
                    
        return self
        
class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao, maze, tamanho_matriz):
        self.tamanho_populacao = tamanho_populacao
        self.tamanho_matriz = tamanho_matriz
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = None
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
    
    def visualiza_geracao(self): 
        pass
    def resolver(self, taxa_mutacao):
        self.inicializa_populacao()
        
        for individuo in self.populacao:
            individuo.avaliacao()
        
        self.ordena_populacao()
        
        
        while True:
             ### while
                soma_avaliacao = self.soma_avaliacoes()
                nova_populacao = []
                
                for individuos_gerados in range(0, self.tamanho_populacao, 2):
                    pai1 = 0 # Sempre o melhor vai ser passado para o crossover
                    #pai1 = self.seleciona_pai(soma_avaliacao)
                    pai2 = self.seleciona_pai(soma_avaliacao) #  retorna indice aleatorio para o crossover

                    if pai2 == 0:   #garantindo que não vai ser o mesmo cromossomo para crossover
                        pai2 = random.randint(1, 50)
                    filhos = self.populacao[pai1].crossover(self.populacao[pai2])

                    nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                    nova_populacao.append(filhos[1].mutacao(taxa_mutacao))

                self.populacao = list(nova_populacao)

                for individuo in self.populacao:
                    individuo.avaliacao()
                        
                self.ordena_populacao()
               
                
                melhor = self.populacao[0]
                self.melhor_individuo(melhor) 
                print(f"\nMelhor solução -> Nota: {self.melhor_solucao.nota_avaliacao} Index: {self.melhor_solucao.salva_index} Comidas: {self.melhor_solucao.comidas_encontradas} Cromossomo: {self.melhor_solucao.cromossomo}")

                if self.melhor_solucao.comidas_encontradas == 5:
                    return self.melhor_solucao
        
                
         

if __name__ == '__main__':
    with open("./Genetic/labirinto1.txt", 'r') as f:
        arquivo = f.readlines()
        tamanho_matriz, maze = cria_matriz(arquivo)
        print(tamanho_matriz)
        print(maze[tamanho_matriz-1][tamanho_matriz-1])

        taxa_mutacao = 80
        tamanho_populacao = 200
        ag = AlgoritmoGenetico(tamanho_populacao, maze, tamanho_matriz)
        achou = ag.resolver(taxa_mutacao)
        print(achou.comidas_encontradas)

        
    
    