## Explicacion de las tecnicas de preprocesamiento

* Escalamiento de características:

En algunas situaciones, es necesario escalar las características de los datos para que estén en la misma escala. Esto se hace para que las características con grandes magnitudes no dominen a las características con magnitudes más pequeñas. En este dataset hay columnas con diferentes escalas, como el precio y la cantidad de imágenes. Por lo tanto, es necesario escalar estas características.

> Técnica utilizada: MinMaxScaler 

* Codificación de variables categóricas:

En este datset se observo que hay varias columnas que son variables categóricas, como la categoría del producto y el país de origen. Para que estas variables puedan ser utilizadas en el análisis, necesitan ser codificadas en valores numéricos.

> Técnica utilizada: OneHotEncoder 

* Manejo de valores faltantes:

En este dataset se observo que puede haber valores faltantes que deben ser manejados antes de realizar cualquier análisis. Los valores faltantes pueden ser eliminados o reemplazados por algún otro valor.

> Técnica utilizada: SimpleImputer 