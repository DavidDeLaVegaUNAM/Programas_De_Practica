import random
import sys
import matplotlib.pyplot as plt

def colocar_azulejos_y_actualizar_contador(x1, y1, x2, y2, x3, y3, contador_azulejos, cuadricula):
    """
    Coloca tres azulejos con el mismo contador en las posiciones especificadas.

    Parámetros:
        x1 (int): Coordenada X del primer azulejo.
        y1 (int): Coordenada Y del primer azulejo.
        x2 (int): Coordenada X del segundo azulejo.
        y2 (int): Coordenada Y del segundo azulejo.
        x3 (int): Coordenada X del tercer azulejo.
        y3 (int): Coordenada Y del tercer azulejo.
        contador_azulejos (int): Contador a asignar a los azulejos.
        cuadricula (list): Lista 2D que representa la cuadrícula.

    Devolución:
        int: Contador actualizado después de colocar los azulejos.
    """
    contador_azulejos += 1
    cuadricula[x1][y1] = contador_azulejos
    cuadricula[x2][y2] = contador_azulejos
    cuadricula[x3][y3] = contador_azulejos
    return contador_azulejos

def azulejar_cuadricula(n, x, y, contador_azulejos, cuadricula):
    """
    Azuleja recursivamente la cuadrícula con azulejos de tamaño decreciente.

    Parámetros:
        n (int): Tamaño de la cuadrícula actual.
        x (int): Coordenada X de la esquina superior izquierda de la cuadrícula actual.
        y (int): Coordenada Y de la esquina superior izquierda de la cuadrícula actual.
        contador_azulejos (int): Contador a asignar a los azulejos.
        cuadricula (list): Lista 2D que representa la cuadrícula.

    Devolución:
        int: Contador actualizado después de azulejar la cuadrícula.
    """
    if n == 2:
        contador_azulejos += 1
        for i in range(n):
            for j in range(n):
                if cuadricula[x + i][y + j] == 0:
                    cuadricula[x + i][y + j] = contador_azulejos
        return contador_azulejos

    # Encontrar la posición de un azulejo existente
    for i in range(x, x + n):
        for j in range(y, y + n):
            if cuadricula[i][j] != 0:
                r = i
                c = j
    if r < x + n // 2 and c < y + n // 2:
        contador_azulejos = colocar_azulejos_y_actualizar_contador(x + n // 2, y + n // 2 - 1, x + n // 2, y + n // 2,
                                                                    x + n // 2 - 1, y + n // 2, contador_azulejos, cuadricula)
    elif r >= x + n // 2 and c < y + n // 2:
        contador_azulejos = colocar_azulejos_y_actualizar_contador(x + n // 2 - 1, y + n // 2, x + n // 2, y + n // 2,
                                                                    x + n // 2 - 1, y + n // 2 - 1, contador_azulejos, cuadricula)
    elif r < x + n // 2 and c >= y + n // 2:
        contador_azulejos = colocar_azulejos_y_actualizar_contador(x + n // 2, y + n // 2 - 1, x + n // 2, y + n // 2,
                                                                    x + n // 2 - 1, y + n // 2 - 1, contador_azulejos, cuadricula)
    elif r >= x + n // 2 and c >= y + n // 2:
        contador_azulejos = colocar_azulejos_y_actualizar_contador(x + n // 2 - 1, y + n // 2, x + n // 2, y + n // 2 - 1,
                                                                    x + n // 2 - 1, y + n // 2 - 1, contador_azulejos, cuadricula)
    contador_azulejos = azulejar_cuadricula(n // 2, x, y + n // 2, contador_azulejos, cuadricula)
    contador_azulejos = azulejar_cuadricula(n // 2, x, y, contador_azulejos, cuadricula)
    contador_azulejos = azulejar_cuadricula(n // 2, x + n // 2, y, contador_azulejos, cuadricula)
    contador_azulejos = azulejar_cuadricula(n // 2, x + n // 2, y + n // 2, contador_azulejos, cuadricula)
    return contador_azulejos

def main():
    """
    Función principal para generar e imprimir la cuadrícula azulejada.

    Esta función toma el tamaño de la cuadrícula de los argumentos de la línea de comandos,
    genera una cuadrícula azulejada con un azulejo vacío aleatorio, e imprime la representación
    ASCII art resultante de la cuadrícula.
    """
    if len(sys.argv) != 2:
        print("Uso: python3 main.py <tamaño_de_cuadrícula>")
        sys.exit(1)

    try:
        tamaño_de_cuadrícula = int(sys.argv[1])
        if tamaño_de_cuadrícula <= 0:
            raise ValueError
    except ValueError:
        print("Error: Tamaño de cuadrícula no válido. Por favor, proporcione un entero positivo.")
        sys.exit(1)

    tamaño_de_cuadrícula = 2 ** tamaño_de_cuadrícula
    contador_azulejos = 0
    cuadricula = [[0 for _ in range(tamaño_de_cuadrícula)] for _ in range(tamaño_de_cuadrícula)]

    # Establecer el azulejo vacío en una posición aleatoria
    x_vacío = random.randint(0, tamaño_de_cuadrícula - 1)
    y_vacío = random.randint(0, tamaño_de_cuadrícula - 1)
    cuadricula[x_vacío][y_vacío] = -1

    contador_azulejos = azulejar_cuadricula(tamaño_de_cuadrícula, 0, 0, contador_azulejos, cuadricula)

    # Generar representación gráfica
    plt.figure(figsize=(8, 8))
    plt.imshow(cuadricula, cmap='binary', interpolation='nearest')
    plt.colorbar(label='Número', orientation='horizontal')
    plt.title('Cuadrícula de Azulejos')
    plt.axis('off')  # Ocultar ejes
    plt.show()

if __name__ == "__main__":
    main()

