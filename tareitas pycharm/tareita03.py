# ESTA ES LA TAREITA 03 DEL CURSO
# ejemplo de métodos de diccionarios, con cosas que me gustan:)

diccionario1 = {
    'animal': 'gatitos', 'actividad': 'escribir'
}
print(type(diccionario1))
# función POP
diccionario1.pop('actividad')
print(diccionario1)

# función get => acceder a los elementos e n un diccionario. si no existe, declara none

diccionario1.get('animal')
print(diccionario1)

# función copy
diccionario2 = {
    'comida': 'pasta', 'película': 'billy elliot'
}
print(type(diccionario2))
diccionario2.copy()
print(diccionario2)

# función keys => visualización de las llaves del diccionario
llaves = diccionario2.keys()
print(llaves)

# función ítems => visualización de todos los pares de llave-valor
items = diccionario2.items()
print(items)

# función clear => eliminar todos los elementos de un diccionario
diccionario2.clear()
print(diccionario2)

# función fromkeys => crear un nuevo diccionario con valor que se asignará a todas las llaves
diccionario3 = {
    'color': 'azul', 'mar': 'azul', 'cielo': 'azul'
}
print(type(diccionario3))
diccionario3.fromkeys(['color', 'mar', 'cielo'])
print(diccionario3)

# función popitem => eliminar y regresar un par llave-valor del diccionario
cielo, azul = diccionario3.popitem()
print('llave eliminada: {cielo}, valor eliminado: {azul}')
print(diccionario3)

# función setdefault => obtener valor de una llave en un diccionario
# si la llave no existe, la agrega con el valor proporcionado
valor_color = diccionario3.setdefault('color', 'azul')
print(valor_color)

# función update => actualizar el diccionario con los pares de llave-valor
# de otro diccionario => FUSIONAR diccionarios

diccionario3.update(diccionario1)
print(diccionario3)

# función values => visualizar todos los VALORES del diccionario
valores = diccionario3.values()
print(valores)