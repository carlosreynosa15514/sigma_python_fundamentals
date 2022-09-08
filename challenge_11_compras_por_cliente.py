"""
➔ Crear un programa que permita al usuario ingresar los montos de las compras
de un cliente(se desconoce la cantidad de datos que se cargarán,
que pueden cambiar en cada ejecución), cortando el ingreso de datos
cuando el usuario ingresa el monto 0.

➔ Si ingresa una cantidad negativa, no debe procesarse y se le debe 
solicitar que ingrese una nueva cantidad. 

➔ Al ﬁnalizar, informar el total a pagar teniendo en cuenta que, 
si las ventas superan el total de $ 1000, se debe aplicar un 10 % de descuento.

¡Importante hacerlo en Visual Studio!
"""

# importar libreria para limpiar pantalla
import os

# Inicio de Operacion de Compra

while True:

    # Declaracion de variables
    importe_item = 0
    subtotal = 0
    total = 0
    descuento = 0
    contador_compra = 0
    otra_compra = ""

    # Inicio de Captura del Ticket
    os.system("clear")
    while True:
        contador_compra += 1
        importe_item = float(
            input("Capture Importe Item {0} <0 Para Salir> ".format(contador_compra)))
        if importe_item == 0:
            contador_compra -= 1
            break
        elif importe_item < 0:
            contador_compra -= 1
            print("No se periten numeros negativos")
            continue
        else:
            subtotal += importe_item

    # Calcula descuento y total
    if subtotal > 1000:
        descuento = subtotal * 0.10
    total = subtotal - descuento

    # Muestra Totales
    os.system("clear")
    print("=" * 50)
    print("Resumen de Compra")
    print("=" * 50)
    print("Cantidad de Articulos............. {0}".format(contador_compra))
    print("Sub Total ........................ {0}".format(subtotal))
    print("Descuento ........................ {0}".format(descuento))
    if descuento > 0:
        print("En compras mayores de $1,000 obtiene 10% Descuento")
    print("-" * 50)
    print("Total a Pagar .................... {0}".format(total))
    print("-" * 50)

    otra_compra = input("Captura otra Compra? <Salir -> N> ").upper()
    if otra_compra == 'N':
        break

os.system("clear")
print("*" * 50)
print("Gracias por sus Compras !!! ")
