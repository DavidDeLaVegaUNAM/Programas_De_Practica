
# Algoritmo de Prim para Árbol de Expansión Mínimo en Bosques

## Descripción

Este script implementa el algoritmo de Prim para encontrar el árbol de expansión mínimo (MST) en grafos. Si el grafo no es conexo, encontrará el bosque de expansión mínimo, es decir, el conjunto de MSTs para cada componente conexa del grafo.

## Requisitos

- Python 3.x

# Librerías requeridas
sys: Para manejar argumentos de la línea de comandos.

heapq: Para manejar colas de prioridad (min heap).

collections: Para manejar diccionarios con valores por defecto y colas de doble extremo (defaultdict y deque).

## Uso

Para ejecutar el script, necesitas proporcionar un archivo de entrada que contenga la definición del grafo. El archivo debe seguir el siguiente formato:

1. La primera línea contiene una lista de vértices separados por comas.
2. Las siguientes líneas contienen las aristas, con el formato `u,v : peso`, donde `u` y `v` son los vértices conectados por la arista y `peso` es el peso de la arista.

### Ejemplo de archivo de entrada

```
A,B,C,D
A,B : 1
B,C : 2
C,D : 3
A,D : 4
B,D : 5
```

### Comando para ejecutar el script

python prim_forest.py <archivo_de_entrada>

### Ejemplo de ejecución

python prim_forest.py grafo.txt


## Salida

El script imprimirá la cantidad de árboles de expansión mínima encontrados (uno por cada componente conexa) y las aristas que conforman cada árbol.

## Diseño del Código



### Proceso de Diseño

1. Definición de Clases:
    - Clase `Arista`: Representa una arista del grafo, con atributos para los vértices inicial y final, y el peso de la arista. Se define el operador `<` para comparar aristas por su peso, lo que es fundamental para el algoritmo de Prim.
    
    - Clase `Grafo`**: Representa el grafo, con una lista de vértices y un diccionario de listas de adyacencias para almacenar las aristas.

2. Algoritmo de Prim:
    - Se implementó una función `prim` que utiliza una cola de prioridad (min heap) para seleccionar las aristas de menor peso y construir el MST.

3. Búsqueda de Componentes Conexas:
    - Dado que el grafo puede no ser conexo, se implementó una función `encontrar_componentes` que utiliza BFS para identificar las componentes conexas del grafo.

4. Integración y Ejecución:
    - La función `main` maneja la lectura del archivo de entrada, la creación del grafo, la identificación de componentes conexas y la ejecución del algoritmo de Prim en cada componente.

### Decisiones de Diseño

- Eficiencia: Se eligió una cola de prioridad para asegurar que la selección de aristas sea eficiente.
- Flexibilidad: Se diseñó el código para manejar grafos no conexos, devolviendo un bosque de expansión mínima en lugar de un solo MST.


