import importlib.util
import os
import re

# Definición de la clase Nodo para el árbol binario de búsqueda
class Nodo:
    def __init__(self, valor):
        """
        Constructor de la clase Nodo.

        Args:
            valor (str): El valor que contendrá el nodo.
        """
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Definición de la clase ArbolBinarioBusqueda
class ArbolBinarioBusqueda:
    def __init__(self):
        """
        Constructor de la clase ArbolBinarioBusqueda.
        """
        self.raiz = None

    # Método para insertar un valor en el árbol
    def insertar(self, valor):
        """
        Inserta un valor en el árbol de búsqueda binaria.

        Args:
            valor (str): El valor que se desea insertar en el árbol.
        """
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    # Método auxiliar recursivo para insertar un valor en el árbol
    def _insertar_recursivo(self, nodo, valor):
        """
        Inserta un valor en el árbol de búsqueda binaria de manera recursiva.

        Args:
            nodo (Nodo): El nodo actual en el que se está considerando la inserción.
            valor (str): El valor que se desea insertar en el árbol.
        """
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    # Método para buscar un valor en el árbol
    def buscar(self, valor):
        """
        Busca un valor en el árbol de búsqueda binaria.

        Args:
            valor (str): El valor que se desea buscar en el árbol.

        Returns:
            bool: True si se encuentra el valor en el árbol, False en caso contrario.
        """
        return self._buscar_recursivo(self.raiz, valor)

    # Método auxiliar recursivo para buscar un valor en el árbol
    def _buscar_recursivo(self, nodo, valor):
        """
        Busca un valor en el árbol de búsqueda binaria de manera recursiva.

        Args:
            nodo (Nodo): El nodo actual en el que se está realizando la búsqueda.
            valor (str): El valor que se desea buscar en el árbol.

        Returns:
            bool: True si se encuentra el valor en el árbol, False en caso contrario.
        """
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        return self._buscar_recursivo(nodo.derecha, valor)

# Función para cargar las funciones de procesado desde un archivo externo
def cargar_funciones_desde_archivo(nombre_archivo):
    """
    Carga las funciones de procesado desde un archivo externo.

    Args:
        nombre_archivo (str): El nombre del archivo que contiene las funciones de procesado.

    Returns:
        module: El módulo que contiene las funciones de procesado.
    """
    # Obtenemos la ruta del directorio del script en ejecución
    directorio_actual = os.path.dirname(__file__)
    # Construimos la ruta del archivo relativa al directorio actual
    ruta_absoluta = os.path.join(directorio_actual, nombre_archivo)
    
    # Cargamos las funciones de procesado desde el archivo
    spec = importlib.util.spec_from_file_location("procesador", ruta_absoluta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo

# Función para construir un árbol de búsqueda binaria a partir de un texto
def construir_arbol(texto):
    """
    Construye un árbol de búsqueda binaria a partir de un texto.

    Args:
        texto (str): El texto del cual se construirá el árbol.

    Returns:
        ArbolBinarioBusqueda: El árbol de búsqueda binaria construido.
    """
    arbol = ArbolBinarioBusqueda()
    palabras = re.findall(r'\b\w+\b', texto.lower())
    for palabra in palabras:
        arbol.insertar(palabra)
    return arbol

# Función para buscar errores en un texto utilizando un árbol de búsqueda binaria y funciones de procesado
def buscar_errores(texto, arbol, funciones):
    """
    Busca errores en un texto utilizando un árbol de búsqueda binaria y funciones de procesado.

    Args:
        texto (str): El texto en el cual se buscarán los errores.
        arbol (ArbolBinarioBusqueda): El árbol de búsqueda binaria que se utilizará para buscar las palabras.
        funciones (list): La lista de funciones de procesado que se aplicarán a las palabras.

    Returns:
        list: La lista de palabras que representan errores encontrados en el texto.
    """
    errores = []

    # Aplicamos las funciones de procesamiento a cada palabra en el texto
    palabras = re.findall(r'\b\w+\b', texto.lower())
    for palabra in palabras:
        for funcion in funciones:
            if funcion(palabra):
                errores.append(palabra)
                break  # Si encontramos una coincidencia, pasamos a la siguiente palabra
    return errores

# Función principal
def main():
    # Cargamos las funciones de procesado desde el archivo Procesador.py
    funciones_procesador = cargar_funciones_desde_archivo("Procesador.py")

    # Obtenemos la ruta del directorio del script en ejecución
    directorio_actual = os.path.dirname(__file__)
    # Construimos la ruta del archivo de texto relativa al directorio actual
    ruta_texto = os.path.join(directorio_actual, "LoR.txt")

    # Cargamos el texto desde el archivo .txt
    with open(ruta_texto, "r") as archivo:
        texto = archivo.read()

    # Construimos el árbol de búsqueda binaria con las palabras del texto
    arbol = construir_arbol(texto)

    # Definimos las funciones de procesado
    funciones = [funciones_procesador.procesado1, 
                 funciones_procesador.procesado2, 
                 funciones_procesador.procesado3]

    # Buscamos los errores en el texto
    errores = buscar_errores(texto, arbol, funciones)

    # Imprimimos los errores encontrados
    print("Errores encontrados:")
    if errores:
        for error in set(errores):  # Usar set para evitar duplicados
            print("- La palabra '{}' es un error.".format(error))
    else:
        print("No se encontraron errores en el texto.")

# Entrada principal del programa
if __name__ == "__main__":
    main()

