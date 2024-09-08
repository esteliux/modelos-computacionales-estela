# LIBRETA - PYTHON

list1 = ['tomate', 'aguacate', 'papa']
print(list1)
print(list1[1])
print('ejemplo de slicing:', list1[1])
texto = 'python'
print('texto')
list2 = [1, 2, 3]
print(list2)

# operaciones con listas
print(list1, list2)
print('sumando listas list1 y list2, se obtiene:\n', list1+list2)
# las sumas concatenan las listas
print('sumando listas list1 y list2, se obtiene:\n', list2+list1)
print('sumando listas list2 y list2, se obtiene:\n', list2+list2)

list3 = [3, 6, 'sirena']
print('list3 = ', list3)
#producto por escalar
print('3*list3 =', list3*3)
# slicing de nuevo...
list_ = list1 + list2
print(list_[1:6])
print(list_[::2])
# estructura general de slicing: inicio:fin:index jump.

# las listas son modificables
print('list_ = ', list_)
list_[1] = 'gato'
print(list_)
print(list_.index('gato'))

# agregar valores a una lista, al final, usando el metodo append
print(list_)
list_.append(5)
print(list_)
# se pueden concatenar listas con listas, no listas con enteros o palabras o algo asi xd
# para insertar un valor en una posición específica, se usa el metodo insert
list_.insert(3,['rosa', 'amarillo', 'azul', 'blanco', 'y ya'])
print(list_)

# para determinar numero de elementos de la lista, se usa la funcion len
len(list_)
print(len(list_))

texto = 'quiero llegar a casita a descansar después de un día largo como este'
print(texto.split())
print(type(texto.split()))

# eliminar elementos de una lista. forma más fácil, igualarlo a una lista vacía
print(list_)
list_.remove('papa')
print(list_)

# clase del 26 de agosto

lista = ['gato', 'película', 'libro', 'azul']
print(lista)
lista.reverse()
print(lista)
lista.sort(reverse=True)
print(lista)

# TUPLAS
# es una colección de DISTINTOS elementos ordenados entre () y separados por COMAS

tupla = (7, 'julio', 8)
print('la tupla:', tupla, 'es de tipo:', type(tupla))
# cómo definir tupla con un elemento; con COMILLAS
tupla = ('5')
print('la tupla de un elemento:', tupla, 'es de tipo:', type(tupla))

#slicing

tupla = (5, 7, 'dieciséis', 'gato', 'agua', 'libreta', [9.2], 'pantalla')
print('tupla', tupla)
print('aplicando slicing con números negativos:', tupla[-4:-1])

# LAS TUPLAS SON NO MUTABLES!
# suma de tuplas

tupla1, tupla2 = (1, 2, 3), ('algo', 'cosa', 'toser')
print('suma de tuplas:', tupla1 + tupla2)
print('suma de tuplas:', tupla2 + tupla1)
print('multiplicar tuplas por un entero:', tupla1*3)

# convertir tuplas a listas
print('convirtiendo tupla a lista:', list(tupla1))

# en RESUMEN:
# mutabilidad
# operaciones con tuplas: suma, producto por un entero
# slicing
# conversión de tuplas a listas y viceversa

# RANGOS!!! sucesión de números en un rango particular

rango1 = range(5)
print(rango1, type(rango1))

# conversión de rango a lista => aparecen todos los números del 0-4

print('convirtiendo rango a lista:', list(rango1))

# siempre tomamos el valor siguiente para que sea incluido
# aplicando slicing al rango

rango2 = range(3, 104, 3)
print(rango2[0])

# BOOLEANOS!! representan uno de dos posibles valores: verdadero o falso

valor1 = True # TRUE
valor2 = False # FALSE
print('tipos de valores booleanos:', valor1, valor2)
print('usando type', type(valor1), type(valor2))

print('usando and:', valor1 and valor2)
print('usando or:', valor1 or valor2)

# conversión a valores booleanos; todos los números que no sean 0 son VERDADEROS

print('int', bool(0))
print('int', bool(1))
print('int', bool(-7))

# condicionales

if (5+3-8):
    print('otra vez print')
else:
    print('ya ven')

# conversiones a boleano de strings => cadenas vacías FALSE. aplica para tuplas también.

# DICCIONARIOS {} usados para almacenar datos en formatos de key:value

diccionario1 = dict()
print('ejemplo de diccionario:', diccionario1, 'su tipo es:', type(diccionario1))

diccionario1 = {'llave1': 'gato', 'llave2': 1984}
print(diccionario1)

# slicing a diccionario => con base a la llave que definimos

print(diccionario1['llave2'])

# CONJUNTOS: valores no ordenados que no admiten duplicados, en {} y separados por comas

set1 = {6, 3, 'azul'}
print(set1)
print(type(set1))

# CLASE 27 DE AGOSTO DEL 2024
# asignadores

