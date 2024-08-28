# TAREA 4
# ejercicio 1
calif1 = 10
calif2 = 7
calif3 = 4
print('considera las siguientes calificaciones')
print('calificación 1:', calif1, '\n','calificación 2:', calif2,'\n', 'calificación 3:', calif3)
print('calcula el promedio de las calificaciones considerando que\n'
      'la primera nota vale un 15% del total\n'
      'la segunda nota vale un 35% del total\n'
      'la tercera nota vale un 50% del total\n')
calif1_ponderada = calif1*0.15
calif2_ponderada = calif2*0.35
calif3_ponderada = calif3*0.50
print('la calificación 1 ponderada:', calif1_ponderada,'\n'
      'la calificación 2 ponderada:', calif2_ponderada,'\n'
      'la calificación 3 ponderada:', calif3_ponderada,'\n')
calif_total = calif1_ponderada + calif2_ponderada + calif3_ponderada
print('la calificación total:', calif_total,'\n')

# ejerccio 2
print('la siguiente matriz debe cumplir que el 4to valor de cada fila debe ser\n'
      'igual a la suma de los primeros tres valores.\n'
      'crea un código para hacer las correciones necesarias'
      )
matriz = [
      [1, 1, 1, 3],
      [2, 2, 2, 7],
      [3, 3, 3, 9],
      [4, 4, 4, 13]
]
matriz_corregida = [
      [1, 1, 1, 3],
      [2, 2, 2, 6],
      [3, 3, 3, 9],
      [4, 4, 4, 12]
]
print( 'MATRIZ:', matriz)
print( 'CORREGIDO:', matriz_corregida)
if matriz_corregida == matriz:
      print('está bien')
else:
      print('corregir\n')

# extra que quería ver si funcionaba
if matriz[0][3] == matriz[0][0] + matriz[0][1] + matriz[0][2] and matriz[1][3] == matriz[1][0] + matriz[1][1] + matriz[1][2] and matriz[2][3] == matriz[2][0] + matriz[2][1] + matriz[2][2] + matriz[2][3] and matriz[3][3] == matriz[3][0] + matriz[3][1] + matriz[3][2] + matriz [3][3]:      print('está bien')
else:
      print('no está bien')
