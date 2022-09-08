"""
Actividad Sesion 11 - Funcion Cuadrática - Basica
    Crea una función en la cual recibas como argumentos los parámetros reales 
    de una función cuadrática, y te regrese x1 y x2.

¡Importante hacerlo en Visual Studio! 

Los parametros deben ser a, b, c    
"""

# Se importa libreria para funciones matematicas
import math  # funciones basicas

# Funcion utilizando funciones basicas
def cuadratica(a, b, c):
    x1 = -b - (math.sqrt((b**2)-(4*a*c))) / (2 * a)
    x2 = -b + (math.sqrt((b**2)-(4*a*c))) / (2 * a)
    return "El valor de x1 = {0} y el valor de x2 = {1} Tipos: {2} {3}" \
        .format(x1, x2, type(x1), type(x2))

# Llamando a la funcion
a = float(input("Captura constante a: "))
b = float(input("Captura constante b: "))
c = float(input("Captura constante c: "))
print(cuadratica(a, b, c))
