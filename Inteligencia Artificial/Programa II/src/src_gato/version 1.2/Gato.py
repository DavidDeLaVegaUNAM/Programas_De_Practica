import tkinter as tk
from functools import partial

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

# Función para actualizar el tablero gráfico
def actualizar_tablero_grafico():
    for i in range(3):
        for j in range(3):
            botones[i][j].config(text=tablero[i][j])

# Función que maneja el clic del jugador
def clic_jugador(fila, columna):
    if tablero[fila][columna] == VACIO and not juego_terminado(tablero):
        hacer_movimiento(tablero, JUGADOR_MIN, fila, columna)
        actualizar_tablero_grafico()
        if not juego_terminado(tablero):
            movimiento_computadora()

# Función que maneja el movimiento de la computadora
def movimiento_computadora():
    fila, columna = movimiento_optimo(tablero)
    if fila is not None and columna is not None:
        hacer_movimiento(tablero, JUGADOR_MAX, fila, columna)
        actualizar_tablero_grafico()
    if juego_terminado(tablero):
        mostrar_resultado()

# Función para mostrar el resultado del juego
def mostrar_resultado():
    resultado = utilidad(tablero)
    if resultado == 1:
        mensaje.set("¡Perdiste!")
    elif resultado == -1:
        mensaje.set("¡Ganaste!")
    else:
        mensaje.set("¡Empate!")

# Función principal del programa
def main():
    global tablero, botones, mensaje
    tablero = [[VACIO for _ in range(3)] for _ in range(3)]
    
    # Configurar la interfaz gráfica
    root = tk.Tk()
    root.title("3 en Línea")

    frame = tk.Frame(root)
    frame.pack()

    botones = [[None for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            boton = tk.Button(frame, text=VACIO, width=10, height=3, command=partial(clic_jugador, i, j))
            boton.grid(row=i, column=j)
            botones[i][j] = boton

    mensaje = tk.StringVar()
    label = tk.Label(root, textvariable=mensaje)
    label.pack()

    root.mainloop()

# Ejecutar el programa
if __name__ == "__main__":
    main()
