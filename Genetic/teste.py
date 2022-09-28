from ga import Individuo
import random
from random import random as rand
from maze import cria_matriz


if __name__ == '__main__':
    with open("./Genetic/labirinto1.txt", 'r') as f:
        arquivo = f.readlines()
        tamanho_matriz, maze = cria_matriz(arquivo)
        

        taxa_mutacao = 0.01
        tamanho_populacao = 100
        salva = []
        for x in range(tamanho_populacao):
            salva.append(Individuo(maze, tamanho_matriz))


        for individuo in salva:
            individuo.avaliacao()


        for x in salva:
            print(x.nota_avaliacao, end=" ")   

        best = salva[0]

        for outro in salva:
            if outro.nota_avaliacao > best.nota_avaliacao:
                best = outro
        
        print('\n')
        print(best.nota_avaliacao)
        print(best.cromossomo)
        print(f'Comidas = {best.comidas_encontradas}')
        print(f'Index do ultimo = {best.salva_index}')
        