"""
Sesion 11 - Actividad - Compras por Cliente
Actividad: Avanzada

Crear un programa que permita al usuario ingresar el tiempo dentro en un estacionamiento , cortando el ingreso de datos cuando el usuario ingresa 0 minutos.
Si ingresa una cantidad negativa, no debe procesarse y se le debe solicitar que ingrese una nueva cantidad.
Ingresar una tarifa fija durante la primera hora (60 minutos) de  25𝑦 15 por cada hora adicional. Al finalizar, informar el total a pagar teniendo en cuenta que, si el monto supera las 8 horas se aplica una tarifa de $200 extra.
¡Importante hacerlo en Visual Studio! Suerte
"""

# Inicio del Proceso de pago de estacionamiento
while True:

    # Declaracion de variables
    horas = 0
    minutos = 0
    primera_hora = 25
    adicional_hora = 15
    penalizacion = 200
    total = 0
    continuar = ""
    horas_adicionales = 0

    # Inicio del cobro
    print("***** BIENVENIDO A COBRO DE ESTACIONAMIENTO *** \n")
    while True:

        # Obteniendo las horas y los minutos
        horas = int(input("Ingrese Horas Sin Minutos "))
        minutos = int(input("Ingrese Minutos "))
        if horas < 0 or minutos < 0:
            print("Los valores deben ser Mayores a Cero .. Intente de nuevo")
            continue

        # Se calcula el total a cobrar del tiempo capturado

        # Se tarifican horas
        if horas == 0 and minutos <= 15:
            total = 0
        elif horas <= 1:
            total = primera_hora
        else:
            total = primera_hora
            total = total + (horas-1)*adicional_hora

        # Se tarifican minutos
        if minutos > 15 and horas >= 1:  # menos de 15 minutos no se cobra la hora
            total = total + adicional_hora

        # Se calcula la penalizacion
        if horas > 8:
            total = total + penalizacion

        # Se imprime resultado
        print("*" * 50)
        print("El total a pagar es {0}".format(total, "###,###.00"))
        break

    # Desea Continuar?
    continuar = input("Enter - Otro Cobro / N -> Salir ")
    if continuar == 'N' or continuar == 'n':
        print("\n Gracias por su Visita ... ")
        break
