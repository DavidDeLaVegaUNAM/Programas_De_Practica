class NodoArbol:
    """
    Clase para representar un nodo en un árbol binario de búsqueda.
    """
    def __init__(self, clave):
        """
        Inicializa un nuevo nodo con la clave proporcionada.
        """
        self.izquierda = None
        self.derecha = None
        self.valor = clave

def insertar(raiz, clave, pasos):
    """
    Inserta un nuevo nodo con la clave dada en un árbol binario de búsqueda y
    guarda los pasos intermedios.

    Args:
        raiz: Nodo raíz del árbol.
        clave: Clave del nuevo nodo a insertar.
        pasos: Lista para almacenar los pasos intermedios.

    Returns:
        El nodo raíz actualizado después de insertar el nuevo nodo.
    """
    if raiz is None:
        pasos.append(f"Insertar {clave} como raíz.")
        return NodoArbol(clave)
    else:
        if raiz.valor < clave:
            pasos.append(f"Insertar {clave} a la derecha de {raiz.valor}.")
            raiz.derecha = insertar(raiz.derecha, clave, pasos)
        else:
            pasos.append(f"Insertar {clave} a la izquierda de {raiz.valor}.")
            raiz.izquierda = insertar(raiz.izquierda, clave, pasos)
    return raiz

def recorrido_en_orden(raiz, lista_ordenada, pasos):
    """
    Realiza un recorrido en orden del árbol binario de búsqueda y guarda los
    valores en una lista, en orden ascendente.

    Args:
        raiz: Nodo raíz del árbol.
        lista_ordenada: Lista para almacenar los valores en orden.
        pasos: Lista para almacenar los pasos intermedios.

    Returns:
        None
    """
    if raiz:
        recorrido_en_orden(raiz.izquierda, lista_ordenada, pasos)
        lista_ordenada.append(raiz.valor)
        pasos.append(f"Visitar nodo {raiz.valor}.")
        recorrido_en_orden(raiz.derecha, lista_ordenada, pasos)

def ordenar_arbol(arreglo):
    """
    Ordena un arreglo utilizando el algoritmo de Tree Sort, que consiste en
    insertar los elementos en un árbol binario de búsqueda y luego realizar un
    recorrido en orden del árbol.

    Args:
        arreglo: Arreglo que se desea ordenar.

    Returns:
        Lista con el arreglo ordenado y los pasos intermedios del algoritmo.
    """
    raiz = None
    pasos = []
    for clave in arreglo:
        raiz = insertar(raiz, clave, pasos)
    lista_ordenada = []
    recorrido_en_orden(raiz, lista_ordenada, pasos)
    return lista_ordenada, pasos

def ordenamiento_insercion(arreglo):
    """
    Ordena un arreglo utilizando el algoritmo de Local Insertion Sort, que
    consiste en iterar sobre los elementos e insertarlos en la posición
    correcta respecto a los elementos anteriores.

    Args:
        arreglo: Arreglo que se desea ordenar.

    Returns:
        Lista de pasos intermedios del algoritmo.
    """
    n = len(arreglo)
    pasos = []
    for i in range(1, n):
        clave = arreglo[i]
        j = i - 1
        pasos.append(f"Seleccionar {clave} para inserción.")
        while j >= 0 and arreglo[j] > clave:
            arreglo[j + 1] = arreglo[j]
            pasos.append(f"Mover {arreglo[j]} a la posición {j + 1}.")
            j -= 1
        arreglo[j + 1] = clave
        pasos.append(f"Insertar {clave} en la posición {j + 1}. Arreglo actual: {arreglo}")
    return pasos

