# TAREA 2 DE MODELOS - ejercicios de estructura de datos
# Listas de mis artistas favoritos
list1 = ['pink floyd', 'brutalismus 3000', 'zoe', 'fleetwood mac']
print(list1)
# para agregar un dato al FINAL de la lista
list1.append('siddhartha')
print(list1)
# extender la lista, agregando datos
list2 = ['the doors', 'mehro', 'red hot chili peppers']
print(list2)
list1.extend(list2)
print(list1)
# insertar un dato en una posición particular
list1.insert(4, 'depeche mode')
print(list1)
# quitar el primer dato de la lista
list1.remove('pink floyd')
print(list1)
# quitar un dato en una posición determinada y después regresarlo
list2.pop(2)
print(list2)
# quitar todos los elementos de la lista
list2.clear()
print(list2)
list2 = ['the doors', 'mehro', 'red hot chili peppers']
print(list2)
# buscar en la lista el primer elemento equivalente a un valor que damos, y regresa la posición de ese elemento
list2.index('mehro')
posicion = list2.index('mehro')
print(posicion)
# encontrar el número de veces que un dato aparece en la lista
list2.count('the doors')
print(list2.count('the doors'))
# acomodar los datos de la lista; no crea una nueva lista, solo la modifica. en este caso, por LONGITUD de palabras
list2.sort(key=len)
print(list2)
# revolver al revés los elementos de la lista
list2.reverse()
print(list2)
list2.reverse()
# regresar una copia "superficial" de la lista
list2.copy()
print(list2)

# listas en pila
stack = ['mehro', 'pink floyd', 'zoe']
print(stack)
# agregar un dato en la pila
stack.append('fleetwood mac')
print(stack)
# quitar un elemento de la pila
stack.pop()
print(stack)

# crear listas: list comprehension, filtrando elementos que cumplan con ciertas condiciones
texto = 'corazón'
mayusculas = [texto.upper() for letra in texto]
print(mayusculas)
# eliminar elementos de lista con función del
del list2[0:1]
print(list2)

# tuplas: no pueden ser modificadas una vez que son creadas
tuple = ('pink floyd', 'brutalismus 3000', 'mehro')
print(tuple[0])
print(tuple[0:2])
print(tuple[2:])