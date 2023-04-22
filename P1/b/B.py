#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 11:28:12 2023

@author: garynova
"""

#importamos numpy y pandas
import pandas as pd


# leemos el archivo CSV
df = pd.read_csv('/home/garynova/Universidad/INF-354/Primer Parcial/P1/a/summer-products-with-rating-and-performance_2020-08.csv')

# Separamos todos los datos numericos
df = df.select_dtypes(include=['float64', 'int64'])

# Calculamos la media de cada columna numerica
print("Media:")
print(df.mean())

# Calculamos la moda de cada columna numerica
print("\nModa:")
print(df.mode().iloc[0])

# Calculamos los cuartiles por columna
print("\nCuartiles:")
print(df.quantile([0.25, 0.50, 0.75]))

# Calculamos los Percentiles por columna
print("\nPercentiles:")
print(df.quantile([0.10, 0.25, 0.50, 0.75, 0.90]))
