# TIPOS DE DATOS, CARACTERÍSTICAS, OPERACIONES

# NUMÉRICOS
int = 8 # enteros
print(type(int))
float = 4.2 # flotantes => racionales (se expresan en fracción)
print(type(float))
print(float)
 # complex => COMPLEJOS o imaginarios
# SINTAXIS DE OPERACIONES
a = 4**2  # potencia => ** (doble asterisco)
b = 4**.2 # raíz cuadrada => **. => 4**.2
c = 8 # signo igual => asignar valores!

# CADENAS => datos guardados entre comillas, separadas por puros espacios
cadenita = 'hola' # string!!!
print(cadenita)
print(type(cadenita))
cadenita2 = 'hola, ¿cómo estás?'
print(cadenita + cadenita2) # las cadenas se pueden "sumar" => concatenar xd
print(cadenita*3) # multiplicación por un ENTERO!! sí se puede.
print(str(10)) # para convertir algún dato a CADENA => str
# SLICING => obtener un elemento de una lista, cadena, tupla
print(cadenita[0:3]) # aplicando slicing
print('hola'[0]) # aplicando slicing
print('hola'[-3]) # slicing de regreso
print(cadenita[0:3:2])
print(cadenita[1:-3:2])
print(len(cadenita))

cadenita3 = '58' 'hola' 'fin'
print(cadenita3)
print(type(cadenita3))
# LISTAS => secuencia de elementos separados por comas, entre CORCHETES!
listita = [1,2,3,4,5]
print(type(listita))
print(listita)
listita2 = ['fuego', 'aire', 'agua', 'tierra']
print(listita + listita2) # las listas se pueden sumar
print(listita2[1:3]) # a las listas se les puede aplicar slicing
print(listita2.index('fuego')) # index para id la posición de cierto elemento

# TUPLAS => secuencia de elementos separados por comas, entre PARÉNTESIS!!!
tuplita = ('hola', 1, 2, 3)
print(tuplita)
print(type(tuplita))
tuplita2 = ('neurona', 'astrocito', 'célula de schwann')
print(tuplita2)
print(tuplita + tuplita2) # las tuplas se pueden sumar
print(tuplita*3) # se pueden multiplicar
# no son mutables ni modificables!!!!!

# BOOLEANOS: representan uno de dos posibles valores: verdadero o falso
valor1 = True
valor2 = False
print(type(valor1))
print('int', bool(0)) # 0 = FALSE!!
print('int', bool(10)) # todos los valores diferentes a 0 = TRUE

# RANGOS => sucesión de números en un rango particular
rango1 = range(1,21) # tomamos el siguiente valor para que pueda ser incluido
print(rango1)
print('convirtiendo rango a lista:', list(rango1)) # para visualizarlos!
rango2 = range(3, 30, 3) # SLICING con COMAS!! => del 3 al 30 en saltos de 3
print(list(rango2))
# no son mutables, ni se pueden sumar

# DICCIONARIOS => formato para almacenar información con LLAVES.
diccionario1 = dict()
print('ejemplo de diccionario:', diccionario1, 'su tipo es:', type(diccionario1))
diccionario1 = {'llave1': 'gato', 'llave2': 1984}
print(diccionario1)
print(diccionario1['llave2']) # slicing!!

# CONJUNTOS / SETS: valores no ordenados que NO admiten duplicados, en {} y separados por comas
set1 = {6, 3, 'azul'}
print(set1)
print(type(set1))

# MATRICES
