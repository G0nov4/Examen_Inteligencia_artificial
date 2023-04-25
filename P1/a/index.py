"""
 El cálculo de la media, moda, cuartiles de datos y de percentiles por columna; 
 explique qué significa en cada caso mediante Python sin uso de librerías

 @author: Nova
"""

# Importamos el módulo csv para leer el archivo CSV
import csv

# funcion media
def media(datos):
    return sum(datos) / len(datos)

#funcion moda
def moda(datos):
    moda = max(set(datos), key = datos.count)
    return moda

#funcion cuartiles
def cuartiles(datos):
    datos_ordenados = sorted(datos)
    q1_index = int(len(datos_ordenados) * 0.25)
    q2_index = int(len(datos_ordenados) * 0.5)
    q3_index = int(len(datos_ordenados) * 0.75)
    q1 = datos_ordenados[q1_index]
    q2 = datos_ordenados[q2_index]
    q3 = datos_ordenados[q3_index]
    return (q1, q2, q3)

#funcion percentiles
def percentiles(datos, p):
    datos_ordenados = sorted(datos)
    p_index = int(len(datos_ordenados) * p / 100)
    return datos_ordenados[p_index]

# Abrimos el archivo CSV y leemos los datos
with open('/home/garynova/Universidad/INF-354/Primer Parcial/P1/a/summer-products-with-rating-and-performance_2020-08.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=',')


    # Leemos la primera fila con los nombres de las columnas
    nombres_columnas = next(lector_csv)


    # Creamos una lista vacía para almacenar los datos numéricos
    datos_numericos = [[] for _ in range(len(nombres_columnas))]


    # Leemos las filas restantes y almacenamos los datos numéricos en la lista correspondiente
    for fila in lector_csv:
        for i, valor in enumerate(fila):
            try:
                # Verificamos si el valor el la fila es numerico
                valor_numerico = float(valor)
                datos_numericos[i].append(valor_numerico)
            except ValueError:
                pass
    
    # Calculamos la media, moda, cuartiles y percentiles para cada columna numérica
    for i, datos_columna in enumerate(datos_numericos):
        if len(datos_columna) > 0:
            nombre_columna = nombres_columnas[i]
            media_columna = media(datos_columna)
            moda_columna = moda(datos_columna)
            cuartiles_columna = cuartiles(datos_columna)
            percentil25_columna = percentiles(datos_columna, 25)
            percentil50_columna = percentiles(datos_columna, 50)
            percentil75_columna = percentiles(datos_columna, 75)
            print(f'{nombre_columna}: \nmedia={media_columna}, \nmoda={moda_columna}, \ncuartiles={cuartiles_columna}, \npercentil 25={percentil25_columna}, \npercentil 50={percentil50_columna}, \npercentil 75={percentil75_columna}\n')
