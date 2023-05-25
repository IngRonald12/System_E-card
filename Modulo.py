import random
from os import system; system("cls")
import csv
datos_usuario = {}

def generar_codigo():
    codigo = random.randint(100, 999)
    return codigo

def main_menu():
    while True:
        system("cls")
        print("===========================================")
        print("     ***  SYSTEM E-CARD AGUACHICA  ***     ")
        print("                                           ")
        print("1.   -   Comprar tarjeta")
        print("2.   -   Registro clientes")
        print("3.   -   Consultar tarjetas activas")
        print("4.   -   Consultar tarjetas inactivas")
        print("5.   -   Consultar recargas por fecha")
        print("6.   -   Buscar usuario")
        print("7    -   Buscar una tarjeta")
        print("8.   -   Salir del programa")
        print("============================================")
        opcion = int(input("Ingrese la opcion que desea utilizar: "))
        
        if opcion == 1:
            comprar_tarjeta()
            break

def comprar_tarjeta():
    system("cls")
    print("*** COMPRA DE TARJETA ***")
    print("                         ")
    print("")

main_menu()