from puzzle import generar_estado_aleatorio, generar_estado_final_aleatorio, Rompecabezas
from puzzle_state import EstadoRompecabezas, bfs, dfs
from a_star import a_estrella

def simular_juego(estado_inicial, estado_final):
    print("Estado inicial:")
    print(estado_inicial)
    while not estado_inicial.esta_resuelto():
        print("Selecciona una posición para mover (fila columna):")
        x, y = map(int, input().split())
        if estado_inicial.mover(x, y):
            print(estado_inicial)
        else:
            print("Movimiento no válido. Intenta de nuevo.")
    print("¡Felicidades! Has ganado.")

def main():
    estado_inicial = generar_estado_aleatorio()
    estado_final = generar_estado_final_aleatorio()
    simular_juego(estado_inicial, estado_final)

    rompecabezas_inicio = [[1, 0, 2], [6, 3, 4], [7, 5, 8]]
    rompecabezas_meta = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    estado_inicio = EstadoRompecabezas(rompecabezas_inicio)
    estado_meta = EstadoRompecabezas(rompecabezas_meta)

    resultado = bfs(estado_inicio, estado_meta)

    if resultado:
        print("Solución encontrada en {} movimientos:".format(resultado.movimientos))
        print(resultado)
    else:
        print("No se encontró una solución.")

    visitado = set()
    resultado = dfs(estado_inicio, estado_meta, visitado)

    if resultado:
        print("Solución encontrada en {} movimientos:".format(resultado.movimientos))
        print(resultado)
    else:
        print("No se encontró una solución.")

    estado_inicial = [[5, 4, 2], [3, 1
