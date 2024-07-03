# Definición de los valores de los jugadores
JUGADOR_MAX = 'x'
JUGADOR_MIN = 'o'
VACIO = ' '

# Función para convertir la representación de cadena del tablero en una matriz
def parsear_tablero(tablero_str):
    return [list(fila.strip()) for fila in tablero_str.split('\n') if fila.strip()]

# Función para imprimir un tablero en forma de cadena
def imprimir_tablero(tablero):
    for i, fila in enumerate(tablero):
        print("".join(fila))
        if i < len(tablero) - 1:
            print("-"*9)

# Función para generar y mostrar el árbol de juego utilizando el algoritmo minimax con poda alfa-beta
def generar_arbol(tablero_str):
    tablero = parsear_tablero(tablero_str)
    
    def minimax(tablero, profundidad, alfa, beta, es_min):
        if profundidad == 0 or juego_terminado(tablero):
            return utilidad(tablero)
        if es_min:
            min_utilidad = float('inf')
            for movimiento in movimientos_validos(tablero):
                fila, columna = movimiento
                hacer_movimiento(tablero, JUGADOR_MIN, fila, columna)
                min_utilidad = min(min_utilidad, minimax(tablero, profundidad - 1, alfa, beta, False))
                deshacer_movimiento(tablero, fila, columna)
                beta = min(beta, min_utilidad)
                if beta <= alfa:
                    break
            return min_utilidad
        else:
            max_utilidad = float('-inf')
            for movimiento in movimientos_validos(tablero):
                fila, columna = movimiento
                hacer_movimiento(tablero, JUGADOR_MAX, fila, columna)
                max_utilidad = max(max_utilidad, minimax(tablero, profundidad - 1, alfa, beta, True))
                deshacer_movimiento(tablero, fila, columna)
                alfa = max(alfa, max_utilidad)
                if beta <= alfa:
                    break
            return max_utilidad
    
    def juego_terminado(tablero):
        for fila in tablero:
            if fila.count(JUGADOR_MAX) == 3 or fila.count(JUGADOR_MIN) == 3:
                return True
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != VACIO:
                return True
        if tablero[0][0] == tablero[1][1] == tablero[2][2] or tablero[0][2] == tablero[1][1] == tablero[2][0]:
            if tablero[1][1] != VACIO:
                return True
        return False
    
    def movimientos_validos(tablero):
        movimientos = []
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == VACIO:
                    movimientos.append((i, j))
        return movimientos
    
    def hacer_movimiento(tablero, jugador, fila, columna):
        tablero[fila][columna] = jugador
    
    def deshacer_movimiento(tablero, fila, columna):
        tablero[fila][columna] = VACIO
    
    def generar_arbol_aux(tablero, jugador, profundidad, espacio=""):
        if profundidad == 0 or juego_terminado(tablero):
            return
        for movimiento in movimientos_validos(tablero):
            fila, columna = movimiento
            hacer_movimiento(tablero, jugador, fila, columna)
            utilidad_movimiento = minimax(tablero, profundidad - 1, float('-inf'), float('inf'), jugador == JUGADOR_MIN)
            print(f"{espacio}{jugador} en ({fila},{columna}) - Utilidad: {utilidad_movimiento}")
            imprimir_tablero(tablero)
            generar_arbol_aux(tablero, JUGADOR_MIN if jugador == JUGADOR_MAX else JUGADOR_MAX, profundidad - 1, espacio + "  ")
            deshacer_movimiento(tablero, fila, columna)
    
    # Imprimir el tablero inicial
    print("Tablero Inicial:")
    imprimir_tablero(tablero)
    
    # Generar y mostrar el árbol de juego
    print("\nÁrbol de Juego:")
    generar_arbol_aux(tablero, JUGADOR_MAX, 6)  # Profundidad máxima del árbol

# Estados del juego
estado_juego_1 = """
o| |x 
x|o|     
  | |        
"""
estado_juego_2 = """
x| |o 
  |x|o     
  | |        
"""

estado_juego_3 = """
  |x|  
x| |     
  |o|        
"""

estado_juego_4 = """
  | |  
  |x|     
  | |o       
"""

# Ejecutar el programa
if __name__ == "__main__":
    generar_arbol(estado_juego_1)
    #generar_arbol(estado_juego_2)
    #generar_arbol(estado_juego_3)
    #generar_arbol(estado_juego_4)