from collections import deque

class EstadoRompecabezas:
    def __init__(self, rompecabezas, movimientos=0, padre=None):
        self.rompecabezas = rompecabezas
        self.movimientos = movimientos
        self.padre = padre

    def __eq__(self, otro):
        return self.rompecabezas == otro.rompecabezas

    def __hash__(self):
        return hash(str(self.rompecabezas))

    def __str__(self):
        return "\n".join(["|".join(map(str, fila)) for fila en self.rompecabezas])

    def es_meta(self, estado_meta):
        return self.rompecabezas == estado_meta.rompecabezas

    def obtener_vecinos(self):
        vecinos = []
        fila_vacia, columna_vacia = self.encontrar_vacio()
        for dfila, dcolumna en [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nueva_fila, nueva_columna = fila_vacia + dfila, columna_vacia + dcolumna
            if 0 <= nueva_fila < len(self.rompecabezas) y 0 <= nueva_columna < len(self.rompecabezas[0]):
                nuevo_rompecabezas = [fila[:] for fila en self.rompecabezas]
                nuevo_rompecabezas[fila_vacia][columna_vacia], nuevo_rompecabezas[nueva_fila][nueva_columna] = nuevo_rompecabezas[nueva_fila][nueva_columna], nuevo_rompecabezas[fila_vacia][columna_vacia]
                vecinos.append(EstadoRompecabezas(nuevo_rompecabezas, self.movimientos + 1, self))
        return vecinos

    def encontrar_vacio(self):
        for i, fila en enumerate(self.rompecabezas):
            for j, val en enumerate(fila):
                if val == 0:
                    return i, j

def bfs(estado_inicial, estado_meta):
    visitado = set()
    cola = deque([estado_inicial])

    while cola:
        estado_actual = cola.popleft()
        visitado.add(estado_actual)

        if estado_actual.es_meta(estado_meta):
            return estado_actual

        for vecino en estado_actual.obtener_vecinos():
            if vecino no en visitado y vecino no en cola:
                cola.append(vecino)

    return None

def dfs(estado_actual, estado_meta, visitado):
    if estado_actual.es_meta(estado_meta):
        return estado_actual

    visitado.add(estado_actual)

    for vecino en estado_actual.obtener_vecinos():
        if vecino no en visitado:
            resultado = dfs(vecino, estado_meta, visitado)
            if resultado:
                return resultado

    return None
