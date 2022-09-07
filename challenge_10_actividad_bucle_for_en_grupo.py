# Challenge Sesion 10 - Actividad 10

# ACTIVIDAD BASICA
# =======================================================================================================
# 1.- Cada compañero dirá un numero. Los guardarás en un diccionario junto con el nombre de tu pareja

# Se inicializa un diccionario vacío
numeros={}

# Se pregunta cuantas personas participan
personas = int(input("Cuantas Personas Participan: "))

# Se llena el diccionario preguntando nombre y valor
for turno in range(personas):
    nombre = input("Captura Nombre {0}: ".format(turno+1))
    numero = int(input("Captura Numero {0}: ".format(turno+1)))
    numeros[nombre] = numero

# Se muestran los numeros capturados
print("\nSe muestran los datos capturados")
print(numeros)
print()

# =======================================================================================================
# 2.- Luego imprimirán los valores del diccionario (nombre de la persona y número que dijo) (Usando el bucle for)

print("Se imprimen los valores del diccinario")
for key, value in numeros.items():
    print("{0} --> {1}".format(key, value))
print()
    
# =======================================================================================================

# 3.-- Al final imprimiran dos mensajes, mostrando el número más grande y el número más pequeño que dijeron, 
# sin el nombre del socio, solo el número.

mayor = numeros[max(numeros, key=numeros.get)]
menor = numeros[min(numeros, key=numeros.get)]
print("El numero mas grande es: ", mayor)
print("El numero mas pequeño es: ", menor)

# =======================================================================================================
    
# ACTIVIDAD AVANZADA

# 1.Asigna un numero aleatorio a tu compañero. Los guardarás en un diccionario, junto con el nombre de tu pareja

# Se importa libreria para aleatorios
import numpy as np

# Se inicializa un diccionario vacío
dic_numeros = {}

print("ACTIVIDAD AVANZADA")

# Se pregunta cuantas personas participan
dic_personas = int(input("Cuantas Personas Participan: "))

# Se llena el diccionario preguntando nombre y valor
for turno in range(dic_personas):
    # Se pregunta el nombre
    dic_nombre = input("Captura Nombre {0}: ".format(turno+1))
    # Se asigna un numero random entre 100 y 500
    dic_numero = np.random.randint(100, 500)
    # Se agrega al diccionario
    dic_numeros[dic_nombre] = dic_numero

# Se muestran los numeros capturados
print()
print("="*80)
print(dic_numeros)

# =======================================================================================================

# 2.Luego imprimirán los valores del diccionario (nombre de la persona y número que dijo) (Usando el bucle for )

print("="*80)
for key, value in dic_numeros.items():
    print("{0} --> {1}".format(key, value))

# =======================================================================================================

# 3.Al final imprimiran dos mensajes, mostrando el número más grande y el número más pequeño que dijeron, sin el nombre del socio, solo el número.
print("="*80)
dic_mayor = dic_numeros[max(dic_numeros, key=dic_numeros.get)]
dic_menor = dic_numeros[min(dic_numeros, key=dic_numeros.get)]
print("El numero mas grande es: ", dic_mayor)
print("El numero mas pequeño es: ", dic_menor)

print("Fin ")