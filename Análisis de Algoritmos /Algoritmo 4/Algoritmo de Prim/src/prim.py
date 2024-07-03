import sys  
# Biblioteca para manejar argumentos de la línea de comandos
from heapq import heappop, heappush  
# Biblioteca para manejar colas de prioridad (min heap)
from collections import defaultdict, deque  
# Biblioteca para manejar diccionarios con valores por defecto y colas de doble extremo

class Arista:
    """
    Representa una arista en el grafo.

    Atributos:
        u (str): El vértice inicial de la arista.
        v (str): El vértice final de la arista.
        peso (int): El peso de la arista.
    """
    def __init__(self, u, v, peso):
        self.u = u
        self.v = v
        self.peso = peso

    def __lt__(self, other):
        """
        Define el operador < para comparar aristas según su peso.
        """
        return self.peso < other.peso

    def __repr__(self):
        """
        Representación en string de la arista.
        """
        return f"{self.u},{self.v} : {self.peso}"

class Grafo:
    """
    Representa un grafo.

    Atributos:
        vertices (list): Lista de vértices en el grafo.
        aristas (defaultdict): Diccionario de listas de aristas adyacentes a cada vértice.
    """
    def __init__(self, vertices):
        self.vertices = vertices
        self.aristas = defaultdict(list)
    
    def agregar_arista(self, u, v, peso):
        """
        Agrega una arista al grafo.

        Args:
            u (str): Vértice inicial de la arista.
            v (str): Vértice final de la arista.
            peso (int): Peso de la arista.
        """
        self.aristas[u].append(Arista(u, v, peso))
        self.aristas[v].append(Arista(v, u, peso))
    
    def obtener_aristas(self, vertice):
        """
        Obtiene las aristas adyacentes a un vértice dado.

        Args:
            vertice (str): El vértice del que se desean obtener las aristas adyacentes.

        Returns:
            list: Lista de aristas adyacentes al vértice.
        """
        return self.aristas[vertice]

def prim(grafo, inicio):
    """
    Implementación del algoritmo de Prim para encontrar el árbol de expansión mínimo.

    Args:
        grafo (Grafo): El grafo sobre el que se realizará el algoritmo.
        inicio (str): El vértice inicial del árbol.

    Returns:
        list: Lista de aristas del árbol de expansión mínimo.
    """
    mst = []
    visitado = {v: False for v in grafo.vertices}
    min_heap = []
    
    def agregar_aristas(v):
        visitado[v] = True
        for arista in grafo.obtener_aristas(v):
            if not visitado[arista.v]:
                heappush(min_heap, arista)
    
    agregar_aristas(inicio)
    
    while min_heap:
        arista = heappop(min_heap)
        if not visitado[arista.v]:
            mst.append(arista)
            agregar_aristas(arista.v)
    
    return mst

def encontrar_componentes(grafo):
    """
    Encuentra las componentes conexas en un grafo utilizando BFS.

    Args:
        grafo (Grafo): El grafo sobre el que se realizará la búsqueda.

    Returns:
        list: Lista de listas, donde cada lista representa una componente conexa.
    """
    visitado = {v: False for v in grafo.vertices}
    componentes = []

    def bfs(inicio):
        cola = deque([inicio])
        componente = []
        while cola:
            vertice = cola.popleft()
            if not visitado[vertice]:
                visitado[vertice] = True
                componente.append(vertice)
                for arista in grafo.obtener_aristas(vertice):
                    if not visitado[arista.v]:
                        cola.append(arista.v)
        return componente

    for vertice in grafo.vertices:
        if not visitado[vertice]:
            componente = bfs(vertice)
            componentes.append(componente)
    
    return componentes

def main(file_path):
    """
    Función principal que ejecuta el algoritmo.

    Args:
        file_path (str): La ruta al archivo de entrada.
    """
    with open(file_path, 'r') as file:
        lineas = file.readlines()
    
    vertices = lineas[0].strip().split(',')
    grafo = Grafo(vertices)
    
    for linea in lineas[1:]:
        u_v, peso = linea.strip().split(' : ')
        u, v = u_v.split(',')
        peso = int(peso)
        grafo.agregar_arista(u, v, peso)
    
    componentes = encontrar_componentes(grafo)
    bosque = []
    
    for componente in componentes:
        sub_grafo = Grafo(componente)
        for vertice in componente:
            for arista in grafo.obtener_aristas(vertice):
                if arista.v in componente and arista.u == vertice:
                    sub_grafo.agregar_arista(arista.u, arista.v, arista.peso)
        mst = prim(sub_grafo, componente[0])
        bosque.append(mst)
    
    print(f"Se encontraron {len(bosque)} árboles:")
    for i, mst in enumerate(bosque, 1):
        print(f"Árbol {i}:")
        for arista in mst:
            print(arista)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python prim_forest.py <archivo_de_entrada>")
    else:
        main(sys.argv[1])