def ordenamiento_cuenta(arreglo, exp, pasos):
    """
    Ordena un arreglo utilizando el algoritmo de Counting Sort, aplicado en
    un paso de Radix LSD Sort. Se ordena basado en el valor del dígito en la
    posición dada por 'exp'.

    Args:
        arreglo: Arreglo que se desea ordenar.
        exp: Posición del dígito que se utiliza para ordenar.
        pasos: Lista para almacenar los pasos intermedios.

    Returns:
        None
    """
    n = len(arreglo)
    salida = [0] * n
    cuenta = [0] * 16

    pasos.append(f"Ordenar según el dígito en la posición {exp}.")
    for i in range(n):
        indice = int(arreglo[i][exp], 16) if exp < len(arreglo[i]) else 0
        cuenta[indice] += 1
    pasos.append(f"Cuenta después del conteo: {cuenta}")

    for i in range(1, 16):
        cuenta[i] += cuenta[i - 1]
    pasos.append(f"Cuenta acumulada: {cuenta}")

    i = n - 1
    while i >= 0:
        indice = int(arreglo[i][exp], 16) if exp < len(arreglo[i]) else 0
        salida[cuenta[indice] - 1] = arreglo[i]
        cuenta[indice] -= 1
        i -= 1
    pasos.append(f"Arreglo ordenado después del conteo: {salida}")

    for i in range(n):
        arreglo[i] = salida[i]

def ordenamiento_radix_lsd(arreglo):
    """
    Ordena un arreglo utilizando el algoritmo de Radix LSD Sort, que
    ordena basado en los dígitos hexadecimales de las cadenas en el arreglo.

    Args:
        arreglo: Arreglo que se desea ordenar.

    Returns:
        Lista de pasos intermedios del algoritmo.
    """
    max_longitud = len(max(arreglo, key=len))
    pasos = []
    for exp in range(max_longitud - 1, -1, -1):
        pasos.append(f"Ordenar según el dígito en la posición {exp}.")
        ordenamiento_cuenta(arreglo, exp, pasos)
        pasos.append(f"Arreglo después de ordenar por dígito {exp}: {arreglo}")
    return pasos

def imprimir_pasos(pasos):
    """
    Imprime los pasos intermedios de un algoritmo de ordenamiento.

    Args:
        pasos: Lista de pasos intermedios del algoritmo.

    Returns:
        None
    """
    for i, paso in enumerate(pasos):
        print(f"Paso {i + 1}: {paso}")

def main():
    """
    Función principal del programa. Solicita al usuario un algoritmo de ordenamiento
    y una lista, luego muestra los pasos intermedios de cada algoritmo.
    """
    while True:
        algoritmo = input("Ingrese el algoritmo que desea usar (1: Ordenamiento por Inserción Local, 2: Ordenamiento de Árbol, 3: Radix LSD): ")
        if algoritmo not in ('1', '2', '3'):
            print("Por favor, ingrese una opción válida.")
            continue

        if algoritmo == '1':
            arreglo = input("Ingrese la lista que desea ordenar separada por espacios (Ejemplo '3 2 1'):").split()
            pasos = ordenamiento_insercion(arreglo)
            imprimir_pasos(pasos)
        elif algoritmo == '2':
            arreglo = list(map(int, input("Ingrese la lista que desea ordenar separada por espacios (Ejemplo '3 2 1'):").split()))
            arreglo_ordenado, pasos = ordenar_arbol(arreglo)
            imprimir_pasos(pasos)
            print("Arreglo ordenado:", arreglo_ordenado)
        elif algoritmo == '3':
            arreglo = input("Ingrese la secuencia hexadecimal que desea ordenar (por ejemplo, '1A B3 2F'): ").split()
            if all(all(c in '0123456789ABCDEF' for c in s) and len(s) <= 2 for s in arreglo):
                pasos = ordenamiento_radix_lsd(arreglo)
                imprimir_pasos(pasos)
            else:
                print("Por favor, ingrese solo cadenas hexadecimales de longitud válida.")
                continue

        eleccion = input("¿Desea ordenar otra cadena? (s/n): ")
        if eleccion.lower() != 's':
            break

if __name__ == "__main__":
    main()

