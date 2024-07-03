import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from hmmlearn import hmm
from collections import defaultdict

# Paso 1: Cargar los datos
# Cargar el archivo con el formato especificado
data = pd.read_csv('ner_dataset.csv', sep='\t', header=None, names=['entrada', 'etiqueta'])

# Paso 2: Preprocesar los datos
# Convertir los datos de entrada a minúsculas y dividir por espacios
data['entrada'] = data['entrada'].str.lower()
data['entrada'] = data['entrada'].str.split()
data['etiqueta'] = data['etiqueta'].str.split()

# Aplanar las listas para tener una lista de palabras y una lista de etiquetas
palabras = [palabra for oracion in data['entrada'] for palabra in oracion]
etiquetas = [etiqueta for oracion in data['etiqueta'] for etiqueta in oracion]

# Obtener la lista de secuencias de palabras y etiquetas
secuencias = list(zip(data['entrada'], data['etiqueta']))

# Paso 3: Dividir los datos en entrenamiento y evaluación
# Dividir las secuencias en conjuntos de entrenamiento (70%) y evaluación (30%)
train_sequences, test_sequences = train_test_split(secuencias, test_size=0.3, random_state=42)

# Función para convertir las secuencias a un formato adecuado para el modelo HMM
def transformar_secuencias(secuencias):
    X = []
    longitudes = []
    for palabras, etiquetas in secuencias:
        X.extend(palabras)
        longitudes.append(len(palabras))
    return X, longitudes

# Transformar las secuencias de entrenamiento y prueba
X_train, longitudes_train = transformar_secuencias(train_sequences)
X_test, longitudes_test = transformar_secuencias(test_sequences)

# Convertir palabras y etiquetas a índices
palabra_a_idx = {palabra: idx for idx, palabra in enumerate(set(palabras))}
etiqueta_a_idx = {etiqueta: idx for idx, etiqueta in enumerate(set(etiquetas))}

# Convertir las secuencias a índices
X_train_idx = [palabra_a_idx[palabra] for palabra in X_train]
X_test_idx = [palabra_a_idx.get(palabra, -1) for palabra in X_test]  # Si la palabra no está en el entrenamiento, asignar -1
y_train_idx = [etiqueta_a_idx[etiqueta] for oracion in train_sequences for etiqueta in oracion[1]]

# Paso 4: Entrenar el modelo HMM
modelo = hmm.MultinomialHMM(n_components=len(etiqueta_a_idx), n_iter=100)
X_train_array = np.array(X_train_idx).reshape(-1, 1)
modelo.fit(X_train_array, longitudes_train)

# Paso 5: Predecir con el algoritmo de Viterbi
X_test_array = np.array([idx if idx != -1 else 0 for idx in X_test_idx]).reshape(-1, 1)  # Asignar probabilidad 1 a palabras no reconocidas
logprob, y_pred_idx = modelo.decode(X_test_array, longitudes_test)

# Convertir los índices predichos a etiquetas
idx_a_etiqueta = {idx: etiqueta for etiqueta, idx in etiqueta_a_idx.items()}
y_pred = [idx_a_etiqueta[idx] for idx in y_pred_idx]
y_true = [etiqueta for oracion in test_sequences for etiqueta in oracion[1]]

# Paso 6: Evaluar el modelo
print(classification_report(y_true, y_pred))
