import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

# leemos el archivo CSV
df = pd.read_csv('/home/garynova/Universidad/INF-354/Primer Parcial/P1/a/summer-products-with-rating-and-performance_2020-08.csv')


# escalar las características
scaler = MinMaxScaler()
df[['price', 'units_sold', 'rating']] = scaler.fit_transform(df[['price', 'units_sold', 'rating']])
print("Aplicando MinMaxScaler")
print(df)


# codificar las variables categóricas
print("APLICANDO CODIFICACION DE VARIABLES CATEGORICAS")
encoder = OneHotEncoder()
encoder.fit(df[['product_color', 'product_variation_size_id', 'product_variation_inventory', 'shipping_option_name', 'countries_shipped_to']])
encoded = encoder.transform(df[['product_color', 'product_variation_size_id', 'product_variation_inventory', 'shipping_option_name', 'countries_shipped_to']])
df_encoded = pd.DataFrame(encoded.toarray(), columns=encoder.get_feature_names_out())
print(df_encoded,"\n")


print("APLICANDO El MANEJO DE VALORES FALTANTES")
imputer = SimpleImputer(strategy='mean')
imputed = imputer.fit_transform(df[['rating_count', 'rating_five_count', 'rating_four_count', 'rating_three_count', 'rating_two_count', 'rating_one_count']])
df_imputed = pd.DataFrame(imputed, columns=['rating_count', 'rating_five_count', 'rating_four_count', 'rating_three_count', 'rating_two_count', 'rating_one_count'])

print(df_imputed)
