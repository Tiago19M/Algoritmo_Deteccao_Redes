import networkx as nx
import numpy as np

grafo = nx.Graph()

MAX_ITERACOES = 100  #Valor arbitrário que deve ser definido como possível limite para o algoritmo


def le_entrada (nomeArquivo):
    caminho = "data/" + nomeArquivo  #Monta o caminho do arquivo a partir do diretório do projeto
    with open(caminho, 'r') as arquivo:
        for linha in arquivo:
            origem, destino = linha.strip().split(',')
            grafo.add_edge(int(origem), int(destino))   #Insere a aresta  origem -> destino  na estrutura do grafo

def calcular_moda_com_empate_aleatorio(rotulosVizinhos):
    ...
    #
    #
    # Falta implementar a lógica do cálculo da moda em caso de frequências iguais
    #
    #


nomeArquivo = input ("Digite aqui o nome do arquivo a ser lido: ")
le_entrada(nomeArquivo)

numVertices = grafo.number_of_nodes()

rotulos = np.arange (0, numVertices)  #rotulos é um 'ndarray' (da biblioteca numpy), contendo índices de a 0 até numVertices-1
ordemVertices = np.arange(numVertices)  #inicia ordemVertices como uma "cópia" dos rótulos, para que posteriormente seja embaralhado e defina a ordem de visitação dos vértices no grafo, a cada iteração.

iteracao = 0
mudou = True

while (iteracao < MAX_ITERACOES and mudou):
    mudou = False
    np.random.shuffle(ordemVertices)  #Embaralha os rótulos, definindo uma nova ordem de visitação dos vértices

    for i in ordemVertices:
        vizinhos = list(grafo.neighbors(i))  #Seguindo a ordem de visitação, armazenamos em 'vizinhos' os vizinhos do vértice atual
        semVizinhos = bool(len(vizinhos)==0)  #Se len(vizinhos) for igual a 0, significa que o vértice atual não tem vizinhos

        if (not semVizinhos):
            rotulosVizinhos = rotulos[vizinhos]
            novoRotulo = calcular_moda_com_empate_aleatorio(rotulosVizinhos)  #O novo rótulo do vértice atual é definido aqui (pode permanecer igual ou não)

            if novoRotulo != rotulos[i]:
                rotulos[i] = novoRotulo
                mudou = True

    iteracao = iteracao+1

print (rotulos)



