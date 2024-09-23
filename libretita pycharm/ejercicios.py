# EJERCICIOS
# 1. Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario
# tiene una longitud mayor o igual que 3 y a su vez es menor que 10
# (es suficiene con mostrar True o False

# palabra = input('introduce una cadena: ')
# if len(palabra) >= 3 and len(palabra) <10:
  #  print('true:', palabra)

# else:
   # print('false')
# 2. Realiza un programa que lea 2 números por teclado y determine
# los siguientes aspectos (es suficiene con mostrar True o False):
# Si los dos números son iguales
# Si los dos números son diferentes
# Si el primero es mayor que el segundo
# Si el segundo es mayor o igual que el primero

# numero1, numero2  = float(input('escribe un número: ')), float(input('escriba otro número: '))
# print('ambos números son iguales: ', numero1 == numero2)
# print('ambos números son diferentes: ', numero1 != numero2)
# print('el primer número es mayor que el segundo: ', numero1 > numero2)
# print('el segundo número es mayor que el primero: ', numero2 > numero1)

# 3. Realiza un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, debe repetise el proceso
# hasta que lo introduzca correctamente.

while True: # el bucle se repetirá de forma indefinida hasta que se cumpla con el break
    num_impar = int(input('escribe un número impar: '))

    if num_impar % 2 !=0 :
       print('gracias por tu cooperación!')
       break
    else:
       print('este no es un número impar, hazlo de nuevo')

# crea un programa que pida al usuario que ingrese una contraseña.4
# el programa debe seguir pidiendo la contraseña hasta que el usuario ingrese
# la correcta. Define la contraseña correcta como una variable al inicio del programa.
# Si el usuario introduce la contraseña correcta, imprime "Acceso concedido"
# y termina el programa

password = str('holamundo')

while True:
    pswrd = input('escriba la contraseña: ')
    if pswrd == password: # equiparar las dos variables!!
        print('acceso concedido')
        break
    else:
        print('la contraseña es incorrecta, inténtelo de nuevo')

# Crea un programa que pida al usuario que ingrese un número entre
# 1 y 10. Si el usuario ingresa un número fuera de este rango,
# el programa debe seguir pidiendo un número hasta que esté dentro del rango.
# Cuando el usuario ingrese un número válido, imprime un mensaje
# que confirme el número ingresado.

while True:
    numero_rango = int(input('introduce un número entre el 1 y 10: '))
    if numero_rango >= 1 and numero_rango <= 10:
        print('muchas gracias :) el número ingresado fue: ', numero_rango)
        break
    else:
        print('ese número no está dentro del rango, inténtalo de nuevo')

# realiza un programa que sume todos los números enteros pares
# desde el 0 hasta el 100

suma = 0
for numero in range(101):
    if numero %2 == 0: # para verificar que el número es par!!
        suma += numero
print('la suma de todos los números pares desde 0 hasta 100 es: ', suma)

# Realiza un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números y realiza una media aritmética:


