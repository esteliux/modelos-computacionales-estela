# EJERCICIOS
# 1. Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario
# tiene una longitud mayor o igual que 3 y a su vez es menor que 10
# (es suficiene con mostrar True o False

# palabra = input('introduce una cadena: ')
# if len(palabra) >= 3 and len(palabra) <10:
  #  print('true:', palabra)

# else:
   # print('false')

a = -2
if a > 0: # IF: siempre que la expresión que se comprueba devuelva true
    print('es mayor que cero:', a)

a = 5
b = 10
if a == 5:
    print('a vale: ', a)
    if b == 10: # anidar if dentro de if
        print('y b vale: ', b)
# como condición podemos evaluar múltiples expresiones!!!
# siempre que éstas devuelvan True o False:
# podemos usar expresiones anidadas
a = 5
b = 10
if b == 10 and a == 5:
    print('a vale 5 y b vale 10')

# entencia ELSE => para comprobar el caso contrario de un if

a = 15
if a == 5:
    print('a es igual a a 5')
else:
    print('a no es igual a a 5')

n = 78
if n % 2 == 0:
    print(n, 'es un número par')
else:
    print(n, 'es un número impar')

# sentencia ELIF => si no se cumple la condicional #1, verifica una SEGUNDA condicional
# se comprueban múltiples condiciones siempre que las anteriores no se ejecuten

# a = int(input('escriba un valor numérico: '))

#if a % 2 == 0:
 #   print(a, 'es par')
#elif a > 20:
 #   print(a, 'es mayor que 20')

nota = float(input('introduce una nota: '))
if nota >= 7:
    print('notable')
elif nota >= 6:
    print('bien')
elif nota >= 5:
    print('suficiente')
elif nota >= 9:
    print('sobresaliente')
else:
    print('insuficiente')

# sentencia WHILE => repetir un bloque a partir de evaluar una condición lógica
# siempre y cuando esta sea VERDADERA
# no conocemos el número exacto de iteraciones!! => queremos repetir el
# código mientras se cumpla una condición!

c = 0
while c <= 5:
    c += 1
    print('c vale: ', c)

else:
    print('se ha completado toda la iteración y c vale: ', c)

c = 0
while c <= 5:
    c += 1
    if (c == 4):
        print("Rompemos el bucle cuando c vale",c)
        break # rompe la ejecución de while. no se ejecutará el else
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale",c)

# sentancia FOR => imprimir código para x número de iteraciones
# cuando ya conocemos # de iteraciones o se está iterando sobre secuencia
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