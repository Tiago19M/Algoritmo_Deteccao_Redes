import networkx as nx

grafo = nx.Graph()

def le_entrada (nomeArquivo):
    caminho = "data/" + nomeArquivo
    with open(caminho, 'r') as arquivo:
        for linha in arquivo:
            origem, destino = linha.strip().split(',')
            grafo.add_edge(origem, destino)

nomeArquivo = input ("Digite aqui o nome do arquivo a ser lido: ")
le_entrada(nomeArquivo)

