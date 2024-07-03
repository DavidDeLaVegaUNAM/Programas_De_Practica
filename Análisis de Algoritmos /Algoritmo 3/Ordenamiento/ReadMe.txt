David de la Vega Bautista
Vi un vídeo buenardo papá sobre como hacer redacción para un ReadMe, ahora sí, ya voy a dokumentar kbrones.

Este programa implementa tres algoritmos de ordenamiento diferentes. Los usuarios pueden elegir entre:
1. Ordenamiento por Inserción Local (Local Insertion Sort)
2. Ordenamiento de Árbol (Tree Sort)
3. Radix LSD Sort

El programa muestra los pasos intermedios del proceso de ordenamiento.

## Estructura del Código

### Clases y Funciones

#### `NodoArbol`
Representa un nodo en un árbol binario de búsqueda.
- `__init__(self, clave)`: Crea un nuevo nodo con la clave dada.

#### `insertar(raiz, clave)`
Añade un nuevo nodo al árbol binario de búsqueda.
- `raiz`: El nodo raíz del árbol.
- `clave`: La clave del nuevo nodo.

#### `recorrido_en_orden(raiz, lista_ordenada)`
Realiza un recorrido en orden del árbol binario, guardando los valores en una lista.
- `raiz`: El nodo raíz del árbol.
- `lista_ordenada`: La lista donde se almacenan los valores en orden.

#### `ordenar_arbol(arreglo)`
Ordena un arreglo utilizando Tree Sort.
- `arreglo`: El arreglo que se quiere ordenar.

#### `ordenamiento_insercion(arreglo)`
Ordena un arreglo utilizando Local Insertion Sort.
- `arreglo`: El arreglo que se quiere ordenar.

#### `ordenamiento_cuenta(arreglo, exp)`
Utiliza Counting Sort en un paso de Radix LSD Sort, ordenando basado en un dígito específico.
- `arreglo`: El arreglo que se quiere ordenar.
- `exp`: La posición del dígito utilizado para ordenar.

#### `ordenamiento_radix_lsd(arreglo)`
Ordena un arreglo utilizando Radix LSD Sort.
- `arreglo`: El arreglo que se quiere ordenar.

#### `imprimir_pasos(pasos)`
Imprime los pasos intermedios de un algoritmo de ordenamiento.
- `pasos`: Lista de los pasos intermedios.

### Función Principal

#### `main()`
Esta es la función principal que ejecuta el programa. Solicita al usuario que elija un algoritmo de ordenamiento y una secuencia de datos, luego muestra los pasos intermedios del proceso de ordenamiento.

## Cómo Usar el Programa

1. **Ejecución del Programa**
   - Abrir la terminal y ejecutar el archivo Python: `python nombre_del_archivo.py`
   
2. **Selección de Algoritmo**
   - El programa solicita que se seleccione uno de los algoritmos:
     - `1`: Ordenamiento por Inserción Local (Local Insertion Sort)
     - `2`: Ordenamiento de Árbol (Tree Sort)
     - `3`: Radix LSD Sort

3. **Ingreso de la Secuencia**
   - Dependiendo del algoritmo seleccionado, se ingresa la secuencia de datos:
     - Para `1` y `2`: Ingresar una secuencia de números enteros separados por espacios.
     - Para `3`: Ingresar una secuencia de cadenas hexadecimales de longitud máxima de 2 caracteres, separadas por espacios.

4. **Visualización de Pasos**
   - El programa ejecuta el algoritmo seleccionado y muestra los pasos intermedios del proceso de ordenamiento.

5. **Repetición o Salida**
   - El programa pregunta si se desea ordenar otra secuencia. Responder `s` para sí o `n` para no.


## Descripción de los Algoritmos

### 1. Ordenamiento por Inserción Local (Local Insertion Sort)
- Recorre el arreglo de izquierda a derecha.
- Toma cada elemento y lo inserta en su posición correcta en la parte ya ordenada del arreglo.
- Guarda y muestra los pasos intermedios después de cada inserción.

### 2. Ordenamiento de Árbol (Tree Sort)
- Inserta cada elemento del arreglo en un árbol binario de búsqueda.
- Realiza un recorrido en orden (in-order traversal) del árbol para obtener los elementos en orden ascendente.
- Guarda y muestra los pasos intermedios del recorrido en orden del árbol después de cada inserción.

### 3. Radix LSD (Least Significant Digit) Sort
- Ordena los elementos del arreglo basándose en los dígitos individuales de menor a mayor significancia (de derecha a izquierda).
- Utiliza Counting Sort para ordenar los elementos basándose en el dígito actual.
- Guarda y muestra los pasos intermedios después de cada paso de ordenamiento basado en un dígito.

## Requisitos
- Python 3.x

## Notas
- Para Radix LSD Sort, se debe ingresar solo cadenas hexadecimales válidas (0-9 y A-F) de longitud máxima de 2 caracteres.



