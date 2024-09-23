# TAREA 2

print('crear un archivo llamado tarea02.py para determinar si los tipos de dato range cumplen con las '
      'siguientes características:\n')
rango1 = range(1, 5, 10)
print('mutabilidad: NO')
rango2 = range(16, 200)
print('suma: NO')
print('producto por entero: NO')
rango_slicing = rango2[0]
print('slicing:SÍ:', rango_slicing)
lista_rango = list(rango2)
print('convertir a lista: SÍ:', lista_rango)
print('función LEN: NO directamente\n'
      'en formato de lista, SÍ =>',
      len(lista_rango))