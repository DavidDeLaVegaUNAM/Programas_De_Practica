import random

class Rompecabezas:
    def __init__(self, tablero):
        self.tablero = tablero

    def __str__(self):
        return '\n'.join(['|'.join(map(str, fila)) for fila in self.tablero])

    def mover(self, x, y):
        fila_vacia, columna_vacia = self.encontrar_vacio()
        if (x, y) in self.obtener_movimientos_validos(fila_vacia, columna_vacia):
            self.tablero[fila_vacia][columna_vacia] = self.tablero[x][y]
            self.tablero[x][y] = 0
            return True
        else:
            return False

    def encontrar_vacio(self):
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    return i, j

    def obtener_movimientos_validos(self, x, y):
        movimientos = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        return [(i, j) for i, j in movimientos si 0 <= i < 3 y 0 <= j < 3]

    def esta_resuelto(self):
        return self.tablero == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def generar_estado_aleatorio():
    numeros = list(range(9))
    random.shuffle(numeros)
    return Rompecabezas([[numeros.pop() for _ in range(3)] for _ in range(3)])

def generar_estado_final_aleatorio():
    numeros = list(range(9))
    random.shuffle(numeros)
    return Rompecabezas([[numeros.pop() for _ in range(3)] for _ in range(3)])

