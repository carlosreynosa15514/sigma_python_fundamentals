"""
Actividad: Básica

1. Crear un programa en Visual Studio que me permita saber cuál es el competidor más 
veterano que ha recibido medalla (oro, plata o bronce).
2. Crear un programa en Visual Studio que me permita saber cuál es el competidor más 
joven que ha recibido medalla de oro
3. Encuentra al competidor más ganador de la historia y crea un csv con 
toda su información.
"""

# Importa librerias
import pandas as pd
import os
pd.set_option('display.max_columns', None)

# Carga dataset
data = pd.read_csv("athlete_events.csv")

# Se crea DataFrame sin NaN en la column "Medal"
data_sin_nan = data[data['Medal'].notna()]

# Se crean DataFrames por cada Medalla
df_oro = data_sin_nan[data_sin_nan['Medal'] == 'Gold']
df_silver = data_sin_nan[data_sin_nan['Medal'] == 'Silver']
df_bronze = data_sin_nan[data_sin_nan['Medal'] == 'Bronze']

# Se limpia la pantalla de Bash
os.system("clear")

# ==========================================================================
# ****** 1. Jugador mas Veterano que ha ganado una medalla ****
# ==========================================================================

veterano = data_sin_nan[data_sin_nan['Age'] == data_sin_nan['Age'].max()]
print("Jugador mas veterano con Medalla de Oro")
print(veterano)
print("=" * 80)

# ==========================================================================
# ****** 2. Calculo de cuál es el competidor más joven que ha recibido
# medalla de oro ******
# ==========================================================================

mas_joven_oro = df_oro[df_oro['Age'] == df_oro['Age'].min()]
print("El competidor mas joven que ha recibido medalla de Oro")
print(mas_joven_oro)
print("=" * 80)

# ==========================================================================
# ******  3. Encuentra al competidor más ganador de la historia y crea un csv 
# con toda su información ******
# ==========================================================================

# Se suman las medallas de cada competidor
competidores = data_sin_nan['Name'].value_counts()

# Se asigna el nombre del primer registro, que es el de mas medallas
nombre_ganador = competidores.index[0]

# Se crea un DataFrame solo con los datos de ese competidor
informacion_ganador = data_sin_nan[data_sin_nan['Name'] == nombre_ganador]

# Se graba el DataFrame a un archivo csv
file_mayor_ganador = "Mayor_Ganador.csv"
informacion_ganador.to_csv(file_mayor_ganador)
print("Se ha creado el archivo: ", file_mayor_ganador)
print("=" * 80)

# ==========================================================================
# ==========================================================================

"""
    Actividad: Avanzada

3. Encuentra al competidor más ganador de la historia en medallas totales, 
medallas de oro, medallas de plata y medallas de broce. Crea un csv con toda 
su información.    
"""

# Filtrando los mas ganadores por medalla en un DataFrame por medalla
mas_ganador_oro = df_oro['Name'].value_counts().index[0]
mas_ganador_silver = df_silver['Name'].value_counts().index[0]
mas_ganador_bronze = df_bronze['Name'].value_counts().index[0]

# Creando los DataFrames con la informacion del mas ganador por medalla
info_oro = df_oro[df_oro['Name'] == mas_ganador_oro]
info_silver = df_silver[df_silver['Name'] == mas_ganador_silver]
info_bronze = df_bronze[df_bronze['Name'] == mas_ganador_bronze]

# Creando los files.csv con la informacion de cada ganador por medalla
file_mas_ganador_oro = "Mas_ganador_oro.csv"
file_mas_ganador_silver = "Mas_ganador_silver.csv"
file_mas_ganador_bronze = "Mas_ganador_bronze.csv"
info_oro.to_csv(file_mas_ganador_oro)
info_silver.to_csv(file_mas_ganador_silver)
info_bronze.to_csv(file_mas_ganador_bronze)
print("Se ha creado el archivo: ", file_mas_ganador_oro)
print("Se ha creado el archivo: ", file_mas_ganador_silver)
print("Se ha creado el archivo: ", file_mas_ganador_bronze)

# *** Fin ***

