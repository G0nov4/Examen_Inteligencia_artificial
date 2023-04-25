import random
import pandas as pd

# leer el archivo csv
data = pd.read_csv('/home/garynova/Universidad/INF-354/Primer Parcial/P1/a/summer-products-with-rating-and-performance_2020-08.csv')

# Obtenemos el tamaño del dataset
n_samples = len(data)

# Definimos la proporción para el split
train_prop = 0.8
test_prop = 0.2

# Calculamos el número de muestras para entrenamiento y pruebas
n_train = int(n_samples * train_prop)
n_test = n_samples - n_train

# Generamos una lista con los índices de las muestras
sample_indices = list(range(n_samples))

# Mezclamos los índices aleatoriamente
random.shuffle(sample_indices)

# Dividimos los índices en dos sublistas para entrenamiento y pruebas
train_indices = sample_indices[:n_train]
test_indices = sample_indices[n_train:]

# Creamos los conjuntos de entrenamiento y pruebas
train_set = data.iloc[train_indices]
test_set = data.iloc[test_indices]

print("INDICES")
print(train_indices,test_indices)

print("Conjuntos de entrenamientos")
print(train_set, test_set)