# Ejercicio 1. Genera un arreglo 1D, llamado freq,
# de 4 elementos de números aleatorios enteros en el intervalo [1, 8]
import numpy as np

from paquetito_pandas import array

freq = np.random.randint(1, 9, size = 4)
print(freq)

# Ejercicio 2. Genera un arreglo 1D, llamado amplitud, de 4 elementos de números aleatorios con distribución uniforme
# en el intervalo [3, 6]

amplitud = np.random.uniform(3, 7, size = 4)
print(amplitud)

# Ejercicio 3. Use el metodo arange para generar un arreglo, llamado t, de 2000 números en el intervalo [0, 1]

t = np.arange(0, 1, 2000)

# Ejercicio 4. Genere 4 ondas sinusoidales con cada frecuencia y amplitud.
# Recuerde que la ecuación de la onda sinusoidal es y(t) = A*sin(2*piB*t)
# donde A es la amplitud y B es la frecuencia.
# Para usar pi en numpy, use np.pi
# Sugerencia: para visualizar las ondas sinusoidales puede usar las líneas de código

A = amplitud
B = freq
t = np.ndarray

def onda_sinusoidal(A, B, t):
    return A * np.sin(2 * np.pi * B * t)

valores_ondas = onda_sinusoidal(A, B, t)
print(valores_ondas)

# Ejercicio 5. Cree un arreglo llamado x, que sea la suma de las 4 ondas sinusoidales


# Numpy también permite aplicar operadores tales como la transormada de fourier a un arreglo de datos con
# el paquete np.fft, en particular la función np.fft.fft(x) aplica la transformada discreta de fourier al arreglo x
# X = np.fft.fft(x)

# Ejercicio 6. Cree un arreglo, llamado frequence, de los enteros en el intervalo [0, 1999]


# Ejercicio 7. Calcular el valor absoluto a todos los elementos del arreglo X


# Ejercicio 8. De los primeros 10 elementos del arreglo del ejercicio anterior, determine los 4 elementos máximos y en
# qué índices se localizan


# Para mostrar la frecuencia y la amplitud en el dominio de Fourier use las siguientes líneas de código
plt.stem(frequence, absX)
plt.show()