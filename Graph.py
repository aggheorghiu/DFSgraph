import doctest


class Graph:
    """
init - initializes the class with an empty dict;
este_gol(self) -> bool: Returns True if the graph is empty;
adauga_varf(self, eticheta: str) -> None: Adds a vertex 'etocheta/x' to the graph;
adauga_muchie(self, dela_eticheta: str, la_eticheta: str) -> None: (undirected graph) adds an edge between two vertices;
vecini(self, eticheta: str) Returns neighbor vertices;
get_varfuri(self): Returns all vertices in the graph;
get_muchii(self): Returns all edges in the graph;
dfs(self, start_varf): Returns visited vertices in their order.
    """
    def __init__(self):
        self._varfuri: dict[str, list[str]] = {}

    def este_gol(self) -> bool:
        return self._varfuri == 0

    def adauga_varf(self, eticheta: str) -> None:
        if eticheta not in self._varfuri:
            self._varfuri[eticheta] = []

    def adauga_muchie(self, dela_eticheta: str, la_eticheta: str) -> None:
        if dela_eticheta in self._varfuri and la_eticheta in self._varfuri:
            self._varfuri[dela_eticheta].append(la_eticheta)
            self._varfuri[la_eticheta].append(dela_eticheta)

    def vecini(self, eticheta: str):
        if eticheta in self._varfuri:
            return self._varfuri[eticheta]

    def dfs(self, start_varf):
        vizitat = []
        cos = [start_varf]

        while cos:
            varf = cos.pop()
            if varf not in vizitat:
                vizitat.append(varf)
                vecini = self._varfuri[varf]
                for vecin in vecini[::-1]:
                    if vecin not in vizitat:
                        cos.append(vecin)
        return vizitat

    def get_varfuri(self):
        """
        Returns all vertice
        >>> graph = Graph()
        >>> graph.adauga_varf('A')
        >>> graph.adauga_varf('B')
        >>> graph.get_varfuri()
        ['A', 'B']
        """
        return list(self._varfuri.keys())

    def get_muchii(self):
        """
        Returns all edges
        >>> graph = Graph()
        >>> graph.adauga_varf('A')
        >>> graph.adauga_varf('B')
        >>> graph.adauga_muchie('A', 'B')
        >>> graph.get_muchii()
        [('A', 'B'), ('B', 'A')]
        """
        muchii = []
        for varf, vecini in self._varfuri.items():
            for vecin in vecini:
                if(vecin, varf) not in muchii:
                    muchii.append((varf, vecin))
                if (vecin, varf) not in muchii:
                    muchii.append((vecin, varf))
        return muchii


if __name__ == '__main__':
    doctest.testmod()
