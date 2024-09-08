# numero_str = input('Introduce un número del 1 al 150: ')
# n = int(numero_str)

# print(list(range(1, n+1)))

# realiza un programa que sume todos los números enteros pares desde el 0
# hasta un número que se introduzca por teclado

numeros_str = input('introduce un número:')
numeros = int(numeros_str)
pares = range(0, numeros, 2)
print(sum(pares))
