import pandas as pd
import matplotlib.pyplot as plt

# Carga el dataset
df = pd.read_csv("/home/garynova/Universidad/INF-354/Primer Parcial/P1/a/summer-products-with-rating-and-performance_2020-08.csv")


df = df.select_dtypes(include=['float64', 'int64'])
# Itera sobre cada columna e imprime las estadísticas
for columna in df.columns:
    print("\nColumna:", columna)
    if df[columna].dtype == 'int64' or df[columna].dtype == 'float64':
        print("Media:", df[columna].mean())
        print("Moda:", df[columna].mode().iloc[0])
        print("Mediana:", df[columna].median())
        print("Cuartiles:")
        print(df[columna].quantile([0.25, 0.50, 0.75]))
        print("Percentiles:")
        print(df[columna].quantile([0.10, 0.25, 0.50, 0.75, 0.90]))
        
        # Grafica la distribución de la columna
        plt.figure()
        df[columna].plot(kind='hist')
        plt.xlabel(columna)
        plt.show()
    else:
        print("Esta columna no es numérica.")