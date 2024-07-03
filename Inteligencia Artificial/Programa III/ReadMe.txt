
# Reconocedor de Entidades Nombradas (NER)

Este proyecto implementa un sistema de reconocimiento de entidades nombradas (NER) utilizando Modelos Ocultos de Markov (HMM). El modelo está entrenado para identificar y clasificar palabras en una oración según las etiquetas predefinidas (como nombres de personas, ubicaciones, organizaciones, etc.).

## Requisitos

- Python 3.x
- NumPy
- Pandas
- Scikit-learn
- hmmlearn

Puedes instalar las dependencias necesarias utilizando `pip`:

pip install numpy pandas scikit-learn hmmlearn

## Estructura del Proyecto

- `ner_dataset.csv`: Archivo de datos que contiene las oraciones y sus etiquetas correspondientes.
- `ner_hmm.py`: Script principal que contiene la implementación del reconocedor de entidades nombradas.
- `README.md`: Este archivo.

## Formato del Archivo de Datos

El archivo `ner_dataset.csv` debe tener dos columnas separadas por tabulaciones (`\t`):

- La primera columna contiene las oraciones.
- La segunda columna contiene las etiquetas correspondientes para cada palabra en la oración.

Ejemplo de una fila del archivo de datos:

```
Thousands of demonstrators have marched through London to protest the war in Iraq and demand the withdrawal of British troops from that country .    O O O O O B-geo O O O O O B-geo O O O O O B-gpe O O O O O
```

## Uso

1. **Preparar los datos**: Asegúrate de que el archivo `ner_dataset.csv` esté en el mismo directorio que el script `ner_hmm.py`.

2. **Ejecutar el script**: Ejecuta el script `ner_hmm.py` para entrenar el modelo y evaluar su rendimiento.

```bash
python ner_hmm.py
```

3. **Resultados**: El script imprimirá un reporte de clasificación que muestra la precisión, recuperación y puntuación F1 para cada etiqueta.

## Código

El script `ner_hmm.py` realiza los siguientes pasos:

1. **Carga de datos**:
   - Carga el archivo CSV con `pandas`.

2. **Preprocesamiento**:
   - Convierte las palabras a minúsculas.
   - Divide las oraciones y etiquetas en listas.

3. **División de datos**:
   - Divide las secuencias en conjuntos de entrenamiento y prueba.

4. **Transformación de secuencias**:
   - Convierte las palabras y etiquetas en índices.

5. **Entrenamiento del modelo**:
   - Entrena un modelo HMM con las secuencias de entrenamiento.

6. **Predicción y evaluación**:
   - Utiliza el algoritmo de Viterbi para predecir las etiquetas en el conjunto de prueba.
   - Evalúa el modelo y muestra un reporte de clasificación.


