import random
import sys
import matplotlib.pyplot as plt
import numpy as np

# Primera sección: Funciones de adoquinamiento.

def colocar_azulejos(x1, y1, x2, y2, x3, y3, contador_azulejos, cuadricula):
    contador_azulejos += 1
    cuadricula[x1][y1] = contador_azulejos
    cuadricula[x2][y2] = contador_azulejos
    cuadricula[x3][y3] = contador_azulejos
    return contador_azulejos

def azulejar_cuadricula(n, x, y, contador_azulejos, cuadricula):
    # Casos base
    if n == 1:
        return contador_azulejos
    if n == 2:
        contador_azulejos += 1
        for i in range(x, x + n):
            for j in range(y, y + n):
                if cuadricula[i][j] == 0:
                    cuadricula[i][j] = contador_azulejos
        return contador_azulejos

    # Buscar celda ocupada con manejo de errores
    r, c = -1, -1
    encontrado = False
    for i in range(x, x + n):
        for j in range(y, y + n):
            if cuadricula[i][j] != 0:
                r, c = i, j
                encontrado = True
                break
        if encontrado:
            break
    if not encontrado:
        print("Error: No se encontró celda ocupada")
        return contador_azulejos

    # Mitad del tamaño actual
    mitad = n // 2
    
    # Colocar tromino central según cuadrante ocupado
    if r < x + mitad and c < y + mitad:  # Cuadrante superior izquierdo
        contador_azulejos = colocar_azulejos_y_actualizar_contador(
            x + mitad, y + mitad - 1, 
            x + mitad, y + mitad, 
            x + mitad - 1, y + mitad,
            contador_azulejos, cuadricula
        )
    elif r < x + mitad and c >= y + mitad:  # Cuadrante superior derecho
        contador_azulejos = colocar_azulejos_y_actualizar_contador(
            x + mitad, y + mitad - 1, 
            x + mitad, y + mitad, 
            x + mitad - 1, y + mitad - 1,
            contador_azulejos, cuadricula
        )
    elif r >= x + mitad and c < y + mitad:  # Cuadrante inferior izquierdo
        contador_azulejos = colocar_azulejos_y_actualizar_contador(
            x + mitad - 1, y + mitad, 
            x + mitad, y + mitad, 
            x + mitad - 1, y + mitad - 1,
            contador_azulejos, cuadricula
        )
    else:  # Cuadrante inferior derecho
        contador_azulejos = colocar_azulejos_y_actualizar_contador(
            x + mitad - 1, y + mitad, 
            x + mitad, y + mitad - 1, 
            x + mitad - 1, y + mitad - 1,
            contador_azulejos, cuadricula
        )

    # Llamadas recursivas a los cuatro cuadrantes
    contador_azulejos = azulejar_cuadricula(mitad, x, y, contador_azulejos, cuadricula)  # Sup. Izq.
    contador_azulejos = azulejar_cuadricula(mitad, x, y + mitad, contador_azulejos, cuadricula)  # Sup. Der.
    contador_azulejos = azulejar_cuadricula(mitad, x + mitad, y, contador_azulejos, cuadricula)  # Inf. Izq.
    contador_azulejos = azulejar_cuadricula(mitad, x + mitad, y + mitad, contador_azulejos, cuadricula)  # Inf. Der.
    
    return contador_azulejos

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 main.py <exponente>")
        print("Ejemplo: python3 main.py 3  # Para una cuadrícula 8x8")
        sys.exit(1)

    try:
        exponente = int(sys.argv[1])
        if exponente < 1:
            raise ValueError
    except ValueError:
        print("Error: Exponente debe ser un entero ≥ 1")
        sys.exit(1)

    tamaño = 2 ** exponente
    contador = 0
    cuadricula = [[0] * tamaño for _ in range(tamaño)]
    
    # Celda vacía aleatoria
    x_vacio = random.randint(0, tamaño - 1)
    y_vacio = random.randint(0, tamaño - 1)
    cuadricula[x_vacio][y_vacio] = -1  # Marcador de vacío

    # Azulejar la cuadrícula
    contador = azulejar_cuadricula(tamaño, 0, 0, contador, cuadricula)

    # Visualización mejorada
    plt.figure(figsize=(8, 8))
    img = np.array(cuadricula)
    plt.imshow(img, cmap='viridis', interpolation='nearest')
    
    # Destacar celda vacía
    for i in range(tamaño):
        for j in range(tamaño):
            if cuadricula[i][j] == -1:
                plt.text(j, i, 'X', ha='center', va='center', color='white', fontsize=12)
    
    plt.colorbar(label='Número de Azulejo')
    plt.title(f'Azulejado con Trominos ({tamaño}x{tamaño})')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()

