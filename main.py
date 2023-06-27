from Graph import Graph


def graph_constructor():
    g = Graph()
    varfuri = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'M']
    for eticheta in varfuri:
        g.adauga_varf(eticheta)
    muchii = [('A', 'B'), ('A', 'G'), ('A', 'J'), ('A', 'E'),
              ('B', 'F'), ('B', 'H'), ('B', 'C'),
              ('C', 'G'), ('C', 'I'), ('C', 'D'),
              ('D', 'H'), ('D', 'J'), ('D', 'E'),
              ('E', 'F'), ('E', 'I'),
              ('F', 'J'), ('F', 'G'),
              ('G', 'H'),
              ('H', 'I'),
              ('I', 'J')
              ]
    for muchie in muchii:
        g.adauga_muchie(muchie[0], muchie[1])

    return g


def main():
    graph = graph_constructor()
    start_varf = 'A'
    traversare = graph.dfs(start_varf)
    print("DFS: ", traversare)

    print("Este gol Graph-ul? ", graph.este_gol())

    varfuri = graph.get_varfuri()
    print("Varfurile Graph-ului sunt: ", varfuri)

    muchii = graph.get_muchii()
    print("Muchiile Graph-ului sunt: ", muchii)

    este_conex = len(traversare) == len(graph.get_varfuri())
    print("Graph-ul este conex? ", este_conex)



if __name__ == '__main__':
    main();
