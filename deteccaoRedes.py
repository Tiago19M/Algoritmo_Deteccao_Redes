import networkx as nx
import numpy as np

grafo = nx.Graph()

MAX_ITERACOES = int(input("Defina aqui o número máximo de iterações do algoritmo: "))  #Valor arbitrário que deve ser definido como possível limite para o algoritmo


def le_entrada (nomeArquivo):
    caminho = "data/" + nomeArquivo  #Monta o caminho do arquivo a partir do diretório do projeto
    with open(caminho, 'r') as arquivo:
        for linha in arquivo:
            origem, destino = linha.strip().split(',')
            grafo.add_edge(int(origem), int(destino))   #Insere a aresta  origem -> destino  na estrutura do grafo

def calcular_moda_com_empate_aleatorio(rotulosVizinhos):

    #Conta a frequência de cada rótulo dentre os rótulos vizinhos do vértice atual e encontra a maior frequência
    frequencia = {}
    maior = -1
    for rotulo in rotulosVizinhos:
        if rotulo in frequencia:
            frequencia[rotulo]+=1
        else:
            frequencia[rotulo]=1

        if frequencia[rotulo] > maior:
            maior = frequencia[rotulo]

    #Monta a lista de candidatos com base na moda (os que mais se repetiram)
    candidatos = []
    for rotulo in frequencia:
        if frequencia[rotulo] == maior:
            candidatos.append(rotulo)

    #Faz uma escolha aleatória entre os candidatos para decidir o "vencedor"
    return np.random.choice(candidatos)

nomeArquivo = input ("Digite aqui o nome do arquivo a ser lido: ")
le_entrada(nomeArquivo)

#Lógica de remapeamento do grafo: caso o arquivo de entrada não seja composto por vértices no intervalo [0, n], mapeamos cada vértice do grafo original
#como um vértice correspondente entre 0 a n, formando um novo grafo denominado 'grafoRemapeado'
nosOriginais = list(grafo.nodes())

idxNo = {} #idxNo armazena na chave nó (índice original), seu novo índice 'i'
for i, no in enumerate(nosOriginais):
    idxNo[no] = i

noIdx = {} #noIdx[i] retorna, dado um índice 'i' entre 0 e n, seu índice original associado.
for no, i in idxNo.items():
    noIdx[i] = no

grafoRemapeado = nx.Graph()
for origem, destino in grafo.edges():
    grafoRemapeado.add_edge(idxNo[origem], idxNo[destino])

grafo = grafoRemapeado #Salvas as relações de índice original e novo índice, fazemos ambos apontar pro mesmo conteúdo, para evitar ambiguidades


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

comunidades = {}

for contador, label in enumerate(rotulos):
    verticeOriginal = noIdx[contador]
    if label not in comunidades:
        comunidades[label] = []
    comunidades[label].append(verticeOriginal)


print ("VÉRTICES POR COMUNIDADE:")
for label, vertices in comunidades.items():
    verticesStr = ", ".join(f"vértice {v}" for v in vertices)
    print (f"Comunidade de label {label}: {verticesStr}")




