import random
import os
import csv

datos_usuario = {}

def generar_codigo():
    codigo = random.randint(100, 999)
    return codigo

def main_menu():
    while True:
        os.system("cls")
        print("===========================================")
        print("     ***  SYSTEM E-CARD AGUACHICA  ***    ")
        print("                                           ")
        print("1.   -   Comprar tarjeta")
        print("2.   -   Recargar tarjeta")
        print("3.   -   Registro clientes")
        print("4.   -   Consultar tarjetas activas")
        print("5.   -   Consultar tarjetas inactivas")
        print("6.   -   Consultar recargas por fecha")
        print("7.   -   Buscar usuario")
        print("8.   -   Buscar una tarjeta")
        
        print("9.   -   Salir del programa")
        print("============================================")
        try:
            opcion = int(input("Ingrese la opción que desea utilizar: "))
        except ValueError:
            print("Ingresa una opción válida.")
            continue
        
        if opcion == 1:
            comprar_tarjeta()
            break
        elif opcion == 2:
            recargar_tarjeta()
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            pass
        elif opcion == 9:
            print("SALIENDO...")
            exit()

def buscar_tarjeta_usuario():
    os.system("cls")
    print("*** BÚSQUEDA DE TARJETA DE USUARIO ***\n")
    try:
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        if nombre_usuario in datos_usuario:
            tarjeta = datos_usuario[nombre_usuario]
            print("Tarjeta encontrada:")
            print(f"Usuario: {nombre_usuario}")
            print(f"Número de tarjeta: {tarjeta['numero']}")
            print(f"Saldo: {tarjeta['saldo']}")
        else:
            print("No se encontró la tarjeta de usuario.")
    except KeyError:
        print("Error: Nombre de usuario inválido.")

def comprar_tarjeta():
    os.system("cls")
    print("* COMPRA DE TARJETA *")
    print("                         ")
    print("")

def recargar_tarjeta():
    os.system("cls")
    print("*** RECARGA DE TARJETA ***")
    print("                         ")
    valor = float(input("Ingrese cuánto desea recargar: "))
    tarjeta = buscar_tarjeta_usuario()
    saldo_actual = tarjeta.get("saldo", 0)
    nuevo_saldo = saldo_actual + valor
    tarjeta["saldo"] = nuevo_saldo
    print(f"¡Tarjeta recargada con éxito! Valor: {valor}")
    print(f"Nuevo saldo: {nuevo_saldo}")

