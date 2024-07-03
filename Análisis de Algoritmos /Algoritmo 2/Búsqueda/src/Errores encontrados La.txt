## Estrategia para el Funcionamiento del Código

El objetivo de este código es buscar errores en un texto utilizando un árbol de búsqueda binaria y funciones de procesamiento definidas en un archivo externo. Aquí se detalla la estrategia utilizada para lograr este propósito:

### Clases y Estructuras de Datos

1. Nodo (clase Nodo): Esta clase representa un nodo en el árbol binario de búsqueda. Cada nodo contiene un valor y referencias a sus nodos hijos izquierdo y derecho.

2. ArbolBinarioBusqueda (clase ArbolBinarioBusqueda): Esta clase implementa un árbol binario de búsqueda. Permite insertar valores en el árbol y buscar valores en él utilizando un enfoque recursivo.

### Funciones Principales

1. cargar_funciones_desde_archivo(nombre_archivo): Esta función carga las funciones de procesamiento desde un archivo externo. Utiliza el módulo `importlib.util` para cargar dinámicamente las funciones definidas en el archivo especificado.

2. construir_arbol(texto): Esta función construye un árbol de búsqueda binaria a partir de un texto dado. Divide el texto en palabras utilizando expresiones regulares y luego inserta cada palabra en el árbol.

3. buscar_errores(texto, arbol, funciones): Esta función busca errores en un texto utilizando un árbol de búsqueda binaria y funciones de procesamiento. Para cada palabra en el texto, aplica las funciones de procesamiento y registra cualquier palabra que genere un resultado verdadero como un error.

### Flujo Principal del Programa

1. Carga de Funciones de Procesamiento: El programa carga las funciones de procesamiento desde el archivo `Procesador.py` utilizando la función `cargar_funciones_desde_archivo`.

2. Construcción del Árbol: El texto del archivo `LoR.txt` se carga y se utiliza para construir un árbol de búsqueda binaria mediante la función `construir_arbol`.

3. Búsqueda de Errores: Se definen las funciones de procesamiento y se pasan junto con el árbol y el texto a la función `buscar_errores`. Esta función identifica y registra las palabras que se consideran errores.

4. Presentación de Resultados: Por último, se imprimen los errores encontrados en el texto, si los hay.

### Importante Consideración

Ya le entendí a las clases, (Más o menos) Me costó entender como usarlas. LO mando ya nocturnamente porque la verdad es que fueron horas y horas de ver videos de como hacer que se abriera el texto, fue lo que más me complicó. Salu2
