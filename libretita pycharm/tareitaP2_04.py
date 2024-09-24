# Mediante teclado especificar lo siguiente:
# - Numero de columnas que tendrá el dataframe
# - Una vez que se especifique, preguntar por los datos que tendra esa Serie
# - Preguntar por los nombres de las columnas que tendrá el dataframe
# - Preguntar por los nombres de las filas que tendrá el dataframe
# - Una vez introducidos los datos, crear el dataframe que contenga esa información
# - Mostrar el dataframe

import pandas as pd

no_columnas = int(input('vamos a hacer un data frame :D primero, introduce el número de columnas que tendrá: '))

columnas = []
names_columnas = []

for i in range(no_columnas):
    nombre_columna = input('escribe el nombre de la columna: ')
    names_columnas.append(nombre_columna)
    data_columna = input('escribe el dato de la columna: ').split(',')
    columnas.append(data_columna)

names_filas = input('ahora escribe los nombres de las FILAS separados por comas: ').split(',')
data_dict = {names_columnas[i]: columnas[i] for i in range(no_columnas)}
df = pd.DataFrame(data_dict, index = names_filas)
print(df)

