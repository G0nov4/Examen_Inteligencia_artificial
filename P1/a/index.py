"""
 El cálculo de la media, moda, cuartiles de datos y de percentiles por columna; 
 explique qué significa en cada caso mediante Python sin uso de librerías

 @author: Nova
"""

import csv

# Abrir el archivo CSV
with open('/home/garynova/Universidad/INF-354/Primer Parcial/P1/a/summer-products-with-rating-and-performance_2020-08.csv', 'r') as file:

    # Crear un lector CSV
    reader = csv.reader(file)
    print(reader)

    # Saltar la primera fila, que contiene los encabezados de las columnas
    headers = next(reader)

    # Crear una lista vacía para cada columna
    columns = [[] for _ in range(len(headers))]

    # Leer los datos de cada fila y agregarlos a la lista correspondiente de cada columna
    for row in reader:
        for i in range(len(row)):
            columns[i].append(float(row[i]))

    # Calcular la media, moda, cuartiles y percentiles por columna
    for i in range(len(headers)):
        column = columns[i]
        mean = sum(column) / len(column)
        mode = max(set(column), key=column.count)
        quartiles = [np.percentile(column, 25), np.percentile(column, 50), np.percentile(column, 75)]
        percentiles = [np.percentile(column, p) for p in range(0, 101, 10)]

        # Imprimir los resultados para cada columna
        print(f"Columna: {headers[i]}")
        print(f"Media: {mean:.2f}")
        print(f"Moda: {mode}")
        print(f"Cuartiles: {quartiles}")
        print(f"Percentiles: {percentiles}")
        print()