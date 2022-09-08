"""
Actividad Sesion 11 - Funcion Cuadrática - Avanzada
Crea una funcion en la cual recibas como argumentos los parámetros reales e 
imaginarios de una funcion cuadratica y te regrese x1 y x2

En caso de obtener valores imaginarios, imprime valores de la constante real x 
y la constante imaginaria (2xj)
Los parametros deben ser a, b, c    
"""

# Se importa libreria para funciones matematicas
import math # funciones basicas
import cmath # funciones avanzadas con numeros complejos

# Funcion utilizando funciones avanzadas y numeros complejos
def cuadratica2(a, b, c):
    cx1 = -b - (cmath.sqrt((b**2)-(4*a*c))) / (2 * a)
    cx2 = -b + (cmath.sqrt((b**2)-(4*a*c))) / (2 * a)
    print("Constante real de x1 = {0}, Constante imaginaria de x1 = {1}".format(
        cx1.real, cx1.imag))
    print("Constante real de x2 = {0}, Constante imaginaria de x2 = {1}".format(
        cx2.real, cx2.imag))
    return "El valor de x1 = {0} y el valor de x2 = {1} Tipos: {2} {3}" \
        .format(cx1, cx2, type(cx1), type(cx2))


# Se llama a la funcion
# Llamando a la funcion
a = float(input("Captura constante a: "))
b = float(input("Captura constante b: "))
c = float(input("Captura constante c: "))
print(cuadratica2(a, b, c))