variable = 5
print(variable)
variable1 = 10
print('la variable 1:', variable1)
variable1 += 3.2
print('la variable 1:', variable1)

# =, +=, *=, /=, //=, %=,
variable1 = 2
variable1 **=3
print('la variable 1:', variable1)

# aplicando suma de cadenas

cad1 = ('hola')
cad2 = ('¿cómo estás?')
print(cad1 + cad2)
# cuando usamos este operador +=, ya tenemos guardada la suma de las cadenas
cad1 += cad2
print(cad1)

# <, >, ==, != => regresan booleanos

print('para establecer diferencias: !=')

# operadores or, and y not

((5 < 8) and 0) or bool('carro')

# expresiones anidadas => con REGLAS jerárquicas
# 1- paréntesis
# 2- expresiones aritméticas
# 3- expresiones relacionales
# 4- expresiones lógicas

a = 10
b = 5

print(a * b - 2**b >= 20 and not (a % b) != 0)

# controladores de flujo => estructura de control CONDICIONAL
# sirven para evaluar si una condición se cumple
# sólo pueden dar UN resultado

if 'oración':
    print('caso positivo')

var1, var2 = 5, 2
if True:
    print('caso positivo')
    if var2/var1 < var1:
        print('segundo nivel de if')
# ejemplo de if ELSE
if not False:
    print('la condicional es verdadera')
else:
    print('la condicional es falsa')

# ejemplo de if else

n = 78
if n % 2 == 0:
    print(n, 'es un número par')
else:
    print(n, 'es número impar')

# tercer comando => ELIF
# si no se cumple la condicional #1, verifica una SEGUNDA condicional

condicional = 32
if condicional < 10:
    print('condicional es ternurín')
elif condicional < 20:
    print('condicional no es tan ternurín')
elif condicional < 35:
     print('condicional no es ternurín :c')

# comando pass => simplifica el código ish???

if condicional != 0:
    pass

# comando FOR => imprimir código para x número de iteraciones
# para una variable local en la lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for idx in numeros:
    print(idx)

promedio = 0 # si no lo defino igual a 0, alterará el valor subsecuente
numeros = [0, 2, 4, 6, 8]
for idx in numeros: # idx hace referencia al VALOR que va a tomar esa variable, para cada iteración
    promedio += idx
    print(str(idx))
promedio /= len(numeros) # para dividir por el numero de elementos en la lista!
print('el promedio es:', promedio)

# otro ejemplo de for

numeros = [0, 2, 4, 5, 6]
diosito = 0
for _ in numeros:
    diosito += 1
    print('se está ejecutando el for')
print('la longitud de la lista es:', diosito)

# estructura del enumerate
# crea una tupla por cada lista
# devuelve un entero y el elemento de la lista (posición)
# valioso si queremos saber el índice de la variable
lista = ['azul', 'rosa', 'morado']
print(list(enumerate(lista)))
for elemento in enumerate(lista):
    print(elemento)

# uso de continue y break
# usarlos dentro de los ciclos for
# break => terminar súbitamente el for, independientemente de en
# qué parte de la iteración nos encontremos
# continue => si se cumple cierta condición, ignora todo el código debajo de, y sigue con la otra iteración

for idx in range(2, 18):
    print(idx)
    if idx % 2 == 0:
        print('es par')
        continue
    else:
        print('es impar')

# funciones de entrada y salida de datos
# input

# string = input('introduce un número:\n')

# print('se recibió la cadena:', string)
# print('con tipo de dato:', type(string))

# numero = float(string)
# print('el número es:', numero, 'con tipo de dato:', type(numero))

# funcion while
# repetir un bloque a partir de una condicional
# while condición: si es verdadera, se ejecutará el código.
# requisitos: condición inicial, de PARO y de incremento => para que
# llegue un momento en el que haya un FALSE y se ejecute el stop

val = 3
while val<5:
    print(val)
    val += 1

# else en bucle while

lista = ['chocolate', 'tristeza', 'cualquiera', 'naranja', 'azul', 'parque']
indice = -3 # esta es la condición inicial!!
while lista[indice] != 'cualquiera':
    print(indice, lista[indice])
    indice += 1
else:
    print('se cumplió la condición, ya me quiero mimir')

# FUNCIONES!!!!!
# código q se puede ejecutar varias veces
# definición y llamada
def saludar():
    print('Hola, este print se llama desde la función saludar()')
# saludar()

def escribir_tabla_del_5():
    for i in range(10):
        print('5 * ', i, ' = ', 5*i)
escribir_tabla_del_5()

# formas de usar el print
val = 10
print('5 * ', val, ' = ', 5*val)
print('5 * {} = {}'.format(10, 50))
print('5 * {1} = {0}'.format(10, 50)) # format: reconoce las llaves y sabe que debe poner ALGO => aquello que esté dentro
print(f'5 * {val} = {5*val}')

