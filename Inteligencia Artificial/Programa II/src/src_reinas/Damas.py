import matplotlib.pyplot as plt
import numpy as np
from random import uniform
from numpy.random import randint

# Tamaño del torneo para selección aleatoria
TAMANO_TORNEO = 4

class Individuo:
    def __init__(self, n):
        # Inicializa un individuo con un arreglo de genes aleatorio
        self.size = n
        self.genes = [randint(0, n) for _ in range(n)]

    def obtener_aptitud(self):
        # Calcula la aptitud del individuo
        penalizacion = 0
        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    continue
                if self.genes[i] == self.genes[j]:
                    penalizacion += 1
        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    continue
                if abs(i-j) == abs(self.genes[i]-self.genes[j]):
                    penalizacion += 1
        return 1 / (penalizacion + 1)

    def __repr__(self):
        # Representación del individuo como una cadena de caracteres
        return ''.join(str(e) for e in self.genes)

class Poblacion:
    def __init__(self, tamano_poblacion, n):
        # Inicializa una población de individuos
        self.tamano_poblacion = tamano_poblacion
        self.size = n
        self.individuos = [Individuo(n) for _ in range(tamano_poblacion)]

    def obtener_mas_apto(self):
        # Retorna el individuo más apto de la población
        mas_apto = self.individuos[0]
        for individuo in self.individuos[1:]:
            if individuo.obtener_aptitud() > mas_apto.obtener_aptitud():
                mas_apto = individuo
        return mas_apto

    def obtener_mas_apto_elitismo(self, n):
        # Retorna los 'n' individuos más aptos de la población (elitismo)
        self.individuos.sort(key=lambda ind: ind.obtener_aptitud(), reverse=True)
        return self.individuos[:n]

    def obtener_tamano(self):
        # Retorna el tamaño de la población
        return self.tamano_poblacion

    def obtener_individuo(self, index):
        # Retorna el individuo en la posición 'index'
        return self.individuos[index]

    def guardar_individuo(self, index, individuo):
        # Guarda un individuo en la posición 'index'
        self.individuos[index] = individuo

class AlgoritmoGenetico:
    def __init__(self, tamano_poblacion=100, tasa_cruce=0.65, tasa_mutacion=0.1, param_elitismo=5):
        # Inicializa el algoritmo genético con los parámetros dados
        self.tamano_poblacion = tamano_poblacion
        self.tasa_cruce = tasa_cruce
        self.tasa_mutacion = tasa_mutacion
        self.param_elitismo = param_elitismo

    def ejecutar(self, n):
        # Ejecuta el algoritmo genético para resolver el problema de las n reinas
        pop = Poblacion(self.tamano_poblacion, n)
        contador_generaciones = 0
        while pop.obtener_mas_apto().obtener_aptitud() != 1:
            contador_generaciones += 1
            pop = self.evolve_population(pop)
        return pop.obtener_mas_apto().genes

    def evolve_population(self, population):
        # Evoluciona la población actual para la siguiente generación
        next_population = Poblacion(self.tamano_poblacion, population.size)
        next_population.individuos.extend(population.obtener_mas_apto_elitismo(self.param_elitismo))
        for index in range(self.param_elitismo, next_population.obtener_tamano()):
            first = self.random_selection(population)
            second = self.random_selection(population)
            next_population.guardar_individuo(index, self.crossover(first, second))
        for individual in next_population.individuos:
            self.mutate(individual)
        return next_population

    def crossover(self, offspring1, offspring2):
        # Realiza el operador de cruce entre dos individuos
        cross_individual = Individuo(offspring1.size)
        start = randint(offspring1.size)
        end = randint(offspring1.size)
        if start > end:
            start, end = end, start
        cross_individual.genes = offspring1.genes[:start] + offspring2.genes[start:end] + offspring1.genes[end:]
        return cross_individual

    def mutate(self, individual):
        # Realiza el operador de mutación en un individuo
        for index in range(individual.size):
            if uniform(0, 1) <= self.tasa_mutacion:
                individual.genes[index] = randint(individual.size)

    def random_selection(self, actual_population):
        # Realiza la selección aleatoria de un individuo de la población
        new_population = Poblacion(TAMANO_TORNEO, actual_population.size)
        for i in range(new_population.obtener_tamano()):
            random_index = randint(new_population.obtener_tamano())
            new_population.guardar_individuo(i, actual_population.obtener_individuo(random_index))
        return new_population.obtener_mas_apto()

def resolver_n_reinas(n):
    # Resuelve el problema de las n reinas utilizando el algoritmo genético
    algoritmo = AlgoritmoGenetico(8)
    solucion = algoritmo.ejecutar(n)
    return solucion

def dibujar_tablero(tablero):
    # Crear un array para representar el tablero
    tablero_array = np.zeros((len(tablero), len(tablero), 3), dtype=np.uint8)

    # Asignar colores a las casillas
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if (i + j) % 2 == 0:
                tablero_array[i, j] = [255, 255, 255]  # Blanco
            else:
                tablero_array[i, j] = [0, 0, 0]  # Negro

    # Marcar las posiciones de las reinas en rojo
    for i in range(len(tablero)):
        tablero_array[i, tablero[i]] = [255, 0, 0]  # Rojo

    # Mostrar el tablero
    plt.imshow(tablero_array, interpolation='nearest')
    plt.xlim(-0.5, len(tablero) - 0.5)
    plt.ylim(-0.5, len(tablero) - 0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks(range(len(tablero)))
    plt.yticks(range(len(tablero)))
    plt.gca().invert_yaxis()
    plt.grid(True, color='black', linewidth=0.5)
    plt.grid(False) 
	
    plt.show()

def main():
    # Función principal del programa
    n = int(input("Introduce el número de reinas: "))
    solucion = resolver_n_reinas(n)
    print("Solución encontrada:")
    dibujar_tablero(solucion)

if __name__ == '__main__':
    main()

