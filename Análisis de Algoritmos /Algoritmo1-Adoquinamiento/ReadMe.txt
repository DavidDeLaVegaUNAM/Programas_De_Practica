
# Cuadrícula de Azulejos

Este programa genera una cuadrícula de azulejos utilizando el algoritmo de azulejos de Wang Tiles. Los azulejos son dispuestos de manera recursiva, dividiendo la cuadrícula en cuadrantes más pequeños y colocando los azulejos en función de los azulejos ya colocados en cuadrantes vecinos.

## Requisitos

- Python 3
- Matplotlib

## Uso

se ejecuta el programa desde la línea de comandos proporcionando el tamaño deseado de la cuadrícula como argumento:

python3 main.py <tamaño_de_cuadrícula>

El tamaño de la cuadrícula debe ser un número entero positivo. Por ejemplo, para generar una cuadrícula de 8x8 azulejos, ejecute:

python3 main.py 3


## Funcionamiento

El programa se basa en la demostración inductiva, en específico el algoritmo mostrado en clase para generar la cuadrícula. Los azulejos se colocan recursivamente, dividiendo la cuadrícula en cuadrantes más pequeños y colocando los azulejos en función de los azulejos ya colocados en cuadrantes vecinos.

El azulejo inicial se coloca aleatoriamente en la cuadrícula, y luego se generan los azulejos adicionales de forma recursiva. Dada la demostración inductiva de la clase