# variables globales y locales
# todo lo que hagamos dentro de una función, existirá dentro de ella solamente!:
def test():
    n = 10 # solo aquí dentro de esta función la definición de n existirá :) LOCAL

# return de las funciones
def test():
    n = 10
    print('n =', n)
    return n # saca de la función el valor de n, para que al imprimir la línea 347, sí exista.

m = test()

def test():
    return [1,2,3,4,5]
variable = test()
print(variable)
print('usando slicing:', variable[-2:]) # alch no entendí para qué es esto lol

# envío de valores => recibir info tmb, por parte de la función

def test_funcion(parametro1: int, parametro2: float): #aquí se recomienda especificar el tipo de dato, pero no altera nada no hacerlo.
    print(parametro1, parametro2) #akí son parámetros, en la DEFINICIÓN DE FUNCIÓN.

argumento1, argumento2 = 5, ['casa'] #akí son argumentos, en la llamada de la función (afuera)
test_funcion(argumento1, argumento2)

# argumentos por POSICIÓN

def funcion1(a, b):
    print (a-b)

funcion1(25, 7)
# podemos especificar el orden => funcion1(a = 7, b= 25)

# parámetros por defecto
def funcion_resta(a = 25, b = 7): #podemos especificar aquí el valor por default
    print(a - b)

funcion_resta() # si no ponemos nada, tomará los valores que establecimos. así como si solo definimos uno de los valores

funcion_resta(a = 50, b = 30) # si especificamos, tomará estos valores.

# paso por valor y paso por referencia

variable = 10
var2 = variable

# pase por valor => CREAMOS COPIAS, y por eso nunca son modificadas

def duplicar_numero(numero):
    print(numero*2)

val = 10
print('antes de la función:', val)
duplicar_numero(val)
print('después de la función', val)
# copia de la definición de arriba, pero guardada con otro nombre en el argumento
# espacio de memoria!! asignar a

# pase por referencia => NO se crean copias, se modifica la propia inicial.

def duplicar_valores_lista(lista):
    for i, n in enumerate(lista):
        lista[i] *=2
    print('dentro de la función', lista)

ns = [10, 50, 100]
print('antes de la función:', ns)
duplicar_valores_lista(ns)
print('después de la función', ns) # esta línea se modificó

# hacer una funcion que obtenga un integer y calcular el factorial de ese numero (integer no negativo)

def factorial(valor: int) -> int: # ->int hace referencia al valor que va a regresar
    if valor < 0:
        print('no existe el factorial de un número negativo')
        return
    resultado = 1 # valor inicial de 1 por definición de factorial

    for i in range(1, valor+1): # range para permitir las iteraciones!!
        resultado *= i # el resultado es = al resultado x el valor siguiente.

    return resultado

# val = int(input('introduce un número entero para calcular el factorial: ')) # input para...
print(factorial(3))

# crear función que recibe 3 números y verificar si el tercer numero se encuentra entre los 2 primeros

# def verificacion_valor(val1, val2, val3):
    # if val1 <= val3 <= val2:
        #print('SÍ')
    #else:
        #print('NO')
# valores_str = input('Ingrese tres valores: ')
# val1, val2, val3 = valores_str.split()
# val2, val2, val3 = float(val2_str),
#verificacion_valor(val2, val2, val3)

# dada una lista, da una función que imprima los numeros impares

def imprimir_impares(lista: list):
    for numero in lista:
        if numero %2 !=0:
            print(numero)

listado = [2, 4, 1, 393, 4, 5, 43, 1]
imprimir_impares(listado)

# RECURSIVIDAD => cuando tenemos muchas tareas por hacer, subdividirlas
def cuenta_atras(num):
    num -= 1
    if num > 0: # TENER CLARO LA CONDICIÓN DE PARO!!
        print(num)
        cuenta_atras(num)
    else:
        print('BOOM clap sound of my heart')
    print('fin de la función', num)

cuenta_atras(5)

def quitando_letra(palabra):
    if len(palabra) > 0:
        print('palabra:', palabra)
        palabra = palabra[:-1]
        quitando_letra(palabra)
    else:
        print('palabra nula', palabra)
    print('saliendo de la función ', len(palabra))

quitando_letra('123')

# bin(10) # conversión de entero a binario
# eval('2+4') # si en un string tenemos operaciones matemáticas, evaluarlas
# count: contar las veces q un elemento dado se encuentra presente

#def cuenta_factorial(valor: int):
 #   var = valor >= 1
  #  if valor >= 0:
   #cuenta_factorial(valor)
    #resultado = 1
    #for i in range(valor + 1):
     #   resultado *= i
    #else:
     #   print('BOOM clap sound of my heart')
    #print('fin de la función', valor)

#def cuenta_atras(num):
    #num -= 1
    #if num > 0:
     #   print(num)
      #  cuenta_atras(num)
    #else:
     #   print('BOOM clap sound of my heart')
   # print('fin de la función', num)