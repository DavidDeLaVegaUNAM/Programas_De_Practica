import tkinter as tk
from tkinter import messagebox

# Definición de los valores de los jugadores
JUGADOR_MAX = 'x'
JUGADOR_MIN = 'o'
VACIO = ' '

# Función de utilidad
def utilidad(tablero):
    # Filas
    for fila in tablero:
        if fila.count(JUGADOR_MAX) == 3:
            return 1
        elif fila.count(JUGADOR_MIN) == 3:
            return -1
    # Columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col]:
            if tablero[0][col] == JUGADOR_MAX:
                return 1
            elif tablero[0][col] == JUGADOR_MIN:
                return -1
    # Diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] or tablero[0][2] == tablero[1][1] == tablero[2][0]:
        if tablero[1][1] == JUGADOR_MAX:
            return 1
        elif tablero[1][1] == JUGADOR_MIN:
            return -1
    # Si no hay ganador
    return 0

# Función para verificar si el juego ha terminado
def juego_terminado(tablero):
    # Verificar si hay un ganador
    if utilidad(tablero) != 0:
        return True
    # Verificar si hay casillas vacías
    for fila in tablero:
        if VACIO in fila:
            return False
    # Si no hay ganador y no hay casillas vacías, entonces hay un empate
    return True

# Función para generar los movimientos válidos
def movimientos_validos(tablero):
    movimientos = []
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == VACIO:
                movimientos.append((i, j))
    return movimientos

# Función para realizar el movimiento en el tablero
def hacer_movimiento(tablero, jugador, fila, columna):
    tablero[fila][columna] = jugador

# Función para deshacer el movimiento en el tablero
def deshacer_movimiento(tablero, fila, columna):
    tablero[fila][columna] = VACIO

# Función para el algoritmo minimax con poda alfa-beta
def minimax(tablero, profundidad, alfa, beta, es_max):
    if juego_terminado(tablero) or profundidad == 0:
        return utilidad(tablero)
    if es_max:
        max_utilidad = float('-inf')
        for movimiento in movimientos_validos(tablero):
            fila, columna = movimiento
            hacer_movimiento(tablero, JUGADOR_MAX, fila, columna)
            max_utilidad = max(max_utilidad, minimax(tablero, profundidad - 1, alfa, beta, False))
            deshacer_movimiento(tablero, fila, columna)
            alfa = max(alfa, max_utilidad)
            if beta <= alfa:
                break
        return max_utilidad
    else:
        min_utilidad = float('inf')
        for movimiento in movimientos_validos(tablero):
            fila, columna = movimiento
            hacer_movimiento(tablero, JUGADOR_MIN, fila, columna)
            min_utilidad = min(min_utilidad, minimax(tablero, profundidad - 1, alfa, beta, True))
            deshacer_movimiento(tablero, fila, columna)
            beta = min(beta, min_utilidad)
            if beta <= alfa:
                break
        return min_utilidad

# Función para realizar el movimiento óptimo
def movimiento_optimo(tablero):
    mejor_utilidad = float('-inf')
    mejor_movimiento = None
    for movimiento in movimientos_validos(tablero):
        fila, columna = movimiento
        hacer_movimiento(tablero, JUGADOR_MAX, fila, columna)
        utilidad_actual = minimax(tablero, float('inf'), float('-inf'), float('inf'), False)
        deshacer_movimiento(tablero, fila, columna)
        if utilidad_actual > mejor_utilidad:
            mejor_utilidad = utilidad_actual
            mejor_movimiento = movimiento
    return mejor_movimiento

# Clase para la interfaz gráfica del juego
class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("3 en Línea (Tic Tac Toe)")
        self.tablero = [[VACIO for _ in range(3)] for _ in range(3)]
        self.turno = 0
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()
    
    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=VACIO, font=('normal', 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.hacer_movimiento(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def hacer_movimiento(self, fila, columna):
        if self.tablero[fila][columna] == VACIO and not juego_terminado(self.tablero):
            if self.turno % 2 == 0:
                # Turno del jugador humano (MIN)
                hacer_movimiento(self.tablero, JUGADOR_MIN, fila, columna)
                self.buttons[fila][columna].config(text=JUGADOR_MIN)
            else:
                # Turno del algoritmo (MAX)
                fila, columna = movimiento_optimo(self.tablero)
                hacer_movimiento(self.tablero, JUGADOR_MAX, fila, columna)
                self.buttons[fila][columna].config(text=JUGADOR_MAX)
            self.turno += 1
            if juego_terminado(self.tablero):
                self.mostrar_resultado()

    def mostrar_resultado(self):
        resultado = utilidad(self.tablero)
        if resultado == 1:
            messagebox.showinfo("Resultado", "¡Ganó el jugador X!")
        elif resultado == -1:
            messagebox.showinfo("Resultado", "¡Ganó el jugador O!")
        else:
            messagebox.showinfo("Resultado", "¡Empate!")

# Función principal del programa
def main():
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()

# Ejecutar el programa
if __name__ == "__main__":
    main()
