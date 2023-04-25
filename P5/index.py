import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import numpy as np

# leer el archivo csv
df = pd.read_csv('/home/garynova/Universidad/INF-354/Primer Parcial/P1/a/summer-products-with-rating-and-performance_2020-08.csv')

# Seleccionamos 4 columnas y 20 filas
subset = df[['price', 'rating', 'rating_count', 'uses_ad_boosts']].sample(n=20)

# Transformamos uses_ad_boots
subset['uses_ad_boosts'] = subset['uses_ad_boosts'].replace({'Yes': 1, 'No': 0})
X = subset[['price', 'rating', 'rating_count', 'uses_ad_boosts']]
y = subset['uses_ad_boosts']

# entrenar el modelo de árbol de decisión
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

# graficar el árbol de decisión
fig, ax = plt.subplots(figsize=(8, 6))
plot_tree(clf, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)
plt.show()